---
title: How transformers work
---

# How transformers work

This chapter covers the fundamental theory of transformers: how energy crosses from primary to secondary, how the physical construction is laid out, and what separates a mediocre transformer from a great one.

For the specific transformers in the ST-70, see the [PA-060](../components/pa-060-power-transformer.md) and [A-470](../components/a-470-output-transformer.md) pages.

!!! note "Diagram placeholders"
    ASCII transformer cross-sections here will be replaced with proper schematic-style SVGs before final PDF conversion. See [diagram plan](../index.md) for the full diagram roadmap.

## The fundamental principle

A transformer is two coils of wire wound around a shared chunk of iron. AC current flowing in coil #1 (the "primary") creates a changing magnetic field in the iron. That changing magnetic field induces a voltage in coil #2 (the "secondary"). Energy transfers from primary to secondary through the magnetic field — the two coils never electrically touch.

The voltage ratio is determined by the **turns ratio**: if the primary has 1000 turns of wire and the secondary has 100 turns, you get 10:1 step-down. 1000:6000 = 6:1 step-up. The PA-060 steps 120V AC up to 360V AC on each half of its high-voltage winding, and *down* to 6.3V on the heater windings — all from a single primary, with multiple secondaries each having a different turn count.

## Physical construction

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../assets/diagrams/transformer-cross-section.svg" aria-label="Transformer cross-section showing internal construction">
    Transformer cross-section (your browser does not support inline SVG).
  </object>
  <figcaption>Cutaway of a power transformer: end bells, laminated iron core, bobbin, layered windings (primary innermost, HV secondary, heater secondaries outermost), and the leads exiting the bottom. Hover any element for what it does. Click to zoom.</figcaption>
</figure>

The build sequence is roughly:

1. **Bobbin** — a non-conductive form (paper, plastic, or fiber) that the wire gets wound around
2. **Primary winding** — many turns of relatively thin wire (it carries low primary current at 120V)
3. **Insulation layers** between windings — paper, mylar, or varnish-impregnated tape
4. **Secondary windings** — wound on top of the primary, in layers separated by more insulation. Higher-current windings (heaters) use thicker wire; high-voltage windings (B+) use thinner wire but more turns
5. **Core lamination stack** — thin sheets of silicon steel ("laminations") shaped like Es and Is, stacked through the bobbin to form a closed magnetic loop
6. **End bells** — the metal covers that keep everything mechanically clamped and act as an electrostatic shield
7. **Varnish or oil impregnation** — fills the air gaps in the windings, locks turns in place, prevents vibration ("singing"), and improves heat conduction

## Why iron, and why laminated?

Iron (specifically silicon steel) has high **magnetic permeability** — it concentrates magnetic field lines far more than air. A coil of wire wrapped around an iron core produces hundreds or thousands of times more magnetic flux than the same coil in air.

But there's a problem: when a magnetic field changes inside a conductor, it induces electrical currents in that conductor. A solid iron block in a changing magnetic field would have huge circulating currents flowing within it — **eddy currents** — which would heat the iron up and waste enormous amounts of energy.

The fix is **lamination**: instead of one solid block of iron, you use many thin sheets, each separated by a microscopic layer of insulating varnish. The eddy currents can't flow across the insulation, so they're confined to tiny loops within each sheet, which dramatically reduces the energy loss.

Thinner laminations = less eddy current loss = more efficient = less heat. Cheap transformers use thicker laminations to save on stamping and assembly costs. Premium transformers (like the Pacific Transformer reproductions in the DynakitParts kit) use thinner, often grain-oriented silicon steel.

## What separates a good output transformer from a great one

For the **[A-470 output transformer](../components/a-470-output-transformer.md)** specifically — the one that actually carries your audio signal — winding geometry is critical and arguably the single biggest determinant of sound quality.

The challenge: an output transformer has to faithfully transform a wide audio bandwidth (20Hz to 20kHz, ideally well beyond on both ends) at high power levels. This is technically very hard.

- **Bass response** depends on having lots of primary inductance. More turns = more inductance = better bass. But more turns also means thinner wire (to fit in the same window), more resistance, more capacitance, and worse high-frequency response.
- **Treble response** depends on minimizing the **leakage inductance** — magnetic flux that doesn't link primary to secondary perfectly. Leakage inductance acts like a series inductor in the signal path, rolling off the highs.

The trick: leakage inductance is minimized by **interleaving the windings**. Instead of winding all the primary first and then all the secondary, you split them into sections — primary, secondary, primary, secondary — sandwiched together. The closer the primary turns are to the secondary turns, the better the magnetic coupling, and the lower the leakage inductance.

The Dynaco A-470 uses multiple-section interleaved winding — typically 5+ alternating layers. This is why it has wide bandwidth (the original spec sheet claimed −1dB from 6Hz to 30kHz at full power, which was extraordinary in 1959 and is still excellent today).

## Why audiophiles obsess over output transformers

The output transformer determines:

- **Frequency response** — how flat the amp is, how far the bass extends, how clean the highs are
- **Phase response** — how the timing of different frequencies aligns, which affects imaging and soundstage
- **Distortion character** — what kind of harmonics dominate when the amp is pushed
- **Damping factor** — how well the amp controls the speaker's motion, which affects bass tightness

A great output transformer with mediocre tubes will sound far better than mediocre transformers with great tubes. This is part of why the ST-70 platform supports such a wide range of tube swaps and modifications — the transformer is *good enough* that the tubes get to express themselves.

## See also

- [PA-060 power transformer](../components/pa-060-power-transformer.md) — the specific power transformer in this build
- [A-470 output transformer](../components/a-470-output-transformer.md) — the specific output transformer
- [Rectification](rectification.md) — what happens after the AC leaves the secondary
- [Heater circuits](heater-circuits.md) — the low-voltage secondaries
