---
title: E5. Capacitors with AC — filters
---

# Extra E5 — Capacitors with AC: coupling and filtering

*Optional module. Assumes [exercise 4](../04-capacitors-dc.md) (RC time constants) and [exercise 5](../05-oscilloscope-fundamentals.md) (scope basics). You'll want an AC source: the signal generator from exercise 5, or a phone playing a tone/music through a headphone-jack or dongle output.*

## The concept

Exercise 4 established that a cap blocks DC once charged. The flip side: a cap **passes AC**, and how easily depends on frequency. Its opposition to AC — the capacitive **reactance** — is:

$$ X_C = \dfrac{1}{2\pi f C} $$

in ohms, with f in hertz and C in farads. Low frequency → big X_C (cap fights the signal); high frequency → small X_C (cap is nearly a wire). A 0.1 µF cap is ~16 kΩ at 100 Hz but only ~160 Ω at 10 kHz.

Put a cap and a resistor in series and you've made a frequency-dependent **voltage divider** — the AC version of exercise 2. Two arrangements, two filters:

```
  HIGH-PASS ("coupling")            LOW-PASS ("smoothing")

  in ──┤C├──┬── out                 in ──[R]──┬── out
           [R]                                ┤C├
            │                                  │
           GND                                GND
```

- **High-pass:** output is taken across R. High frequencies sail through the cap; low frequencies are dropped across it. This is a **coupling cap** — it hands the AC signal to the next stage while blocking DC.
- **Low-pass:** output is taken across C. Low frequencies survive; high frequencies are shorted to ground through the cap. This is **smoothing/filtering** — the B+ ripple filter's job.

Each has a single characteristic number, the **corner frequency** — where X_C = R and the output is down 3 dB (~71% of full amplitude):

$$ f_c = \dfrac{1}{2\pi R C} $$

Below f_c a high-pass rolls off; above f_c a low-pass rolls off. One formula, both filters.

## Bench exercise E5A — a coupling cap on the scope

**Parts:** 0.1 µF film cap, 10 kΩ resistor, signal source, scope.

Build the high-pass: source → cap → resistor → ground, scope probing across the resistor (source and scope grounds common).

**Predict the corner:**

$$ f_c = \dfrac{1}{2\pi \times 10{,}000 \times 0.1\times10^{-6}} \approx 159\text{ Hz} $$

| Frequency | Predicted output (vs. input amplitude) | Yours |
|---|---|---|
| 1.6 kHz (10 × f_c) | ~100% | |
| 159 Hz (f_c) | ~71% | |
| 16 Hz (f_c / 10) | ~10% | |

**Measure:** set the source to a sine around 1 Vp-p, sweep those three frequencies, and read amplitudes off the scope. (No generator? A free tone-generator app through the headphone output works — set the phone volume once and don't touch it between measurements.)

Then swap the 0.1 µF for **1 µF** and confirm the corner drops 10× (to ~16 Hz): at 159 Hz the output that was 71% is now ~99.5%. Bigger coupling cap → deeper bass gets through. That single sentence is most of "capacitor tone" folklore, quantified.

## Bench exercise E5B — hear the corner with a speaker

**Parts:** 4 Ω speaker, an electrolytic cap or three (say 47 µF, 100 µF, 470 µF), phone playing music.

Wire the phone's output → cap (+ toward the phone) → speaker → back to the phone's ground. The speaker's ~4 Ω *is* the R of a high-pass filter.

**Predict** the corner for each cap into 4 Ω:

$$ f_c(100\ \mu\text{F}) = \dfrac{1}{2\pi \times 4 \times 100\times10^{-6}} \approx 400\text{ Hz} $$

| Cap | Predicted f_c | What it should sound like |
|---|---|---|
| 47 µF | ~850 Hz | Telephone — no bass, thin mids |
| 100 µF | ~400 Hz | Noticeably thin, bass gone |
| 470 µF | ~85 Hz | Nearly full-range; only deep bass misses |
| straight wire | — | Reference |

**Listen:** play something bass-heavy at modest volume and swap caps. The math you just did is *audible*. (The phone will be quiet into 4 Ω — that's fine, and it's [E6's](e6-driving-a-speaker.md) topic.)

## Bench exercise E5C — a low-pass, seen and heard

Swap the arrangement: source → **10 kΩ** → output node, with **0.1 µF** from the output node to ground. Same parts as E5A, same f_c ≈ 159 Hz, opposite behavior — now 16 Hz passes at ~100% and 1.6 kHz is cut to ~10%. Verify the three-point table on the scope, inverted.

This is the topology of the **B+ ripple filter** (with the choke playing the series role and doing it better) and of the **bias supply's RC filtering** — the 10 kΩ + 100 µF sections from [steps 19–22](../../build/output-stage/step-19-bias-cap-1.md) are literally this circuit, sized to crush 60 Hz ripple: f_c = 1/(2π × 10 kΩ × 100 µF) ≈ 0.16 Hz, so 60 Hz arrives ~50 dB down. You can now compute why the bias rail is quiet.

## What if my number is different?

- **Output at 10 × f_c is well under 100%:** your source has its own output impedance ([E4](e4-source-impedance-and-sag.md)!) adding to the series leg, or the scope's 1× probe capacitance is loading the node — use the 10× probe.
- **The corner lands at the wrong frequency:** electrolytics are ±20% parts, and their marked value drifts down with age. A corner 20–30% off predicted is within honesty; 2× off means the cap isn't the value on the sleeve — you may have just diagnosed an old cap with a scope and a formula.
- **E5B's speaker version sounds less dramatic than predicted:** the speaker's impedance isn't a flat 4 Ω across frequency (it rises at resonance and at HF), so the corner smears. Real loads are not resistors — a preview of why amp designers sweat OPT behavior.

## Why this matters for the ST-70

- The **coupling caps on the PC-3A** (pentode plate → cathodyne grid, cathodyne outputs → EL34 grids) are E5A with the next stage's grid resistor as R. Their values are chosen to put f_c well below 20 Hz so the audio band passes untouched — and now you can check that: C and R off the schematic, one formula.
- **"Bigger coupling caps = more bass" has a limit** you can now articulate: once f_c is below the audio band, going bigger changes nothing audible — it only slows recovery from DC shifts (and, past the OPT's own low-frequency limit, invites trouble).
- The **cathode bypass caps** are E5C in disguise: at signal frequencies the cap's tiny X_C shorts the cathode resistor, raising stage gain — the parallel-impedance point from exercise 2, now with a number attached at every frequency.
- And the **390 pF cap in the HF compensation feedback path** ([negative feedback](../../signal-paths/negative-feedback.md)) is a high-pass built to pass *only* frequencies far above audio — same divider, aimed at stability instead of tone. [Module E7](e7-feedback-divider.md) picks up that thread.

[← Back to optional extras](index.md)
