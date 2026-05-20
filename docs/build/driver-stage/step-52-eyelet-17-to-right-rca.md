---
title: 'Step 52: Eyelet #17 to right RCA long lug'
---

# Step 52: 1¾" wire from eyelet #17 (S) to right RCA long lug (S)

> *Connect one end of a 1 ¾" wire to eyelet #17 (S). Connect the other end to the (long) lug of the right input socket (S).* — manual page 9

## What you're doing physically

A 1¾" wire from PC-3 eyelet #17 to the long lug of the right RCA. Both ends soldered.

The right RCA's long lug now has: the wire from input switch lug 3 (step 49) + the 470 kΩ grid leak (step 50) + this wire. Three connections soldered together.

## What this carries

Eyelet #17 is the **right channel signal input** on the PC-3 board. This wire brings the right RCA jack's signal hot directly to the input stage.

The signal path now exists end-to-end for the right channel:

1. Audio source → right RCA center pin (long lug)
2. → 470 kΩ grid leak to ground (clamps DC)
3. → this wire → PC-3 eyelet #17
4. → on-board coupling cap → 6GH8A pentode grid
5. → amplified by pentode → phase splitter → coupling caps → V6/V7 grids
6. → EL-34s push-pull → OPT primary → speaker output

## See also

- [Step 49 — Input switch lug 3 to right RCA](step-49-input-switch-to-right-rca.md)
- [Step 50 — Right grid leak](step-50-right-grid-leak.md)
- [Step 53 — Eyelet #7 to left RCA](step-53-eyelet-7-to-left-rca.md) — channel B's equivalent
