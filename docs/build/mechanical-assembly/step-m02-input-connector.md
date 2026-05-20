---
title: M2 — Input connector
---

# M2: Mount the dual RCA input connector with bakelite insulator

> *Place the brown Bakelite insulator over the front of the two socket input connector and mount the combination from the inside of the chassis using 4/40 hardware.* — manual page 4

## What you're doing physically

The kit supplies a **dual RCA input socket** (one chrome-plated frame with two RCA jacks side by side: left and right channel inputs). It mounts to the front panel of the chassis, accessible from outside.

The brown **Bakelite insulator** is a thin disc that goes between the metal RCA socket frame and the chassis metal — it electrically isolates the RCA jacks' frames from the chassis ground. Without it, you'd have a hard short from input signal ground to chassis at this point, which would create ground-loop problems.

Assembly order, from outside in:

1. Chassis front panel (metal).
2. Bakelite insulator (brown plastic disc, fits in the cutout).
3. RCA socket frame (chrome-plated metal, with two RCA jacks).
4. #4-40 screws inserted from outside through the RCA frame.
5. Kep nuts on the inside.

## Why the Bakelite insulator matters

The RCA socket's signal grounds (the outer barrel of each RCA jack) need to be at *audio signal ground*, not chassis ground. These two grounds are mostly the same potential but the path matters — see [grounding and hum](../../theory/grounding-and-hum.md).

If the RCA frame is grounded directly to the chassis at this point, signal ground current can flow through the chassis (a multi-path conductor with weird inductance and resistance characteristics), creating audible hum.

With the Bakelite insulator in place, the signal ground stays isolated until it deliberately joins chassis ground at the star ground point (manual step 15) — exactly one connection between signal and chassis ground.

## Polarity / orientation

The RCA frame has "LEFT" and "RIGHT" stamped on it (or sometimes "L" and "R"). Mount so the orientation matches the labels on the chassis front panel — there's only one correct orientation that fits.

## See also

- [Grounding and hum](../../theory/grounding-and-hum.md) — why the star ground topology matters
- [Step M15](step-m15-ground-lugs.md) — where signal ground actually meets chassis
