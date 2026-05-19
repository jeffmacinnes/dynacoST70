---
title: 1N4007 diode
---

# 1N4007 diode

The 1N4007 is a general-purpose silicon rectifier diode. In this ST-70 build, it replaces the original selenium rectifier in the bias supply — a small but important [safety modification](../modifications/1n4007-replacement.md).

## Specs

| Parameter | Value |
|---|---|
| Peak inverse voltage (PIV) | 1000V |
| Forward current | 1A continuous |
| Forward voltage drop | ~0.7V |
| Package | DO-41 axial (small glass body with a banded end) |

The "banded end" marks the cathode — the side current flows *out of* when the diode is conducting.

## Why it's here

The PA-060's bias winding produces 55V AC. The 1N4007 rectifies this to pulsating DC, which then gets filtered and divided down by resistors (and the [individual bias pots](../modifications/individual-bias-pots.md) in this modified build) to provide the −40V DC bias for the EL34 control grids.

## Why we use a silicon diode instead of the original selenium

The original Dynaco design used a selenium rectifier for the bias supply. Selenium was standard in 1959, but:

- Selenium rectifiers degrade slowly over decades, raising their forward voltage drop and reducing bias supply reliability.
- When they fail catastrophically, they can release **toxic fumes** (selenium oxide).
- 1N4007 silicon diodes are vastly more reliable, cheaper, and safer.

This is one of the universally-recommended ST-70 modifications. See the [1N4007 modification page](../modifications/1n4007-replacement.md) for the full discussion.

## A note on bias voltage

Silicon has a lower forward voltage drop than selenium (about 0.7V vs. about 1.5V), so the rectified bias voltage ends up slightly *higher* (more negative) than the original spec. This is usually within the range that the bias pots can adjust out, but worth keeping an eye on during bias-up. If the resulting bias voltage is too high to dial in correctly, a small dropping resistor can be added in series with the diode to drop a few extra volts.

## In this build

The 1N4007 is mounted on a 2-lug terminal strip near the bias supply area. The relevant wiring step:

- [Step 1](../build/power-supply/step-01-bias-diode.md) — red-black bias winding lead → 1N4007 cathode (banded end)

## Failure modes

- **Open** — no bias voltage. EL34 grids drift positive, output tubes run away on first power-on. Always verify bias voltage *before* installing output tubes.
- **Shorted** — passes both halves of the AC, no rectification. Bias supply becomes AC instead of DC. EL34s see AC on their grids, sound terrible if they even run.

Silicon diodes rarely fail in low-stress applications like this one. The 1N4007 will likely outlive the amp.

## See also

- [1N4007 modification](../modifications/1n4007-replacement.md) — why we make this swap
- [Step 1 — Bias diode](../build/power-supply/step-01-bias-diode.md) — the wiring step
- [Individual bias pots modification](../modifications/individual-bias-pots.md) — what the bias supply feeds in this build
