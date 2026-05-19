---
title: Step 3 — 5AR4 anodes
---

# Step 3: Twist the red pair of leads and connect to V1 pins #4 and #6

> *Twist the red pair of leads and dress them to socket V1. Connect one red lead to pin #4 of V1 (S). Connect the other red lead to pin #6 of V1 (S).*

Both connections get soldered now (both have the (S) marker), unlike step 2 where pin 8 was left unsoldered for a later wire to land on.

## What you're doing physically

Connecting the **two ends of the high-voltage secondary winding** of the [PA-060](../../components/pa-060-power-transformer.md) (the red-red pair, which produces 720V AC across the full winding) to **the two anodes of the [5AR4 rectifier tube](../../components/5ar4-rectifier-tube.md)** at V1.

This is the moment you're wiring up the actual rectification. The [1N4007 from step 1](step-01-bias-diode.md) was a small auxiliary diode for the bias supply. *This* is the main rectifier — the part that will make the high-voltage DC that powers your output tubes.

## Why pins #4 and #6 specifically

The 5AR4 is a **dual-diode** in one tube envelope:

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../../assets/diagrams/5ar4-internal-structure.svg" aria-label="5AR4 internal structure">
    5AR4 internal structure (your browser does not support inline SVG).
  </object>
  <figcaption>Two anodes flanking a shared cathode, indirectly heated. Hover any internal element or pin for spec and wiring details. Click to zoom.</figcaption>
</figure>

Two separate plates, each acting as the anode of its own diode, sharing one cathode (pin 8) and one heater (pins 2 and 8). This shared-cathode arrangement is what lets the tube do **full-wave rectification** in a single envelope.

## How full-wave rectification actually works here

Once this step is complete, plus [step 7](step-07-hv-ct.md) (red-yellow center tap to ground), the rectifier circuit is electrically complete. Here's how it operates:

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../../assets/diagrams/full-wave-rectifier-topology.svg" aria-label="Full-wave rectifier topology">
    Full-wave rectifier topology (your browser does not support inline SVG).
  </object>
  <figcaption>PA-060 HV secondary on the left feeds the 5AR4's two anodes; the cathode delivers pulsating DC through the filter cap to the B+ rail. Hover any component for details. Click to zoom.</figcaption>
</figure>

On any given AC half-cycle, only one of the two RED leads is positive relative to the center tap. The diode connected to that positive end conducts, dumping electrons across the vacuum to the cathode. On the next half-cycle, the polarity flips: now the *other* RED lead is positive, and *that* anode's diode conducts.

So the cathode (pin 8) sees a positive pulse on every half-cycle — both halves of the AC waveform get used. This is full-wave rectification, and it's twice as efficient as half-wave.

```
Input AC (across full secondary):

   ╱╲      ╱╲      ╱╲
  ╱  ╲    ╱  ╲    ╱  ╲
─╱────╲──╱────╲──╱────╲──→ time
       ╲╱      ╲╱      ╲╱

What the 5AR4's cathode (pin 8) sees:

   ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲
  ╱
─╱──────────────────→ time

(both halves used as positive pulses, frequency doubled to 120Hz)
```

The 120Hz output ripple (twice the 60Hz line frequency) is much easier to filter than a 60Hz half-wave waveform — both because there's more energy per unit time and because the "valleys" between pulses are shorter, giving the [filter caps](../../components/filter-capacitors.md) less time to discharge.

## Why the two ends of the winding are 180° out of phase

The center tap is exactly halfway through the high-voltage coil. Both halves of the secondary are wound around the same core, share the same magnetic field, and have the same number of turns. So they produce equal-magnitude voltages.

But because we measure each half "from the center tap outward," the two ends end up with opposite polarities at any instant:

```
       RED (one end)
        │
        ║  ← top half of winding
        ║
        ║
   RED/YEL (center tap)
        ║
        ║  ← bottom half of winding (same number of turns)
        ║
        │
       RED (other end)
```

When the magnetic field is rising in one direction:

- **Top RED end:** +360V relative to CT
- **Bottom RED end:** −360V relative to CT

Half a cycle later (1/120th of a second), the field reverses and so does the polarity:

- **Top RED end:** −360V relative to CT
- **Bottom RED end:** +360V relative to CT

The two ends are **always opposite** — when one is +360V, the other is −360V. This is what "180° out of phase" means: the two waveforms are mirror images across zero.

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../../assets/diagrams/phase-180-degrees.svg" aria-label="180 degree phase relationship across a center-tapped winding">
    180° phase relationship (your browser does not support inline SVG).
  </object>
  <figcaption>Top RED and bottom RED, measured against the center tap. They're mirror images of each other on every half-cycle. Click to zoom.</figcaption>
</figure>

See [rectification](../../theory/rectification.md#the-180-phase-relationship-across-a-center-tap) for the full derivation (Faraday's law) and why this same pattern reappears in [phase splitting](../../theory/phase-splitting.md) and [push-pull output stages](../../theory/push-pull-topology.md).

## Why this enables full-wave rectification

The two anodes **take turns conducting**, like a relay race:

**During the first half-cycle** (top RED is +360V, bottom RED is −360V):

- Anode 1 (pin 4) is at +360V relative to CT — diode conducts
- Anode 2 (pin 6) is at −360V relative to CT — diode blocked

**During the second half-cycle** (top RED is −360V, bottom RED is +360V):

- Anode 1 (pin 4) is at −360V — blocked
- Anode 2 (pin 6) is at +360V — conducts

While one anode is "off duty" (blocked by reverse bias), the other is delivering current to the cathode. The cathode never sees a moment without positive voltage being driven into it — that's why the rectified output looks like a continuous train of positive humps rather than a series of pulses with gaps.

## Why we twist this pair too

Same logic as the white pair in [step 2](step-02-5ar4-heater.md#why-we-twist-the-leads): AC current flows out through one wire and back through the other. Twisting the wires forces their magnetic fields to cancel locally, minimizing radiated hum into nearby signal circuitry.

But there's an added consideration with this pair: **it's high voltage**. The 720V AC peak-to-peak is far more than the heater windings, and the magnetic field from any imbalance is correspondingly stronger. Sloppy wiring here can produce audible 60Hz hum that even good filtering downstream can't fully eliminate.

This is also why we **dress the leads close to the chassis** — keeping the wires physically near the grounded metal helps shield their fields from the rest of the amp.

## What's NOT being connected yet

The **red-yellow center tap** doesn't get touched in this step. It's saved for [step 7](step-07-hv-ct.md), where it connects to a ground reference at the filter capacitor area. Without that center tap connection, the rectifier circuit isn't complete — it has the two anodes wired up, but no return path for current to flow through the load.

Think of it as: step 3 wires the "input" of the rectifier; step 7 wires its "output ground reference." Together they form the full-wave rectifier topology. Until step 7 is done, no current would flow through this circuit even if the amp were powered up.

## A subtle thing about rectifier current flow

In the steady-state circuit:

- Current flows from one end of the transformer winding → through the conducting diode (one of the 5AR4's plates) → out the cathode → through the load (which is the rest of the amp, drawing current to power the tubes) → back to the center tap of the transformer winding.

The center tap is the **return path**. Current goes "out" through the active anode and "back" through the CT. On the next half-cycle, current goes "out" through the *other* anode and "back" through the same CT.

This is why the center tap goes to a ground reference: it's the common return point for both halves of the rectified AC. If you grounded one end of the secondary instead of the CT, you'd have half-wave rectification — only one anode would ever conduct, because the other end of the winding would never go positive relative to ground.

The center tap is what makes the dual-anode topology work as a true full-wave rectifier rather than two separate half-wave rectifiers.

## Crossing into the high-voltage zone

This step is when the amp transitions from "low-voltage circuits" to "circuits that can hurt you." The wiring you're doing right now is electrically inert (the amp is unpowered), but once the build is complete and powered, these red leads carry 720V AC peak-to-peak and connect to a node that will become +450V DC after the rectifier and filter caps are in place.

See [high-voltage safety](../../test-equipment/high-voltage-safety.md) for the full HV safety discussion. The short version: never assume a capacitor is discharged, follow the [one-hand rule](../../test-equipment/high-voltage-safety.md#one-hand-rule) when probing live circuits, and discharge filter caps through a resistor before reaching inside a powered-down amp.

## See also

- [5AR4 rectifier tube](../../components/5ar4-rectifier-tube.md) — the dual-anode rectifier being wired
- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — the HV secondary
- [Rectification](../../theory/rectification.md) — full-wave rectification and the 180° phase relationship
- [High-voltage safety](../../test-equipment/high-voltage-safety.md) — required reading before bring-up
- [Previous: Step 2](step-02-5ar4-heater.md) · [Next: Step 4 — V2 heater](step-04-v2-heater.md)
