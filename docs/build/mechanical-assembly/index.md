---
title: Mechanical assembly (pages 4-5)
---

# Mechanical assembly — pages 4-5

Before any wiring, every major component gets mechanically mounted to the chassis. 15 steps total, all on pages 4-5 of the manual.

The manual is brief on these — most steps are "put the thing in the hole and bolt it down." This documentation adds a level-2 explainer for each one: *why* that thing goes in that orientation, what gets affected if you mount it wrong, and any one-time decisions (like ground lug placement) that lock in later wiring choices.

## Step status

| Step | Title | Manual step |
|---|---|---|
| M1 | [Octal sockets](step-m01-octal-sockets.md) | 1 |
| M2 | [Input connector](step-m02-input-connector.md) | 2 |
| M3 | [Mono/stereo input switch](step-m03-input-switch.md) | 3 |
| M4 | [Rear 4-screw terminal strips](step-m04-rear-terminal-strips.md) | 4 |
| M5 | [Bias potentiometers](step-m05-bias-pots.md) | 5 |
| M6 | [Bias 2-lug strip with diode](step-m06-bias-2lug-strip.md) | 6 |
| M7 | [Power cord grommet](step-m07-grommet.md) | 7 |
| M8 | [Fuse post](step-m08-fuse-post.md) | 8 |
| M9 | [On-off switch](step-m09-on-off-switch.md) | 9 |
| M10 | [PA-060 power transformer](step-m10-pa-060.md) | 10 |
| M11 | [C-354 choke](step-m11-choke.md) | 11 |
| M12 | [Seven-lug terminal strip](step-m12-seven-lug-strip.md) | 12 |
| M13 | [A-470 output transformers](step-m13-output-transformers.md) | 13 |
| M14 | [Quad filter capacitor](step-m14-filter-cap.md) | 14 |
| M15 | [Main ground solder lug(s)](step-m15-ground-lugs.md) | 15 |

## General principles

A few things apply across most steps:

### Tightening hardware

- **#4-40 hardware** (small screws) is used for sockets, the input connector, the input switch, the bias pots, and the on-off switch. Torque to "snug" — these threads strip easily.
- **#6 hardware** is used for the seven-lug terminal strip and the bottom plate.
- **#8 hardware** is used for the power transformer (PA-060), the choke, the output transformers (A-470), and the cable clamps. These carry weight; tighten firmly.
- **Kep nuts** (the ones with a built-in lock washer) prevent vibration loosening — used wherever long-term mechanical stability matters.

### Socket keyways

The seven octal sockets have a small slot or keyway in their center hole. This must face the same direction across all sockets — refer to the wiring pictorial (manual page 22). If you mount them with random orientations, you can't follow the pin-numbered wiring steps without mentally rotating the pinout each time.

### Two countersunk holes per fastener

Most chassis-mount components have **countersunk** holes — the bevel goes on the **top** of the chassis (where the screw head sits). Mount from the top, fasten from underneath with a kep nut.

### Mounting from above vs. below

- Components on the TOP of the chassis (transformers, tubes when inserted): screw goes through the chassis from the top, nut underneath.
- Components hanging UNDER the chassis (choke, filter cap, terminal strips): screws go through the chassis from the top, components are bolted to the underside.

## What's different on a modern kit

The 2017 DynakitParts manual notes a few minor variations from the original 1959 kit:

- **One solder lug** at the main ground point, where the original called for two (manual step 15 marginalia).
- The diode in step 6 is a **silicon diode** (1N4007-class), not the original selenium rectifier. See [historical context](../../modifications/1n4007-replacement.md).
- Otherwise the parts and mounting are identical to the original.

## See also

- [Power supply wiring overview](../power-supply/overview.md) — starts after all mechanical assembly is done
- [Reading this manual](../../getting-started/reading-this-manual.md) — conventions used in step pages
