---
title: Build
---

# Build progress

The procedural spine of the manual: every wiring step, in manual order, each with a level-2 explainer of what's happening electrically.

## Current physical build state

**Page 6, steps 1–6 soldered.** Next is [step 7](power-supply/step-07-hv-ct.md) — red-yellow center tap to the solder lug near the filter capacitor. This completes the HV rectifier circuit by establishing the ground return path for full-wave rectification.

## Sections

- **[Mechanical assembly (pages 4-5)](mechanical-assembly/index.md)** — mounting every component on the chassis: sockets, transformers, choke, filter cap, switches, fuse, terminal strips. Steps M1–M15.
- **[Power supply (page 6)](power-supply/index.md)** — first wiring phase: transformer leads, rectifier heater + anodes, heater windings, heater CTs, HV CT, OPT B+ feeds, choke, fuse/switch, right OPT secondaries. Steps 1–11.
- **[Output stage](output-stage/index.md)** — wiring steps 12-37: left OPT secondaries, OPT primary leads to EL-34s, bias network on 7-lug strip, cathode connections to Biaset sockets, grid stoppers.
- **[Driver stage](driver-stage/index.md)** — wiring steps 38-65: PC-3 board mounting, eyelet-to-tube-pin connections, B+ feeds to the board, input wiring, RCA jacks, input switch, power cord.
- **[Final assembly](final-assembly.md)** — chassis closure, dressing, final inspection.

## Power supply step status

| Step | Title | Written | Soldered |
|---|---|---|---|
| 1 | [Bias diode](power-supply/step-01-bias-diode.md) | ✅ | ✅ |
| 2 | [5AR4 heater (V1)](power-supply/step-02-5ar4-heater.md) | ✅ | ✅ |
| 3 | [5AR4 anodes (V1)](power-supply/step-03-5ar4-anodes.md) | ✅ | ✅ |
| 4 | [V2 heater](power-supply/step-04-v2-heater.md) | ✅ | ✅ |
| 5 | [V7 heater](power-supply/step-05-v7-heater.md) | ✅ | ✅ |
| 6 | [Heater center taps](power-supply/step-06-heater-cts.md) | ✅ | ✅ |
| 7 | [HV center tap](power-supply/step-07-hv-ct.md) | scaffold | pending |
| 8 | [OPT red leads to B+](power-supply/step-08-opt-b-plus.md) | scaffold | pending |
| 9 | [Choke](power-supply/step-09-choke.md) | scaffold | pending |
| 10 | [Primary fuse & switch](power-supply/step-10-primary-fuse-switch.md) | scaffold | pending |
| 11 | [Right OPT secondaries](power-supply/step-11-right-opt-secondaries.md) | scaffold | pending |

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
