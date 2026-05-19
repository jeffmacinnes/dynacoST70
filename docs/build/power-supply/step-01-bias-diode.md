---
title: Step 1 — Bias diode
---

# Step 1: Connect the red-black power transformer lead to the banded side of the diode

> *Connect the red-black power transformer lead to the banded side of the diode at the (2) lug terminal strip (S)*

## What you're doing physically

Connecting one specific wire from the [PA-060](../../components/pa-060-power-transformer.md)'s bias winding to the cathode (banded end) of a [1N4007 silicon diode](../../components/1n4007-diode.md) mounted on a 2-lug terminal strip.

## What this accomplishes

This is the very first stage of the **bias supply circuit** — the small negative DC supply that holds the EL34 control grids at the correct operating point.

The chain you're starting to build:

1. Wall AC (120V) → power transformer → stepped up to **55V AC** on the bias secondary winding
2. The red-black lead is one end of that 55V winding
3. The diode you're connecting it to converts that AC to **pulsating DC** by blocking the negative half-cycles
4. Downstream, this gets filtered, divided down by resistors (and individual bias pots in [this build's bias mod](../../modifications/individual-bias-pots.md)), and arrives at the EL34 grids as ~−40V DC

## Why the banded end matters

The band on a diode marks the **cathode** — the side current flows *out of* when the diode is conducting. By connecting the transformer lead to the banded side, you're defining which direction the diode will pass current — and therefore the polarity of your DC output.

Get this backwards and you've reversed your bias supply polarity, which means **positive voltage on your EL34 grids** instead of negative — which would dump runaway current through the output tubes and destroy them on first power-up.

## Context: this is the safety mod

The 1N4007 is the modern silicon diode replacing the original selenium rectifier in the ST-70 design. The original selenium part has degraded reliability after decades and can fail catastrophically (releasing toxic fumes when it lets go). The 1N4007 is a robust silicon part that does the same job reliably and safely. See [1N4007 modification](../../modifications/1n4007-replacement.md) for the full discussion.

!!! note "Note on voltage"
    The silicon diode has a lower forward voltage drop than selenium (about 0.7V vs. about 1.5V), so the rectified bias voltage will end up slightly higher (more negative) than the original spec. Worth keeping an eye on during bias-up. If the resulting bias voltage is too high to dial in correctly with the bias pots, a small dropping resistor can be added in series.

## Why this step is at the start

The bias supply has to be working *first*. When the amp powers up, the rectified bias voltage starts holding the EL34 grids negative immediately. The slow-warming [5AR4](../../components/5ar4-rectifier-tube.md) rectifier delays the high-voltage B+ from arriving for ~30 seconds, by which time the bias is fully established. This sequence prevents the EL34s from ever seeing high B+ without proper grid bias — which would be destructive.

## See also

- [1N4007 diode](../../components/1n4007-diode.md) — the diode being wired
- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — the source of the red-black lead
- [Individual bias pots modification](../../modifications/individual-bias-pots.md) — what the bias supply ultimately feeds
- [1N4007 replacement modification](../../modifications/1n4007-replacement.md) — why we're using this diode instead of the original selenium part
- [Rectification](../../theory/rectification.md) — the underlying theory
- [Next: Step 2 — 5AR4 heater](step-02-5ar4-heater.md)
