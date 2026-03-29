---
name: Iterate until visually correct
description: When fixing layout/visual issues, compile, screenshot, and keep iterating without returning control until it looks right
type: feedback
---

When working on visual/layout problems in the presentation, run `quarto render` (or `quarto preview`), take a screenshot of the result, and keep iterating autonomously if something looks wrong. Do not hand control back to the user after each attempt — only return when the result looks correct or a genuine blocker is hit.

**Why:** User got frustrated having to manually check each failed layout attempt (e.g. the bottom-alignment issue required multiple back-and-forth rounds).

**How to apply:** For any task involving CSS, positioning, image sizing, or slide layout: render → screenshot → assess → fix, in a loop until satisfied.
