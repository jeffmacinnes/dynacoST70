---
title: E1. Wattage — power and heat
---

# Extra E1 — Wattage: power and heat you can feel

*Optional module. Standalone — only assumes [exercise 1](../01-ohms-law-and-power.md).*

## The concept

Exercise 1 gave you the power equations:

$$ P = V \times I = \dfrac{V^2}{R} = I^2 R $$

This module is about what that number *physically is*: heat, produced continuously inside the part, that has to escape through the part's surface. A resistor's **wattage rating** (¼ W, ½ W, 2 W…) isn't about how much power it can "handle" electrically — it's about how much heat its body can shed without cooking itself. Bigger body, more surface area, more watts.

Two consequences worth internalizing:

1. **The rating is a thermal budget, not a cliff.** A ¼ W resistor at 0.25 W doesn't fail — it runs hot (surface temps well over 100 °C are within spec for many parts). At 2–3× rating it discolors, drifts in value, and eventually opens. Designers usually run resistors at **half their rating or less** so they stay merely warm and their value stays stable.
2. **Dissipation divides the same way current does.** Put N equal resistors in parallel and each carries 1/N of the current — so each dissipates 1/N of the power. A bank of small resistors can do a big resistor's job. (Series works too: each resistor sees 1/N of the voltage, so each dissipates 1/N of the power.)

## Bench exercise E1A — feel the ratings

**Parts:** 9 V battery, one 1 kΩ and one 330 Ω resistor (¼ W), DMM.

**Predict** the dissipation of each connected directly across 9 V:

$$ P_{1k} = \dfrac{9^2}{1{,}000} = 81\text{ mW} \qquad P_{330} = \dfrac{9^2}{330} = 245\text{ mW} $$

So the 1 kΩ runs at about ⅓ of its ¼ W rating — it should get barely warm. The 330 Ω runs at essentially **100% of its rating** — it should get uncomfortably hot to the touch, and that's *within spec*.

**Build and measure.** Connect the 1 kΩ across the battery, wait 30 seconds, touch it. Then the 330 Ω: connect, wait 30 seconds, and touch it *briefly* — expect it to be genuinely hot. Disconnect it after a minute or so; there's no reason to leave it cooking.

One rule while you're here: **do not put anything under ~220 Ω directly across the 9 V unless it's a 1 W+ part.** A ¼ W 100 Ω resistor across 9 V dissipates 810 mW — more than 3× its rating. It will scorch, stink, and possibly open. (You'll build a 100 Ω that *can* take it in the next step.)

## Bench exercise E1B — sharing the load

**Parts:** ten 1 kΩ resistors, 9 V battery, DMM.

**Predict:** ten 1 kΩ in parallel make

$$ R_\text{eq} = \dfrac{1{,}000}{10} = 100\ \Omega $$

(equal resistors in parallel divide by N — intuition 2 from [exercise 2](../02-voltage-dividers.md)). Across 9 V, the bank draws 90 mA and dissipates 810 mW **total** — but each resistor only carries its own 9 mA, so each dissipates:

$$ P_\text{each} = \dfrac{9^2}{1{,}000} = 81\text{ mW} $$

The same 810 mW that would destroy a single ¼ W part is a comfortable 81 mW per resistor when split ten ways.

**Build it:** ten 1 kΩ resistors side by side on the breadboard, all left leads in one bus strip, all right leads in the other. Measure the bank's resistance first (expect ~100 Ω), then connect it across the battery.

**Measure:** total current (~90 mA, DMM in series on the mA range), and touch a few of the resistors after a minute — barely warm, exactly like the lone 1 kΩ in E1A. You've just built a ~2.5 W-capable 100 Ω resistor out of ¼ W parts.

## What if my number is different?

- **The 330 Ω doesn't feel hot:** your battery may be tired (a sagging 7.5 V battery gives only 170 mW — check the actual voltage and redo the math), or 30 s wasn't long enough for the body to come up to temperature.
- **The parallel bank reads well off 100 Ω:** one resistor isn't seated (9 in parallel = 111 Ω), or one lead is in the wrong strip. The math is sensitive enough to *count* your resistors for you.
- **Bank current is well under 90 mA:** the battery is sagging under the 90 mA load. That's not an error — that's [module E4](e4-source-impedance-and-sag.md) happening in front of you. Measure the battery voltage *while loaded* and the current will match V/100 again.

## Why this matters for the ST-70

Walk the chassis with this lens and the part choices explain themselves:

- The **6.8 kΩ B+ dropping resistor** ([step 30](../../build/output-stage/step-30-b-plus-dropping-resistor.md)) drops ~40 V at ~6 mA: P = 40 × 0.006 ≈ **0.24 W**. It's specified far above that so it runs warm, not hot, for decades.
- The EL34 **grid stoppers and bias-network resistors** dissipate milliwatts — small-bodied parts are fine there.
- The planned **bleeder resistor** across the filter cap is the extreme case: 435 V across, say, 270 kΩ = V²/R ≈ **0.7 W continuously**, which is why bleeders are specified as physically large multi-watt parts — and why the parallel-bank trick from E1B is a legitimate way to build one.

And the touch test you just calibrated is a real diagnostic: a resistor that's *discolored or smells* has been living beyond its rating, which means the current through it is bigger than design — which, by I = V/R, points you at the fault upstream.

[← Back to optional extras](index.md)
