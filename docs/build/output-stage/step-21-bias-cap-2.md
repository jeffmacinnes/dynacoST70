---
title: 'Step 21: Second 100 µF bias filter cap'
---

# Step 21: 100 µF cap with negative end to lug 3, positive to lug 1

> *Connect the negative (-) end of the other 100 MFD capacitor to lug #3 of the 7 lug strip and the positive (+) end to lug #1.* — manual page 7

## What you're doing physically

The second 100 µF electrolytic. Negative end to lug 3, positive end to lug 1. Same polarity discipline as [step 19](step-19-bias-cap-1.md) — get the negative on the more-negative side.

Neither lug is soldered final at this step.

## What this cap does

Together with the 10 kΩ resistor from [step 20](step-20-bias-resistor-1.md), this cap forms the **second RC stage** of bias-supply filtering. The first stage (steps 19-20) cuts the 60 Hz half-wave ripple down to a tiny fraction; this second stage cuts that residue down again by a similar factor.

After both stages, the bias supply is far cleaner than anything the EL-34 grids could ever respond to. Effectively pure DC.

## Why two stages instead of one bigger cap

A single bigger cap would also smooth the ripple but uses much more capacitance. Cascade two stages of moderate-sized caps:

- 2× 100 µF caps + 2× 10 kΩ resistors = cheap and small.
- One stage would need ~10× more capacitance for the same ripple rejection.

Plus the cascaded RC pair has the secondary benefit of presenting higher source impedance into the rest of the network — which decouples the bias network from any transients on the rectifier output.

## See also

- [Step 19 — First bias cap](step-19-bias-cap-1.md) — first stage
- [Step 22 — Second bias resistor](step-22-bias-resistor-2.md) — the 10 kΩ this cap pairs with
