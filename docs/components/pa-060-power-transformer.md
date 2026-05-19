---
title: PA-060 power transformer
---

# PA-060 power transformer

The PA-060 is the Dynakit-branded Pacific Transformer reproduction of the original Dynaco ST-70 power transformer. It produces every voltage the amp needs — high-voltage DC for the plates, low-voltage AC for the heaters, and a small negative bias supply — from a single primary, with five separate secondary windings.

## What it is

A multi-secondary mains transformer designed specifically for the ST-70. One primary takes in 120V AC from the wall; five secondaries provide the various voltages the amp's tubes need. Physically it's a heavy steel-can transformer mounted on the chassis between the rectifier socket and the output transformers.

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../assets/diagrams/pa-060-windings.svg" aria-label="PA-060 power transformer winding diagram">
    PA-060 winding diagram (your browser does not support inline SVG).
  </object>
  <figcaption>Primary on the left, five color-coded secondaries on the right. Hover any winding for its voltage, current, and where it lands in the build.</figcaption>
</figure>

## Windings (the spec sheet)

The PA-060 has one primary (120V AC, 50–60Hz) and **five separate secondary windings**, each engineered for a specific job:

| Winding | Voltage | Current | Purpose |
|---|---|---|---|
| RED ↔ RED with RED/YEL center tap | 720V AC CT | 300mA | Main HV — feeds the 5AR4 rectifier, becomes ~450V B+ |
| RED/BLK ↔ RED/YEL CT | 55V AC | (low) | Bias winding — feeds the 1N4007, produces negative grid bias |
| GRN ↔ GRN with GRN/YEL CT | 6.3V AC | 5A | Heater winding #1 — for half the signal/output tubes |
| BRN ↔ BRN with BRN/YEL CT | 6.3V AC | 5A | Heater winding #2 — for the other half of the signal/output tubes |
| WHT ↔ WHT | 5V AC | 4A | Heater for the 5AR4 rectifier (different voltage from other tubes) |

### Why the color coding makes sense

| Color family | What it carries |
|---|---|
| **RED** | Main high-voltage AC (the dangerous winding) |
| **RED/BLK** | Bias winding (related to RED but distinguished) |
| **WHT** | 5V rectifier heater |
| **GRN** | 6.3V heater #1 |
| **BRN** | 6.3V heater #2 |
| **/YEL suffix** | Center tap of whatever winding it belongs to |

Two wires of the same base color = the two ends of the same winding. The colors keep different windings visually distinct so you don't accidentally cross them during wiring.

## How it works

The PA-060 is a standard mains transformer in physical principle — see [how transformers work](../theory/how-transformers-work.md) for the underlying theory. What's specific to this transformer is the **five-secondary topology**, where each winding is purpose-built for one job in the amp.

## Why two 6.3V heater windings instead of one big one

Splitting the heater current across two windings has several practical benefits:

1. **Less load on any single winding** — easier on the wire gauge and insulation.
2. **Better hum balance** — each channel of the amp can have its own heater supply with its own center-tap-to-ground reference, reducing inter-channel hum coupling.
3. **Symmetric layout** — the two windings can be physically placed on opposite sides of the bobbin, helping balance the magnetic flux in the core.
4. **Hum cancellation between channels** — heater hum in one channel is uncorrelated with the other, so it doesn't sum coherently in the final output.

See the [step 5 explainer](../build/power-supply/step-05-v7-heater.md#why-two-separate-63v-heater-windings-instead-of-one) for the full discussion.

## Why the 5AR4 gets its own dedicated winding

The 5AR4 was designed for **5V filaments** — most other tubes in the amp use 6.3V. You can't share these. See [heater circuits](../theory/heater-circuits.md#why-5v-for-the-5ar4-and-63v-for-everything-else).

## In this build

The PA-060 sits on the top of the chassis with its leads dropping through to the underside, where they're routed and connected during page 6 of the manual. Specific steps that touch the PA-060:

- [Step 1](../build/power-supply/step-01-bias-diode.md) — red-black bias winding lead → 1N4007
- [Step 2](../build/power-supply/step-02-5ar4-heater.md) — white pair → V1 (5AR4) filament
- [Step 3](../build/power-supply/step-03-5ar4-anodes.md) — red pair → V1 (5AR4) anodes
- [Step 4](../build/power-supply/step-04-v2-heater.md) — green pair → V2 heater
- [Step 5](../build/power-supply/step-05-v7-heater.md) — brown pair → V7 heater
- [Step 6](../build/power-supply/step-06-heater-cts.md) — green/yellow and brown/yellow CTs → seven-lug terminal strip
- [Step 7](../build/power-supply/step-07-hv-ct.md) — red/yellow HV CT → filter cap area
- [Step 10](../build/power-supply/step-10-primary-fuse-switch.md) — primary black leads → fuse + switch

## Failure modes

- **Open winding** — most common after decades. Usually a thermal failure in one secondary. Detectable with a continuity test.
- **Shorted turns** — produces excess current draw on the primary and hum/heat. Harder to diagnose without specialized equipment.
- **Insulation breakdown** — typically between primary and secondary. Catastrophic when it happens; the amp goes from quiet to deadly.

The original Dynaco PA-060s have mostly held up well. The Pacific Transformer reproductions are built to similar standards.

## See also

- [How transformers work](../theory/how-transformers-work.md) — general transformer theory
- [Heater circuits](../theory/heater-circuits.md) — what happens with the 6.3V and 5V windings
- [Rectification](../theory/rectification.md) — what happens with the 720V CT winding
- [Transformer specs](../appendices/transformer-specs.md) — at-a-glance reference data
- [A-470 output transformer](a-470-output-transformer.md) — the other transformer in the build
