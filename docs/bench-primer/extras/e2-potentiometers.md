---
title: E2. Potentiometers
---

# Extra E2 — Potentiometers: the divider you can turn

*Optional module. Standalone — only assumes [exercise 2](../02-voltage-dividers.md).*

## The concept

A potentiometer is one resistive element with three terminals: the two **ends** (call them 1 and 3) and a **wiper** (2) that slides along the element as you turn the shaft. Electrically, that's a two-resistor voltage divider where turning the shaft trades resistance between the top leg and the bottom leg:

```
        1 ──[ R_upper ]──┬──[ R_lower ]── 3
                         │
                         2 (wiper)

   R_upper + R_lower = R_total, always.
```

Wire 9 V across ends 1–3 and the wiper voltage is just the divider formula from exercise 2:

$$ V_\text{wiper} = 9 \times \dfrac{R_\text{lower}}{R_\text{total}} $$

Every volume knob, balance control, and bias pot is this circuit. There are only two other things to know:

1. **Taper.** A *linear* pot changes resistance proportionally to rotation — half turn, half resistance. An *audio* (logarithmic) pot bunches most of its resistance change into the second half of rotation, because hearing is logarithmic and a linear pot would make a volume control feel like "all the loudness lives in the first 20 degrees." You can identify which kind you have with a DMM in about a minute.
2. **Rheostat wiring.** Use just the wiper and *one* end, and the pot becomes a plain variable resistor instead of a divider.

## Bench exercise E2A — map your pot

**Parts:** any pot you have, DMM. No battery needed yet.

**Measure the element first:** DMM on ohms across ends 1–3. This is R_total and it does **not** change as you turn the shaft — verify that. (If it changes, you're on the wiper.)

Now measure end-to-wiper (1–2) at five shaft positions: full counter-clockwise, ¼, ½, ¾, full clockwise. Record them.

| Shaft position | R (1→2), linear pot predicts | Yours |
|---|---|---|
| Full CCW | ~0 | |
| ¼ | ~25% of R_total | |
| ½ | ~50% of R_total | |
| ¾ | ~75% of R_total | |
| Full CW | ~R_total | |

If the halfway reading is near 50%, it's a linear pot. If it's more like 10–20% of R_total, you have an audio-taper pot — that's not a defect, it's the taper doing its job.

## Bench exercise E2B — the adjustable divider

**Parts:** the pot, 9 V battery, DMM.

Wire 9 V across ends 1–3, DMM from wiper to ground. **Predict:** the wiper sweeps smoothly from 0 V to 9 V, and (for a linear pot) sits at 4.5 V at half rotation.

**Measure** at the same five positions as E2A and check them against V = 9 × R_lower/R_total using your recorded resistances. This is worth actually doing: the wiper voltages should match your resistance map to within a few percent, which confirms the pot really is nothing more than exercise 2's divider with a movable tap.

## Bench exercise E2C — loading the wiper

Here's the one that catches people. Leave the divider from E2B set to **half rotation** (wiper at ~4.5 V for a linear pot). Now hang a **1 kΩ resistor from the wiper to ground** — a stand-in for whatever downstream circuit the pot feeds.

**Predict** (for a 10 kΩ pot; scale to yours): the wiper now looks back into 5 kΩ of upper element, and the bottom leg is 5 kΩ ∥ 1 kΩ ≈ 833 Ω. The divider formula gives:

$$ V_\text{wiper} = 9 \times \dfrac{833}{5{,}000 + 833} \approx 1.3\text{ V} $$

Not 4.5 V — **1.3 V**. The load didn't shift the dial slightly; it collapsed the top half of the pot's range.

**Measure**, then sweep the shaft and notice how the response curve is bent: most of the output voltage change now happens near the top of rotation. Then swap the 1 kΩ load for 100 kΩ and watch the divider behave almost ideally again (predict: 9 × 4,762/9,762 ≈ 4.4 V at center).

The rule that falls out: **a pot behaves like its markings only when the load is much larger than the pot** — 10× is okay, 100× is clean. This is the same loading effect as the DMM in [exercise 3](../03-dmm-fundamentals.md), now happening on purpose inside a circuit.

## What if my number is different?

- **Wiper voltage jumps around as you turn:** dirty or worn element. Real pots do this with age — it's the "scratchy volume knob" failure, and in a bias pot it's far more serious (a momentary open wiper can un-bias an output tube).
- **1–2 plus 2–3 don't sum to 1–3:** they should, always, within tolerance. If not, re-check which terminal is the wiper (it's usually the middle one, but not guaranteed).
- **Half rotation isn't half resistance:** audio taper, as above.

## Why this matters for the ST-70

The **Biaset pots** ([step M5](../../build/mechanical-assembly/step-m05-bias-pots.md)) are exactly circuit E2B: a 10 kΩ pot forming the middle of the three-section bias divider you modeled in exercise 2, wiper feeding the EL34 grids. Two things you just learned apply directly:

- The wiper feeds the EL34 grid circuit, which is **very high impedance** — so the pot behaves like its ideal divider math, per E2C's rule. That's *why* the −43 V to −22 V sweep prediction in [exercise 6D](../../bench-primer/06-from-bench-to-amp.md) works.
- The scratchy-wiper failure mode is why bias pots are worth buying good and exercising occasionally: a wiper dropout drives the grid toward the top of the divider, the tube's bias goes wrong, and the tube red-plates.

And when you eventually put a preamp in front of the ST-70, its volume control is E2C with the ST-70's 470 kΩ input impedance as the load — comfortably in the "100× — clean" regime.

[← Back to optional extras](index.md)
