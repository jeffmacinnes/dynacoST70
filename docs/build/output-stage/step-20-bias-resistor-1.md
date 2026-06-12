---
title: 'Step 20: 10 kΩ resistor between lugs 4 and 3'
---

# Step 20: 10 kΩ resistor from lug 4 to lug 3

> *Select one 10,000 ohm resistor and connect one end of the resistor to lug #4 of the 7 lug strip and the other end to lug #3. Trim and form leads as needed.* — manual page 7

## What you're doing physically

One of the two **10 kΩ resistors** (#115103) lands between lug 4 and lug 3 of the seven-lug strip. Trim the resistor's leads to leave only what's needed to reach both lugs cleanly (about ½" of lead on each side). Neither lug is soldered final at this step.

## What this resistor does

The 10 kΩ + the 100 µF cap from [step 19](step-19-bias-cap-1.md) together form a **first-order RC low-pass filter** on the bias supply.

Math:

- Cutoff frequency: `f_c = 1 / (2π × R × C) = 1 / (2π × 10 kΩ × 100 µF) = 0.16 Hz`
- The bias rectifier is half-wave, so its ripple is at **60 Hz** — hundreds of times above that cutoff, so the stage knocks the ripple down by a factor of several hundred.

That's enormous attenuation. The 60 Hz ripple on the bias supply shrinks to a tiny fraction of its raw value after this RC stage — completely inaudible. The bias supply is essentially pure DC by the time it reaches the bias pots.

A second RC stage ([step 21](step-21-bias-cap-2.md) + [step 22](step-22-bias-resistor-2.md)) follows, doubling the filtering for good measure.

## See also

- [Step 19 — First bias cap](step-19-bias-cap-1.md) — the cap this resistor pairs with
- [Step 22 — Second bias resistor](step-22-bias-resistor-2.md) — the second stage of bias filtering
