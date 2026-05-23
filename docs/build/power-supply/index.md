---
title: Power supply
---

# Power supply wiring

The power supply wiring phase: every secondary of the [PA-060 power transformer](../../components/pa-060-power-transformer.md) gets connected to its destination (rectifier, heaters, bias diode, filter caps), and the primary side gets fused and switched.

This is conceptually the densest part of the build, because it's where the [theory](../../theory/index.md) chapters become concrete wiring. Each step pairs the verbatim manual instruction with a level-2 explainer.

The original manual covers this work on its **page 6**, with the exception of step 11 (right OPT secondaries), which is also physically on page 6 of the manual but belongs to the output stage functionally — we group it with [step 12](../output-stage/step-12-left-opt-secondaries.md) in the [output-stage section](../output-stage/index.md) instead.

## In this section

- **[Overview](overview.md)** — page 6 introduction, conventions, "complete power supply at a glance" diagram.
- **[Step 1 — Bias diode](step-01-bias-diode.md)** — red-black bias lead → 1N4007 cathode.
- **[Step 2 — 5AR4 heater](step-02-5ar4-heater.md)** — white pair → V1 pins 2 and 8.
- **[Step 3 — 5AR4 anodes](step-03-5ar4-anodes.md)** — red pair → V1 pins 4 and 6.
- **[Step 4 — V2 heater](step-04-v2-heater.md)** — green pair → V2 pins 2 and 7.
- **[Step 5 — V7 heater](step-05-v7-heater.md)** — brown pair → V7 pins 2 and 7.
- **[Step 6 — Heater CTs](step-06-heater-cts.md)** — green/yellow and brown/yellow CTs → seven-lug strip.
- **[Step 7 — HV center tap](step-07-hv-ct.md)** — red/yellow CT → filter cap ground area. *(Scaffold.)*
- **[Step 8 — OPT B+ feeds](step-08-opt-b-plus.md)** — OPT red leads → filter cap lug #1. *(Scaffold.)*
- **[Step 9 — Choke](step-09-choke.md)** — choke leads → filter cap lugs #1 and #2. *(Scaffold.)*
- **[Step 10 — Primary fuse & switch](step-10-primary-fuse-switch.md)** — primary black leads → fuse + switch. *(Scaffold.)*

Step 11 (right OPT secondaries) is the last numbered step on manual page 6 but lives in the [output-stage section](../output-stage/index.md) of these docs, next to its mirror image at step 12.

## Current build state

**Steps 1–6 are soldered.** Step 7 is next.

See the [build index](../index.md) for the full progress table.
