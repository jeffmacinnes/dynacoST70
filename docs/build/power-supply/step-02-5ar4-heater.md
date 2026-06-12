---
title: Step 2 — 5AR4 heater
---

# Step 2: Twist the white pair of leads and connect to V1 pins #2 and #8

> *Twist the pair of white leads and dress them from the power transformer to socket V1. Connect one lead to pin #2 of V1 (S). Connect the other white lead to pin #8 of V1.*

## What you're doing physically

Connecting the **5V heater winding** (rated 4A) of the [PA-060](../../components/pa-060-power-transformer.md) to the **filament pins of the [5AR4 rectifier](../../components/5ar4-rectifier-tube.md)** (V1).

## Why two wires for the heater

Any electrical circuit needs two paths — current has to flow somewhere and return from somewhere. You can't power anything with a single wire.

For the 5AR4 filament:

```
Transformer 5V winding ─── white wire ─── pin 2 ─┐
                                                 │
                                                 ├── filament inside tube (~2.6Ω hot)
                                                 │
Transformer 5V winding ─── white wire ─── pin 8 ─┘
```

5V AC drives the 5AR4's rated 1.9A through the filament's ~2.6Ω hot resistance, dissipating about 9.5W of heat. (The winding is *rated* for 4A — that's its capacity, not the actual draw.) That heat brings the cathode sleeve up to roughly 800°C — hot enough for thermionic emission to begin.

## Why both wires are white (no polarity)

The 5V winding is a simple two-end secondary with no center tap. Both ends of the winding are electrically identical — they're just the two terminations of a single coil of wire. At any instant, one is positive and the other negative; 1/120th of a second later they've swapped (it's AC, after all).

Neither end is "hot" or "neutral" — that distinction would only make sense for DC. Using the same color for both wires honestly reflects that they're interchangeable. You could swap which white wire goes to pin 2 vs. pin 8 and the circuit would behave identically.

## Why the 5AR4 needs heat at all

All vacuum tubes need their cathodes heated to function. Electrons don't spontaneously leave a cold piece of metal — they're held there by atomic bonds. To get them to "boil off" the cathode surface (thermionic emission), you have to heat the metal until thermal energy overcomes those bonds. For oxide-coated cathodes (the standard for audio tubes), that's around 800°C.

**No heat = no electron flow = the tube is just an empty glass bulb.**

For the broader theory, see [heater circuits](../../theory/heater-circuits.md).

## Why 5V (and not 6.3V like the others)

The 5AR4 was designed for a 5V filament — that's why it has its own dedicated transformer winding. Most other tubes in the ST-70 use 6.3V, which is provided by separate 6.3V windings (the green and brown pairs). You can't share these — running a 5AR4 on 6.3V would shorten its life dramatically. See [heater circuits](../../theory/heater-circuits.md#why-5v-for-the-5ar4-and-63v-for-everything-else) for the full explanation.

## Why we twist the leads

Heater current is **AC at 60Hz**. AC current generates an oscillating magnetic field around the wires. If those fields reach into the audio signal circuitry, they induce 60Hz hum — the audible enemy of every tube amp.

When two wires carry the same current in opposite directions (which is what a transformer secondary's two leads do), their magnetic fields are also in opposite directions. **Twisting** the pair forces those fields to cancel locally rather than radiate outward.

The principle is the same as twisted-pair Ethernet cable (CAT5/6/7) — minimize crosstalk by canceling fields at the source. See [heater circuits](../../theory/heater-circuits.md#how-twisting-the-leads-helps) for more.

## Why we "dress them from the transformer to socket V1"

Routing the wires close to the chassis (and away from signal-carrying wires) provides additional shielding via the grounded chassis. Good wire dressing is one of the things that separates a quiet amp from a hummy one.

## What if you connected the two white leads directly together?

A short circuit. The transformer's 5V secondary would try to push 5V across essentially zero resistance, with current limited only by the transformer's internal impedance and saturation. Theoretical current: 5V / 0.05Ω ≈ 100A — vastly more than the 4A rating.

In practice, the wire would heat up rapidly, the transformer would saturate and limit the current to something less, but still enough to either:

- Burn through one of the white leads (lucky outcome — the wire acts as a fuse)
- Blow the AC mains fuse (designed-for outcome)
- Damage the transformer itself if neither of the above happens fast enough (worst outcome — you've destroyed a $200 component)

This is why the AC mains fuse exists, and why continuity-checking before power-up is mandatory.

### Comparison to a wall outlet

A wall outlet with nothing plugged in has 120V available between hot and neutral, but **no current flows** because there's no complete circuit (air has near-infinite resistance). Plug in a lamp, and current flows in the designed amount. Jam a wire across the slots, and you have a short circuit and a tripped breaker.

The transformer secondary works exactly the same way:

| State | Resistance | Current | Outcome |
|---|---|---|---|
| Connected to V1 pins, no tube | Infinite | 0 A | Safe (boring) |
| 5AR4 installed | ~2.6Ω | 1.9 A | Designed operation |
| Two white leads tied together | ~0Ω | Catastrophic | Damage/fire |

Voltage alone doesn't cause harm. Voltage *across a low resistance* is what creates dangerous current. See [voltage vs current](../../theory/voltage-vs-current.md) for the full mental model.

## Why pin 2 is soldered (S) but pin 8 isn't

Pin 2 of V1 only ever has one wire on it — this one white lead. So it gets soldered now. Pin 8, however, is *also* where the 5AR4's cathode lives — when the rectifier is conducting, B+ comes out at pin 8 and exits the tube to feed the filter caps. So pin 8 will have **two wires** on it: one of the white heater leads (this step), and a later wire connecting it to the filter cap area. That second wire lands in a subsequent step; only then does pin 8 get soldered with both wires in place.

## See also

- [5AR4 rectifier tube](../../components/5ar4-rectifier-tube.md) — the tube being heated
- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — the 5V heater winding
- [Heater circuits](../../theory/heater-circuits.md) — the underlying theory
- [Voltage vs current path](../../theory/voltage-vs-current.md) — the mental model that prevents short-circuit catastrophes
- [Previous: Step 1](step-01-bias-diode.md) · [Next: Step 3 — 5AR4 anodes](step-03-5ar4-anodes.md)
