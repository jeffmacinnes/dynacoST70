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

**Compute the choke drop yourself.** The choke has ~100 Ω DCR (a number you can verify in [exercise 1's continuity check](../bring-up/continuity-checks.md)). The total current through it is the sum of:

- Four EL34s, ~50 mA each plate current (manual p.11) = 200 mA total.
- PC-3A board draw, ~10 mA.

So total ≈ 210 mA. Choke drop = 0.21 × 100 = **21 V**. Predicted lug 1 = 435 − 21 = **414 V**. Matches the manual chart's 415.

**Now compute the 6.8 kΩ drop.** The PC-3A board pulls a few mA through that resistor (just the cathodyne plate-load and pentode screen current — order ~6 mA). Drop = 0.006 × 6800 = **41 V**. Predicted lug 4 = 414 − 41 = **373 V**. Manual says 375 ✓.

**The 22 kΩ drop.** Pentode plate-load current alone, ~3 mA. Drop = 0.003 × 22,000 = **66 V**. Predicted lug 3 = 373 − 66 = **307 V**. Manual says 305 ✓.

When you bring up the amp and measure a rail that's 30 V different from what *you* just computed, the math tells you exactly where to look: the current through that stage's dropping element isn't what you assumed, which means either the element is wrong, or the downstream load is wrong.

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

**Predict the ripple at lug 1.** A choke-input filter with 1.5 H, 20 µF, at 120 Hz, and a load of 210 mA:

The 120 Hz ripple coming off the rectifier (before the choke) is large — the cap at lug 2 only smooths the peaks by ~50%. Let's say ~30 Vp-p of 120 Hz at lug 2 (worst case).

The choke + 20 µF at lug 1 forms a low-pass filter. At 120 Hz, the inductive reactance is X_L = 2πfL = 2π × 120 × 1.5 = 1131 Ω. The capacitive reactance is X_C = 1/(2πfC) = 1/(2π × 120 × 20e-6) = 66 Ω. The attenuation factor is roughly X_C / X_L = 66/1131 = 0.058, so ~17× attenuation, or ~25 dB.

Predicted lug 1 ripple: 30 Vp-p / 17 ≈ **1.8 Vp-p of 120 Hz**. Realistically lower because we overestimated the lug-2 ripple — call it **~100 mV to 500 mV** as a healthy range.

**Setup the scope:**

- **AC coupling** (essential — the DC offset is 415 V).
- 10× probe (rated; check your spec).
- Probe tip to lug 1, ground clip to chassis ground at the cap.
- 100 mV/div vertical.
- 2 ms/div horizontal (so ~2 cycles of 120 Hz fit).
- Trigger on channel, rising, level at 0 V.

You should see a roughly-triangular 120 Hz ripple riding on the rail. Amplitude is the diagnostic:

- **<200 mVp-p:** excellent. Choke and caps are doing their job.
- **200 mV – 1 Vp-p:** acceptable.
- **>1 Vp-p:** something is wrong — probably the lug-2 cap section has lost capacitance, or one half of the 5AR4 is dead (which would show 60 Hz instead of 120 Hz).

The **frequency** is also diagnostic: 120 Hz = full-wave rectification working; 60 Hz = half-wave failure (one rectifier leg dead).

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
| Pentode plate (board eyelet for V_a plate node) | ~5 Vp-p, **inverted** | 50× voltage gain from the pentode |
| Triode plate (V_b of 6GH8A) | ~5 Vp-p, same phase as pentode plate (cathodyne unity) | Splits to two outputs |
| Triode cathode | ~5 Vp-p, **inverted** vs the plate output | The other half of the split |
| V3 grid (EL34, left channel, via board eyelet 2) | ~5 Vp-p | Direct from cathodyne |
| V2 grid (EL34, left channel, via board eyelet 1) | ~5 Vp-p, opposite phase from V3 | Push-pull drive |
| OPT secondary, 16 Ω tap | ~6 Vp-p (depends on output level setting and feedback) | The amplified signal |

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
