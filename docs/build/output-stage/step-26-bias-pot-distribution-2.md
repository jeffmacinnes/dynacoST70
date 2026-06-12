---
title: 'Step 26: Lug 2 to left bias control lug 3'
---

# Step 26: 8" wire from lug 2 (S) to left bias control lug 3

> *Connect one end of an 8" wire to lug #2 of the 7 lug strip (S). Connect the other end to lug #3 of the left bias control.* — manual page 7

## What you're doing physically

An 8" wire from lug 2 of the seven-lug strip to lug 3 of the **left bias pot**. Lug 2 is soldered final at this step — it now has the second 10 kΩ filter resistor (step 22) + this distribution wire.

The pot's lug 3 is NOT soldered yet — it'll receive more wires in steps 27 and 28.

## What this completes

Lug 2 of the seven-lug strip is the **bottom node of the bias-setting divider** — it sits at roughly −22 V, held there by the second 10 kΩ resistor (step 22) running from lug 2 to ground. This wire delivers that voltage to lug 3 of the left bias pot's resistance element.

Together with step 24 (which wired strip lug 3 — the more negative intermediate node of the divider — to lug 1 of the left pot), this places the pot's resistance element **across a section of the divider**:

- **Left pot lug 1**: the more negative end (fed from strip lug 3)
- **Left pot lug 3**: the less negative end (≈ −22 V, fed from strip lug 2 via this wire)

The two ends of the pot do **not** sit at the same potential — the pot is one leg of a voltage divider hanging across roughly −65 V at the raw end and ground at the bottom. The wiper taps a point between the two pot ends, swinging from about −43 V to about −22 V, centering near the −32 V the EL-34 grids need. Turning the pot moves the wiper along that range, which adjusts the grid bias.

## See also

- [Step 22 — Second bias resistor](step-22-bias-resistor-2.md) — what else is on lug 2
- [Step 27 — Inter-pot wire (lug 3)](step-27-bias-pot-interconnect-1.md) — next wiring of the pot lug 3
- [Bias adjustment](../../bring-up/bias-adjustment.md) — what the pot wiper actually does
