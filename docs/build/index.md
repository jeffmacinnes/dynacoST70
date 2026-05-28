---
title: Build
---

# Build progress

The procedural spine of the manual: every wiring step, in manual order, each with a level-2 explainer of what's happening electrically.

## Current physical build state

**Mechanical assembly done. Power supply wiring complete (steps 1–10). Output stage wiring soldered through step 24** — both OPT secondaries landed at their rear terminal strips, both OPT primaries running to the EL-34 plates and screen taps, the heater daisy chains closed, and the bias network on the seven-lug terminal strip built out and partly distributed to the bias pots.

Next is [step 25](output-stage/step-25-bias-from-diode.md) — wiring the bias supply's output (the banded end of the [1N4007 bias diode](power-supply/step-01-bias-diode.md)) to the seven-lug terminal strip's lug 4, which feeds the rest of the bias distribution network.

## Sections

- **[Mechanical assembly (pages 4-5)](mechanical-assembly/index.md)** — mounting every component on the chassis: sockets, transformers, choke, filter cap, switches, fuse, terminal strips. Steps M1–M15.
- **[Power supply](power-supply/index.md)** — first wiring phase: transformer leads, rectifier heater + anodes, heater windings, heater CTs, HV CT, OPT B+ feeds, choke, fuse/switch. Steps 1–10 (mostly manual page 6).
- **[Output stage](output-stage/index.md)** — wiring steps 11-37: OPT secondaries (right then left), OPT primary leads to EL-34s, bias network on 7-lug strip, cathode connections to Biaset sockets, grid stoppers.
- **[Driver stage](driver-stage/index.md)** — wiring steps 38-65: PC-3 board mounting, eyelet-to-tube-pin connections, B+ feeds to the board, input wiring, RCA jacks, input switch, power cord.
- **[Final assembly](final-assembly.md)** — chassis closure, dressing, final inspection.

## Step status — mechanical assembly (M1-M15)

Mechanical mounting on the chassis. None of these involve wiring yet.

See [mechanical assembly overview](mechanical-assembly/index.md) for the full step list. The 15 mechanical steps cover sockets, transformers, the choke, the filter cap, switches, fuse post, and terminal strips.

## Step status — wiring

Each section's step pages live under their own subsection; click the section link to see the full per-step status table.

| Section | Manual pages | Steps | Index |
|---|---|---|---|
| **Power supply** | 6 (steps 1–10) | 1–10 | [power-supply](power-supply/index.md) |
| **Output stage** | 6 (step 11) → 8 | 11–37 | [output-stage](output-stage/index.md) |
| **Driver stage** | 8–10 | 38–65 | [driver-stage](driver-stage/index.md) |

### Power supply — soldering progress

| Step | Title | Soldered |
|---|---|---|
| 1 | [Bias diode](power-supply/step-01-bias-diode.md) | ✅ |
| 2 | [5AR4 heater (V1)](power-supply/step-02-5ar4-heater.md) | ✅ |
| 3 | [5AR4 anodes (V1)](power-supply/step-03-5ar4-anodes.md) | ✅ |
| 4 | [V2 heater](power-supply/step-04-v2-heater.md) | ✅ |
| 5 | [V7 heater](power-supply/step-05-v7-heater.md) | ✅ |
| 6 | [Heater center taps](power-supply/step-06-heater-cts.md) | ✅ |
| 7 | [HV center tap](power-supply/step-07-hv-ct.md) | ✅ |
| 8 | [OPT red leads to B+](power-supply/step-08-opt-b-plus.md) | ✅ |
| 9 | [Choke](power-supply/step-09-choke.md) | ✅ |
| 10 | [Primary fuse & switch](power-supply/step-10-primary-fuse-switch.md) | ✅ |

Power supply wiring is **complete**.

### Output stage — soldering progress

| Step | Title | Soldered |
|---|---|---|
| 11 | [Right OPT secondaries](output-stage/step-11-right-opt-secondaries.md) | ✅ |
| 12 | [Left OPT secondaries](output-stage/step-12-left-opt-secondaries.md) | ✅ |
| 13 | [Right OPT primary](output-stage/step-13-right-opt-primary.md) | ✅ |
| 14 | [Left OPT primary](output-stage/step-14-left-opt-primary.md) | ✅ |
| 15 | [Disc caps on 7-lug strip](output-stage/step-15-disc-caps.md) | ✅ |
| 16 | [V6 ↔ V7 heater daisy](output-stage/step-16-v6-v7-heater-daisy.md) | ✅ |
| 17 | [V2 ↔ V3 heater daisy](output-stage/step-17-v2-v3-heater-daisy.md) | ✅ |
| 18 | [Bias jumper (lug 1 ↔ 6)](output-stage/step-18-bias-jumper.md) | ✅ |
| 19 | [First bias filter cap](output-stage/step-19-bias-cap-1.md) | ✅ |
| 20 | [First bias resistor](output-stage/step-20-bias-resistor-1.md) | ✅ |
| 21 | [Second bias filter cap](output-stage/step-21-bias-cap-2.md) | ✅ |
| 22 | [Second bias resistor](output-stage/step-22-bias-resistor-2.md) | ✅ |
| 23 | [Bias ground](output-stage/step-23-bias-ground.md) | ✅ |
| 24 | [Bias to left pot lug 1](output-stage/step-24-bias-pot-distribution-1.md) | ✅ |

**Currently:** output stage soldered through step 24. Next is [step 25 — Bias from diode](output-stage/step-25-bias-from-diode.md) — connecting the banded end of the bias diode (built way back in step 1) to lug 4 of the seven-lug terminal strip. This finally ties the bias supply *source* to the bias distribution network you've spent steps 18–24 assembling.

## Build configuration recap

- **Kit:** DynakitParts ST-70, 6GH8A driver board version
- **Power transformer:** Dynakit PA-060 (Pacific Transformer reproduction) — see [PA-060](../components/pa-060-power-transformer.md)
- **Output transformers:** Dynakit A-470 (Pacific Transformer reproduction)
- **Output tubes:** Electro-Harmonix EL34 Apex Matched Quad
- **Rectifier:** Sovtek 5AR4
- **Driver tubes:** 6GH8A (with adapter set from Amplified Parts)

## Modifications in this build

- [3-prong grounded power cord](../modifications/3-prong-cord.md) (safety)
- [Anti-click capacitor on power switch](../modifications/anti-click-cap.md)
- [Individual bias pots per output tube](../modifications/individual-bias-pots.md) (instead of original shared bias)
- VTA driver board deferred as future upgrade

The kit's silicon bias-supply diode (DynakitParts #544042) is now a stock component, not a modification — see [historical context](../modifications/1n4007-replacement.md) for the selenium rectifier it replaced in older ST-70s.
