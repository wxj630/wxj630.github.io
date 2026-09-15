# Preflight Review

Latest pre-render report: `preflight-cycle0d.json`.

- `FAIL`: 0. The hard pre-render gate is passed.
- The two horizontal-spacing warnings in the General lane compare the intentional 20 px gap between sibling model cards with the 510 px separation to a benchmark card in a different lifecycle column. The stage headers and dashed Harness boundary make these separate semantic regions; no local sibling spacing mismatch exists.
- The Finance horizontal-spacing warning compares three cards that deliberately occupy lifecycle columns of different widths. Their left/right insets within each stage are consistent with the grid; forcing equal raw gaps would break column alignment.
- The vertical-spacing warning compares within-General card spacing with the deliberate 25 px inter-lane gaps and different lane heights. Within each lane, the data cards are aligned and non-overlapping.
- The prior empty Harness-container warning was fixed by putting `Cross-domain harness layer` directly on the dashed container.

All remaining warnings are reviewed geometry-grouping false positives rather than visible defects; they will be checked again in the screenshot loop.

## Final preflight review

Latest report: `preflight-final.json`.

- `FAIL`: 0; strict structural validation also reports zero errors and zero warnings.
- `actor_icon` is intentionally 78 pt because the Agent Structure track requires a large standalone workstation actor. The borderline 211 px estimate for a 200 px text cell is conservative for a single emoji glyph; `screenshots-cycle3.png` confirms the glyph is fully visible and not clipped.
- No external image, embedded raster, or base64 payload is present in the final `.drawio` source.
