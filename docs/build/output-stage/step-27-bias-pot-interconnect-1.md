---
title: 'Step 27: Inter-pot wire (lug 3)'
---

# Step 27: 3" wire from right pot lug 3 (S) to left pot lug 3 (S)

> *Connect one end of a 3" wire to lug #3 of the right side bias potentiometer (S). Connect the other end to lug #3 of the left side bias potentiometer (S).* — manual page 7

## What you're doing physically

A short 3" wire connects lug 3 of the right pot to lug 3 of the left pot. Both ends are soldered (S) at this step.

For the left pot, lug 3 now has the step 26 wire (from seven-lug strip lug 2) + this jumper. For the right pot, lug 3 has only this jumper (the right pot hasn't been wired to anything else yet).

## What this completes

By connecting the two pots' lug-3 terminals, both pots now share the same voltage at that end of their resistance elements — the bias divider's bottom node (≈ −22 V, fed from strip lug 2). This is an intermediate node of the divider, not the raw −65 V rail; together with step 28 (which ties the lug-1 ends), the two inter-pot wires place both pots in parallel across the same section of the divider.

The right channel's bias supply doesn't need its own separate wire from the seven-lug strip — it shares the left channel's supply via this inter-pot jumper. This works because:

1. The bias supply has very little current draw (it just sets a voltage on the EL-34 grids, which draw essentially no current at idle).
2. The 3" wire has negligible resistance, so the two pots effectively see identical source voltages.

A single bias supply driving both channels is simpler than two separate supplies, and there's no electrical reason to keep them isolated for bias purposes.

## See also

- [Step 28 — Inter-pot wire (lug 1)](step-28-bias-pot-interconnect-2.md) — mirror of this step for the other pot end
- [Step 24 — Lug 1 distribution](step-24-bias-pot-distribution-1.md) — what lug 1 of the left pot gets
- [Bias adjustment](../../bring-up/bias-adjustment.md) — how the per-channel pots interact
