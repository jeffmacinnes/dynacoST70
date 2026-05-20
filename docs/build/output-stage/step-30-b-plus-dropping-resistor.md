---
title: 'Step 30: 6.8 kΩ B+ dropping resistor'
---

# Step 30: 6.8 kΩ resistor between filter cap lugs 1 and 4

> *Trim the leads of the 6800 ohm resistor to 1". Connect one lead to lug #1 of the filter capacitor (S). Connect the other end to lug #4 of the filter capacitor.* — manual page 8

## What you're doing physically

Take the **6.8 kΩ resistor** (DynakitParts #114682). Trim its leads to 1" each side. Mount it spanning filter cap lugs 1 and 4. The lug 1 end is soldered (S) at this step; lug 4 stays unsoldered (more components land there in later steps).

## What this builds

This resistor extends the B+ chain to the next stage. Specifically, it drops the voltage from lug 1 (= "lug C", 415 V — the main B+ rail) down to lug 4 (= "lug B", 375 V — the screen/driver-stage feed).

Math:

- Voltage drop needed: 415 − 375 = 40 V
- Current through this resistor: ~6 mA (driver-stage current)
- Required resistance: 40 V / 6 mA = ~6.7 kΩ
- Actual value: 6.8 kΩ (closest standard E12 value)

Power dissipation: 6 mA × 40 V = 0.24 W. A ½ W resistor handles this comfortably with a 2× safety margin.

## Why a dropping resistor instead of a separate winding

The PA-060 could in principle have a separate HV tap that produces 375 V directly. It doesn't. Instead, the kit uses a single high-voltage winding (720 V CT) and derives lower voltages by dropping them with resistors.

Advantages of dropping resistors:

- **Simpler transformer**: one HV winding instead of multiple taps.
- **Cheaper**: a resistor costs $0.10; a transformer with extra taps costs significantly more.
- **Per-stage isolation**: each dropping resistor + cap = an RC filter that isolates the stages from each other (one stage's transients don't propagate to others).

Disadvantage: the resistor wastes some power as heat (0.24 W here — not much).

## Mapping back to manual lug numbers

Manual wiring uses lug 1/2/3/4 (physical numbering on the cap can). The voltage table uses lug A/B/C/D (function-based naming). The mapping:

| Manual wiring | Voltage table | Voltage |
|---|---|---|
| lug 2 | lug D | 435 V (rectifier output) |
| lug 1 | lug C | 415 V (after choke) |
| lug 4 | lug B | 375 V (after 6.8 kΩ — this step) |
| lug 3 | lug A | 305 V (after 22 kΩ — future step 42) |

## See also

- [Step 29 — Rectifier to filter cap](step-29-rectifier-to-filter-cap.md) — what feeds the cap
- [Step 42 — 22 kΩ dropping resistor](../driver-stage/step-42-22k-dropping-resistor.md) — the next stage in the chain
- [Voltage checks](../../bring-up/voltage-checks.md) — expected values at each lug
