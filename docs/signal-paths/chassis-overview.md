---
title: Chassis overview — all paths
---

# Chassis overview — all five paths on the underside floorplan

A view of the ST-70 chassis **from the underside** (the wiring side — what the builder sees while wiring) with every major component in its actual position per the original Dynaco wiring pictorial. **All five signal paths drawn simultaneously in distinct colors**. Use this as the "where does what live" overview before diving into a specific path.

The path-specific pages ([audio](audio.md), [B+](b-plus.md), [heater](heater.md), [bias](bias.md), [negative feedback](negative-feedback.md)) trace each path in stage-by-stage detail. This page is the *map*; those pages are the *journeys*.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/chassis-overview-all-paths.svg" alt="ST-70 chassis underside with all five signal paths overlaid">
  <figcaption>Underside (wiring-side) view. Front panel at top, rear panel at bottom — matches the orientation of the original Dynaco wiring pictorial. Wire routes are drawn with strict horizontal/vertical segments (90° bends) for readability; actual physical leads curve and bundle. Hover any component for details. Click to zoom.</figcaption>
</figure>

## How to read the diagram

- **Underside view (wiring side up)** — front panel at top, rear panel at bottom. This is the orientation you see when the chassis is flipped over on the bench for wiring.
- **Components in their actual chassis positions** — laid out to match the original Dynaco pictorial: V3/V2 stack on the left, V6/V7 stack on the right, PC-3A board in the center with V1 directly below it, PA-060 at the rear-center, choke and right speaker strip at the rear-right, left speaker strip and fuse at the rear-left.
- **Orthogonal wire routing** — every wire is horizontal or vertical with 90° bends. Actual physical leads curve and bundle; the simplified routing here is for readability.
- **Color = path**:

| Color | Path | What it carries |
|---|---|---|
| **Blue** (solid) | [Audio signal](audio.md) | The actual audio waveform, RCA → speaker |
| **Red** (solid) | [B+ supply](b-plus.md) | High-voltage DC to every tube plate and screen |
| **Green** (solid) | [Heater](heater.md) | 5 V and 6.3 V AC to every tube filament |
| **Gold** (solid) | [Bias](bias.md) | Small negative DC rail to the EL34 grids |
| **Orange** (dashed) | [Negative feedback](negative-feedback.md) | Sampled output back to the input cathode |

- **Colored dots inside each component** show which paths pass through that part. A component with multiple dots is a junction point where the paths interact — these are the most informative places to study.

## Where the paths overlap

A few components are heavily multi-tasked:

- **PA-060 power transformer** — single source for B+, heater (both channels), and bias. Every power-related path starts here.
- **EL34 sockets (V2, V3, V6, V7)** — touched by audio (grid + plate), B+ (plate), heater (pins 2/7), bias (grid). V3 and V6 also touch feedback (their pin-4 UL taps are sampled).
- **PC-3A driver board** — the convergence point for *every* path: audio passes through, B+ enters via eyelets 19 and 20, heater enters via V3 and V6 daisies, bias is distributed through the on-board pot connections, and feedback returns to the pentode cathode.
- **Filter cap chassis** — owns the entire B+ cascade (rectifier output, both dropping resistors, four filter sections).
- **A-470 output transformers** — audio (primary + secondary), B+ (primary CT), and feedback (both UL primary taps and 16 Ω secondary tap).

## Where the paths don't overlap (and why that matters)

- The **5 V heater winding** to the 5AR4 is the only winding that doesn't share its return with anything else — the 5AR4's cathode rides on this winding, and isolating it from ground keeps the rectifier independent of the rest of the chassis ground topology.
- The **two 6.3 V heater windings** (left and right channel) share *only the chassis ground* via their separate CTs. No heater current crosses between channels — preventing one channel's heater ripple from coupling into the other's signal path.
- The **bias supply** never touches the audio signal except *at the EL34 grids* — by design, so that DC bias modulation doesn't propagate through the audio chain.
- The **feedback wires** are the only path that runs *backwards* through the amp — from output back to input. Every other path goes input-to-output.

## When this diagram earns its keep

- **Conceptual learning** — when the per-path detail pages get dense, zoom out here to remind yourself how they fit together.
- **Debugging by elimination** — if symptom X appears only on one channel, the diagram instantly shows which components are shared (and therefore ruled out) versus which are channel-specific.
- **Modification planning** — adding a mod that touches one path? Use the dots to see what *else* touches the same components.

## What this diagram is NOT

- **Not a physical-routing pictorial.** Wires in the real amp follow specific paths along the chassis (twisted pairs hugging the metal, signal wires perpendicular to AC wires, etc.). The original Dynaco manual's pictorial diagrams are the right reference for that.
- **Not a schematic.** A schematic shows electrical relationships abstracted from physical layout. This is in-between: physical-ish layout, schematic-ish wires.
- **Not interactive yet.** Currently a static SVG with hover tooltips. A future revision may add path-selection (click to highlight one path and dim the others) and a side panel with component-in-path detail.

## See also

- [Audio signal path](audio.md)
- [B+ signal path](b-plus.md)
- [Heater path](heater.md)
- [Bias path](bias.md)
- [Negative feedback path](negative-feedback.md)
- [Components index](../components/index.md) — per-component deep dives
- [Build progress](../build/index.md) — which steps wire which paths
