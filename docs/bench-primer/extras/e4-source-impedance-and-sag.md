---
title: E4. Source impedance and sag
---

# Extra E4 — Source impedance: why every supply sags

*Optional module. Standalone — assumes [exercise 2](../02-voltage-dividers.md). Pairs naturally with [E1](e1-power-and-heat.md) (reuses its resistor bank) and [E2](e2-potentiometers.md) (the loaded wiper is the same effect).*

## The concept

No real voltage source is just a voltage. Every battery, power supply, and signal output behaves like an ideal source **with a resistor hidden in series** — its **source impedance** (or output impedance, or internal resistance; same idea, different contexts):

```
   ideal 9 V ──[ R_internal ]──○ what you can actually touch
```

You can't open the battery and find that resistor — it's chemistry and electrode area — but it's electrically real, and it means the terminal voltage is a **voltage divider between R_internal and whatever load you connect**:

$$ V_\text{terminal} = V_\text{ideal} \times \dfrac{R_\text{load}}{R_\text{internal} + R_\text{load}} $$

Light load (big R_load): terminal voltage ≈ the ideal value. Heavy load: the terminal voltage **sags**, and the missing volts are being dropped — and dissipated as heat — inside the source itself.

The practical skill is running this backwards: measure the sag, infer the hidden resistor.

$$ R_\text{internal} = R_\text{load} \times \dfrac{V_\text{open} - V_\text{loaded}}{V_\text{loaded}} $$

The same math defines the output impedance of *any* node. A divider's tap, for instance, looks like a source with R_internal = R₁ ∥ R₂ — which is exactly why loading a pot's wiper bent the dial in [E2C](e2-potentiometers.md).

## Bench exercise E4A — weigh your battery's hidden resistor

**Parts:** 9 V battery, the 100 Ω bank from [E1B](e1-power-and-heat.md) (ten 1 kΩ in parallel) or any load around 100 Ω that can take ~1 W, DMM.

**Measure V_open first:** battery unloaded, DMM across it. Say it reads 9.40 V.

**Predict the sag.** A fresh alkaline 9 V has R_internal of roughly 1–2 Ω; a well-used one can be 5–10 Ω or more. With a 100 Ω load and R_internal = 2 Ω:

$$ V_\text{loaded} = 9.40 \times \dfrac{100}{102} \approx 9.22\text{ V} $$

— a sag of ~0.2 V. A tired battery might sag 0.5–1 V on the same load.

**Build and measure:** keep the DMM across the battery terminals, connect the 100 Ω bank, and read the loaded voltage within a few seconds (chemistry drifts if you hold the load on). Then compute:

$$ R_\text{internal} = 100 \times \dfrac{V_\text{open} - V_\text{loaded}}{V_\text{loaded}} $$

Do it for a fresh battery and the most depleted one in the drawer. The open-circuit voltages may be nearly identical — **the internal resistance is the honest health metric**, which is why "reads 9 V unloaded" tells you almost nothing about a battery.

## Bench exercise E4B — the divider as a sagging source

**Parts:** 9 V battery, two 10 kΩ resistors, one 10 kΩ and one 100 kΩ for loads, DMM.

Build the equal divider (10 kΩ over 10 kΩ): the tap sits at 4.5 V unloaded, and its source impedance is:

$$ R_\text{out} = R_1 \parallel R_2 = \dfrac{10k \times 10k}{10k + 10k} = 5\text{ kΩ} $$

**Predict** the tap voltage under each load using the sag divider (4.5 V ideal source behind 5 kΩ):

| Load from tap to ground | Predicted V_tap | Yours |
|---|---|---|
| None | 4.5 V | |
| 100 kΩ | 4.5 × 100/105 ≈ 4.29 V | |
| 10 kΩ | 4.5 × 10/15 = 3.0 V | |

**Measure** all three. The 10 kΩ load — equal to the divider's own resistors — knocks a third of the voltage off. This is the quantitative version of the rule you met in E2C and exercise 3: **a tap only holds its designed voltage when the load is much bigger than the tap's source impedance.**

## What if my number is different?

- **Loaded battery voltage keeps falling while you watch:** normal for a weak battery — the chemistry can't sustain the current. Take the reading at a consistent moment (e.g., 3 seconds after connecting).
- **Computed R_internal is negative or absurd:** V_open and V_loaded were taken with different meter contact points or the battery recovered between readings. Measure both without moving the probes.
- **E4B's numbers are off by more than tolerance:** remember the DMM's own 10 MΩ is a (tiny) extra load; at these impedances it's negligible, so a real mismatch means a wrong resistor value.

## Why this matters for the ST-70

Sag is everywhere in the amp, and now it's arithmetic instead of folklore:

- **B+ sag under load.** The B+ supply — transformer winding resistance, 5AR4 (whose effective series resistance is large), choke DCR — adds up to a real source impedance of hundreds of ohms. Pull 200 mA through it and the rail sits tens of volts below its unloaded value. That's why [exercise 6E](../06-from-bench-to-amp.md) notes the rail floats up toward ~500 V with the tubes out: no load, no sag.
- **Voltage-chart readings that run a few volts low across the board** often just mean your wall voltage is low or the load current is a touch high — a uniform sag signature, not ten separate faults. The *pattern* of sag is diagnostic.
- **Why the OPT output can drive a speaker at all:** the feedback loop drops the amp's output impedance to well under an ohm (see [feedback theory](../../theory/feedback.md)), so the 4 Ω speaker — a brutally heavy load by divider standards — barely sags it. [Module E7](e7-feedback-divider.md) shows the mechanism.

[← Back to optional extras](index.md)
