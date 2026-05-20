---
title: 'Step 23: Lug 6 to chassis ground'
---

# Step 23: 6" wire from lug 6 to the ground lug near the filter cap

> *Connect one end of a 6" wire to lug #6 of the 7 lug strip (S). Connect the other end to the ground lug near the filter capacitor. See pictorial.* — manual page 7

## What you're doing physically

A 6" wire connects lug 6 of the seven-lug strip to the **main ground solder lug** near the filter capacitor (the lug installed in [M15](../mechanical-assembly/step-m15-ground-lugs.md)). Lug 6 is **soldered (S)** at this step — it now has the disc cap from step 15 + this ground wire.

The ground end of this wire is not yet soldered — more wires will land on the main ground lug in subsequent steps (and especially in step 64 when the star ground is completed).

## What this completes

This is the moment the bias network's "ground" reference is established. Working backwards:

- Lug 6 ← now at chassis ground (via this wire)
- Lug 1 ← at chassis ground via the jumper from step 18
- Bias cap positives (at lug 1) ← at chassis ground

So both 100 µF caps are referenced to chassis ground at their positive ends, with their negative ends carrying the −65 V bias supply. The bias supply now has a complete current path.

## The star-ground design

This wire is one of the "rays" of the **star ground** topology. The main ground lug near the filter cap is the single point where all chassis-ground connections converge. The seven-lug strip's ground returns to this point via ONE wire (this one), even though many components on the strip share the ground node internally.

This avoids ground loops: multiple ground wires from the strip to chassis would create alternative current paths, and the differential voltages between those paths cause audible hum. One wire = no loop.

See [grounding and hum](../../theory/grounding-and-hum.md) for the full philosophy.

## See also

- [Step M15 — Ground lugs](../mechanical-assembly/step-m15-ground-lugs.md) — the star-ground point
- [Step 15 — Disc caps](step-15-disc-caps.md) — what else is on lug 6
- [Grounding and hum](../../theory/grounding-and-hum.md) — star-ground theory
