---
title: Build
---

# Build progress

The procedural spine of the manual: every wiring step, in manual order, each with a level-2 explainer of what's happening electrically.

## Current physical build state

**Mechanical assembly done. Power supply wiring steps 1–10 soldered.** Next is [step 11](output-stage/step-11-right-opt-secondaries.md) — right output transformer secondary leads (BLACK, BROWN, ORANGE, YELLOW) to the right 4-screw terminal strip. Step 11 is the last step on manual page 6 but functionally belongs to the [output stage](output-stage/index.md), so we file it there alongside its mirror in step 12.

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

### Power supply — current soldering progress

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

**Currently:** power supply wiring soldered through step 10 (complete). Next is [step 11](output-stage/step-11-right-opt-secondaries.md) — right OPT secondary leads to the right 4-screw terminal strip — which kicks off the output stage.

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
