---
title: 'Step 29: Rectifier output to filter cap lug 2'
---

# Step 29: 5¼" wire from V1 pin 8 (S) to filter cap lug 2 (S)

> *Connect one end of a 5 ¼" wire to lug #8 of V1 (S). Connect the other end to lug #2 of the quad filter capacitor (S).* — manual page 8

## What you're doing physically

A 5¼" wire connects V1 pin 8 (the GZ-34's cathode = rectified DC output) to lug 2 of the quad filter cap. Both ends are soldered (S) — this is a high-current path that needs solid joints.

## What this completes

This is the **main B+ rail's first wire**. The full HV rectification path now exists end-to-end:

1. PA-060 secondary RED leads (720 V CT) → V1 pins 4 and 6 (HV anodes) — wired in [step 3](../power-supply/step-03-5ar4-anodes.md)
2. GZ-34 rectifies → V1 pin 8 (cathode) carries pulsing DC
3. This wire delivers that DC to filter cap lug 2 (which is "lug D" in the voltage table — the highest voltage in the amp, ~435 V at idle)
4. The cap's 30 µF section at lug D smooths the pulsing DC into ~10 V-ripple DC

From lug D, the choke (already wired in [step 9](../power-supply/step-09-choke.md)) drops the DC further with the second filter cap section to land at lug C (~415 V, the main B+ rail).

The choke's other end is wired in step 9 to lug 1 of the filter cap (= "lug C"). So after this step 29 + step 9, the full smoothing chain exists: rectifier → lug D → choke → lug C → out to the rest of the amp via lug C wire (the OPT primary CT feeds, step 8).

## High-current path

The current flowing through this wire is significant — peaks of ~300 mA during the cap-charging portion of each rectifier cycle (the brief moments at the top of each half-wave when the rectifier conducts and rapidly recharges the cap). Average DC is ~200 mA.

The 5¼" length is chosen to be just long enough to route cleanly between V1 and the filter cap. Don't add excess length — the longer this wire is, the more inductance it has, and inductance in the rectifier-cap path causes voltage spikes that can stress the rectifier and the cap.

## See also

- [Step 3 — 5AR4 anodes](../power-supply/step-03-5ar4-anodes.md) — HV input to V1
- [Step 9 — Choke](../power-supply/step-09-choke.md) — what comes after the first filter cap
- [Filter capacitors](../../components/filter-capacitors.md) — the can this wire lands on
- [Rectification](../../theory/rectification.md) — full theory of what's happening
