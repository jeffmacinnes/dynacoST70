---
title: M12 — Seven-lug terminal strip
---

# M12: Mount the seven-lug terminal strip

> *Using #6 hardware, mount the seven lug terminal strip on the left side opposite the choke, following the position shown in the pictorial diagram. Tighten securely.* — manual page 5

## What you're doing physically

The **seven-lug terminal strip** is a long, thin phenolic strip with seven brass solder lugs arranged in a row. It's the main grounding anchor of the entire amp — see the dedicated [seven-lug terminal strip page](../../components/seven-lug-terminal-strip.md) for the full philosophy.

Mounting:

1. Locate it on the **LEFT** side of the chassis (looking from the front), **opposite the choke** mounted in [M11](step-m11-choke.md).
2. Two **#6 screws** go through the chassis from the top through the strip's mounting holes.
3. Tighten securely with #6 kep nuts from the strip side.

## Why opposite the choke

The seven-lug strip and the choke are roughly mirror-images of each other — both mount under the chassis on opposite sides. This balances the chassis weight distribution and creates symmetric wire-routing paths between the two channels.

## What will land on each lug

The seven lugs will be wired during later steps. Some are channel-specific, some serve both channels. From the [seven-lug page](../../components/seven-lug-terminal-strip.md):

| Lug | Purpose | Wired in |
|---|---|---|
| 1 | Ground (jumpered to lug 6) | later wiring steps |
| 2 | Bias divider bottom node | later wiring steps |
| 3 | Filtered bias feed to the pots | later wiring steps |
| 4 | Raw −65 V bias node (cap negative + diode feed) | later wiring steps |
| **5** | **Heater #1 CT (GRN/YEL)** | [step 6](../power-supply/step-06-heater-cts.md) |
| 6 | Ground tie to main ground at the quad cap | later wiring steps |
| **7** | **Heater #2 CT (BRN/YEL)** | [step 6](../power-supply/step-06-heater-cts.md) |

For now, just mount it. All the wiring happens in subsequent steps.

## Mounting orientation

The strip has lug-numbering printed (or implied by position) — lug 1 is on one end, lug 7 on the other. The Dynaco manual shows the orientation in the pictorial (page 22). Get this right at mount-time so future wiring steps land where they should.

## Why #6 hardware (not #4 or #8)

The seven-lug strip is mid-weight and needs more clamping force than #4 hardware can provide, but doesn't need the heavy #8 hardware used for transformers. #6 is the right middle ground.

## See also

- [Seven-lug terminal strip](../../components/seven-lug-terminal-strip.md) — the full role of this strip in the grounding network
- [Step 6 — Heater CTs](../power-supply/step-06-heater-cts.md) — the first wires that will land on lugs 5 and 7
- [Grounding and hum](../../theory/grounding-and-hum.md) — why concentrating ground connections here matters
