# Presentations

Published at <https://symplectomorphism.github.io/presentations/>.

Each talk lives on its own branch (Quarto reveal.js, rendered to `docs/`).
`master` holds only the site builder, which copies each talk's rendered output
into a subfolder of the `gh-pages` branch and generates the index page.

To publish a new talk, add it to `site/decks.json`, then:

```sh
git worktree add .worktrees/site gh-pages    # once
python3 site/build.py .worktrees/site
cd .worktrees/site && git add -A && git commit -m "Rebuild site" && git push
```
