---
title: M11 — C-354 choke
---

# M11: Mount the C-354 filter choke

> *Mount the choke, C-354, on the right side below the chassis. Put the #8 screws through the chassis from the top and fasten underneath with kep nuts. The leads should face the front of the chassis.* — manual page 5

## What you're doing physically

The **C-354 choke** is a small iron-core inductor (about ⅓ the size of the PA-060). It mounts **on the UNDERSIDE of the chassis** on the right side, near the PA-060 power transformer.

Mounting procedure:

1. Insert two **#8-32 screws** from the top of the chassis through the appropriate holes.
2. From the underside, hold the choke against the chassis with its leads pointing toward the **FRONT**.
3. Thread #8 kep nuts onto the screws from the choke side, firming up.
4. Tighten.

The choke hangs under the chassis. Its 6"-long leads will be routed and connected in [step 9 of wiring](../power-supply/step-09-choke.md).

## Choke specs (per manual page 25)

| Parameter | Value |
|---|---|
| Inductance | 1.75 H |
| DC current rating | 200 mA |
| DC resistance | 62 Ω |
| Max DC voltage | 400 VDC |

For full theory see the [choke component page](../../components/choke.md).

## Why underneath, not on top

Three reasons:

1. **Chassis real estate**: the top is fully occupied by the PA-060 (center), two A-470s (sides), and the seven octal sockets. No room for the choke up top.
2. **Heat**: the choke runs cool (it dissipates only ~0.6 W in DCR losses at full current). It doesn't need top-of-chassis cooling like the tubes do.
3. **Magnetic coupling**: keeping the choke off the top reduces unwanted hum coupling between it and the A-470 output transformers. They all have iron cores; positioning them perpendicular and separated minimizes stray-field interactions.

## Why leads facing the front

Same logic as the PA-060: the wiring procedure assumes specific lead exit points. The choke's leads will route up through the chassis (via openings near the filter cap) and connect to filter cap lugs 1 and 2. Front-facing leads make that routing short.

## Mechanical sanity check

The choke sits inverted (relative to its label orientation when on a workbench) when mounted below the chassis. Make sure the mounting bolts aren't touching anything they shouldn't — the choke body has end bells and laminations that should NOT touch the chassis bottom directly. The mounting holes are spaced to keep the choke body floating just below the chassis with a small air gap.

## Common mistake: mounting from the wrong side

If you mount the choke from the BOTTOM (screws coming up from below the chassis into the choke from outside), you'll get the wrong orientation. The screws go DOWN through the chassis from above; the choke hangs BELOW.

## See also

- [Choke](../../components/choke.md) — full theory and specs
- [Step 9 — Choke wiring](../power-supply/step-09-choke.md) — connecting the choke into the B+ chain
- [Rectification — smoothing](../../theory/rectification.md#smoothing-from-pulsating-dc-to-clean-dc) — what the choke does in the broader smoothing chain
