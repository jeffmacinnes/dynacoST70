---
title: 'Step 34: V7 15.6 Ω cathode sense resistor'
---

# Step 34: 15.6 Ω resistor from V7 ground lug to V7 pin 1

> *Connect one end of the other 15.6 ohm resistor to the ground lug at the base of socket V7 (S). Connect the other end to pin #1 of V7.* — manual page 8

## What you're doing physically

Mirror of [step 31](step-31-v2-cathode-sense.md), but for the channel A pair (V6 and V7).

The second 15.6 Ω precision resistor lands between V7's chassis ground lug and **V7 pin 1**. (Note: V7 pin 1 here, not pin 8 like step 31 used. This DOES matter electrically: pin 1 is the suppressor grid (g3), not the cathode, and the two are NOT joined inside the tube — see [pinout](../../appendices/tube-pinouts.md). Pin 1 only becomes equivalent to pin 8 once the cathode daisy wire in [step 35](step-35-v6-v7-cathode-daisy.md) straps them together externally. The manual's sequence works because that strap is coming next.)

Chassis ground end is soldered (S); V7 pin 1 stays unsoldered for the next step.

## See also

- [Step 31 — V2 cathode sense](step-31-v2-cathode-sense.md) — the channel B equivalent
- [Step 35 — V6/V7 cathode daisy](step-35-v6-v7-cathode-daisy.md) — what V7 pin 1 connects to next
- [Bias adjustment](../../bring-up/bias-adjustment.md) — what the resistor enables
