---
title: 'Step 28: Inter-pot wire (lug 1)'
---

# Step 28: 3" wire from right pot lug 1 (S) to left pot lug 1 (S)

> *Connect one end of a 3" wire to lug #1 of the right side bias potentiometer (S). Connect the other end to lug #1 of the left side potentiometer (S).* — manual page 7

## What you're doing physically

Mirror of [step 27](step-27-bias-pot-interconnect-1.md). A 3" wire joins lug 1 of the right pot to lug 1 of the left pot. Both ends soldered (S).

For the left pot, lug 1 has the step 24 wire (from seven-lug strip lug 3) + this jumper. For the right pot, lug 1 now connects to the bias supply network via the left pot.

## What this completes

Both pots' lug 1 terminals are now tied together at the voltage fed from strip lug 3 — the more negative intermediate node of the bias divider. The two pot ends do **not** sit at the same potential: lug 1 is the more negative end, lug 3 (tied in step 27) is the less negative end (≈ −22 V, the divider's bottom node at strip lug 2). Combined with [step 27](step-27-bias-pot-interconnect-1.md), the inter-pot wires place **both pots in parallel across the same section of the divider**.

This means turning the left pot affects only the left channel's grid bias (via the wiper, lug 2), and turning the right pot affects only the right channel — even though they share both supply rails.

The wiper (lug 2) is what the EL-34 grids see, and that's wired in later steps (47 and 57) connecting the wipers to the PC-3A board's bias-distribution eyelets.

## After step 28

The bias supply network is complete:

- ✅ Bias diode rectifying 50 V AC → ~−65 V DC pulsing
- ✅ Two stages of RC filtering on the seven-lug strip → clean DC
- ✅ Distribution to both bias pots
- ✅ Both pots tied together at both ends

The grid voltage at each pot's wiper now depends on the cathode network (steps 31-36 below), since the bias loop closes through the EL-34 grid → grid stopper → coupling cap → driver board → ... back to the bias supply.

## See also

- [Step 27 — Inter-pot wire (lug 3)](step-27-bias-pot-interconnect-1.md) — the mirror
- [Step 47 — Eyelet 21 to right pot wiper](../driver-stage/step-47-eyelet-21-to-right-pot.md) — where the wiper meets the driver board
- [Bias adjustment](../../bring-up/bias-adjustment.md)
