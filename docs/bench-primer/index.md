---
title: Bench primer
---

# Bench primer

A short, hands-on series of exercises to build your intuition for circuits, the equations you'll actually use, and the test equipment on your bench. Built for ST-70 builders who want to *predict* a measurement before making it, not look it up.

## Why this section exists

Most of bring-up boils down to the same workflow:

1. **Predict** what a measurement should be from first principles.
2. **Measure** it.
3. **Compare** and either confirm the build or chase the discrepancy.

If step 1 is "ask the manual" or "guess from a range someone quoted," you're flying blind when reality doesn't match. If step 1 is "compute it from V = IR and the topology in front of me," then a mismatch becomes an actual signal — *something specific is different from what the math predicts, and that tells me where to look*.

This primer builds your step-1 muscle. Every exercise uses parts you already have (breadboard, resistors, caps, batteries, DMM, scope, variac) and follows the same shape: **predict, build, measure, explain**. By the end you'll be able to walk into any node of the ST-70 with a confident expectation, and use mismatches as diagnostic data instead of confusion.

## How to use this section

Work through the exercises in order — each builds on the previous. Each page has:

- The **concept** in one or two paragraphs.
- The **equation(s)** you'll actually use, with the units called out.
- A **bench exercise**: parts list, schematic in ASCII, prediction step, measurement step.
- **"What if my number is different?"** — the most common deviations and what they mean.

Allow 15–30 minutes per exercise. Skip nothing — the early exercises seem trivial, but their mental model is what makes the later ones land.

## Tools you'll need

- **Breadboard**, jumper wires.
- **9 V battery** with leads, or a low-voltage bench supply.
- **Resistors**: a handful in the 100 Ω, 1 kΩ, 10 kΩ, 100 kΩ, 1 MΩ ranges. Tolerance doesn't matter — 5% is fine.
- **Capacitors**: a few small electrolytics (e.g., 10 µF, 47 µF, 100 µF) and a couple of film caps (0.1 µF, 1 µF). Voltage rating ≥ 16 V is plenty for these exercises.
- **DMM** (any modern handheld with V/A/Ω/diode/capacitance modes).
- **Oscilloscope** (analog or digital), with a 10× passive probe.
- **Variac** (you'll only need it for the last exercise; everything else is bench-top low-voltage).

## Safety baseline

All exercises here run at **9 V or less**. No HV anywhere. You can be sloppy with probe placement without risk — that's part of the point of doing them on the breadboard first instead of in the live amp.

The one exception: the final "apply it to the ST-70" exercise. By then you'll know how to think about HV measurements; until then, keep the ST-70 unpowered and discharged whenever you're poking inside it.

## The exercises

1. [Ohm's law and power](01-ohms-law-and-power.md) — the foundation. V = IR, P = IV, predicting current and dissipation.
2. [Series, parallel, and voltage dividers](02-voltage-dividers.md) — how series resistance distributes voltage (the bias network) and how parallel resistance reduces it (the trick behind DMM loading and bypass caps).
3. [DMM fundamentals](03-dmm-fundamentals.md) — what your meter is actually doing in each mode, accuracy, and the "loading" effect that catches everyone.
4. [Capacitors at DC](04-capacitors-dc.md) — charging, discharging, RC time constants, and what "leakage" really means quantitatively. **This is the exercise that explains the filter cap test.**
5. [The oscilloscope](05-oscilloscope-fundamentals.md) — timebase, vertical, triggering, AC vs DC coupling, what each control actually does. First measurements.
6. [From bench to amp](06-from-bench-to-amp.md) — applying everything: heater AC on the scope, B+ ripple measurement, voltage-divider math at the bias pots, and a rigorous filter-cap leakage diagnosis.

By the end of exercise 4 you'll be able to make a definitive judgment about whether your ST-70 filter cap is healthy. By the end of exercise 6 you'll be able to make a definitive judgment about anything in the amp.

## Optional extras

Beyond the core sequence there's a set of [**optional extra modules**](extras/index.md) — standalone breadboard experiments in the same predict–build–measure style, covering circuit patterns that show up throughout audio amplifiers: wattage and heat, pots, diodes and LEDs, source impedance and sag, RC filters and coupling caps, speaker loads, and the negative-feedback divider.

**Nothing in the amp work waits on these.** Exercises 1–6 are the complete preparation; the extras are for when the predict-and-measure loop is fun in its own right and you want more reps. Dip into them in any order, any time.

## A note on uncertainty

Real components vary. A "10 kΩ 5%" resistor can be anywhere from 9.5 kΩ to 10.5 kΩ. A "30 µF" cap might be 28 or 32 µF. Your DMM has its own accuracy spec (typically 0.5–1% for DC volts, worse for AC and resistance). The point of "predict then measure" isn't to hit the exact number — it's to confirm the measurement is **inside the band** that all those tolerances allow. A reading 3% off from prediction is fine; a reading 30% off is a real signal.

The exercises will teach you how to think about that band quantitatively, so you can call "fine" and "not fine" yourself, with reasons.
