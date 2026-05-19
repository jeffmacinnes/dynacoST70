---
title: EL34 output tube
---

# EL34 output tube

The EL34 is the workhorse pentode that produces the ST-70's output power. Four of them, configured as two push-pull pairs, drive the two [A-470 output transformers](a-470-output-transformer.md). This build uses an Electro-Harmonix EL34 Apex Matched Quad.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/el34-internal-structure.svg" alt="EL34 internal structure">
  <figcaption>Power pentode: cathode at the center, three grids (g1 control, g2 screen, g3 suppressor), and an outer plate. Hover any element or pin for spec and wiring details. Click to zoom.</figcaption>
</figure>

## Pinout (octal base, viewed from wiring side)

| Pin | Function | Notes |
|---|---|---|
| 1 | Internal connection / shield | Sometimes tied to ground |
| 2 | Heater | 6.3V AC |
| 3 | Plate (anode) | HV B+ via OPT primary |
| 4 | Screen grid (g2) | Slightly below B+ via dropping resistor |
| 5 | Control grid (g1) | Negative bias from bias supply |
| 6 | Internal connection | |
| 7 | Heater | 6.3V AC |
| 8 | Cathode | Usually grounded via small R |

*Page to be expanded.* Planned coverage:

- Pentode operation: cathode, control grid, screen grid, plate, and what each does
- Heater specs (6.3V at 1.5A per tube)
- Operating points: idle current, plate voltage, screen voltage in the ST-70 config
- Why we set bias and what happens if it drifts
- Triode-strap vs. ultralinear vs. pentode mode
- Failure modes: red-plating, screen failure, cathode poisoning
- Tube matching and why we use a "matched quad"
- EL34 vs. KT77 vs. 6CA7 vs. 6L6GC — what swaps are reasonable

## In this build

The EL34s occupy sockets **V2, V3, V6, V7**. They're driven by the [6GH8A phase splitters](6gh8a-driver-tube.md) on the [PC-3A board](pc-3a-driver-board.md).

Wiring steps that touch the EL34 sockets so far:

- [Step 4](../build/power-supply/step-04-v2-heater.md) — green pair → V2 heater
- [Step 5](../build/power-supply/step-05-v7-heater.md) — brown pair → V7 heater
- Later steps will land plate, screen, cathode, and grid connections on these sockets.

## See also

- [A-470 output transformer](a-470-output-transformer.md) — what the EL34 plates drive
- [Push-pull topology](../theory/push-pull-topology.md) — how the four EL34s work together
- [Individual bias pots modification](../modifications/individual-bias-pots.md) — the per-tube bias adjustment
