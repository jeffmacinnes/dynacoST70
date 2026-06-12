---
title: Functional testing
---

# Functional testing

The amp powers up cleanly. B+ is right. Bias is set. Now it's time to actually run audio through it and see if it sounds like an amplifier. This page covers the progression from "I think it's working" to "I'm confident enough to wire it to my real speakers."

## Equipment you'll want

- **A signal source** — a phone with a 1 kHz sine wave generator app, a function generator if you have one, or just music from a streaming service.
- **A dummy load** for initial testing — an 8 Ω 50 W resistor (or 4× 33 Ω 25 W in series-parallel). NOT a speaker. The first time you run the amp at full power, you want resistive load, not a $500 transducer.
- **Real speakers** for the actual listening test (after the dummy load proves the amp doesn't smoke).
- **A DMM** still set up at the cathode sense resistors so you can watch bias under signal.
- **Optionally an oscilloscope** — see [oscilloscope](../test-equipment/oscilloscope.md) for what it shows.

## Why a dummy load first

A speaker is a fragile, expensive, complex load. If something is wrong with the amp — DC offset, oscillation, runaway bias — a speaker can be damaged or destroyed in seconds. A resistor is none of those things; it dissipates the same power and gives a representative test of the amp's behavior without the risk.

An 8 Ω 50 W resistor is sufficient. Wire it between the 8 Ω secondary tap and the GND tap of the 4-screw terminal strip on each channel.

## Stage 1 — bias check under signal

With the dummy load connected and bias set to ~50 mA per tube:

1. Power on, let warm up 5 minutes.
2. Confirm bias is still at ~50 mV per tube (DMM on cathode sense).
3. Feed a low-level 1 kHz sine wave into the input (start at ~10 mV, way below normal listening level).
4. Watch the DMM on each cathode sense resistor.

What you should see: the cathode reading oscillates slightly around 50 mV but the average stays at 50 mV. The oscillation is class-AB behavior — the tube conducts more on signal peaks. Magnitude depends on signal level.

**What you should NOT see:**

- Bias creeping UP over time (tube going thermal-runaway-positive).
- Bias creeping DOWN to zero (tube cutting off / dying).
- One channel's bias dramatically different from the other under signal.
- A sudden jump in bias that doesn't return.

Any of these = power off, troubleshoot.

## Stage 2 — listen for hum (no signal)

With the amp powered, warmed up, dummy load connected, and **no signal input**:

1. Disconnect the dummy load and connect a known-good speaker. (You're about to listen at very low volume, so speaker risk is low — but if you're paranoid, keep the dummy load wired and use small speakers in parallel just for this listening test.)
2. Volume control all the way down.
3. Put your ear close to the speaker.

What you should hear: ideally nothing. Realistically, a faint background hum at 60 Hz or 120 Hz. Quality benchmarks:

- **Excellent**: hum is inaudible at 1 foot from the speaker. (~80 dB below full output.)
- **Acceptable**: hum is audible only with your ear right at the speaker. (~70 dB below.)
- **Poor**: hum is audible across a quiet room. (Less than 60 dB below.)
- **Broken**: hum is audible at normal listening distance — something is wrong with the grounding, heater wiring, or filter caps.

If hum is poor: check the [heater CT grounds](../build/power-supply/step-06-heater-cts.md), the [seven-lug strip](../components/seven-lug-terminal-strip.md), and the [3-prong cord earth](../modifications/3-prong-cord.md) wiring. See [grounding and hum](../theory/grounding-and-hum.md) for the diagnostic procedure.

## Stage 3 — first signal (low level)

Feed a 1 kHz sine wave at ~50 mV peak (use a function generator if you have one; a phone signal-gen app works too).

1. Volume control to about 25 % of max.
2. Listen to the dummy load (use headphones across the load if you want — DON'T do this with the amp at full volume).
3. The dummy load doesn't produce sound; you have to either use a speaker or hook a scope across the load.
4. **What you want:** a clean, pure tone — no buzz, no distortion, no scratching.
5. **Roll the volume up slowly.** The tone should get louder without distorting. Listen for any onset of harshness.

If you hear:

- **Scratching/intermittent** noise → bad solder joint or socket pin.
- **Crackling on volume changes** → dirty volume pot, clean with DeoxIT.
- **Mid-range honk** → output transformer issue or imbalanced phase splitter.
- **Distortion at moderate levels** → bias might be too cold, or a tube is weak.

!!! tip "4-ch scope: watch the gain chain build the audio signal"
    This is the educational measurement that ties the whole signal path together. Inject a 1 kHz sine, 50 mV into one input. Probe (AC-coupled, time base 200 µs/div for ~2 cycles):

    - **Ch1**: Left RCA input (~50 mVp-p, the original signal)
    - **Ch2**: 6GH8A pentode plate (PC-3A eyelet for plate, look for ~2.5 Vp-p — that's gain of ~50)
    - **Ch3**: 6GH8A triode plate (the **+phase** output of the cathodyne)
    - **Ch4**: 6GH8A triode cathode (the **−phase** output of the cathodyne)

    What you should see:

    - Ch1 is the small input sine.
    - Ch2 is the same waveform amplified ~50× and **inverted** (pentodes invert phase by their nature; the plate goes negative when the grid goes positive).
    - Ch3 and Ch4 are the same amplitude as ch2 (unity gain through the cathodyne), but **ch3 and ch4 are exactly 180° apart from each other** — that's the [phase split](../theory/phase-splitting.md). When one rises, the other falls by the same amount. Their sum equals zero at all times.

    What it tells you: every gain and inversion stage from input to phase-splitter output is working as designed. If ch3 and ch4 are *unequal* in amplitude, the cathodyne resistors don't match (or the triode itself is asymmetric — possibly a tube on its way out). If ch2 isn't ~50× ch1, the pentode B+ is wrong or the cathode bypass is failing.

!!! tip "4-ch scope: see push-pull at the output stage"
    With the same input signal applied, swap the probes to:

    - **Ch1**: V2 plate (pin 3) — should swing **~400 Vp-p** when the amp is near full output. **Use a 100:1 probe** here; 10:1 will pin the trace.
    - **Ch2**: V3 plate (pin 3) — same as ch1 but **180° out of phase**
    - **Ch3**: 8 Ω secondary tap (across the dummy load)
    - **Ch4**: Same input signal as before

    What you should see: ch1 and ch2 are mirror images of each other — when V2's plate falls, V3's rises by the same amount. Their *difference* is what couples into the secondary (ch3). The output (ch3) is in phase with the input (ch4) — the amp doesn't invert overall, because there's an even number of inversions in the chain.

    What it tells you: push-pull is balanced (both halves of the OPT primary are being driven equally). If ch1 and ch2 are unequal, one EL34 is weaker — fix it before driving real speakers, since asymmetric drive saturates the OPT core and clips early. If ch3 has obvious 60 Hz or 120 Hz on top of the 1 kHz, you have hum coupling that needs investigating.

## Stage 4 — square wave test (if you have a scope)

The single most diagnostic test for an audio amp.

1. Set the function generator to 1 kHz square wave, ~50 mV input.
2. Scope on the dummy load (use a 10× probe so you don't load the output).
3. Look at the output square wave shape:

| What you see | What it means |
|---|---|
| Clean, flat tops with sharp transitions | Amp is good across audio range |
| Rounded leading edges | High-frequency loss (often coupling cap aging) |
| Tilted/sloped tops | Low-frequency loss (different coupling cap aging) |
| Ringing on the rising edge | Instability — feedback loop is marginal |
| Asymmetric clipping at high amplitude | Push-pull tubes unbalanced (re-bias) |
| Output gets noticeably narrower at the right side of the screen | High-frequency rolloff |

A square wave test takes 30 seconds and tells you 90 % of what's wrong with an amp.

Step the frequency from 100 Hz up to 50 kHz, watching the wave shape. The ST-70 should produce clean square waves from ~30 Hz up to ~15 kHz without significant degradation.

!!! tip "4-ch scope: per-stage frequency response with one square wave"
    A 4-channel scope lets you see *where* in the chain a square wave starts degrading — which is far more diagnostic than only seeing the final output. Inject a 1 kHz square wave, ~50 mV. Probe (AC-coupled):

    - **Ch1**: Input (the original square)
    - **Ch2**: 6GH8A pentode plate (pentode output)
    - **Ch3**: V2 plate (post-EL34, pre-OPT)
    - **Ch4**: 8 Ω secondary tap (final output)

    Sweep the square wave from 30 Hz up to 30 kHz. At each frequency, compare the four traces:

    - **All clean** → that frequency is good through the whole chain.
    - **Ch1 clean, ch2 sloped** → low-frequency loss at the pentode input coupling cap (aged input cap).
    - **Ch1, ch2 clean, ch3 sloped** → loss at the coupling cap between triode output and EL34 grid.
    - **Ch1-ch3 clean, ch4 sloped or ringy** → the OPT itself is rolling off (normal at the extremes — it's a transformer) or has stability issues with the feedback loop.

    What it tells you: localizes any frequency-response issue to a specific stage. With a single-channel scope you only see the final output and have to guess which stage caused the problem; the 4-channel view eliminates the guessing.

## Stage 5 — full-power test

This is the moment of truth: the amp running at or near its rated 35 W output.

1. Still using the dummy load.
2. 1 kHz sine wave, scope across the load (if available).
3. Crank the volume control until you see clipping start (flat tops on the sine wave at the load).
4. Note where on the volume pot this happens — this is your maximum output point.
5. Back off slightly until the sine is clean again.
6. Run for 5 minutes at this near-max level.

What to watch for during this 5 minutes:

- **EL34 plates** — should NOT glow red. Some heating is normal; visible red is too hot.
- **Filter cap** — should NOT get hot to the touch. A warm cap is OK; hot suggests a problem.
- **Transformer** — should NOT smell like burning. A faint warm-electronics smell is normal; burnt insulation is not.
- **Bias** — should stay stable. If bias creeps up under load, the tube is becoming gassy.
- **Sound** — should stay clean. Distortion that wasn't there at lower volumes = problem.

If anything goes wrong, drop the volume immediately. Don't power off mid-signal — that can cause transients into the speakers.

!!! tip "4-ch scope: see the feedback loop in action"
    The [global negative feedback loop](../signal-paths/negative-feedback.md) is invisible until you scope its summing junction. With a 1 kHz sine at low-to-moderate level:

    - **Ch1**: Input (RCA, ~50 mVp-p)
    - **Ch2**: Output (8 Ω secondary tap, dummy load — proportional to ch1 with the closed-loop gain)
    - **Ch3**: OPT 16 Ω secondary tap (the feedback sample point, before the feedback resistor)
    - **Ch4**: Pentode cathode (the feedback summing node — where ch3 returns through R_fb)

    What you should see:

    - Ch1 (input) and ch2 (output) are in phase, output is much larger.
    - Ch3 (16 Ω tap) is in phase with ch2 (it's the same signal, just at lower amplitude).
    - **Ch4 (pentode cathode) is the interesting one** — it should be a small AC signal (~10–20 mVp-p), and it should be **in phase with the input** because the feedback opposes the input (the *math* is `cathode = input − k·output`, and since output is in phase with input, the residual at the cathode is the small uncorrected error).

    What it tells you: if ch3 is essentially zero (no signal at the 16 Ω tap), the feedback wire is disconnected — and you'd notice immediately because the amp would suddenly have ~10× more gain and ~10× more distortion (the loop is worth 20 dB). If ch4 is *not* in phase with ch1, the feedback is positive (wiring inversion somewhere) and the amp is moments away from oscillating.

    **Bonus measurement**: temporarily disconnect the feedback wire (from the rear-strip lug 1 to PC-3A eyelet 12 or 13 — pull the wire at the eyelet end so you can re-solder it), and watch ch4 change. With feedback open, the gain shoots up (output for the same input grows by ~10×) and any distortion in ch2 becomes much more obvious. Reconnect to see the loop "fix" the signal — visceral demonstration of what feedback buys you.

## Stage 6 — connect real speakers

When all the above passes, swap the dummy load for your actual speakers. Match the impedance tap to the speaker (8 Ω speaker → 8 Ω tap, etc.).

1. Volume to 0 before connecting.
2. Power on, warm up 5 minutes.
3. Feed a familiar piece of music — something you know well.
4. Slowly raise the volume.
5. Listen for:
   - **Channel balance** — does one channel sound louder/quieter?
   - **Stereo image** — does the soundstage feel correct?
   - **Frequency balance** — does bass / midrange / treble sound right?
   - **Anything weird** — buzz, hum, distortion, intermittent noise

Pick something you've heard on other amps. The point isn't to evaluate whether the ST-70 sounds *good* (it does); it's to verify it doesn't have any obvious defects.

## Long-warm-up stability check

After 60+ minutes of running:

1. Re-measure bias. Compare to the cold-warm-up bias from [bias adjustment](bias-adjustment.md).
2. Re-measure B+. Should be within ~10 V of the cold-warm-up value.
3. Note any new noises.

Long-term stability matters. A tube that biases at 50 mA when cold and 65 mA after an hour has a heating-related issue — possibly a gassy tube, possibly a thermal problem in the bias divider. Tubes with significant warm-up drift have shorter useful life.

## Listening — the real test

After 5-10 hours of "burn-in" listening (light to moderate levels), the amp should settle into its mature character. Then put on a familiar recording — your favorite album, something with a wide dynamic range, ideally well-recorded.

Listen for what's *missing* as much as what's there:

- **Detail in quiet passages** — can you hear breaths, fingerings, room acoustic?
- **Bass tightness** — does the bass have shape and timing, or does it sound mushy?
- **Vocal naturalness** — does the singer sound real, or does the recording sound "engineered"?
- **Soundstage** — do instruments occupy specific places, or all crowd to the speakers?
- **Dynamics** — does loud feel loud, quiet feel quiet?

If you've never heard high-end audio: the ST-70 will impress you. If you have: it'll sound exactly like a well-built ST-70 — clean, smooth, slightly warm.

## Sign-off

When everything passes:

- Final bias check.
- Final voltage check.
- Note the date and any tube serial numbers in your build log.
- Take a "completion photo" of the chassis.

You're done with bring-up. The amp now goes into regular service. Plan to re-bias in ~50 hours.

## See also

- [Bias adjustment](bias-adjustment.md) — the procedure before this one
- [Oscilloscope](../test-equipment/oscilloscope.md) — what a scope shows during signal testing
- [Heater circuits](../theory/heater-circuits.md) — what hum-floor numbers to expect
- [Grounding and hum](../theory/grounding-and-hum.md) — if hum is bad, diagnose here
