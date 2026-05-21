---
title: Step 7 — HV center tap
---

# Step 7: Connect the red-yellow lead to the filter capacitor solder lug

> *Connect the red-yellow lead to the solder lug near the filter capacitor.* — manual page 6

## What you're doing physically

A single lead exits the PA-060 — **RED with a YELLOW tracer** — and it lands at the **main solder lug near the filter capacitor** (the lug installed in [M15](../mechanical-assembly/step-m15-ground-lugs.md)). The lug end stays unsoldered for now; many more wires will arrive there over the next 50+ steps, and they all get soldered together in [step 64](../driver-stage/step-64-star-ground-completion.md).

## Why the red-yellow lead is special

The PA-060's high-voltage secondary is a single winding of 720 V AC total, but it has a **center tap** brought out separately as the red-yellow lead. The two **RED leads** (already wired to V1 pins 4 and 6 in [step 3](step-03-5ar4-anodes.md)) are the two **ends** of that 720 V winding; RED/YEL is the **midpoint** of the same winding.

Voltage-wise, with the midpoint grounded:

- RED end #1: swings between +360 V and −360 V (relative to RED/YEL)
- RED/YEL: 0 V (chassis ground)
- RED end #2: swings opposite phase — between −360 V and +360 V

When one RED end is at +360 V, the other is at −360 V. They're always exactly opposite.

## How this completes full-wave rectification

[Step 3](step-03-5ar4-anodes.md) wired the two RED ends to the 5AR4's two anode pins. The 5AR4 has two internal diodes — one for each anode → cathode. Each diode conducts only during the half-cycle when its anode is positive relative to the cathode.

Without a grounded center tap, the rectifier circuit had no return path — there was nothing for current to flow back through. With this step, RED/YEL gets pinned to chassis ground, and the current path completes:

1. RED end (say, end #1) → positive → through 5AR4 anode #1 → cathode (V1 pin 8) → through the filter cap to ground
2. From ground, back through this RED/YEL wire to the transformer center tap
3. Through the transformer winding back to RED end #1

Same loop happens on the other half-cycle, just using anode #2 and the other half of the winding. Both halves of the AC cycle produce positive DC at the rectifier cathode — full-wave rectification.

Until this step, every winding has been wired but **none have had a return path established**. This is the first wire that creates a complete current loop for any of the PA-060's secondaries.

## Why route to the filter cap area

The center tap carries every milliamp of B+ current as it returns from the rest of the circuit. That's hundreds of milliamps. The physical wire path needs to be:

- **Short** — minimize voltage drop and inductance.
- **Direct** — fewer joints means fewer failure points.
- **Near the filter cap** — the filter cap's negative terminal is also at this same node (signal ground), and putting both at the same lug minimizes the loop area for the high-current rectifier circuit.

The main solder lug near the filter cap is the **star ground point** of the amp. Eventually six wires will land here. The HV CT is the first.

## See also

- [Step 3 — 5AR4 anodes](step-03-5ar4-anodes.md) — the two RED leads this CT completes
- [Step M15 — Main ground lugs](../mechanical-assembly/step-m15-ground-lugs.md) — the lug this wire lands on
- [Step 64 — Star ground completion](../driver-stage/step-64-star-ground-completion.md) — when the lug finally gets soldered
- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — the HV winding structure
- [Rectification](../../theory/rectification.md) — full theory of full-wave rectification
- [Grounding and hum](../../theory/grounding-and-hum.md) — why the star ground point matters
- [Previous: Step 6](step-06-heater-cts.md) · [Next: Step 8 — OPT B+ feeds](step-08-opt-b-plus.md)
