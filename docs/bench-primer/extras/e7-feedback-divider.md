---
title: E7. The feedback divider
---

# Extra E7 — Negative feedback is a voltage divider plus subtraction

*Optional module. Assumes [exercise 2](../02-voltage-dividers.md); an AC source (signal generator or phone tone) and scope make the bench half better, but the arithmetic half needs only a calculator. Read alongside [feedback theory](../../theory/feedback.md).*

## The concept

Negative feedback sounds like the most advanced thing in the amp. Strip it down and it's two operations you already own:

1. **A voltage divider** samples a fraction β of the output: β = R_bottom / (R_top + R_bottom). Nothing new — this is exercise 2.
2. **A subtraction**: the amp is arranged so that what it actually amplifies is `input − β·output`. In the ST-70 the subtraction happens at the input pentode's cathode, but the *math* doesn't care where.

Everything feedback does follows from solving that loop (derived in [feedback theory](../../theory/feedback.md#the-mechanism-in-one-paragraph)):

$$ \text{closed-loop gain} \; A_{CL} = \dfrac{A}{1 + A\beta} $$

where A is the amp's raw ("open-loop") gain. When Aβ is much bigger than 1:

$$ A_{CL} \approx \dfrac{1}{\beta} $$

Read that twice, because it's the punchline of the whole module: **the gain of the finished amplifier is set by two resistors, not by the tubes.** The tubes just need to supply *enough* raw gain; the divider decides what the amp actually does. All the famous benefits — 10× less distortion, low output impedance, flat response — are this one equation applied to different disturbances.

## Bench exercise E7A — build and measure a β network

**Parts:** 10 kΩ and 1 kΩ resistors, signal source, scope (or DMM on AC volts with a low-frequency tone, ~100 Hz, where cheap meters are still accurate).

Pretend the signal generator is the amp's output — its signal stands in for what appears at the OPT's 16 Ω tap. Build the sampler:

```
"output" (sig gen) ──[ 10 kΩ ]──┬──→ fed-back signal, to the scope
                                │
                              [ 1 kΩ ]
                                │
                               GND
```

**Predict:**

$$ \beta = \dfrac{1{,}000}{10{,}000 + 1{,}000} = \dfrac{1}{11} \approx 0.091 $$

With the generator at 5 Vp-p, the tap should show 5 × 0.091 ≈ **0.45 Vp-p** — same wave, same phase, one-eleventh the size.

**Measure** at a few frequencies across the audio band (100 Hz, 1 kHz, 10 kHz): the fraction shouldn't budge, because resistive dividers are frequency-blind. That flatness is *why* feedback flattens an amp's response — the reference the loop enforces is flat.

## Bench exercise E7B — run the loop on paper with your measured β

Now give your divider an amplifier to govern. Take A = 1,000 as the raw gain (a plausible open-loop number for a multi-stage tube amp) and your measured β ≈ 0.091:

$$ A_{CL} = \dfrac{1{,}000}{1 + 1{,}000 \times 0.091} = \dfrac{1{,}000}{92} \approx 10.9 \qquad \text{vs.} \qquad \dfrac{1}{\beta} = 11 $$

The amp had gain to burn; the loop threw ~99% of it away and bought things with it. Watch what, exactly:

**The tubes get worse; the amp doesn't.** Age the tubes: let A sag 30%, to 700.

$$ A_{CL} = \dfrac{700}{1 + 700 \times 0.091} = \dfrac{700}{64.7} \approx 10.8 $$

A 30% collapse in raw gain moved the finished amp **0.6%**. Now do it in the other direction (A = 1,300 → A_CL ≈ 10.96) and, for contrast, with feeble raw gain (A = 30 → A_CL ≈ 8.1, a 26% error — the approximation A_CL ≈ 1/β only holds when there's excess gain to spend). Distortion is just this same insensitivity applied moment-to-moment: a tube's gain wobbling within a cycle *is* distortion, and the loop shrugs it off by the factor (1 + Aβ) — here ~92, or ~39 dB.

**The loop opens.** Set β = 0 (the feedback wire falls off the terminal strip):

$$ A_{CL} = \dfrac{A}{1 + 0} = 1{,}000 $$

Gain jumps ~92× (~39 dB), distortion and output impedance jump with it. That's not hypothetical — "channel has way too much gain (audibly loud)" is the first row of the [feedback troubleshooting table](../../signal-paths/negative-feedback.md#where-it-can-break), and now you know why the symptom is *loud*, specifically.

## Bench exercise E7C — see the subtraction (scope, two channels)

If your scope has two channels: feed the same sine into CH1 (the "input") and probe your E7A divider's tap on CH2 (the "fed-back sample"), both grounds common. Overlay them. What the pentode's cathode does in the real amp is present the *difference* of these two waves to the tube. Now imagine the output misbehaving — bigger than it should be for an instant: the CH2 sample grows, the difference shrinks, the amp drives less, the output falls back. Undershoot: the reverse. The loop is a thermostat running at audio speed, and both of its sensory organs are on your breadboard.

(Only the subtraction itself is missing, because it needs an active device — that part you get for free inside the ST-70.)

## What if my number is different?

- **β is off prediction:** resistor tolerance — measure both resistors and recompute; the divider never lies.
- **β changes with frequency:** at 10 kHz with long unshielded leads and a 1× probe you may be seeing cable/probe capacitance loading the 1 kΩ leg. Use the 10× probe. (Real feedback networks fight this exact parasitic — it's one reason HF stability compensation exists.)
- **The paper numbers feel like cheating:** they're not — E7A *measured* β, and β is the only part of the loop equation the designer actually builds. A is whatever the tubes bring that day, which is precisely the point.

## Why this matters for the ST-70

Now walk the [negative feedback path](../../signal-paths/negative-feedback.md) with your breadboard in mind:

- The **main loop** samples the OPT's 16 Ω tap and runs through the 1 kΩ feedback resistor R_fb into the pentode's cathode network — R_fb and the cathode-side impedance form the β divider you built in E7A, scaled to the amp's ~20 dB of feedback (1 + Aβ ≈ 10, so open-loop misbehavior arrives at the speaker ~10× smaller).
- **Output impedance** drops by the same (1 + Aβ) — this is the missing piece from [E6](e6-driving-a-speaker.md): the loop senses the speaker-terminal voltage sagging under load and drives harder to hold it, which *is* a lower source impedance by [E4's](e4-source-impedance-and-sag.md) definition.
- The **second, 390 pF path** from the UL tap is a β network that exists only at high frequency ([E5's](e5-caps-with-ac.md) reactance math says when), added because subtraction turns into *addition* if the loop's phase slips 180° — the stability tax on all of the above.
- And the debugging habit it buys you: an ST-70 channel that's suddenly loud, gritty, and boomy isn't "more powerful" — it's running open-loop, and the first thing to check is a few inches of wire at rear strip lug 1.

[← Back to optional extras](index.md)
