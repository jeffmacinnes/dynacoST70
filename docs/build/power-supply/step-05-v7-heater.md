---
title: Step 5 — V7 heater
---

# Step 5: Twist the brown pair and connect to V7 pins #2 and #7

> *Twist the brown pair and dress them to socket V7. Connect one brown lead to pin #2 of V7. Connect the other brown lead to pin #7 of V7.*

This is the same operation as [step 4](step-04-v2-heater.md), just with a different winding (brown instead of green) going to a different tube (V7 instead of V2).

## Why two separate 6.3V heater windings instead of one

The [PA-060](../../components/pa-060-power-transformer.md) has **two** 6.3V @ 5A windings, not one 6.3V @ 10A winding. Why?

There are several reasons, and they all matter.

### Reason 1: Total current load is huge

The ST-70 has six 6.3V tubes to heat:

| Tube | Heater current |
|---|---|
| V2 ([EL34](../../components/el34-output-tube.md)) | 1.5A |
| V3 (EL34) | 1.5A |
| V6 (EL34) | 1.5A |
| V7 (EL34) | 1.5A |
| V4 ([6GH8A](../../components/6gh8a-driver-tube.md)) | 0.45A |
| V5 (6GH8A) | 0.45A |
| **Total** | **6.9A** |

If you tried to power all of this from a single 6.3V winding, you'd need a winding rated for at least 7A, with some headroom for inrush. The PA-060's two windings at 5A each (total 10A available) gives comfortable margin.

You could in principle design a transformer with a single 10A heater secondary, but it has practical disadvantages:

- **Wire gauge.** 10A continuous current requires substantially thicker wire than 5A. Doubling the current means roughly doubling the wire's cross-section, which means a single thick winding takes more space inside the transformer.
- **Heat distribution.** A single big winding concentrates I²R losses in one region of the bobbin. Two smaller windings distribute the heat more evenly.
- **Manufacturing.** Multiple smaller windings are easier to wind in a balanced configuration than one massive winding.

### Reason 2: Channel separation

The windings are distributed across the tube complement so that each channel of the amp gets its own 6.3V heater supply, with its own center tap grounding reference ([step 6](step-06-heater-cts.md)). This provides better channel isolation — heater current draw on one channel doesn't ripple voltage on the other channel's heater supply.

In a stereo amp, you want the two channels to be as electrically independent as possible. Separate heater windings is one way to achieve that without resorting to two entirely separate power transformers.

### Reason 3: Symmetric magnetic loading

When a transformer's secondaries are physically distributed symmetrically around the bobbin — two 6.3V windings on opposite sides, for instance — the magnetic loading on the core is more balanced than with a single asymmetric heavy winding.

This matters because asymmetric magnetic flux can cause:

- Mechanical vibration ("transformer hum" you can hear from the chassis itself)
- Slightly increased core saturation under load
- Stray magnetic field that radiates into nearby circuits

The Dynaco/Pacific Transformer design probably places the green and brown windings on opposite sides of the bobbin, contributing to the PA-060's quiet operation.

### Reason 4: Hum cancellation between channels

When the two 6.3V windings drive separate channels and each has its own CT-to-ground reference, any residual hum in the heaters of one channel is **uncorrelated** with the hum in the other channel's heaters. They don't add in lockstep.

If a single shared 6.3V winding fed both channels, hum from the heaters would be identical and in-phase in both channels — much more likely to create audible hum in the final mixed output (especially for mono recordings, which sum both channels).

### The big-picture answer

The "two windings instead of one" decision is a beautiful example of how every choice in a vintage tube amp design has multiple reasons. Each individual reason is small; together they add up to a quieter, more balanced, more thermally even, more electrically robust amp. The cost is essentially zero (one extra pair of secondary leads). The benefit is meaningful.

## See also

- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — both heater windings
- [Heater circuits](../../theory/heater-circuits.md) — heater hum theory
- [Step 6 — Heater CTs](step-06-heater-cts.md) — where the CTs land
- [Previous: Step 4](step-04-v2-heater.md) · [Next: Step 6 — Heater CTs](step-06-heater-cts.md)
