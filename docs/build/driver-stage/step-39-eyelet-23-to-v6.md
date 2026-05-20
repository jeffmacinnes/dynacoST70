---
title: 'Step 39: Eyelet #23 to V6 pin 6'
---

# Step 39: 2¾" wire from eyelet #23 (S) to V6 pin 6 (S)

> *Connect a 2 ¾" wire from eyelet #23 (S) of the printed circuit board to pin #6 of V6 (S).* — manual page 8

## What you're doing physically

A 2¾" wire from PC-3 eyelet #23 to V6 pin 6. Both ends soldered (S).

V6 pin 6 now has: the 1 kΩ grid stopper from [step 37](../output-stage/step-37-grid-stoppers.md) + this wire. The grid stopper bridges pin 6 to pin 5 (the actual control grid).

## What this wire carries

Eyelet #23 is one of the **phase-splitter outputs** of the channel A 6GH8A. The cathodyne phase splitter in the 6GH8A produces two signals 180° apart — this one drives V6's grid (through the coupling cap on the board, plus the grid stopper here).

Audio signal flow into V6:

1. Input → 6GH8A pentode (gain stage)
2. → coupling cap → 6GH8A triode (cathodyne phase splitter)
3. → coupling cap (on PC-3 board, between phase splitter cathode and eyelet #23)
4. → this wire to V6 pin 6
5. → 1 kΩ grid stopper to V6 pin 5 (control grid)

The signal arriving at V6 grid is one half of the push-pull drive for channel A. The OTHER half drives V7 (next step).

## See also

- [Step 40 — Eyelet #22 to V7](step-40-eyelet-22-to-v7.md) — the partner of this signal
- [Phase splitting](../../theory/phase-splitting.md) — what the 6GH8A's triode is doing
- [Step 37 — Grid stoppers](../output-stage/step-37-grid-stoppers.md) — what's already on V6 pin 6
