---
name: Screenshotting slides for visual verification
description: How to render and screenshot slides for iterative layout fixes
type: feedback
---

To take a screenshot of a rendered slide for visual verification:

1. Run `quarto render main.qmd` to build to `docs/main.html`
2. Use `fish -c "nvm use lts && node -e \"...puppeteer script...\""` to screenshot
3. Puppeteer is installed locally in `node_modules/` (not committed to git)
4. Use `page.keyboard.press('ArrowRight')` to trigger fragments before screenshotting

**Why:** Node/puppeteer is the available headless screenshot tool on this system. Firefox headless and scrot are not available.

**How to apply:** Always run `nvm use lts` via fish shell before using node. The `node_modules/`, `package.json`, and `package-lock.json` are gitignored and should stay that way.