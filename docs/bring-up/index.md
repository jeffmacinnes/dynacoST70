---
title: Bring-up
---

# Bring-up

After the amp is fully wired and visually inspected, **bring-up** is the procedural sequence for turning it on for the first time without damaging anything (including yourself).

!!! warning "Read first"
    Read [high-voltage safety](../test-equipment/high-voltage-safety.md) before any of this. After the first power-on, the [filter caps](../components/filter-capacitors.md) hold lethal charge for minutes to hours after power-off.

## The sequence

Each page builds on the previous; do them in order on a first build.

1. [Pre-power checklist](pre-power-checklist.md) — visual inspection, lead dress, mechanical, smell test, resistance check before any power.
2. [Continuity checks](continuity-checks.md) — every node verified with a DMM before any power.
3. [First power-on](first-power-on.md) — the slow [variac](../test-equipment/variac.md) ramp, organized as multiple sessions (no tubes → heater-only → 5AR4 added → driver tubes added → all tubes).
4. [Voltage checks](voltage-checks.md) — what to measure where, with the manual's voltage table as the reference.
5. [Bias adjustment](bias-adjustment.md) — setting the four [EL34s](../components/el34-output-tube.md) using the [individual bias pots mod](../modifications/individual-bias-pots.md) or the stock Biaset method.
6. [Functional testing](functional-testing.md) — signal injection, dummy-load tests, listening tests, square-wave testing.

After the staged bring-up:

- [Operating modes](operating-modes.md) — stereo (default), monophonic 70 W, bi-amped configurations, preamp power take-off.
- [Troubleshooting](troubleshooting.md) — symptom-driven index for when something goes wrong, on first power-on or later.

## A note on the 4-channel scope

If you have a 4-channel oscilloscope, it earns its keep across most of these pages. The four-channel format is especially good for:

- **Watching the cathodyne phase splitter** (triode plate vs cathode, 180° apart) and **push-pull** (V2 vs V3 plates, also 180° apart) on the same screen.
- **Comparing input → output simultaneously** to measure gain and phase across the amp.
- **Probing the feedback loop**: input, OPT secondary, pentode cathode, and the residual differential all on one display.

Most pages below have `4-ch scope` callouts pointing out specific probe points and what each waveform should look like. They're optional — you can complete the build with a DMM only — but they pay back the setup time in conceptual understanding.
