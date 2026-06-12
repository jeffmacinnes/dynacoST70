---
title: Step 6 — Heater center taps
---

# Step 6: Dress the brown-yellow and green-yellow center taps to the seven-lug terminal strip

> *Dress the brown-yellow and green-yellow leads around to the seven lug terminal strip. Connect the brown-yellow to lug #7 and the green-yellow to lug #5.*

This is where it gets conceptually rich. We're now wiring the **center taps** of both 6.3V heater windings to specific lugs on the [seven-lug terminal strip](../../components/seven-lug-terminal-strip.md). To understand why, we need to talk about what the terminal strip is, what center taps do for hum, and the beginning of the amp's grounding architecture.

## What is the seven-lug terminal strip

The seven-lug terminal strip is a small phenolic (or similar insulating) board with seven metal lugs sticking out of it, mounted physically to the chassis. Each lug is electrically isolated from the others and from the chassis itself. It's purely a **mechanical anchor point** for wires — like a junction box for the amp's wiring.

Why it exists: in point-to-point wiring (the technique Dynaco used, as opposed to printed circuit boards), you can't just float wires in mid-air. You need physical anchor points where multiple wires can come together at a node. The terminal strip provides those points.

The seven-lug strip in the ST-70 will collect a number of important ground-related signals over the course of the build. We'll see it again in many later steps. See [the component page](../../components/seven-lug-terminal-strip.md) for more.

## What a center tap does for hum

We covered the basics in [heater circuits](../../theory/heater-circuits.md#the-center-tap-to-ground-trick), but step 6 is where the trick actually gets implemented.

A 6.3V heater winding without a CT-to-ground reference is **floating** with respect to the amp's signal ground. Its absolute voltage relative to the rest of the amp is undefined — it could drift anywhere within the limits of the transformer's insulation. In practice, capacitive coupling between the windings ties the heater leads to some imperfect reference, but it's not a clean one.

The two heater leads swing symmetrically around the floating reference: at any instant, one is at +3.15V relative to the floating midpoint, the other at −3.15V. But that floating midpoint itself wanders around, picking up stray noise.

In the ST-70 the center taps are **not hard-grounded**. Each CT lands on its own lug (5 or 7) and reaches ground only through a **0.02 µF disc capacitor** to grounded lug 6 (wired in step 15). That's an AC bypass: at audio frequencies the caps and the winding's symmetry hold the midpoint near 0 V, so:

- One heater lead swings around **+3.15V relative to ground** at any instant
- The other heater lead swings around **−3.15V relative to ground** at the same instant
- 1/120th of a second later, they swap

The two leads swing **symmetrically around zero** at audio frequencies — while at DC the windings stay floating, which avoids creating a DC ground loop through the heater circuit.

<figure class="diagram-fig" markdown="span">
  <img src="../../../assets/diagrams/heater-ct-comparison.svg" alt="Heater winding floating midpoint vs CT grounded comparison">
  <figcaption>Top panel: floating midpoint drifts. Bottom panel: CT tied to ground anchors the midpoint at 0 V. Click to zoom.</figcaption>
</figure>

When the midpoint is held at 0V, any voltage induced into nearby signal-carrying wires (via capacitive coupling between the heater wires and the signal wires running through the chassis) is **balanced** — the +3.15V wire induces a small positive voltage, and the −3.15V wire induces an equal and opposite negative voltage, and they cancel.

When the midpoint is floating, this cancellation is imperfect. The induced voltages don't fully cancel because the reference is wandering. Result: 60Hz hum gets into the audio signal.

## Why the heater AC frequency matters here

Heater AC is at the mains frequency — 60Hz in the US. If hum couples from the heaters into the audio signal, it appears as 60Hz hum at the output. This is exactly the kind of low-frequency hum that's audible (the human ear is quite sensitive in the 60–120Hz range) and that audiophiles obsess over eliminating.

A well-designed tube amp with CT-grounded heaters can achieve hum levels 60–80dB below full output — quiet enough that you have to put your ear up to the speaker to hear it.

A poorly-grounded heater chain can produce visible-on-a-scope hum at the output. The CT-to-ground trick is one of the most cost-effective improvements in tube amp design: a single wire from each CT to a grounding point, and your hum floor drops dramatically.

## Why separate lugs for the two CTs (#5 and #7)

This is the subtle but important detail of step 6. The brown-yellow CT goes to lug #7, the green-yellow CT goes to lug #5. **They are not joined together immediately.**

Why? Because each lug eventually connects to a slightly different ground reference point — typically chosen so that each channel's heater CT grounds at a location near *that channel's* signal-carrying components. This is the start of the amp's **star grounding** architecture.

In a properly star-grounded amp, you don't just connect everything to "the chassis" or "ground" indiscriminately. Different grounds have different roles:

- **Signal ground** for input stages (low current, high sensitivity)
- **Cathode bias return** (small DC current)
- **Driver stage ground** (moderate current)
- **Output stage ground** (high current pulses)
- **Power supply ground** (charging currents for the filter caps, can be high transient currents)
- **Heater CT ground** (60Hz AC return)

Each of these has its own currents. If you tie them all to a single point on the chassis (a *star ground*), the currents return to the supply through separate paths and don't share voltage drops along the chassis. This minimizes the chance of one circuit's current creating a voltage on the chassis that another circuit sees as noise.

Lugs #5 and #7 on the terminal strip become the heater CT anchor points for each channel. Later wiring (step 15) bypasses each to grounded lug 6 through a 0.02 µF disc cap — an AC reference rather than a hard ground connection.

See [grounding and hum](../../theory/grounding-and-hum.md) for the deeper treatment as the build progresses.

## Why we route around to the terminal strip rather than just grounding at the transformer

You could ground the CT leads directly to the chassis right at the transformer with a solder lug under one of the transformer's mounting bolts. That would work, electrically.

But routing the leads to the seven-lug terminal strip serves a different purpose: it concentrates all the ground-related wiring at a known location, making the amp's grounding scheme **systematic and inspectable**. If you're troubleshooting a hum issue years from now, you know where to look — all the grounding decisions are visible at the terminal strip rather than scattered across the chassis.

This is the philosophy of point-to-point wiring done well: every electrical decision should be visible, traceable, and modifiable. The terminal strip is the embodiment of that philosophy for the ground network.

## A subtle thing about ground topology so far

You've now wired:

- [Step 1](step-01-bias-diode.md): bias supply input to its rectifier diode
- [Step 2](step-02-5ar4-heater.md): 5AR4 heater
- [Step 3](step-03-5ar4-anodes.md): 5AR4 anodes
- [Step 4](step-04-v2-heater.md): V2 heater (one channel)
- [Step 5](step-05-v7-heater.md): V7 heater (other channel)
- Step 6 (this one): both heater center taps anchored at the terminal strip

Notice what's *not* yet connected: **none of these wires are yet referenced to chassis ground**. The bias supply has no ground return yet. The HV rectifier has no return path (we haven't done [step 7](step-07-hv-ct.md) yet — that's the red-yellow CT). The heater CTs sit at the terminal strip but haven't been joined to the main ground star yet.

This is by design. Until the amp is fully wired, you don't want partial ground paths through random points on the chassis. Steps 7 onwards will start completing those ground references, and the architecture will emerge.

When the amp is fully built and powered, you'll have a clear chain of ground references that all converge on a single star point — and **that's** what determines whether your amp is quiet or hummy.

## See also

- [Seven-lug terminal strip](../../components/seven-lug-terminal-strip.md) — what the lugs do
- [Heater circuits](../../theory/heater-circuits.md) — CT-to-ground trick theory
- [Grounding and hum](../../theory/grounding-and-hum.md) — star grounding (to be expanded)
- [Previous: Step 5](step-05-v7-heater.md) · [Next: Step 7 — HV CT](step-07-hv-ct.md)
