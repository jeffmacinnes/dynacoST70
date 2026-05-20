---
title: 'Step 26: Lug 2 to left bias control lug 3'
---

# Step 26: 8" wire from lug 2 (S) to left bias control lug 3

> *Connect one end of an 8" wire to lug #2 of the 7 lug strip (S). Connect the other end to lug #3 of the left bias control.* — manual page 7

## What you're doing physically

An 8" wire from lug 2 of the seven-lug strip to lug 3 of the **left bias pot**. Lug 2 is soldered final at this step — it now has the second 10 kΩ filter resistor (step 22) + this distribution wire.

The pot's lug 3 is NOT soldered yet — it'll receive more wires in steps 27 and 28.

## What this completes

Lug 2 of the seven-lug strip is the **final output of the bias filter cascade** — clean −65 V DC. This wire delivers that voltage to lug 3 of the left bias pot's resistance element.

Together with step 24 (which wired lug 3 of the strip — also at −65 V — to lug 1 of the left pot), this creates a slightly unusual arrangement:

- **Left pot lug 1**: −65 V (via step 24 + 10 kΩ R from strip lug 3)
- **Left pot lug 3**: −65 V (via this step + 10 kΩ R from strip lug 2)

Both ends of the pot's resistance element sit at −65 V! Why? Because the two 10 kΩ resistors form a **voltage divider** that the pot wiper taps into. Combined with the cathode return path (via 1 kΩ grid stoppers from the EL-34 grids), the pot wiper voltage is some compromise between −65 V and the per-channel cathode bias point. Turning the pot shifts that compromise, which adjusts the grid bias.

This isn't quite how I described it in earlier steps — Dynaco's bias circuit is more clever than a simple "wiper between negative and ground" topology. The two 10 kΩ resistors on the seven-lug strip combine with the bias pots to form a *current-mode* bias driver, which is more resilient to source voltage variation.

## See also

- [Step 22 — Second bias resistor](step-22-bias-resistor-2.md) — what else is on lug 2
- [Step 27 — Inter-pot wire (lug 3)](step-27-bias-pot-interconnect-1.md) — next wiring of the pot lug 3
- [Bias adjustment](../../bring-up/bias-adjustment.md) — what the pot wiper actually does
