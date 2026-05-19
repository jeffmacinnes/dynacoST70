---
title: 1N4007 selenium replacement
---

# 1N4007 silicon diode (selenium rectifier replacement)

*Page to be expanded.* The summary:

The original ST-70 used a **selenium rectifier** for the bias supply. Selenium was standard in 1959 but it ages poorly. Two reasons to replace it:

1. **Reliability** — old selenium rectifiers slowly increase in forward voltage drop, throwing off the bias supply over time. Eventually they fail.
2. **Safety** — when selenium fails catastrophically, it can release **toxic selenium oxide fumes**. Modern silicon diodes have no such failure mode.

The 1N4007 is the universally-chosen replacement: 1000V PIV, 1A continuous, ~$0.10, sized exactly right for the bias supply's load.

This modification is already incorporated in [step 1](../build/power-supply/step-01-bias-diode.md) of the build — the kit's documentation reflects the modern best practice.

## The voltage-drop side effect

Silicon has a lower forward voltage drop than selenium (~0.7V vs. ~1.5V). The bias supply produces a slightly higher (more negative) bias voltage as a result. Usually the [individual bias pots](individual-bias-pots.md) can adjust this out. If not, a small dropping resistor in series with the diode lowers the bias supply back to the original range.

## See also

- [1N4007 diode component page](../components/1n4007-diode.md) — specs, failure modes, banding
- [Step 1 — Bias diode](../build/power-supply/step-01-bias-diode.md) — the wiring step
- [Individual bias pots](individual-bias-pots.md) — what consumes the bias supply
