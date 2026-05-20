---
title: Home
---

# Dynaco ST-70 Build Manual

A working build manual for the Dynaco ST-70 stereo tube amplifier, capturing not just *what* to wire but *why* each connection works the way it does. Written alongside the build of a DynakitParts ST-70 kit (6GH8A driver board version).

## Purpose

The original Dynaco manual is procedural — it tells you which wire goes where, but assumes you already understand the underlying theory. This document fills in the gaps: what each connection is accomplishing electrically, why the circuit is designed that way, and how the components work together to produce music.

The goal is for a reader to come away with conceptual understanding, not just a working amplifier.

## How this is organized

- **[Getting started](getting-started/index.md)** — what the ST-70 is, the tools and workspace you need, and how to read this manual.
- **[Components](components/index.md)** — one page per significant part. What it is, how it works, where it lives in this build, failure modes.
- **[Theory](theory/index.md)** — conceptual chapters: transformers, rectification, heater circuits, grounding, push-pull topology.
- **[Build](build/index.md)** — step-by-step procedural pages, one per wiring step. Each step pairs the verbatim manual instruction with an explainer.
- **[Modifications](modifications/index.md)** — 3-prong cord, 1N4007 selenium replacement, individual bias pots, anti-click cap.
- **[Bring-up](bring-up/index.md)** — first power-on, voltage checks, bias adjustment, functional testing.
- **[Test equipment](test-equipment/index.md)** — DMM, oscilloscope, probes, variac, high-voltage safety.
- **[Appendices](appendices/index.md)** — tube pinouts, transformer specs, component theory deep dives, references.

## Current build state

See [build progress](build/index.md) for the live status. Short version as of the most recent edit:

- **Physical build:** Page 6, steps 1–6 soldered. Next is step 7 (red-yellow center tap to filter cap solder lug).
- **Documentation:** Steps 1–6 fully written. Steps 7–11 scaffolded only.

## Build configuration

- **Kit:** DynakitParts ST-70, 6GH8A driver board version
- **Power transformer:** Dynakit PA-060 (Pacific Transformer reproduction) — see [PA-060 page](components/pa-060-power-transformer.md)
- **Output transformers:** Dynakit A-470 (Pacific Transformer reproduction)
- **Output tubes:** Electro-Harmonix EL34 Apex Matched Quad
- **Rectifier:** Sovtek 5AR4
- **Driver tubes:** 6GH8A (with adapter set from Amplified Parts)

## Tube layout (this manual's numbering)

The chassis has **seven octal sockets**, numbered V1–V7. Five hold tubes; two (V4 and V5) are the front-panel **Biaset sockets** that hold no tubes — they're meter-probe points for bias adjustment (also wired as preamp power take-offs for legacy preamps that need 6.3V + B+). The 6GH8A drivers don't get a V-number — they're 9-pin miniatures mounted directly on the PC-3A board.

| Position | Designation | Tube / role |
|---|---|---|
| Chassis octal, near power transformer | V1 | 5AR4 rectifier |
| Chassis octals | V2, V3, V6, V7 | EL34 output tubes |
| Chassis octals, front panel | V4, V5 | Biaset sockets (no tube) |
| PC-3A board, 9-pin miniature | (no V-number) | 6GH8A driver/phase-splitters, one per channel |

!!! note
    This numbering differs from the "standard" ST-70 numbering found in some references, where V7 is the rectifier. Always defer to the specific manual that came with your kit.

## Conventions

See [reading this manual](getting-started/reading-this-manual.md) for the full convention list.

- **Manual text** quoted verbatim is set in blockquotes with italics.
- **(S)** in step instructions means *solder this connection now*.
- **Pin numbers** refer to the tube socket as viewed from the wiring side (bottom of the chassis).
- All voltages are AC unless noted as DC.
- "B+" refers to the high-voltage DC rail that powers the output tube plates (~450V DC nominal).

## License

Content licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Site code under MIT.
