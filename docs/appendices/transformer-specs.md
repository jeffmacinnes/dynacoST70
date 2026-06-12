---
title: Transformer specs
---

# Transformer specs

Reference data for the two transformers in this build. The full conceptual treatment is in the per-component pages — this is the at-a-glance card.

## PA-060 power transformer

See the [full PA-060 page](../components/pa-060-power-transformer.md) for the deeper writeup.

| Winding | Voltage | Current | Purpose |
|---|---|---|---|
| RED ↔ RED with RED/YEL center tap | 720V AC CT | 300mA | Main HV — feeds the 5AR4 rectifier, becomes ~450V B+ |
| RED/BLK ↔ RED/YEL CT | 50V AC | (low) | Bias tap — feeds the 1N4007, produces negative grid bias |
| GRN ↔ GRN with GRN/YEL CT | 6.3V AC | 5A | Heater winding #1 — for half the signal/output tubes |
| BRN ↔ BRN with BRN/YEL CT | 6.3V AC | 5A | Heater winding #2 — for the other half of the signal/output tubes |
| WHT ↔ WHT | 5V AC | 4A | Heater for the 5AR4 rectifier (different voltage from other tubes) |

### Color coding logic

| Color family | What it carries |
|---|---|
| **RED** | Main high-voltage AC (the dangerous winding) |
| **RED/BLK** | Bias winding (related to RED but distinguished) |
| **WHT** | 5V rectifier heater |
| **GRN** | 6.3V heater #1 |
| **BRN** | 6.3V heater #2 |
| **/YEL suffix** | Center tap of whatever winding it belongs to |

Two wires of the same base color = the two ends of the same winding.

## A-470 output transformer

| Lead | Purpose | Notes |
|---|---|---|
| Blue | Plate, one side | Push-pull primary, one end |
| Blue/White | Plate, other side | Push-pull primary, other end |
| Red | Primary center tap | B+ feed in |
| Green | UL screen tap | Same half of the winding as the blue plate |
| Green/White | UL screen tap | Same half of the winding as the blue/white plate |
| Black (secondary) | Speaker common | Secondary tap 0 |
| Brown (secondary) | 4Ω secondary tap | |
| Orange (secondary) | 8Ω secondary tap | |
| Yellow | 16Ω secondary tap | |

Original A-470 spec: −1dB from 6Hz to 30kHz at full power.

!!! note "Plates vs. screen taps"
    Both blue leads are plates and both green leads are screen taps — don't pair the leads by base color. Each plate works with the *other*-colored screen tap on its half of the winding (BLUE + GREEN, BLU/WHT + GRN/WHT).

## Tube layout reference

The chassis has **seven octal sockets** total. Five hold tubes; two are front-panel **Biaset sockets** that hold no tubes (they're meter-probe points for bias adjustment, also wired as preamp power take-offs for legacy preamps that need 6.3V + B+). The 6GH8A drivers don't get a chassis V-number — they're 9-pin miniatures mounted directly on the PC-3A board.

| Position | Designation | Tube / role |
|---|---|---|
| Chassis octal, near power transformer | V1 | 5AR4 rectifier |
| Chassis octals | V2, V3, V6, V7 | EL34 output tubes |
| Chassis octals, front panel | V4, V5 | Biaset / preamp power take-off (no tube) |
| PC-3A board, 9-pin miniature | (no V-number) | 6GH8A driver/phase-splitters, one per channel |
