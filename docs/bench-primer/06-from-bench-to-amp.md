---
title: 6. From bench to amp
---

# Exercise 6 — From bench to amp

This is the payoff. Everything in the previous five exercises was building toward making rigorous, math-grounded predictions about the actual ST-70 on your bench. Each of the following is something you can do *now*, with the equipment you already have, with predictions you compute yourself.

## 6A — Predict every B+ rail before bring-up

From the [B+ signal path](../signal-paths/b-plus.md), the rails are:

- **Lug 2:** ~435 V (after the 5AR4, raw rectified DC)
- **Lug 1:** ~415 V (after the choke)
- **Lug 4:** ~375 V (after the 6.8 kΩ dropping resistor)
- **Lug 3:** ~305 V (after the 22 kΩ dropping resistor)

These aren't memorized magic numbers. They come from V = IR applied to the load current at each stage.

**Compute the choke drop yourself.** The choke's DCR is spec'd at 62 Ω and measures **71 Ω** on this build (a number you can verify in [exercise 1's continuity check](../bring-up/continuity-checks.md)). The total current through it is the sum of:

- Four EL34s, ~50 mA each plate current (manual p.11) = 200 mA total.
- PC-3A board draw, ~12 mA (see below).

So total ≈ 212 mA. Choke drop = 0.212 × 71 = **15 V**. Predicted lug 1 = 428 − 15 = **413 V**. Measured on this build: **413 V** ✓.

**Now compute the 6.8 kΩ drop.** The PC-3A board pulls current through that resistor — the cathodyne plate loads plus pentode screens. The manual's chart implies ~6 mA (which would drop 41 V, landing lug 4 at 375 V), but this build **measures a 64 V drop → 349 V at lug 4** — meaning the board actually draws 64/6800 ≈ **9.4 mA**. Neither number is "wrong": the manual's chart is one nominal operating point, and real 6GH8As at real voltages draw what they draw. The resistor is right, the board is healthy, the current is just higher than the chart implies.

**The 22 kΩ drop.** Pentode plate-load current alone: this build measures a 69 V drop → **3.1 mA**, landing lug 3 at **280 V** (manual chart: 305 V).

**The calibrated model for this amp:** choke DCR 71 Ω; total B+ load ≈ 212 mA (200 mA EL34s + 9.4 mA driver + 3.1 mA pentode); mains slightly low (~116 V) so everything starts ~7 V below chart at lug 2 (428 vs 435). Run V = IR down the chain with those numbers and every rail predicts within 1 V of measurement.

When you bring up the amp and measure a rail that's 30 V different from what *you* just computed, the math tells you exactly where to look: the current through that stage's dropping element isn't what you assumed, which means either the element is wrong, or the downstream load is different from assumed. The lug-4 story above is that logic working in real life — the 26 V "discrepancy" wasn't a fault, it was the measurement *correcting the assumed current*, and once corrected, the whole chain became self-consistent.

## 6B — Heater AC on the scope

Bring up only the 5 V and 6.3 V windings (no HV — pull the 5AR4 to break the rectifier circuit), with a 3 A fuse in place. Power on.

Probe V2 pin 2 ↔ V2 pin 7 with a 10× probe, ground clip on chassis.

**Predict:**

- 6.3 V RMS → peak = 6.3 × √2 = **8.9 V peak** → peak-to-peak = **17.8 Vp-p**.
- 60 Hz → period = 1/60 = **16.7 ms**.

**Setup the scope:**

- DC coupling.
- 5 V/div vertical (so the 17.8 Vp-p wave occupies ~3.5 divisions).
- 5 ms/div horizontal (so ~3 cycles fit on screen).
- Trigger on channel, rising, level at 0 V.

**Measure:** confirm 17–18 Vp-p amplitude, ~16.7 ms period. Beautiful 60 Hz sine, symmetric around 0 V. This is the simplest possible scope picture in the amp and a great confidence-builder.

Then probe **just one heater pin to chassis**: V2 pin 2 to ground (with the CT not yet grounded or with the CT cap-coupled to ground per [step 6](../build/power-supply/step-06-heater-cts.md)). You'll see roughly half the amplitude (8.9 Vp-p) centered on 0 V at audio AC, since the CT is the symmetric reference.

## 6C — B+ ripple measurement (after full bring-up)

This one needs B+ powered. Discharge everything between measurements (including before connecting/disconnecting the probe).

**Predict the ripple at lug 2 first** (before the choke). The 30 µF cap there is being drained by the full ~210 mA load between charging pulses, which arrive every half-cycle (Δt ≈ 1/120 s, and the cap supplies the load for most of it — call it ~7 ms). The sawtooth's depth is the charge drained divided by the capacitance:

$$ V_{\text{rip}} \approx \dfrac{I \times \Delta t}{C} = \dfrac{0.21 \times 0.007}{30 \times 10^{-6}} \approx 49\text{ Vp-p worst case} $$

Measured on this build: **~40 Vp-p of 120 Hz sawtooth** — big, and *normal*. (An earlier draft of this exercise guessed 5–10 V by intuition; the I·Δt/C math is the reliable path, and the measurement sided with the math.)

**Now predict lug 1.** The choke + 20 µF at lug 1 forms a low-pass filter. At 120 Hz, the inductive reactance is X_L = 2πfL = 2π × 120 × 1.5 = 1131 Ω. The capacitive reactance is X_C = 1/(2πfC) = 1/(2π × 120 × 20e-6) = 66 Ω. The attenuation factor is roughly X_C / X_L = 66/1131 = 0.058, so ~17× attenuation, or ~25 dB.

Predicted lug 1 ripple: 40 Vp-p / 17 ≈ **2.4 Vp-p of 120 Hz**. Measured on this build: **~2–3 Vp-p** ✓. Trust the divider math — don't second-guess it downward.

**Setup the scope:**

- **AC coupling** (essential — the DC offset is 415 V).
- 10× probe (rated; check your spec).
- Probe tip to lug 1, ground clip to chassis ground at the cap.
- 500 mV/div vertical.
- 2 ms/div horizontal (so ~2 cycles of 120 Hz fit).
- Trigger on channel, rising, level at 0 V.

You should see a roughly-triangular 120 Hz ripple riding on the rail. Amplitude is the diagnostic:

- **~1–3 Vp-p of 120 Hz:** healthy — matches the LC math above.
- **5+ Vp-p:** something is wrong — probably the lug-2 cap section has lost capacitance, or the choke isn't in circuit.
- **Dominant 60 Hz instead of 120 Hz:** see the pickup warning below *before* concluding anything — but genuine 60 Hz ripple means half-wave failure (one rectifier leg dead).

!!! warning "Probe pickup will lie to you at this node"
    On this build, probing lug 1 with a standard alligator-clip ground lead showed **7.6 Vp-p of clean 60 Hz sine** — which looks exactly like a dying rectifier. It wasn't. It was **magnetic pickup from the PA-060** induced in the loop formed by the probe tip and its dangling ground lead. Two ways to unmask it:

    1. **Tight ground loop:** use the probe's spring ground tip (or the shortest possible ground path). The same node then shows only ~100 mVp-p of noise floor from the loop itself.
    2. **FFT mode:** the scope's FFT separates the frequencies. On this build the FFT showed the rail's *true* 60 Hz content is under 5 mV — the 7.6 V of 60 Hz in the time-domain trace was entirely pickup. The real ripple is the ~2–3 Vp-p at 120 Hz.

    General rule from this: **for any small AC measurement on a high-voltage rail, a time-domain trace with a long ground lead is untrustworthy.** Tighten the loop, or characterize with FFT, before diagnosing.

The **frequency** is still diagnostic once pickup is ruled out: 120 Hz = full-wave rectification working; 60 Hz = half-wave failure.

## 6D — Bias voltage divider on the live amp

After bring-up. The bias network is a voltage divider you can poke around in with the DMM.

**Predict the −65 V raw bias supply** at strip lug 4. (You verified this exists at bring-up; voltage chart says −65 V.)

**Predict the pot terminals.** Three 10 kΩ resistances in series across −65 V (10 kΩ filter + 10 kΩ pot + 10 kΩ shunt to ground), assuming the pot is centered:

- Top of pot (strip lug 3 side, after the first 10 kΩ): −65 × 20k/30k = **−43.3 V**
- Bottom of pot (strip lug 2 side, before the second 10 kΩ): −65 × 10k/30k = **−21.7 V**
- Wiper at center: midpoint of the pot's resistance, so between −43.3 and −21.7 → **−32.5 V**

Matches the manual's −32 V ±20% spec on the EL34 grid.

**Measure** with DMM on DC volts. Verify all three. If a value is wildly off, you can now point to which side of the divider has a problem.

## 6E — Coupling cap leakage at operating voltage

The most rigorous filter cap leakage test you can do without a dedicated tester. **Important: this involves 300+ V DC. Be deliberate.**

Setup: pull every tube. Connect a **high-voltage DC supply** to the cap section in question — or use the amp's own B+ in a controlled way (with tubes out, the lug 1 rail will float up to whatever the 5AR4 produces unloaded, around 500 V). Through a **current-limiting resistor** in series — a 100 kΩ, 2 W resistor works.

After applying voltage, **wait 5 minutes** for the cap to fully form. Then measure the **voltage across the 100 kΩ series resistor** — this is the leakage current × 100 kΩ.

For a healthy 30 µF cap, leakage at 435 V should be <150 µA after forming. Voltage across 100 kΩ → <15 V. If you measure 50 V (= 500 µA leakage), the cap is leaky and should be replaced.

Discharge fully before disconnecting.

This is a good "forming and acceptance test" for any electrolytic cap before installing it in the amp. Do it on a brand-new quad cap before final assembly to confirm it's good.

## 6F — Audio signal trace, end to end

After bring-up, with the amp working into a dummy load. Inject a 1 kHz sine wave at 100 mVp-p into the left RCA input from a signal generator (or a phone audio output through a series resistor to attenuate).

Probe the scope through the audio path:

| Probe point | Predicted amplitude | What you should see |
|---|---|---|
| Input RCA (left) | ~100 mVp-p | The clean source |
| Pentode grid (V_a of 6GH8A, board eyelet 17 → left grid) | ~100 mVp-p (no gain yet — the input switch is unity) | Same as input |
| Pentode plate (board eyelet for V_a plate node) | ~2 Vp-p, **inverted** | ~19× measured on this build (see note below) |
| Triode plate (pin 1) | ~2 Vp-p, **inverted vs the pentode plate** — i.e., back in phase with the RCA input (measured −1° on this build) | Cathodyne unity; the pentode's inversion plus the triode plate's inversion cancel |
| Triode cathode (pin 8) | ~2 Vp-p, **180° from the plate output** (so: in phase with the pentode plate, anti-phase to the input) | The other half of the split — a cathode follower doesn't invert |
| V3 grid (EL34, left channel, via board eyelet 2) | ~2 Vp-p | Direct from cathodyne |
| V2 grid (EL34, left channel, via board eyelet 1) | ~2 Vp-p, opposite phase from V3 | Push-pull drive |
| OPT secondary, 16 Ω tap | a few Vp-p (depends on output level setting and feedback) | The amplified signal |

!!! note "Why ~19× and not the pentode's 'gain of ~50×'?"
    The pentode *stage* has an open-loop gain of roughly 50× — that's what the tube and its plate load would do in isolation. But you're probing a **working amp with the global feedback loop closed**, and the feedback signal arriving at the pentode's cathode opposes the input, cutting the *measured* input-to-plate gain. On this build the measured value is **19× (1.75 Vp-p at the plate from 90 mVp-p in)**. Expect **15–25×** on any healthy ST-70 with feedback connected. Below ~5× or above ~50× means a stage problem — and *exactly* ~50× is itself a clue that the feedback loop is open ([why loud = open loop](../signal-paths/negative-feedback.md#where-it-can-break)).

The phase relationships are as important as the amplitudes. The pentode inverts, the cathodyne produces equal-and-opposite outputs, the EL34s drive the OPT primary in push-pull. If any stage isn't doing what it should, the probe-down-the-chain method finds it in 60 seconds.

## You can now diagnose anything in this amp

Every measurement in this manual reduces to:

1. From the schematic, identify the topology at the node.
2. Use V = IR, voltage-divider math, or the τ = RC framework to predict what the meter or scope should read.
3. Measure.
4. If they agree, move on. If they don't, the size and direction of the disagreement tells you what to chase.

That's it. There's no further mystery to bring-up — just the application of the same four equations over and over. The exercises gave you the muscle memory; the schematic and the [signal paths](../signal-paths/index.md) give you the topology; the rest is practice.

Welcome to bench work.

[← Back to bench primer index](index.md)
