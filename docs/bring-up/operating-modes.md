---
title: Operating modes
---

# Operating modes

The ST-70 is most commonly run as a **stereo amplifier** — that's the use case the kit defaults to. But the manual (page 13) also documents two other modes the amp supports: **monophonic 70-watt operation** (channels paralleled for a single 70 W speaker output), and **bi-amped operation** (left channel for bass, right for treble, fed from an active crossover).

This page covers all three modes. Most builders will use stereo and never need the others.

## Stereo (the default)

In stereo, the amp provides **35 W per channel** into a matched speaker on each side.

### Wiring

- **Inputs**: a stereo preamp's two outputs go to the two RCA input jacks (left, right).
- **Speakers**: left speaker to the left 4-screw terminal strip (use the impedance tap matching your speaker — 4 Ω, 8 Ω, or 16 Ω). Right speaker to the right terminal strip.
- **Input switch**: set to **STEREO** (also leave this position if the preamp does its own input switching).
- **Common tap**: terminal "C" on each strip is the speaker common (0 Ω reference).

This is the configuration the build documentation assumes throughout.

## Monophonic 70 W

The two channels can be paralleled for a single 70 W output to one speaker. This is useful if you have only one large bass-heavy speaker to drive, or want to run a subwoofer at full power.

There is a measurable increase in distortion in this mode (the manual notes: "decrease in overall sound quality"). It's not the recommended way to use the amp, but it works.

### Wiring

- **Input**: connect ONE input cable to **either** the left OR the right RCA jack (not both — the unused jack stays open).
- **Input switch**: set to **MONO**.
- **Output**: jumper between the two channels' speaker terminals to combine their outputs:

For an 8 Ω or 16 Ω speaker:

- Jumper "C" terminal on the left strip to "C" terminal on the right strip.
- Jumper "16" terminal on the left strip to "16" terminal on the right strip.
- Connect your speaker between "C" and "16".

For a 4 Ω speaker:

- Jumper "C" terminal on the left strip to "C" terminal on the right strip.
- Jumper "8" terminal on the left strip to "8" terminal on the right strip.
- Connect your 4 Ω speaker between "C" and "8".

The reason for using the 16Ω jumper for an 8Ω or 16Ω speaker: when the two channels are paralleled, the effective impedance the EL34s see is halved. Jumping the 16Ω taps presents 8Ω effective to the speaker — correct for an 8Ω load. For a 16Ω speaker the impedance mismatch is acceptable (the manual notes the max power drops slightly but it's not a problem).

### Quirk noted in the manual

> *"Mono operation of the ST-70 via the selector switch will result in increased distortion."*

For higher-fidelity mono use, leave the input switch on STEREO and instead use a single source feeding ONE channel only (with the other channel's input grounded or unconnected). You'll get cleaner sound at half the power.

## Bi-amped (one amp drives bass, one drives treble)

This requires an **active crossover** between the preamp and the ST-70 — most users won't have one. If you do, the ST-70 supports the topology cleanly.

### Wiring

- **Crossover output**: feed the low-frequency output of the crossover to the **left** RCA input. Feed the high-frequency output to the **right** RCA input.
- **Input switch**: set to **STEREO**.
- **Speakers**: connect the bass driver (or subwoofer) to the **left** terminal strip on the appropriate impedance tap. Connect the tweeter (or mid-and-up driver) to the **right** terminal strip.

In this mode each channel is doing only part of the audio spectrum, which means each EL-34 pair is loaded less — and the amp can produce cleaner audio at higher SPLs.

## Practical use: single source, two speakers, no jumpers

You can also use the "MONO" position with a single input source but **no jumpers** between the output strips — just connect each speaker separately to its respective terminal strip. Each speaker gets its channel's amplifier driving it at its own impedance tap. This is essentially "stereo with a mono source," which is useful if the source is mono (vintage recordings, mono CDs) but you have stereo speakers.

## Preamp power take-off sockets

The front-panel **V4 and V5 octal sockets** can be used to power an external Dynaco-compatible tube preamp:

- Pin 7 of either V4 or V5 = +B+ (around 200 V DC, after the amp's dropping resistors)
- Pin 4 of either V4 or V5 = 6.3 V AC heater (drawn from one of the heater windings)
- Pin 1 of either V4 or V5 = chassis ground

These are mainly useful with a Dynaco PAS-3 preamp or similar from the 1960s. Modern preamps typically have their own power supplies and don't need to draw from the amp.

**Pin 8 of V4 / V5 is the Biaset bias-measurement point** — see [bias adjustment](bias-adjustment.md). Don't connect a preamp lead to pin 8 unless you've also rewired the bias measurement to a different point (see manual page 12).

## See also

- [Bias adjustment](bias-adjustment.md) — where the Biaset socket gets used
- [Functional testing](functional-testing.md) — the listening tests in stereo mode
- [A-470 output transformer](../components/a-470-output-transformer.md) — the multi-tap secondary that enables impedance matching
