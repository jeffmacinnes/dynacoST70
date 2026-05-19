---
title: 6GH8A driver tube
---

# 6GH8A driver tube

The 6GH8A is a 1960s **compactron**-style combined pentode/triode tube — two completely separate working sections inside a single 9-pin glass envelope, sharing only the heater. Dynaco picked it for the ST-70 driver board because one envelope did both the voltage amplification AND the phase splitting needed for one channel of the push-pull output stage. Half the tubes, half the sockets, half the wiring.

The ST-70 uses two 6GH8As — one per channel — in sockets **V4** and **V5** on the [PC-3A driver board](pc-3a-driver-board.md).

## What it is

Inside the glass envelope:

| Section | Role in the ST-70 | Stage |
|---|---|---|
| Pentode | Voltage amplifier (input stage) | gain ~50× |
| Triode | Phase splitter (cathodyne) | unity gain, two outputs 180° apart |

The two sections have their own plates, grids, and cathodes — they're electrically independent. They share the heater filament and the glass envelope, that's it. Signal flows: audio → pentode → triode → EL34 grids.

For the topology each section participates in, see:

- [Phase splitting](../theory/phase-splitting.md) — what the triode section does
- [Push-pull topology](../theory/push-pull-topology.md) — what comes after the 6GH8A
- [Feedback](../theory/feedback.md) — the global loop that lands back at the pentode's cathode

## Specs

| Parameter | Pentode section | Triode section |
|---|---|---|
| Heater | 6.3 V @ 0.45 A (shared between sections) | |
| Plate voltage (max) | 330 V | 330 V |
| Plate dissipation (max) | 2.5 W | 1.5 W |
| Transconductance (g_m) | ~12,000 µmho | ~3,800 µmho |
| Amplification factor (µ) | high (pentode) | ~40 (triode) |

In the ST-70's operating conditions, both sections run comfortably below max ratings — long life.

For the pin assignments, see the [tube pinout chart](../appendices/tube-pinouts.md).

## Why Dynaco picked this tube

The 6GH8A wasn't an audio-specific tube. It was designed for the *television* market — specifically as a video-IF amplifier + sync-separator combination. Mass production for TVs meant:

- **Cheap** (mid-century TVs were a huge volume market).
- **Available** at every electronics distributor.
- **Reliable** because TV manufacturers had standardised on it.

For Hafler's ST-70 cost target, using a mass-market TV tube for the driver stage was a brilliant call. Almost any audio-only equivalent (like a 12AX7+12AU7 combination) would have cost more, used more parts, and required more wiring. The 6GH8A gave him a complete driver-stage-in-one-envelope at TV-tube prices.

The trade-off: the 6GH8A isn't tuned for audio. Its specs are good enough but not optimal. Designed-for-audio tubes can do better — which is part of why the VTA driver board upgrade (see below) exists.

## Adapter set

The ST-70's PC-3A driver board sockets are *almost* but not quite standard 9-pin sockets. The pinout differs slightly from the 6GH8A's compactron base. Originally Dynaco supplied tubes with the right base; today's NOS 6GH8As often have a slightly-different base.

This build uses an **adapter set from Amplified Parts** — small plug-in adapters that translate between modern 9-pin compactron 6GH8As and the PC-3A's socket pinout. They plug into the socket; the tube plugs into the adapter; everything works.

If your tubes come with the original Dynaco-compatible base, you don't need the adapters. The adapters are just convenience for the modern parts ecosystem.

## How the two sections are used in the ST-70

### Pentode (input stage)

The pentode section is the input voltage amplifier. Audio comes in from the input jack, goes through the volume/balance controls, and lands on the pentode's control grid. The pentode amplifies (~50×) and outputs a much larger signal at its plate.

The pentode's cathode is **where the global negative feedback returns** — the feedback wire from the 16 Ω OPT tap arrives here through a resistor, mixing with the local cathode bias. See [feedback](../theory/feedback.md) for the full loop.

### Triode (phase splitter)

The pentode's plate output is coupled (via a coupling cap) to the triode section's grid. The triode is configured as a [cathodyne (split-load) phase splitter](../theory/phase-splitting.md) — equal-value resistors above and below the triode produce two output signals 180° apart, one at the plate, one at the cathode.

Those two phase-split outputs go to the grids of the two EL34s in the push-pull pair (via coupling caps).

## Failure modes

The 6GH8A is generally robust but has a few characteristic ways it can go bad:

### Aging cathode (slow death)

The cathode's oxide coating slowly depletes over years of use. Symptoms:

- Lower stage gain (the pentode can't push as much current).
- Slightly drifty bias (the cathode bias point shifts as transconductance drops).
- Possibly: more 2nd-harmonic distortion as the operating point becomes non-optimal.

Hard to spot without instrumentation. If the amp seems to be losing punch over time, suspect the 6GH8As before the EL34s.

### Microphonics

Tubes can act as microphones — mechanical vibration of the internal structure modulates the plate current. A microphonic 6GH8A will ring when tapped, and may amplify chassis vibration into the audio output.

Test: tap the tube envelope GENTLY with the eraser end of a pencil while listening. Healthy tubes produce a soft "tink" that decays in <100 ms. Microphonic ones ring for seconds, or produce audible pings on every tap.

Solutions: tube damping rings, or just replacement.

### Heater-cathode leakage

The heater is supposed to be electrically isolated from the cathode. In aged tubes, the insulation between them can break down, letting heater AC inject directly into the cathode → 60 Hz hum at the output.

Test: measure resistance between heater pins and cathode pin (with tube cold, out of the socket). Should be MΩ or higher; if it's down in the kΩ range, the tube is hum-prone.

### Phase splitter imbalance (specific to the triode)

The cathodyne topology gives balance automatically *if* the resistors match. But as the triode itself ages, its transconductance changes, which affects the bias point and thus the operating impedance of each output. Slight imbalance creeps in. Not usually audible but measurable on a scope.

## Modern availability

NOS (new-old-stock) 6GH8As are still findable from tube specialists. Some current-production substitutes exist (mostly from Russia or China). Specific NOS brands considered good for audio use:

- **Sylvania** — most commonly found, generally good
- **GE** — slightly different sonic character
- **RCA** — premium NOS, gets bid up on the auction market
- **Tung-Sol** — rarer in this type

For a build like this, any decent NOS tube works fine. Spend the money on the EL34s instead — those make more sonic difference.

## The VTA upgrade alternative

Tubes4HiFi's **VTA driver board** replaces the entire PC-3A board, including the 6GH8As. It uses different tubes (typically 12AU7s) configured as a **long-tail-pair phase splitter** (see [phase splitting](../theory/phase-splitting.md) for what that is). Advantages:

- More headroom (more drive voltage available to the EL34 grids).
- Better balance (long-tail-pair is inherently more balanced than cathodyne).
- Lower output impedance from the driver stage (drives the EL34 grids harder).
- 12AU7 is a current-production audio tube with much wider availability.

The VTA is the obvious "next mod" for an ST-70 builder who wants to upgrade beyond the stock driver. This build keeps the 6GH8A for stock-Dynaco fidelity, but the upgrade is well-documented if you change your mind later.

## In this build

The 6GH8As occupy sockets **V4** (left channel) and **V5** (right channel) on the PC-3A driver board, plugged in via the Amplified Parts adapter set.

## See also

- [PC-3A driver board](pc-3a-driver-board.md) — the board this tube lives on
- [Phase splitting](../theory/phase-splitting.md) — the topology used by the triode section
- [Feedback](../theory/feedback.md) — the loop that lands at the pentode's cathode
- [Tube pinouts](../appendices/tube-pinouts.md) — the pin chart
- [EL34 output tube](el34-output-tube.md) — what the 6GH8A drives
