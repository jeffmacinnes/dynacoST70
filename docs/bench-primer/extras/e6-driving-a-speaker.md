---
title: E6. Driving a speaker
---

# Extra E6 — Driving a speaker: impedance, power, and why DC is forbidden

*Optional module. Assumes [exercise 1](../01-ohms-law-and-power.md); pairs with [E1](e1-power-and-heat.md) (power as heat) and [E5](e5-caps-with-ac.md) (coupling caps).*

## The concept

A speaker is a resistor that sings — almost. Three things separate it from the resistors you've been using:

1. **Its "4 Ω" is an impedance, not a DC resistance.** The nominal rating is an average AC impedance across the audio band. The voice coil's DC resistance (what your DMM reads) is lower — typically 70–85% of nominal — and the actual impedance swings well above nominal at the cone's resonance frequency.
2. **It converts *changing* current into motion.** AC through the coil moves the cone back and forth: sound. Steady DC just shoves the cone off-center and holds it there: silence, plus I²R heat in a coil that's rated for music, not for continuous dissipation. That's why DC through a speaker is forbidden — it wastes the amp's power budget, distorts the cone's travel, and can burn the coil.
3. **It's a brutally heavy load.** After exercises full of 10 kΩ dividers, 4 Ω re-scales your intuition: delivering even 1 V across 4 Ω takes 250 mA. This is why speakers need power amplifiers, and why [source impedance](e4-source-impedance-and-sag.md) matters so much at the output.

Power into the load is the same equation as E1, using RMS voltage:

$$ P = \dfrac{V_\text{RMS}^2}{R} \qquad V_\text{RMS} = \dfrac{V_\text{p-p}}{2\sqrt{2}} $$

## Bench exercise E6A — meet your speaker with the DMM

**Parts:** 4 Ω speaker, DMM.

**Measure the voice coil DCR** (ohms mode across the terminals). **Predict:** ~3–3.5 Ω for a 4 Ω-rated speaker. Watch the cone while you connect the probes — many DMMs push enough test current to visibly twitch it. That twitch *is* the speaker principle: current through the coil, force on the cone.

Then the classic continuity-and-polarity check: **briefly** tap a 9 V battery across the speaker **through a 100 Ω resistor** (never bare — 9 V straight into 4 Ω would ask for 20 W). You'll hear a click on connect and another on disconnect, and *silence in between* even though ~85 mA flows the whole time. The speaker reproduces **change**; steady current is just heat. If you watch closely, the cone moves out on connect and returns on disconnect (or the reverse — that's how you identify the + terminal).

## Bench exercise E6B — how many volts is 35 watts?

No building — this one is arithmetic that recalibrates your sense of scale, using the ST-70's rated 35 W per channel.

**Predict the voltage swing at each OPT tap at full rated power:**

$$ V_\text{RMS} = \sqrt{P \times R} $$

| Tap | V_RMS at 35 W | V_p-p (× 2√2) | Current (RMS) |
|---|---|---|---|
| 4 Ω | √140 ≈ 11.8 V | ~33 V | ~3.0 A |
| 8 Ω | √280 ≈ 16.7 V | ~47 V | ~2.1 A |
| 16 Ω | √560 ≈ 23.7 V | ~67 V | ~1.5 A |

Two things to sit with. First, **3 amps** of audio current at the 4 Ω tap — three hundred times the currents in your divider exercises; this is why output stages and OPTs are big iron. Second, the same 35 W is *fewer amps but more volts* at 16 Ω — the OPT taps are just transformer ratios trading voltage for current at constant power, which is why matching the tap to the speaker matters.

Then flip it around for perspective: late-night listening at 50 mW into 4 Ω is V_RMS = √0.2 ≈ **0.45 V**. The gulf between 0.45 V and 11.8 V — a factor of only 26 in voltage — spans whisper to full power. Amplifier power ratings are logarithmic creatures.

## Bench exercise E6C — why your phone can't do it (source impedance meets 4 Ω)

**Parts:** phone/dongle audio output, 4 Ω speaker, the coupling cap rig from [E5B](e5-caps-with-ac.md) if you built it, scope or DMM (AC volts, with a steady sine tone).

Play a ~400 Hz tone at full phone volume. **Measure the output open-circuit** (probe the plug tip to sleeve, nothing connected): typically ~0.5–1 V RMS. Now connect the speaker (through a big cap, e.g. 470 µF, to keep any DC offset out) and measure again *across the speaker*.

**Predict:** headphone outputs have a source impedance of a few ohms to a few tens of ohms. If yours is, say, 10 Ω, the E4 sag divider gives 4/(10+4) ≈ 29% of the open-circuit voltage — most of the signal never reaches the load. From your two measurements, compute the source impedance the same way as [E4A](e4-source-impedance-and-sag.md):

$$ R_\text{source} = R_\text{speaker} \times \dfrac{V_\text{open} - V_\text{loaded}}{V_\text{loaded}} $$

And compute the actual power delivered: P = V_loaded² / 4. Expect single-digit **milliwatts** — audible in a quiet room, and roughly four orders of magnitude short of the ST-70. "Power amplifier" is not a marketing term; it's the specific job of making a source impedance low enough, and a voltage swing big enough, to feed 4 Ω.

## What if my number is different?

- **DCR reads much higher than ~3 Ω:** you may have an 8 Ω or 16 Ω speaker regardless of what the label says, or corroded terminals are adding contact resistance.
- **No click in E6A:** open voice coil (dead speaker), or the 100 Ω resistor isn't actually in circuit — re-check before trying anything more direct.
- **E6C shows almost no sag:** some dongles/DACs have sub-1 Ω outputs and genuinely drive 4 Ω well at low power. Fine — your measurement just characterized a better source than expected. The method is the point.

## Why this matters for the ST-70

- The **OPT secondary taps** ([steps 11–12](../../build/output-stage/step-11-right-opt-secondaries.md)) are E6B's table in copper: the same 35 W presented as 4, 8, or 16 Ω worth of volts-and-amps. Connecting a 4 Ω speaker to the 16 Ω tap doesn't blow anything up — it just means the amp runs out of voltage swing early (and the feedback, sampled at the 16 Ω tap, sees a different world).
- **No DC in the speaker** is enforced structurally in the ST-70: the OPT's secondary is magnetically coupled — only *changing* primary current induces secondary voltage, so the speaker is DC-isolated by physics, no coupling cap needed. (Solid-state amps without output transformers have to solve E6A's problem other ways.)
- The **damping** you feel when you flick a connected speaker's cone versus a disconnected one — try it, with the amp off, speaker wired to the OPT — is source impedance made tactile: the low-impedance winding (and, powered, the feedback loop per [E7](e7-feedback-divider.md)) brakes the cone electrically. That braking is "tight bass."

[← Back to optional extras](index.md)
