---
title: M10 — PA-060 power transformer
---

# M10: Mount the PA-060 power transformer

> *Mount the power transformer, PA-060, in the large center cutout. The wires should face the front of the chassis. Fasten the two mounting screws at the rear with #8 kep nuts. Place a cable clamp over each of the two front mounting screws and fasten with #8 kep nuts. The green, red and white pairs of wires should be threaded through the left cable clamp as should the green-yellow and brown-yellow ones. Pass the brown pair through the right clamp.* — manual page 5

## What you're doing physically

The PA-060 power transformer is the **largest, heaviest component** in the amp — roughly 3.5 lbs of iron and copper. It sits in the large rectangular cutout in the center of the chassis, with its leads (12" long pigtails) facing forward.

Mounting procedure:

1. Set the PA-060 on the chassis with the cutout centered under it.
2. Verify the leads exit toward the **front** of the chassis (the rear cutout edge is closer to the rear).
3. Insert four **#8-32 screws** from the top through the chassis into the transformer's mounting holes.
4. From the underside, the REAR two screws get **#8 kep nuts** only.
5. The FRONT two screws each get a **cable clamp** between the chassis underside and the kep nut.
6. Tighten all four to firm but not extreme torque.

Then thread the transformer's leads through the appropriate cable clamps for strain relief and routing:

| Leads | Through which clamp |
|---|---|
| GRN pair (heater #1) | Left cable clamp |
| RED pair (HV secondary) | Left cable clamp |
| WHT pair (rectifier filament) | Left cable clamp |
| GRN/YEL (heater #1 CT) | Left cable clamp |
| BRN/YEL (heater #2 CT) | Left cable clamp |
| BRN pair (heater #2) | Right cable clamp |

The two cable clamps separate the leads into two bundles — most secondaries go through the LEFT clamp; only the BRN heater pair goes through the RIGHT clamp. This routing keeps the leads organized and out of the way during subsequent wiring.

## Why the front-facing lead orientation matters

The wiring procedure assumes specific lead exit points. If you mount the transformer 180° rotated (leads facing the rear), all the lead-routing instructions in [the wiring procedure](../power-supply/index.md) become wrong-handed.

## Why #8 hardware

The PA-060 weighs ~3.5 lbs and the screws not only hold it down but transmit any vibration / impact load. #8-32 hardware is strong enough; #4 or #6 would strip or shear over time.

**Kep nuts** prevent the mounting screws from backing out due to thermal cycling and vibration. A plain hex nut would slowly loosen over 10-20 years; a kep nut bites in and stays.

## What the leads do (preview)

The PA-060 has these secondary windings, each documented per the [PA-060 page](../../components/pa-060-power-transformer.md):

| Lead | Voltage | Role |
|---|---|---|
| BLK pair (primary) | 120 V AC input | Mains connection |
| RED pair | 720 V AC CT (360-0-360) | High-voltage rectifier feed |
| RED/YEL | HV center tap | Returns to chassis ground (via solder lug at filter cap) |
| GRN pair | 6.3 V AC | Heater winding #1 (channel B — V2/V3, left) |
| GRN/YEL | Heater #1 CT | To lug 5 of seven-lug strip |
| BRN pair | 6.3 V AC | Heater winding #2 (channel A — V6/V7, right) |
| BRN/YEL | Heater #2 CT | To lug 7 of seven-lug strip |
| WHT pair | 5 V AC | Rectifier filament (GZ-34) |
| RED/BLK | 50 V AC | Bias supply input |

All of these will get wired in subsequent steps.

## Cable clamp tightness

Don't fully tighten the cable clamps yet. Thread the leads through them loosely; you'll snug the clamps later (manual step 9 of wiring procedure) after final lead positions are dressed.

## See also

- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — full specs and theory
- [Step 2 — 5AR4 heater](../power-supply/step-02-5ar4-heater.md) — first wiring step that uses the PA-060 leads
- [How transformers work](../../theory/how-transformers-work.md) — the physics underneath
