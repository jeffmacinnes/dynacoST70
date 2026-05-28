---
title: Negative feedback path
---

# Negative feedback path

Negative feedback is a single circuit decision with outsized consequences: take a small fraction of the output signal, invert it, and add it back to the input. The amplifier then sees its own output and corrects for any difference between intended and actual — trading raw gain for lower distortion, lower output impedance, and flatter bandwidth.

In the ST-70 the feedback loop wraps **every stage** of the amp: from the input pentode all the way through to the speaker terminals and back. For the theory (the closed-loop math, what loop gain buys you, what stability constraints come with it), see [feedback](../theory/feedback.md). This page traces the **physical wires** that implement the loop — and there are two per channel, not one.

## At a glance — one channel

```
       Audio in → pentode → triode → EL34 push-pull → A-470 primary → speaker
                    │
                    │← (feedback returns here, at the pentode cathode)
                    │
                    │   ┌──────────────────────────────────────────────┐
                    │   │  Two feedback wires combine on the PC-3A:    │
                    │   │                                              │
                    │   │  Main loop:    16 Ω secondary tap → eyelet   │
                    │   │                → R_fb → pentode cathode      │
                    │   │                                              │
                    │   │  HF compensation: UL screen tap (primary)    │
                    │   │                → eyelet → R+C → same cathode │
                    │   └──────────────────────────────────────────────┘
```

## Why there are two feedback wires per channel

The main feedback loop samples at the **16 Ω secondary tap** — the conventional choice, because it represents the actual speaker-level output. That tap goes through a resistor (R_fb) to the input pentode's cathode, where it sums against the AC signal arriving at the same cathode through local cathode bias. This is the loop that sets closed-loop gain and gives the ST-70 its low distortion.

The catch: the output transformer adds phase shift at high frequencies, and at some frequency that phase shift accumulates to where the feedback stops being negative and turns positive — at which point the amplifier oscillates. Without compensation, an OPT with steep HF roll-off can push the amplifier into oscillation despite stable behavior at audio frequencies.

The fix: a **second feedback tap from the UL screen winding on the primary**, brought back to the same input cathode through an RC network that bites only at high frequencies. At HF, this second path "feeds forward" some phase-corrected signal that cancels part of the OPT-induced phase shift, restoring negative-feedback margins. At audio frequencies, the cap looks open and the second path contributes nothing — the main loop dominates.

So:

- **Main loop** = 16 Ω tap (secondary). Sets closed-loop gain and audio-band distortion.
- **HF compensation** = UL tap (primary). Keeps the amp stable; only active above a few kHz.

Both terminate at the same node (the pentode cathode) but through different RC networks on the PC-3A board.

## Stage by stage — main loop (16 Ω tap)

### Stage 1 — OPT secondary, YELLOW lead

Each [A-470](../components/a-470-output-transformer.md)'s 16 Ω secondary tap (the YELLOW lead) was landed at lug 1 of its 4-screw rear terminal strip in [step 11](../build/output-stage/step-11-right-opt-secondaries.md) (right channel) and [step 12](../build/output-stage/step-12-left-opt-secondaries.md) (left channel) — and *deliberately left unsoldered* at that step, because the feedback wire would land on the same lug later.

### Stage 2 — Wire from rear strip lug 1 → eyelet on PC-3A board

- **Right channel**: 9½" wire from right strip lug 1 → eyelet 13 ([step 62](../build/driver-stage/step-62-right-strip-1-to-eyelet-13.md)).
- **Left channel**: 12" wire from left strip lug 1 → eyelet 12 ([step 60](../build/driver-stage/step-60-left-strip-1-to-eyelet-12.md)).

The wire length is calibrated — the manual notes that this wire must be routed *close to the chassis* and *around the printed circuit board*. This wire carries a low-level audio signal mixed with the feedback content; nearby AC fields (heaters, power transformer) can induce hum if the wire's loop area is large. Hugging the chassis uses the metal as a partial shield.

### Stage 3 — Through the feedback resistor R_fb on the PC-3A

Inside the board, the feedback wire passes through the **feedback resistor** (~10 kΩ, sized for the desired feedback amount) on its way to the pentode's cathode. The value of this resistor, together with the pentode's cathode bias resistor, sets the feedback fraction `β` and therefore the closed-loop gain.

The original ST-70 uses about **16 dB of feedback** — meaning the closed-loop gain is about 6× lower than the open-loop gain. See [feedback theory](../theory/feedback.md#what-feedback-buys-you-concretely) for what 16 dB buys.

### Stage 4 — At the pentode cathode

The feedback signal arrives at the pentode's cathode and **sums** there with the cathode bias resistor + bypass cap network. The cathode is the magic node: the AC signal coming in from the grid causes the plate current to swing in one direction; the feedback signal coming in at the cathode tries to swing the plate current the *opposite* direction; the net result is whatever combination satisfies both.

Because the feedback is inverted (sampled at the OPT secondary after an even number of phase inversions through the amp), it *opposes* the input signal. The pentode effectively amplifies the *difference* between input and feedback. That's the closed-loop control mechanism.

## Stage by stage — HF compensation (UL tap)

A second wire per channel adds the HF compensation feed-forward:

- **Right channel**: V6 pin 4 (GREEN/WHITE UL screen tap, already landed at V6 pin 4 in [step 14](../build/output-stage/step-14-left-opt-primary.md)) → eyelet 14, via 5½" wire in [step 48](../build/driver-stage/step-48-eyelet-14-to-v6-feedback.md).
- **Left channel**: V3 pin 4 (UL tap on the left side) → eyelet 11, via [step 58](../build/driver-stage/step-58-v3-to-eyelet-11-feedback.md).

The UL tap is closer to the EL34 plate (electrically) than the secondary — it has the audio signal at a higher voltage and with less phase shift from the OPT. Sampling here gives the compensation network a "head start" on the phase rotation that the secondary will impose at HF.

On the board, the wire goes through a small **RC network** (typically ~10–22 kΩ + ~100–470 pF) before joining the main feedback at the pentode cathode. The cap is the key: it shunts the resistor at high frequencies, letting more of the compensation signal through where it's needed; at audio frequencies, the cap looks open and the path contributes negligibly.

## Why sampling from the UL tap (not the 16 Ω tap) for compensation

Two design choices interact:

1. **The 16 Ω secondary tap is the "true" output** — it's what the speaker sees, so it's the right place to sample for the main loop. Sampling earlier in the OPT would mean "controlling" something other than what the speaker actually hears.
2. **The UL tap is "before" the OPT secondary's leakage inductance** — so phase shift at HF is smaller there. Sampling here for *compensation* means the corrective signal arrives with the right phase to push the main loop back into stable territory.

Dynaco's design (taking compensation from the primary UL tap) is one of several valid choices — other designs use a small cap across R_fb (a "step network"), or use a different sample point. The UL-tap approach has the benefit of being implementable with just one extra wire and a small RC on the board.

## Per-channel notes

| | Left channel | Right channel |
|---|---|---|
| Main loop sample point | Left 4-screw strip lug 1 (YELLOW) | Right 4-screw strip lug 1 (YELLOW) |
| Main loop arrives at | Eyelet 12 ([step 60](../build/driver-stage/step-60-left-strip-1-to-eyelet-12.md)) | Eyelet 13 ([step 62](../build/driver-stage/step-62-right-strip-1-to-eyelet-13.md)) |
| HF comp sample point | V3 pin 4 (UL tap) | V6 pin 4 (UL tap) |
| HF comp arrives at | Eyelet 11 ([step 58](../build/driver-stage/step-58-v3-to-eyelet-11-feedback.md)) | Eyelet 14 ([step 48](../build/driver-stage/step-48-eyelet-14-to-v6-feedback.md)) |
| Both terminate at | Left 6GH8A pentode cathode | Right 6GH8A pentode cathode |

Per-channel feedback loops are completely independent — the right channel's feedback doesn't interact with the left channel's. They share no wires.

## Where it can break

| Symptom | Likely cause | DMM probe |
|---|---|---|
| Channel has way too much gain (audibly loud) | Main feedback loop open (broken wire, cold solder at strip lug 1) | Probe continuity from rear strip lug 1 to eyelet 12/13 |
| Channel oscillates (squeals, motorboats, looks like noise on the scope at the speaker) | HF compensation missing (broken UL-tap wire, missing or shorted cap on board) | Check eyelet 11/14 has the right RC network intact |
| Channel has the right gain but ringy / shouty at HF | HF compensation cap value wrong or aged | Replace; this is a small cap on the PC-3A board |
| Channel motorboats at very low frequency | Coupling cap on the board too small or feedback loop has DC gain | Scope at pentode plate; look for sub-audio oscillation |
| Slight hum on one channel only | Feedback wire routed too close to a heater wire or power transformer; inducing AC | Re-dress the wire close to the chassis; check the routing matches the pictorial |
| Feedback wire fell off | Wire snapped or cold joint | Visual inspection; resolder |

A note on debugging feedback: it's tempting to assume "the amp works without feedback so feedback isn't necessary." That's wrong — *without feedback, an ST-70 has roughly 6× more distortion and a much higher output impedance, plus drift problems*. Always restore feedback before judging the amp's sound; an "open-feedback" amp is broken, not honest.

## Why feedback is invisible until it's not

When feedback is working, you don't hear it — by design. What you hear is the *absence* of the things feedback suppresses: distortion at low and mid power, woolly bass, drifty mid-band response. A well-functioning ST-70 sounds tight and clean.

When feedback fails (open wire, dried-up cap, wrong resistor), the amp's character changes immediately and dramatically:
- Gain goes up by 6×
- THD goes up by 6×
- Output impedance goes up by 6×
- HF response gets ringy
- And in the worst case, the amp oscillates

All four feedback wires (two per channel) are equally load-bearing. They're tiny — a few inches each — and easy to forget, but the amp without them is unrecognizable.

## See also

- [Feedback theory](../theory/feedback.md) — the math and the trade-offs
- [Phase splitting](../theory/phase-splitting.md) — what the feedback loop wraps around
- [A-470 output transformer](../components/a-470-output-transformer.md) — both feedback samples come from this part
- [PC-3A driver board](../components/pc-3a-driver-board.md) — where the feedback network lives
- [Audio signal path](audio.md) — the forward path that the feedback wraps
