---
title: Step 8 — OPT B+ feeds
---

# Step 8: Feed the red leads from output transformers to filter capacitor lug #1

> *Feed the red lead from the left output transformer through both cable clamps and the red lead from the right output transformer through the right clamp. Connect both red leads to filter capacitor lug #1 (The lead from the right output transformer can be trimmed to the required length).* — manual page 6

## What you're doing physically

Each A-470 output transformer has a single **RED lead** on its primary side — the **primary center tap** of the push-pull winding. There are two A-470s (one per channel), so two red leads total. Both wire to **filter cap lug #1**.

Cable-routing:

- The **left OPT's** red lead is the longer-traveling one. Feed it through both cable clamps (the ones mounted in [M10](../mechanical-assembly/step-m10-pa-060.md) over the PA-060's front mounting screws) so it's mechanically secured along its path.
- The **right OPT's** red lead is closer to the filter cap. Feed it through just the right cable clamp.
- Trim the right OPT lead to length as needed — the manual notes it can be shortened. Don't trim the left one yet; it has further to travel.

Filter cap lug #1 stays unsoldered at this step — the choke leads (next step) land on the same lug and they all get soldered together.

## Why the red leads go to lug #1 specifically

Lug #1 of the quad filter capacitor is **"lug C"** in the voltage table — the **main B+ rail**, sitting at ~415 V DC after the choke smooths the rectifier output. That's the supply voltage you want feeding the OPT primaries.

The signal flow:

1. B+ DC arrives at lug C from the rectifier-then-choke chain.
2. From lug C, this wire carries it out to the OPT primary center taps (RED leads).
3. At the OPT primary, the center tap is the AC-grounded midpoint of a push-pull winding. DC current flows from the CT outward into both halves of the primary, then out the two plate leads (BLUE and GREEN) into the EL-34 plates.
4. EL-34s draw their plate current from this rail. Audio signal modulates each EL-34's current up and down around the DC operating point.

## Why both OPTs share the same B+ node

Both channels' OPT primaries land at the same filter cap lug. Why isn't there one filter cap section per channel?

Because the **B+ supply is shared** between the two channels in any reasonable amp design. The two channels' EL-34s draw current from the same node; whatever filter caps are at that node smooth the ripple for both.

The two channels remain **signal-isolated** at the OPT primary CT because:

- The CT is the *AC midpoint* of the primary winding. In normal push-pull operation, the two halves of the primary push and pull current equally — net current at the CT is constant (just DC). No audio signal appears at the CT.
- Audio signal exists only in the primary's two end leads (BLUE and GREEN), which go to separate tubes (V2/V3 or V6/V7).

So even though both channels' RED leads share lug #1, audio cannot cross-talk through that node. The push-pull topology guarantees AC isolation at the CT.

## Why cable clamps

The PA-060's two front mounting screws each have a cable clamp underneath (installed in [M10](../mechanical-assembly/step-m10-pa-060.md)). These clamps:

- **Mechanical strain relief**: heavy-gauge wires can't pull on their solder joints if they're clamped down somewhere along their length.
- **Routing**: the clamps guide bundles of wires along a predictable path, keeping the chassis interior organized.
- **Vibration damping**: clamped wires don't oscillate at low frequencies (which would eventually fatigue-crack the copper).

The clamps are tightened in [step 9](step-09-choke.md) — leave them loose for now so you can adjust the lead positions as you go.

## See also

- [A-470 output transformer](../../components/a-470-output-transformer.md) — the RED primary CT lead
- [Step M10 — PA-060 mounting](../mechanical-assembly/step-m10-pa-060.md) — where the cable clamps got installed
- [Step M14 — Quad filter cap](../mechanical-assembly/step-m14-filter-cap.md) — lug numbering reference
- [Filter capacitors](../../components/filter-capacitors.md) — the cap structure
- [Push-pull topology](../../theory/push-pull-topology.md) — why the CT is signal-quiet
- [Step 29 — Rectifier to filter cap](../output-stage/step-29-rectifier-to-filter-cap.md) — what feeds lug 2 (the upstream node)
- [Previous: Step 7](step-07-hv-ct.md) · [Next: Step 9 — Choke](step-09-choke.md)
