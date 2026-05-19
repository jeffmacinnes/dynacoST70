---
title: Seven-lug terminal strip
---

# Seven-lug terminal strip

The seven-lug terminal strip is a small phenolic (or similar insulating) board with seven metal lugs sticking out of it, mounted to the chassis. Each lug is electrically isolated from the others and from the chassis itself. It's purely a **mechanical anchor point** for wires — like a junction box for the amp's wiring.

## Why it exists

In point-to-point wiring (the technique Dynaco used, as opposed to printed circuit boards), you can't just float wires in mid-air. You need physical anchor points where multiple wires can come together at a node. The terminal strip provides those points.

The seven-lug strip in the ST-70 collects a number of important ground-related signals over the course of the build. It's effectively the visible embodiment of the amp's ground network — see [grounding and hum](../theory/grounding-and-hum.md) for the wider context.

## Lug assignments (this build)

| Lug | What lands here | Step |
|---|---|---|
| 5 | Green/yellow heater CT | [Step 6](../build/power-supply/step-06-heater-cts.md) |
| 7 | Brown/yellow heater CT | [Step 6](../build/power-supply/step-06-heater-cts.md) |
| (others) | TBD — covered in later steps | |

## Why heater CTs go to separate lugs instead of one shared point

The two 6.3V heater windings power separate channels of the amp. Tying each CT to its own lug means each channel's heater CT eventually finds its way to ground via a path near *that channel's* signal circuitry. This is the beginning of the amp's **star grounding** architecture — see [step 6](../build/power-supply/step-06-heater-cts.md#why-separate-lugs-for-the-two-cts-5-and-7) for the detailed explanation.

## The philosophy

The terminal strip embodies a design value: **every electrical decision should be visible, traceable, and modifiable.** If you're troubleshooting a hum issue years later, you know where to look — all the grounding decisions are concentrated here rather than scattered across the chassis.

## See also

- [Step 6 — Heater CTs](../build/power-supply/step-06-heater-cts.md) — the first wires that land on the strip
- [Grounding and hum](../theory/grounding-and-hum.md) — the wider ground network
