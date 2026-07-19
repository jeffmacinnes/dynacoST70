---
title: Optional extras
---

# Optional extras

**None of these are required.** The [main primer sequence](../index.md) (exercises 1–6) is everything you need before working on the ST-70. These modules exist for a different reason: the predict–build–measure loop is fun, and each of these builds intuition for a circuit pattern that shows up constantly in audio amplifiers.

Think of them as a parts drawer of experiments, not a curriculum:

- **Dip in, in any order.** Each module is self-contained. Where one borrows an idea from another, it links to it.
- **Do them whenever.** Before the amp, after the amp, during a break while solder joints cool. Nothing in the bring-up sequence waits on these.
- **All low-voltage.** Everything here runs from a 9 V battery or a phone/signal-generator output. No variac, no HV, no amp required.

## The modules

| Module | You'll build intuition for | Parts beyond the basics |
|---|---|---|
| [E1. Wattage — power and heat you can feel](e1-power-and-heat.md) | Why resistors have power ratings, how dissipation is shared, why the ST-70 uses physically big resistors | Nothing extra |
| [E2. Potentiometers](e2-potentiometers.md) | The adjustable voltage divider — bias pots, volume controls, and why loading a wiper bends the dial | A pot |
| [E3. LEDs and diodes](e3-leds-and-diodes.md) | One-way conduction and the forward drop — the heart of the bias supply's 1N4007 | An LED |
| [E4. Source impedance and sag](e4-source-impedance-and-sag.md) | Why every real supply droops under load — the low-voltage version of B+ sag | Nothing extra |
| [E5. Capacitors with AC — filters](e5-caps-with-ac.md) | Coupling caps and RC filters — why cap size sets the bass response | Phone or signal generator |
| [E6. Driving a speaker](e6-driving-a-speaker.md) | Impedance, power into a load, and why DC through a speaker is silence plus heat | A 4 Ω speaker |
| [E7. The feedback divider](e7-feedback-divider.md) | Negative feedback demystified — the β network is just a voltage divider, and the closed-loop math falls out of it | Phone or signal generator |

## Suggested pairings

If you want a thread to pull rather than random access:

- **The wattage thread:** E1 → E6. Power dissipated in a resistor as heat, then power delivered to a speaker as sound. Same P = V²/R, two very different destinations.
- **The divider thread:** E2 → E4 → E7. The pot is a divider you can turn; source impedance is the divider you didn't know was there; feedback is a divider used as a control system. This is the natural continuation of [exercise 2](../02-voltage-dividers.md).
- **The AC thread:** E5 → E6 → E7. Caps passing signal, loads receiving it, and a loop wrapped around the whole thing. Closest to "how the audio path of the ST-70 actually works."
- **The rectifier thread:** E3 on its own. It's the conceptual core of both the [bias diode](../../components/1n4007-diode.md) and the [5AR4](../../components/5ar4-rectifier-tube.md).

Each module keeps the primer's shape — **concept, equations, predict, build, measure, "what if my number is different?"** — and ends with the ST-70 connection, because that's the whole point.

[← Back to the bench primer](../index.md)
