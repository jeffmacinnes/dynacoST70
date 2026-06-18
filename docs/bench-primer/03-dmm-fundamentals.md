---
title: 3. DMM fundamentals
---

# Exercise 3 — DMM fundamentals

## The concept

A DMM is four meters in one box. Each mode operates on a different principle, has a different accuracy spec, and has a different effect on the circuit being measured. Knowing what's happening inside the meter is what separates "the number on the screen" from "what the circuit is doing."

### DC volts

The meter has a very high **input impedance** — typically 10 MΩ (modern handhelds), sometimes 1 MΩ on older meters, or >1 GΩ on high-end bench meters. When you put the probes across a circuit node, the meter draws a tiny current through that 10 MΩ and measures the voltage drop across its own input.

Implications:

- The DMM **loads** the circuit by drawing some current from it.
- In low-impedance circuits (Ω to kΩ source impedance), 10 MΩ is overwhelming and the loading is negligible.
- In high-impedance circuits (MΩ source impedance — like the cathodyne's plate node or a grid leak), 10 MΩ is comparable and the loading is visible.

This is the most important effect to internalize. Your meter's number is *the voltage at that node with a 10 MΩ resistor connected from probe to probe*. Sometimes that equals "the voltage at the node when the meter isn't there." Sometimes it doesn't.

### DC current

Same circuit principle as voltage, but the meter is now configured as a very low resistance (often <1 Ω on low-current ranges) and inserted **in series**. The reading is the voltage across that small internal resistor (called a *shunt*), back-calculated to a current.

Implications:

- Putting the meter in current mode across a voltage source = short circuit. **Blows the meter's fuse instantly.** Always think about what current mode does before connecting it.
- Current measurements always require breaking the circuit. That's annoying, which is why most bench work uses voltage measurements across known resistors to infer current.

### Resistance (Ω) / Continuity

The meter outputs a small, known **source current** through its probes and measures the resulting voltage. R = V/I. The source current is small — typically tens of µA to a few mA depending on the meter and the range.

Implications:

- Only works on **unpowered** circuits. The presence of any other voltage source corrupts the measurement.
- "Loads" the circuit being measured with the source current — usually negligible, but on very fragile circuits (high-impedance amplifier inputs) it can cause damage. Don't probe ohms into a powered amp.
- The reading represents the **DC resistance only**. Inductors read as their winding resistance (a small number), even though they have huge impedance at AC frequencies. Capacitors charge up and confuse the reading (see [exercise 4](04-capacitors-dc.md)).
- "Continuity" mode is the same as ohms mode but with an audible beep below some threshold (typically <50 Ω) — convenient for tracing wires without looking at the display.

### Diode test

Like ohms mode, but optimized for testing diode junctions. The meter sources a specific test current (typically 1 mA) and displays the forward voltage drop in volts. ~0.5–0.7 V for silicon, ~0.2–0.3 V for germanium or Schottky. OL one direction, V_f the other. Use it for any p-n junction (diodes, LEDs, transistor B-E junctions).

## Bench exercise — observing DMM loading

This is the exercise that makes loading viscerally real. You'll measure a high-impedance voltage divider with and without the DMM's loading effect.

**Parts:** 9 V battery, two 1 MΩ resistors, DMM.

**Circuit:**

```
   9V battery (+)
      │
     [R1 = 1 MΩ]
      │
      ├── V_mid (probe here)
      │
     [R2 = 1 MΩ]
      │
   GND
```

**Predict (ideal):**

$$ V_{\text{mid}} = 9 \times \dfrac{1{,}000{,}000}{2{,}000{,}000} = 4.5\text{ V} $$

**Predict (with loading):** the DMM's 10 MΩ input sits in parallel with R₂. Combined:

$$ R_2 \parallel R_{\text{DMM}} = \dfrac{1\text{M} \times 10\text{M}}{1\text{M} + 10\text{M}} = \dfrac{10}{11}\text{ MΩ} \approx 909\text{ kΩ} $$

So the *effective* divider is now 1 MΩ on top, 909 kΩ on the bottom. New V_mid:

$$ V_{\text{mid}} = 9 \times \dfrac{909}{1{,}000 + 909} = 9 \times \dfrac{909}{1{,}909} \approx 4.29\text{ V} $$

So you'll measure **~4.3 V**, not the "ideal" 4.5 V. That ~5% deficit is the DMM loading the divider.

**Build and measure.** Confirm ~4.3 V.

Now **rebuild the same divider with 1 kΩ resistors instead of 1 MΩ.** The DMM's 10 MΩ in parallel with 1 kΩ is essentially still 1 kΩ (loading factor 0.9999). Predicted V_mid = 4.5 V exactly. Measure and confirm.

**The takeaway:** loading is severe when source impedance approaches the DMM's input impedance. Knowing your meter's input impedance (look it up — usually printed on the back) lets you predict and correct for it.

## Bench exercise — current measurement

Don't skip this. Move the red probe to the current jack, set the meter to mA DC, and **break the circuit** to insert it:

```
   9V battery (+)
      │
     [DMM in series, on mA]
      │
     [R = 1 kΩ]
      │
   GND
```

Predict 9 mA. Measure. Then move it to the **other** side of the resistor (between resistor and ground) — the reading is the same, because in a series loop the current is the same everywhere.

Now do something dangerous in a controlled way: with the meter still on mA, touch both probes across the battery directly (no resistor). Don't hold it long. **The meter is now a short circuit.** Most meters will pop their fuse within a second. Hopefully yours has a fuse — replace it if it blew. (If you're nervous, skip this — it's not strictly necessary for the primer.)

The lesson is: **always think about what mode you're in before connecting probes**. Current mode + powered circuit = short. The number of meter fuses replaced by working engineers is large.

## What if my number is different?

- **DMM reads slowly-changing voltages on a high-impedance node:** the node has some capacitance, and the meter's loading is slowly bleeding it. Expected. Note the trend.
- **DMM input impedance you can verify:** put your meter on DC volts, set a known voltage across a known high-value resistor, and infer the meter's input impedance from the voltage divider math above. A useful sanity check that you understand your tool.

## Why this matters for the ST-70

When you measure a grid node (470 kΩ grid leak, very high impedance), your DMM's loading is real. When you measure a B+ rail (low impedance, lots of current flowing), it's invisible. The interpretive lens — *how much is the meter changing the thing it's measuring?* — is something you'll use at every node in the amp.

The earlier confusion about "test 5 expected OL but I got 26 Ω" was a related principle: the meter wasn't lying about 26 Ω; it was reading the actual resistance through the winding-to-CT-to-chassis path. Once you can confidently reason about what the meter is *doing*, readings stop being arbitrary and start being telling.

[Next: Capacitors at DC →](04-capacitors-dc.md)
