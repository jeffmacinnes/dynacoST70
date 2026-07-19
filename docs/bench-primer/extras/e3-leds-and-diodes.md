---
title: E3. LEDs and diodes
---

# Extra E3 — LEDs and diodes: one-way valves with a toll

*Optional module. Standalone — only assumes [exercise 1](../01-ohms-law-and-power.md).*

## The concept

Everything in the primer so far has been **linear**: double the voltage across a resistor and the current doubles. A diode is your first *nonlinear* part, and it has two rules:

1. **Current flows one way only** — from anode to cathode (the cathode is the banded end on a rectifier diode, the shorter leg / flat side on an LED). Reverse it and essentially nothing flows.
2. **Conducting costs a roughly fixed toll: the forward drop V_f.** A silicon rectifier diode drops ~0.6–0.7 V while conducting, almost regardless of current. An LED drops more — ~1.8–2.2 V for red/yellow/green, ~2.8–3.4 V for blue/white — and emits light in proportion to the current through it.

Because the drop is fixed rather than proportional, you can't apply Ohm's law *to the diode*. Instead, you apply it to whatever resistor is in series with it, after subtracting the toll:

$$ I = \dfrac{V_\text{supply} - V_f}{R} $$

That series resistor is mandatory. A diode across a supply with no resistor has nothing limiting the current — the diode conducts harder, drops the same V_f, and the current is bounded only by what the supply can deliver. This is why every LED you've ever seen has a resistor next to it.

## Bench exercise E3A — measure the toll

**Parts:** DMM with a diode-test mode, one LED (any color), one rectifier or small-signal diode if you have one.

Put the DMM in **diode mode** (the symbol looks like an arrow against a bar). Red probe on the anode, black on the cathode. The meter pushes a small test current through the junction and displays V_f directly.

**Predict, then measure:**

| Part | Predicted V_f | Yours (forward) | Yours (reversed probes) |
|---|---|---|---|
| Silicon diode (e.g., 1N400x) | 0.5–0.7 V | | OL / no reading |
| Red/yellow/green LED | 1.8–2.2 V | | OL / no reading |
| Blue/white LED | 2.8–3.4 V | | OL / no reading |

The LED will glow faintly on the meter's test current. Reversed, everything reads open — that's rule 1 on display, and it's also how you identify an unmarked diode's cathode in the wild.

## Bench exercise E3B — predict LED current and brightness

**Parts:** 9 V battery, LED, 1 kΩ resistor. Then a 4.7 kΩ or 10 kΩ.

**Circuit:**

```
9 V (+) ──[ 1 kΩ ]──▶|── (−) 9 V
                    LED
          (anode ──▶|── cathode)
```

**Predict** using the V_f you measured in E3A (say 2.0 V):

$$ I = \dfrac{9 - 2.0}{1{,}000} = 7\text{ mA} $$

That's a comfortably bright indicator (typical LEDs are rated 20 mA max, look fine from ~1 mA up).

**Build and measure:** current with the DMM in series (expect ~7 mA), then voltage across the LED while it's lit — it should read close to your E3A value and it will barely move even as current changes. Prove that by swapping the 1 kΩ for 4.7 kΩ: predict I = 7/4,700 ≈ 1.5 mA, visibly dimmer, **but V_f nearly unchanged**. That's the fixed-toll behavior — the resistor absorbs whatever voltage the diode doesn't.

Now **reverse the LED**. Nothing lights, and the DMM across the LED reads the full 9 V — when a diode blocks, *it* takes all the voltage and the resistor takes none (no current, no IR drop). Worth sitting with for a second: voltage across a non-conducting part = the whole supply.

If you did [module E2](e2-potentiometers.md): put your pot in rheostat wiring (wiper + one end) in series with the LED *plus a fixed 470 Ω* (so the current can't exceed (9 − 2)/470 ≈ 15 mA at the pot's zero end), and you have a smooth brightness control — current steering with a knob.

## What if my number is different?

- **Diode mode reads ~0.0 V both ways:** shorted diode (failed part), or your probes are touching each other.
- **Reads OL both ways:** open diode, or an LED whose V_f exceeds what your meter's diode mode can supply (common with blue/white LEDs on some meters — the LED is fine, the meter just can't pay the toll).
- **LED current is noticeably off prediction:** your V_f guess was off — plug in the *measured* V_f and it should land within battery-and-tolerance error. Notice the lesson: the bigger the supply relative to V_f, the less the V_f estimate matters. At 9 V, a 0.2 V error in V_f moves the current ~3%; at 3 V it would move it ~20%.

## Why this matters for the ST-70

The ST-70 has exactly one silicon diode, and now you know both of its rules from the bench:

- The **1N4007 bias diode** ([step 1](../../build/power-supply/step-01-bias-diode.md)) is rule 1 at work: it conducts only on the half-cycles that make the bias end *negative*, which is how an AC winding becomes the −65 V raw bias rail. Its 0.7 V forward drop is invisible next to 65 V — which your E3B math predicted: big supply, small toll, toll doesn't matter.
- The **5AR4 rectifier** is the same one-way-valve idea implemented in vacuum, with a much bigger toll (tens of volts at full current) — that drop is a real term in the B+ arithmetic of [exercise 6A](../06-from-bench-to-amp.md).
- And the reversed-LED observation — *the blocking element takes the full voltage* — is the mental model for why a rectifier diode's **PIV rating** matters: when it's not conducting, the whole transformer swing lands across it.

[← Back to optional extras](index.md)
