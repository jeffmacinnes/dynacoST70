---
title: 2. Voltage dividers and series circuits
---

# Exercise 2 — Voltage dividers and series circuits

## The concept

When resistors are connected end-to-end (in **series**), the same current flows through all of them. By Ohm's law, each resistor drops a voltage proportional to its resistance:

$$ V_n = I \times R_n $$

If two resistors are in series from V_in to ground, with the midpoint tapped off, the midpoint sits at a fraction of V_in determined by the ratio of resistances. This is the **voltage divider** — one of the most-used circuit patterns in electronics:

```
V_in ──┬── R1
       │
       ├── V_mid
       │
       ├── R2
       │
      GND
```

$$ V_{\text{mid}} = V_{\text{in}} \times \dfrac{R_2}{R_1 + R_2} $$

Memorize that the **bottom resistor** appears in the numerator. Intuition: if R₂ is huge (open), the midpoint approaches V_in. If R₂ is tiny (short), the midpoint goes to 0.

## Bench exercise

**Parts:** 9 V battery, two resistors (1 kΩ and 2 kΩ, or anything where you know both values), DMM.

**Circuit:**

```
   9V battery (+)
      │
     [R1 = 1 kΩ]
      │
      ├──── tap here, call it V_mid
      │
     [R2 = 2 kΩ]
      │
   9V battery (−) / GND
```

**Predict:**

$$ V_{\text{mid}} = 9 \times \dfrac{2{,}000}{1{,}000 + 2{,}000} = 9 \times \dfrac{2}{3} = 6\text{ V} $$

Sanity check: R₂ is twice R₁, so R₂ should drop ⅔ of the input and R₁ should drop ⅓. V_mid = 6 V (across R₂) and the voltage across R₁ = 3 V. The two drops add up to 9 V ✓.

Also predict the current flowing through the divider (it's the same through both resistors):

$$ I = \dfrac{V_{\text{in}}}{R_1 + R_2} = \dfrac{9}{3{,}000} = 3\text{ mA} $$

**Build** it. Note that the order of R₁ and R₂ matters — R₁ is the *top* one (between V_in and the tap), R₂ is the *bottom* one (between the tap and ground).

**Measure:**

| Measurement | Predicted | Yours |
|---|---|---|
| V across R₁ (probe + on V_in, − on V_mid) | 3 V | |
| V across R₂ (probe + on V_mid, − on GND) | 6 V | |
| V across the whole divider (probe + on V_in, − on GND) | 9 V (battery) | |
| Sum: V₁ + V₂ should equal V_in | ✓ | |

Now **swap R₁ and R₂** so the bigger resistor is on top. Re-predict, then re-measure:

$$ V_{\text{mid}} = 9 \times \dfrac{1{,}000}{2{,}000 + 1{,}000} = 9 \times \dfrac{1}{3} = 3\text{ V} $$

## What if my number is different?

- **V_mid is way off (e.g., 4.5 V instead of 6 V):** your DMM is "loading" the divider — its internal resistance is in parallel with R₂, lowering the effective bottom-leg resistance and dropping V_mid. This is real and important, and exercise 3 is all about it. For now, if it bothers you, use smaller resistors (1 kΩ and 2 kΩ make loading negligible) — loading becomes severe when divider resistors are in the MΩ range.
- **V_mid drifts as you watch it:** a poor connection somewhere. Reseat the wires on the breadboard.
- **The two drops don't sum to V_in:** measurement error or one probe wasn't where you thought. Re-check.

## A second variation: three resistors

```
V_in (9 V)
   │
  [R1 = 10 kΩ]
   │── V_a
  [R2 = 10 kΩ]
   │── V_b
  [R3 = 10 kΩ]
   │
  GND
```

Predict V_a and V_b (three equal resistors, so the drops are equal — 3 V each):

- V_a = 6 V
- V_b = 3 V
- V across each resistor = 3 V
- Current = 9 V / 30 kΩ = 0.3 mA

Build, measure, confirm. You've just modeled the ST-70's stock bias divider topology — a chain of resistors from the raw bias rail to ground, with the pot wiper tapping off at an intermediate node.

## Why this matters for the ST-70

The **bias network** is exactly this circuit. Following [signal-paths/bias](../signal-paths/bias.md): the −65 V rail (raw bias from the diode) feeds through the 10 kΩ filter resistor (step 20), into the 10 kΩ pot, and through the second 10 kΩ shunt to ground (step 22). When the pot is centered, you have a three-section divider exactly like the variation above — except scaled to 65 V across the chain instead of 9 V, with intermediate values of −43 V and −22 V on the pot's terminals.

Pot wiper at center → grid bias roughly at the midpoint of those = roughly **−32 V**, which is the manual's spec.

Now you understand *why* it's −32 V from first principles. It's just a voltage divider.

The B+ supply uses the same idea with dropping resistors between filter cap sections: 415 V at lug 1, then drop ~40 V across 6.8 kΩ at ~6 mA (load current of the driver board) to land at 375 V on lug 4. **You can predict every B+ rail with V = IR.**

[Next: DMM fundamentals →](03-dmm-fundamentals.md)
