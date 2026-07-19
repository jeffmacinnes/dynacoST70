---
title: Step 9 — Choke
---

# Step 9: Feed choke leads through right cable clamp to filter cap lugs #1 and #2

> *Feed the two choke leads through the right cable clamp, connect one lead to filter capacitor lug #2 and the other lead to lug #1. (These leads can be trimmed as required). Tighten the two nuts holding the cable clamps.* — manual page 6

## What you're doing physically

The C-354 choke (mounted under the chassis in [M11](../mechanical-assembly/step-m11-choke.md)) has two leads — both about 6" long, both the same gauge, both unpolarized. Feed both through the **right cable clamp** (so they're strain-relieved along their path), then:

- One lead → filter cap **lug #2** (S — soldered final at this step)
- Other lead → filter cap **lug #1** (still unsoldered; gets sealed with the OPT red leads from [step 8](step-08-opt-b-plus.md) in this same soldering operation)

After both choke leads are landed and the OPT red leads (from step 8) are also in place at lug 1, **tighten the cable clamps' mounting nuts** to lock all the wires in place.

## Which lead goes to which lug?

Doesn't matter. The choke is **symmetric** — it's a single coil of wire on an iron core, electrically indistinguishable end-to-end. Connect whichever lead is closer to whichever lug.

## What this builds — the LC pi-filter

The choke is the inductor in the classic **LC pi-filter** that smooths B+ ripple. After this step, the B+ chain looks like:

| Node | Voltage | What's there |
|---|---|---|
| V1 pin 8 (5AR4 cathode) | ~440 V pulsing | Rectifier output |
| Filter cap lug 2 ("D") | ~435 V, ~40 Vp-p ripple | First filter cap section (30 µF) |
| Choke (one lead at lug 2, other at lug 1) | ~15–20 V drop under load (435 → 415 V per the manual's chart; 428 → 413 V measured on this build, matching its 71 Ω DCR × 212 mA) | Smoothing inductor |
| Filter cap lug 1 ("C") | ~415 V, ~2–3 Vp-p ripple | Second filter cap (20 µF) — main B+ rail |
| Out via [step 8](step-08-opt-b-plus.md) RED leads | ~415 V | Feeds OPT primaries → EL-34 plates |

The choke + second cap together form a **second-order low-pass filter**. At 120 Hz (the full-wave ripple frequency), the filter provides about 25 dB of attenuation — turning ~40 Vp-p of sawtooth ripple at lug 2 into ~2–3 Vp-p at lug 1 (both values measured on this build). The push-pull output stage rejects most of what remains, and the further RC stages drop the driver-board rails into the millivolts. That's quiet enough for tube audio.

For the full theory and frequency-response math, see [choke](../../components/choke.md) and [rectification — smoothing](../../theory/rectification.md#smoothing-from-pulsating-dc-to-clean-dc).

Note: at this point in the build, the rectifier output isn't yet wired to lug 2 — that wire (V1 pin 8 → cap lug 2) comes later in [step 29](../output-stage/step-29-rectifier-to-filter-cap.md). So the choke is wired *between* the two filter cap sections, ready to carry current as soon as the rest of the B+ chain comes together.

## Why both leads through one clamp

The right cable clamp gets the choke leads; the left clamp got the OPT-related leads in [step 8](step-08-opt-b-plus.md). Splitting the wire bundle keeps the routes orderly and avoids cramming everything into a single bottleneck.

## Tightening the clamps

After all four wires (two OPT red leads + two choke leads) are landed and the lug 1 / lug 2 solder joints are flowed, the cable clamps' mounting nuts get tightened. This is permanent strain relief — once tightened, the wires stay where they are for the life of the amp.

If you ever need to remove the PA-060 (rare; happens during major repairs), loosen the clamp nuts first, then unsolder the wire ends — don't try to slip the wires out without unclamping.

## See also

- [Choke (C-354)](../../components/choke.md) — full specs and theory of this part
- [Step M11 — Choke mounting](../mechanical-assembly/step-m11-choke.md) — where the choke got mounted
- [Step 8 — OPT B+ feeds](step-08-opt-b-plus.md) — what else lands on cap lug 1
- [Step 29 — Rectifier to filter cap](../output-stage/step-29-rectifier-to-filter-cap.md) — what feeds cap lug 2 (the choke's upstream side)
- [Filter capacitors](../../components/filter-capacitors.md) — the cap can structure
- [Rectification — smoothing](../../theory/rectification.md#smoothing-from-pulsating-dc-to-clean-dc) — the LC filter in context
- [Previous: Step 8](step-08-opt-b-plus.md) · [Next: Step 10 — Primary fuse & switch](step-10-primary-fuse-switch.md)
