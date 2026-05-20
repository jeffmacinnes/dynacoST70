---
title: 'Step 14: Left OPT primary leads to V6 and V7'
---

# Step 14: Repeat step 13 for the right output transformer

> *Repeat Step 13 for right output transformer. The blue lead is twisted with the green and goes to pin #3 of V6 (S), green to pin #4, while the blue-white and green-white, after twisting together are connected to pins #3 (S) and #4 (S) of V7.* — manual page 7

## What you're doing physically

Mirror of [step 13](step-13-right-opt-primary.md), but for the other A-470 — the one whose primary feeds V6 and V7.

| Lead | Goes to | Function |
|---|---|---|
| BLUE | V6 pin 3 (S) | Plate of V6 |
| GREEN | V6 pin 4 | UL screen tap of V6 |
| BLUE/WHITE | V7 pin 3 (S) | Plate of V7 |
| GREEN/WHITE | V7 pin 4 (S) | UL screen tap of V7 |

Twist BLUE+GREEN as a pair; twist BLU/WHT+GRN/WHT as a pair. Pair each plate lead with its matching UL screen tap on the same half of the winding.

V6 pin 4 is NOT soldered at this step — it gets the feedback wire in step 58. V7 pin 4 IS soldered now.

## After this step

All four EL-34s now have their plates and ultralinear screen taps connected to the output transformer primaries. The audio path from the EL-34 plates to the OPT primaries is electrically complete — only the cathode network and grid drive (driver board) remain.

## See also

- [Step 13 — Right OPT primary](step-13-right-opt-primary.md) — the mirror image
- [A-470 output transformer](../../components/a-470-output-transformer.md) — primary lead structure
- [Push-pull topology](../../theory/push-pull-topology.md) — why this wiring topology matters
