---
title: Oscilloscope
---

# Oscilloscope

A scope isn't strictly required for building or operating the ST-70, but it's enormously useful for understanding what the amp is doing and for diagnostics if anything goes wrong.

## What a scope shows that a DMM doesn't

A [DMM](multimeter.md) gives you a number — the average or RMS voltage at a point. A scope shows you the **waveform** — voltage as a function of time. This matters because:

- A DMM can't show you ripple on a DC supply (the small AC variation riding on top)
- A DMM can't show you whether a sine wave is clean or distorted
- A DMM can't show you transient events (clicks, pops, oscillation)
- A DMM can't show phase relationships between two signals

For a tube amp, the most useful applications are:

- **Power supply ripple** — see how clean your B+ actually is
- **Square wave testing** — feed a 1kHz square wave in, look at the output across a dummy load. Tells you about frequency response, ringing, and stability
- **Hum hunting** — see 60Hz or 120Hz hum at any signal point and trace where it enters
- **Distortion visualization** — sine wave in, compare to sine wave out. You can see clipping start to happen as you push the amp

## The Rigol DHO804 (under consideration for this build)

The DHO804 is a 4-channel digital scope with a 12-bit ADC. The 12-bit detail is unusual for the price point — most scopes are 8-bit, so the DHO804 can resolve much finer detail in the signal, which matters when you're looking at millivolts of ripple riding on hundreds of volts of DC.

It ships with two 10× passive probes. That's enough for most tube amp work — single-channel for ripple checks, dual-channel for input-vs-output comparisons.

## Channels and probes — how many do you need?

The DHO804 has four BNC inputs but ships with two probes. Most tube amp work is 1- or 2-channel:

- **Single channel:** ripple, oscillation checks, signal at a single point
- **Two channels:** input vs. output of a stage, both halves of a push-pull output, signal vs. ground reference
- **Three or four channels:** multi-stage signal tracing, multiple bias points monitored simultaneously — useful but rarely essential

Start with the two probes that come in the box. Add more later if you find yourself wanting them.

A more important addition than extra probes: a **high-voltage probe**. See [probes](probes.md#high-voltage-scope-probes) for the discussion.

## Diagnosing capacitors with a scope

A scope isn't the best tool for testing isolated capacitors out of circuit (a capacitance meter or ESR meter does that better). But for **diagnosing capacitor problems in a working amp**, the scope is invaluable.

### The problem with old caps

Capacitors in vintage gear fail in ways that don't reveal themselves at idle but show up under signal:

- **[Filter caps](../components/filter-capacitors.md)** can pass DC voltage measurements (your DMM says "yep, 50V") but fail to filter ripple effectively under load. The amp hums, the bass loses tightness, channels interact, dynamics suffer.
- **Coupling caps** can pass DC blocking duty (no DC voltage on the next stage's grid) but leak audio signal, distort, or fail to pass low frequencies cleanly.
- **Bypass caps** can read correct value but have high ESR (Equivalent Series Resistance), making them ineffective at their job (filtering out high-frequency noise from a power rail).

A DMM gives you an averaged number. A scope shows you the **waveform**, which is where these failure modes become visible.

### Power supply ripple measurement

The single biggest reason to put a scope on a vintage amp. With a probe on the main filter cap, you can directly see how much AC ripple is riding on the DC supply.

A healthy filter cap leaves a few millivolts to maybe 50mV of ripple on the supply. A failing cap can let hundreds of millivolts through. The same DMM that says "supply is at 50V" will read the same number with either cap; the scope shows you immediately which one is failing.

For B+ measurements on a tube amp, you'll need a [high-voltage probe](probes.md#high-voltage-scope-probes). For lower-voltage solid-state amps, standard 10× probes work fine.

### Square wave testing

Feed a 1kHz square wave into the input, look at the output across a dummy load with the scope. A clean square wave out means the entire signal path is healthy. Common failure modes:

- **Rounded leading edges** → high-frequency loss (often a leaky coupling cap or aged compensation cap)
- **Sloped tops** → low-frequency loss (often a dried-out coupling cap)
- **Ringing on edges** → instability somewhere in the feedback loop
- **Asymmetric clipping** → bias issues in the output stage

This single test gives a remarkably good picture of overall amp health in about 30 seconds.

### Signal tracing for noise hunting

Probe successive points along the signal path while listening for noise (or watching for it on the scope). Noise that appears at a specific node and not before tells you where the failing component lives. Useful for tracking down hum, crackle, or hiss in older preamp/phono stages.

### Coupling cap leakage

A scope adds something to coupling cap analysis that a DMM can't: you can see if **AC signal** is passing cleanly. A cap that's gone leaky might pass DC AND distort the signal as it ages. Scope shows the distortion; DMM shows only the DC.

## See also

- [Probes](probes.md) — scope probes, high-voltage probes, what they cost
- [Multimeter](multimeter.md) — when the DMM is the right tool instead
- [Filter capacitors](../components/filter-capacitors.md) — the most common scope-revealed failure mode
