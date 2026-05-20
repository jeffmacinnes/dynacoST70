---
title: 'Step 25: Lug 4 to non-banded side of bias diode'
---

# Step 25: 6" wire from lug 4 (S) to the diode's non-banded side

> *Connect one end of a 6" wire to lug #4 of the 7 lug strip (S). Connect the other end to the non-banded side of the diode at the 2 lug terminal strip (S).* — manual page 7

## What you're doing physically

A 6" wire from lug 4 of the seven-lug strip to the **non-banded end** of the bias diode (the one mounted on the 2-lug strip in [M6](../mechanical-assembly/step-m06-bias-2lug-strip.md)). Both ends are soldered (S) at this step — the diode's non-banded end now has the 55 V AC input from step 1 AND this wire.

Lug 4 is also soldered final — it now has: the negative end of the first bias cap (step 19), the 10 kΩ resistor (step 20), and this wire.

## What this completes

This wire delivers the **diode's negative DC output** (~−65 V, after the diode does its half-wave rectification) up to the seven-lug strip where the filtering happens.

The bias supply path is now complete end-to-end:

1. **PA-060 bias winding** (RED/BLK, 55 V AC) → diode non-banded end
2. **Diode** rectifies → negative pulsing DC at the banded end
3. **Banded end** → this step 25 wire → lug 4 of seven-lug strip
4. **Lug 4** → 10 kΩ → lug 3 → 10 kΩ → lug 2 (the cascade RC filtering)
5. **Lug 2** → distribution to bias pots (next step)

Wait — let me re-check direction. The diode's banded end is the cathode (output of negative DC). The non-banded end is the anode (where the AC comes in). Step 1 already wired the **RED/BLK power transformer lead to the banded side** — so the banded side gets the AC input.

Hmm, that contradicts what I said. Let me look again at step 1...

[Reading step-01-bias-diode.md] "Connect the red-black power transformer lead to the banded side of the diode at the (2) lug terminal strip (S)" — yes, RED/BLK lands on the BANDED side. So the banded side IS the AC input here.

But that's reversed from normal convention — usually the band marks the cathode (DC output for a forward-biased rectifier). Why would Dynaco wire AC to the band?

Because for a **negative**-output bias rectifier, the diode is reversed relative to a normal positive-output rectifier. The band (cathode of the diode) faces the AC input; the anode of the diode (non-banded side) outputs the negative DC.

So:
- Banded side = AC input (RED/BLK from PA-060, step 1)
- Non-banded side = Negative DC output (this step 25 wire, going to lug 4)

Polarity reverses the conventional layout because the bias supply needs negative DC, not positive.

## See also

- [Step 1 — Bias diode AC input](../power-supply/step-01-bias-diode.md) — RED/BLK lands on banded side
- [Step M6 — Bias 2-lug strip + diode](../mechanical-assembly/step-m06-bias-2lug-strip.md) — diode physical mounting
- [1N4007 historical context](../../modifications/1n4007-replacement.md) — what diode this is
