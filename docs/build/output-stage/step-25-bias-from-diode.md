---
title: 'Step 25: Lug 4 to non-banded side of bias diode'
---

# Step 25: 6" wire from lug 4 (S) to the diode's non-banded side

> *Connect one end of a 6" wire to lug #4 of the 7 lug strip (S). Connect the other end to the non-banded side of the diode at the 2 lug terminal strip (S).* — manual page 7

## What you're doing physically

A 6" wire from lug 4 of the seven-lug strip to the **non-banded end** of the bias diode (the one mounted on the 2-lug strip in [M6](../mechanical-assembly/step-m06-bias-2lug-strip.md)). Both ends are soldered (S) at this step. The diode's **banded** end already has the 50 V AC input from step 1; this wire is the only connection at the non-banded end.

Lug 4 is also soldered final — it now has: the negative end of the first bias cap (step 19), the 10 kΩ resistor (step 20), and this wire.

## What this completes

This wire delivers the **diode's negative DC output** (~−65 V, after the diode does its half-wave rectification) up to the seven-lug strip where the filtering happens.

The bias supply path is now complete end-to-end:

1. **PA-060 bias winding** (RED/BLK, 50 V AC) → diode banded end (step 1)
2. **Diode** rectifies → negative pulsing DC at the non-banded end
3. **Non-banded end** → this step 25 wire → lug 4 of seven-lug strip
4. **Lug 4** → 10 kΩ → lug 3 → 10 kΩ → lug 2 (the cascade RC filtering)
5. **Lug 2** → distribution to bias pots (next step)

This may look reversed from the usual rectifier layout — the band marks the diode's cathode, and in a positive-output supply the cathode is where the DC comes out. But the bias supply needs **negative** DC, so the diode is flipped: the AC input from the PA-060 lands on the banded (cathode) end, and the negative DC output comes off the non-banded (anode) end, which is what this wire carries to lug 4.

## See also

- [Step 1 — Bias diode AC input](../power-supply/step-01-bias-diode.md) — RED/BLK lands on banded side
- [Step M6 — Bias 2-lug strip + diode](../mechanical-assembly/step-m06-bias-2lug-strip.md) — diode physical mounting
- [1N4007 historical context](../../modifications/1n4007-replacement.md) — what diode this is
