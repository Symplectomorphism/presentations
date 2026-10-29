#!/usr/bin/env python3
"""Assemble the GitHub Pages site: one subfolder per deck plus an index page.

Each deck's rendered HTML is pulled from its own branch (see decks.json) with
`git archive`, so nothing needs to be checked out or re-rendered.

Usage:
    git worktree add .worktrees/site gh-pages    # once; .worktrees/ is in .git/info/exclude
    python3 site/build.py .worktrees/site
    cd .worktrees/site && git add -A && git commit -m "Rebuild site" && git push
"""
import html
import io
import json
import shutil
import subprocess
import sys
import re
import tarfile
import urllib.parse
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
LATEST_LINK = "main.html"  # old root URL; keep it pointing at the newest deck


def ref(branch):
    """Prefer the remote branch so the site matches what's pushed."""
    for r in (f"origin/{branch}", branch):
        if subprocess.run(["git", "rev-parse", "--verify", "-q", r], cwd=REPO,
                          capture_output=True).returncode == 0:
            return r
    sys.exit(f"branch not found: {branch}")


def extract(deck, dest):
    prefix = deck["path"].strip("/")
    include = deck.get("include")
    if include:
        paths = [f"{prefix}/{p}" if prefix else p for p in include]
    else:
        paths = [prefix or "."]
    tar = subprocess.run(["git", "archive", "--format=tar", ref(deck["branch"]), *paths],
                         cwd=REPO, capture_output=True, check=True).stdout
    strip = len(prefix) + 1 if prefix else 0
    with tarfile.open(fileobj=io.BytesIO(tar)) as tf:
        for m in tf.getmembers():
            if not m.isfile():
                continue
            out = dest / m.name[strip:]
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(tf.extractfile(m).read())


def check_assets(deck, dest):
    """Abort if the deck's own CSS/JS is missing (it would render unstyled); warn on media."""
    page = (dest / deck["entry"]).read_text(errors="ignore")
    refs = re.findall(r'(?:src|href|data-src|data-background-image|data-background-video)="([^"]+)"', page)
    missing = {r for r in refs
               if not re.match(r"^([a-z]+:|//|#|data:)", r) and "{" not in r
               and not (dest / urllib.parse.unquote(r.split("#")[0].split("?")[0])).exists()}
    broken = sorted(r for r in missing if r.endswith((".css", ".js")))
    if broken:
        sys.exit(f"{deck['slug']}: missing {len(broken)} CSS/JS files on branch "
                 f"{deck['branch']}, e.g. {broken[0]} — re-render and commit docs/")
    for r in sorted(missing):
        print(f"    warning: {deck['slug']} references missing {r}")


def redirect(target):
    return (f'<!doctype html>\n<meta charset="utf-8">\n'
            f'<meta http-equiv="refresh" content="0; url={target}">\n'
            f'<link rel="canonical" href="{target}">\n'
            f'<a href="{target}">Redirecting…</a>\n')


def card(deck):
    d = date.fromisoformat(deck["date"])
    e = html.escape
    return f"""      <li>
        <a class="deck" href="{e(deck['slug'])}/">
          <span class="meta"><time datetime="{d}">{d:%b %Y}</time> · {e(deck['venue'])}</span>
          <span class="title">{e(deck['title'])}</span>
        </a>
      </li>"""


def index_page(decks):
    cards = "\n".join(card(d) for d in decks)
    return (HERE / "index.template.html").read_text().replace("{{CARDS}}", cards)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1]).resolve()
    if not (out / ".git").exists():
        sys.exit(f"{out} is not a git worktree; refusing to clear it")

    decks = sorted(json.loads((HERE / "decks.json").read_text()),
                   key=lambda d: d["date"], reverse=True)

    for p in out.iterdir():
        if p.name != ".git":
            shutil.rmtree(p) if p.is_dir() else p.unlink()

    for deck in decks:
        dest = out / deck["slug"]
        print(f"  {deck['slug']:<12} <- {deck['branch']}:{deck['path'] or '.'}")
        extract(deck, dest)
        check_assets(deck, dest)
        if deck["entry"] != "index.html":
            (dest / "index.html").write_text(redirect(deck["entry"]))

    (out / "index.html").write_text(index_page(decks))
    (out / LATEST_LINK).write_text(redirect(f"{decks[0]['slug']}/{decks[0]['entry']}"))
    (out / ".nojekyll").write_text("")
    print(f"built {len(decks)} decks into {out}")


if __name__ == "__main__":
    main()
