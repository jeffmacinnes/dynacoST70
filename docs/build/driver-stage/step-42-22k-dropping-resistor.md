---
title: 'Step 42: 22 kΩ B+ dropping resistor'
---

# Step 42: 22 kΩ resistor from filter cap lug 3 (S) to lug 4

> *Cut the leads of a 22,000 ohm resistor to 1". Connect one end of the resistor to capacitor lug #3 (S). Connect the other end to capacitor lug #4.* — manual page 8

## What you're doing physically

The **22 kΩ resistor** (DynakitParts #114223) lands between filter cap lug 3 and lug 4. Trim leads to 1" each. Lug 3 is soldered (S) at this step — by now it has the step 41 wire + this resistor. Lug 4 stays unsoldered (more wires in step 43).

## What this builds

The full B+ chain dropping network is now:

| Filter cap lug | Voltage | What gets it there |
|---|---|---|
| 2 (= "D") | 435 V | Direct from rectifier (step 29) |
| 1 (= "C") | 415 V | After choke (step 9) |
| 4 (= "B") | 375 V | After 6.8 kΩ from lug 1 (step 30) |
| 3 (= "A") | 305 V | After this 22 kΩ from lug 4 |

Math for this resistor:

- Voltage drop: 375 − 305 = 70 V
- Current: ~3 mA (driver stage's input/screen current)
- Required resistance: 70 V / 3 mA ≈ 23 kΩ
- Actual value: 22 kΩ (closest E12)
- Power: 3 mA × 70 V = 0.21 W → ½ W resistor adequate

## Why the driver stage gets the LOWEST voltage

The 6GH8A pentode has a max plate voltage of 330 V (per the [6GH8A page](../../components/6gh8a-driver-tube.md)). Feeding it from 305 V (or 375 V via the screen) keeps it well within ratings while still providing enough headroom for the pentode's voltage swing.

If we tried to run the pentode from the main 415 V B+ rail, the plate load resistor would drop most of that — but the pentode itself would sit at near-saturation with very little signal swing room. The 22 kΩ dropper brings B+ down to a voltage where the pentode has room to swing.

## See also

- [Step 30 — 6.8 kΩ dropping resistor](../output-stage/step-30-b-plus-dropping-resistor.md) — previous stage in the chain
- [Step 43 — Eyelet #20 to lug 4](step-43-eyelet-20-to-cap-4.md) — what else lands at lug 4
- [Filter capacitors](../../components/filter-capacitors.md)
