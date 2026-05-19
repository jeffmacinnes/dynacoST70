---
title: Safety basics
---

# Safety basics

The ST-70 runs ~450V DC on its B+ rail and stores meaningful energy in its filter capacitors. This is a hobbyist-friendly amp but **not** a hobbyist-friendly voltage range. Take this seriously.

This page is a high-level overview. The detailed safety material lives in [test equipment / high-voltage safety](../test-equipment/high-voltage-safety.md).

## The two big hazards

1. **A powered amp** can deliver lethal current at 450V DC. Currents above ~100mA across the chest can stop the heart, and the B+ rail is *capable* of delivering well above that.
2. **A powered-down amp with charged filter caps** can still deliver lethal current for minutes to hours after power-off. The caps store energy by design. Don't trust "I just turned it off."

## Core habits

- **Power off and unplug** before reaching inside the chassis.
- **Verify with a meter** that filter caps are discharged before touching internal wiring.
- **One-hand rule** during any live measurements: keep one hand in your pocket, work with the other. Prevents current paths across the chest.
- **Probes rated for the voltage involved** — see [probes](../test-equipment/probes.md).
- **Don't work tired.** Most accidents happen during the third hour of "just one more thing."

## Why the build itself is mostly safe

Almost every step of the actual build is done with the amp **unplugged and unwired** — no voltage anywhere. The dangerous work begins at [bring-up](../bring-up/index.md), when the amp gets plugged in for the first time. Until then, you're doing mechanical and soldering work on an inert piece of metal and glass.

The exceptions where wiring-stage care still matters:

- Don't accidentally power the amp before you're ready (keep it unplugged on the bench).
- Once filter caps are installed and the amp has been powered up *once*, those caps can hold a charge. After the first power-on, treat the chassis as live until you've discharged the caps.

## Read this before bring-up

[High-voltage safety](../test-equipment/high-voltage-safety.md) covers:

- Exact voltages at every node
- Filter cap discharge procedure
- Probe ratings and CAT levels
- Why isolation transformers aren't needed for this build
- The full one-hand rule rationale
