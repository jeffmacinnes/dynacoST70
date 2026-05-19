---
title: Push-pull topology
---

# Push-pull topology

A **push-pull** output stage uses two output tubes (or transistors) wired so that each one amplifies one half of the audio waveform. The two halves are combined in a center-tapped output transformer to produce the full signal at the speaker. The ST-70 has two push-pull pairs — one per channel — each driving an [A-470 output transformer](../components/a-470-output-transformer.md).

Push-pull is the dominant topology for tube power amplifiers, and the reasons aren't only about output power. The most interesting properties come from the geometry of how the two tubes' contributions combine.

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../assets/diagrams/push-pull-topology.svg" aria-label="Push-pull output stage with two EL34s and a center-tapped output transformer">
    Push-pull topology (your browser does not support inline SVG).
  </object>
  <figcaption>Two EL34s wired to opposite ends of the OPT's center-tapped primary. B+ enters at the center tap. The two tubes' inputs are 180° out of phase; their outputs combine in the secondary to produce the full audio waveform. Click to zoom.</figcaption>
</figure>

## The basic idea

The driver stage (in the ST-70, a [6GH8A](../components/6gh8a-driver-tube.md) configured as a phase splitter — see [phase-splitting](phase-splitting.md)) produces two copies of the input signal that are *exactly 180° out of phase*. When one swings positive, the other swings negative.

Those two signals drive the grids of two output tubes:

- **Tube A** receives the in-phase signal. When the audio swings positive, tube A conducts more.
- **Tube B** receives the anti-phase signal. When the audio swings positive (tube A conducts more), tube B's grid swings negative, so tube B conducts *less*.

Both tubes share the load (the OPT primary), but they pull current through it in *opposite* directions. The OPT's secondary sees the difference between the two tubes' contributions, which is the full audio waveform.

It's important that this is *the difference*, not the sum:

`output ∝ (current_A) − (current_B)`

Whatever the two tubes have in common — DC bias current, hum picked up equally, distortion products that happen identically in both tubes — gets subtracted out. Whatever differs (the audio signal, which is in opposite phases) gets doubled.

## Three things push-pull gives you

### 1. About twice the power

Each tube provides about half the output peak voltage swing, but they swing in opposite directions, so the total swing across the OPT primary is doubled. Power scales as voltage² over impedance, so push-pull delivers roughly **4× the output voltage swing** of a single tube into the same OPT primary impedance — which works out to about 2× the output power for similar plate dissipation.

The ST-70 delivers 35 W per channel using push-pull EL34s. A single-ended EL34 amplifier maxes out around 8 W. Same tubes, same B+, very different output.

### 2. Even-harmonic cancellation

Pentodes (and triodes) produce both even-order and odd-order harmonic distortion when overdriven. The even-order components (2nd, 4th, 6th harmonics) happen *equally and in phase* in both tubes — so when the OPT subtracts the two tube outputs, they cancel.

Specifically: feed a pure 1 kHz sine into a single tube, you might measure 1 % 2nd-harmonic distortion at the output. Feed the same signal into a push-pull pair, the 2nd-harmonic distortion drops to maybe 0.05 % — a factor of 20 lower. Odd-order harmonics (3rd, 5th) don't cancel — they actually add — but those are also much smaller in magnitude.

This is why push-pull amps measure cleanly. Whether they *sound* cleaner is a matter of taste:

- The "audiophile" argument: push-pull's even-harmonic cancellation removes pleasing 2nd-harmonic "warmth" that single-ended amps preserve.
- The engineering argument: distortion is distortion; less is better; push-pull wins.

Both positions are defensible. The ST-70 is push-pull, and the EL34 push-pull pair is a classical "musical sounding" combination, so the practical answer for this build is: you get the best of both characters.

### 3. DC plate currents cancel in the core

Each tube draws ~100 mA of DC plate current at idle. That current flows through its half of the OPT primary. The two tubes' DC currents flow in *opposite directions* through the magnetic core — they cancel.

This matters because it means the OPT core doesn't have to be designed to handle ~200 mA of DC magnetisation. In a single-ended amp, all the tube's DC current flows one way through the core, magnetising it heavily — the core has to have an air gap to avoid saturating, which reduces inductance and bandwidth.

In push-pull, no gap is needed. The core can be a continuous magnetic path, giving:

- **Higher inductance per turn** → better low-frequency response.
- **Tighter coupling** between primary and secondary → better high-frequency response.
- **Smaller core size** for the same power handling.

The A-470's extraordinary bandwidth (−1 dB from 6 Hz to 30 kHz at full power) is largely possible because of push-pull's DC cancellation.

## Class A, AB, B — operating point matters

Push-pull amps differ in how much of the cycle each tube conducts:

- **Class A**: each tube conducts for the *entire* audio cycle. Both tubes are always partly on. Smoothest distortion characteristic, but inefficient (only ~25 % of B+ becomes output power).
- **Class B**: each tube conducts for *exactly half* the cycle, then cuts off completely. More efficient (~50-70 %), but the transition between tubes (the "crossover") introduces distortion if not handled carefully.
- **Class AB**: somewhere between. Each tube conducts for *more than half* the cycle, so the two overlap during small signal swings (class A behavior). At high signal levels they push into class B for efficiency.

The ST-70's EL34s operate **class AB**. At low listening levels both tubes are always on (class-A territory); pushed hard, the amp slides into class-B operation for the loudest peaks.

The transition is smooth as long as bias is set correctly. Bias too cold → crossover distortion at low levels. Bias too hot → red-plating and short tube life. See [bias adjustment](../bring-up/bias-adjustment.md) and the [individual bias pots mod](../modifications/individual-bias-pots.md) for the practical procedure.

## Why push-pull needs phase splitting

The whole push-pull arrangement depends on having TWO copies of the input signal, in opposite phases. Where do they come from?

The driver stage. In the ST-70 this is the [6GH8A driver tube](../components/6gh8a-driver-tube.md) on the [PC-3A board](../components/pc-3a-driver-board.md), configured as a phase splitter. The 6GH8A takes one input signal and produces two output signals 180° apart — which become the inputs to the push-pull pair.

If the phase splitter is unbalanced (one output stronger than the other), the push-pull cancellation properties degrade. Hum and distortion that would have cancelled now bleed through. So phase splitter balance is critical — see [phase-splitting](phase-splitting.md) for the topology and tradeoffs.

## How this connects to other parts of the manual

- The two EL34s of each channel ([V2/V6 for one channel, V3/V7 for the other](../index.md#tube-layout-this-manuals-numbering)) form a push-pull pair driving an [A-470](../components/a-470-output-transformer.md).
- The OPT's center tap (RED lead) is where B+ enters; the two ends (BLUE / BROWN-primary) connect to the two tube plates. See the [A-470 page](../components/a-470-output-transformer.md) for the lead assignments.
- The phase splitter that feeds the push-pull pair is covered on the [phase splitting](phase-splitting.md) page.
- Even-harmonic cancellation depends on balanced operation, which depends on matched tubes — see the [individual bias pots mod](../modifications/individual-bias-pots.md) for keeping the two tubes balanced.

## See also

- [Phase splitting](phase-splitting.md) — generating the two opposite-phase signals push-pull needs
- [A-470 output transformer](../components/a-470-output-transformer.md) — the center-tapped OPT that combines the two tubes
- [EL34 output tube](../components/el34-output-tube.md) — the tubes themselves
- [Feedback](feedback.md) — the global negative-feedback loop that wraps around the push-pull stage
- [Individual bias pots mod](../modifications/individual-bias-pots.md) — keeping the two halves of each push-pull pair balanced
