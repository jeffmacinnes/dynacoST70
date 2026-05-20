---
title: 'Step 31: V2 15.6 Ω cathode sense resistor'
---

# Step 31: 15.6 Ω resistor from V2 ground lug to V2 pin 8

> *Connect one end of a 15.6 ohm resistor to the ground lug on base of V2 socket (S). Connect the other end to pin #8 of V2.* — manual page 8

## What you're doing physically

A **15.6 Ω 1% precision resistor** (DynakitParts #120150) lands between V2's chassis ground lug (the metal tab on the base of the V2 socket, bonded to chassis) and V2 pin 8. The chassis ground end is soldered (S) immediately; V2 pin 8 stays unsoldered (more wires land there in step 32).

## What this resistor is for

This is the **stock cathode sense resistor** for the channel B EL-34 pair (V2 and V3). It does two things:

1. **Sets up the bias measurement**. With both V2 and V3 cathodes tied together (step 32 next) and routed through this single 15.6 Ω to ground, the voltage across the resistor equals the *combined* cathode current of both tubes × 15.6. At the target bias (50 mA per tube × 2 tubes = 100 mA combined), V = 100 mA × 15.6 Ω = 1.56 V.
2. **Provides cathode degenerative feedback**. The 15.6 Ω adds a small voltage drop that's proportional to the cathode current — that voltage subtracts from the grid-cathode bias, providing a self-correcting effect (cathode current rises → cathode voltage rises → effective bias becomes more negative → cathode current drops back down). This stabilises the operating point against thermal drift and tube aging.

## Why the precise value 15.6 Ω

A round-number choice would be 15 Ω or 16 Ω. The manual uses 15.6 Ω specifically so that the target voltage reads as a memorable round number:

- 100 mA × 15.6 Ω = **1.56 V** exactly

If you ever lose your bias-target reference, you can recover it: "1.56 V" matches "1.56 V" — easy to remember. 15 Ω would have given 1.5 V; 16 Ω would have given 1.6 V. Less mnemonic.

## When this gets used

This resistor is the measurement element for the **stock bias procedure** (see [bias adjustment](../../bring-up/bias-adjustment.md)). The voltage across this resistor will be sampled by the **Biaset socket V4**, wired in [step 33](step-33-v3-to-left-biaset.md).

If you've installed the [individual bias pots modification](../../modifications/individual-bias-pots.md), this resistor would be removed in favor of one 1 Ω resistor per tube. The mod also bypasses the Biaset sockets.

## See also

- [Step 32 — V2/V3 cathode daisy](step-32-v2-v3-cathode-daisy.md) — ties V2 and V3 cathodes together
- [Step 33 — V3 to left Biaset](step-33-v3-to-left-biaset.md) — routes the measurement to V4
- [Bias adjustment](../../bring-up/bias-adjustment.md) — the procedure this enables
- [Individual bias pots](../../modifications/individual-bias-pots.md) — what this gets replaced with under the mod
