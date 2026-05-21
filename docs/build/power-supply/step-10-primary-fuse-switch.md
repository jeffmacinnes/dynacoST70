---
title: Step 10 — Primary fuse & switch
---

# Step 10: Power transformer black leads to fuse post and switch

> *Dress the power transformer black leads around the end bell and connect one lead to lug A of the fuse post (S). Connect other black lead to lug #1 of on-off switch (S).* — manual page 6

## What you're doing physically

The PA-060 has two **BLACK leads** — these are the two ends of the **primary winding** (the 120 V AC mains side). They need to go to:

- One BLACK lead → **fuse post lug A** (S — soldered now)
- Other BLACK lead → **on-off switch lug 1** (S — soldered now)

**Dress the leads around the end bell** of the PA-060 — meaning route them along the curved end of the transformer's case rather than letting them dangle freely across the chassis. The end bell of the PA-060 is the dome-shaped cover at each end of the transformer; the leads exit from underneath it.

Routing logic:

- Both BLACK leads sit close together (they come out of the same end of the transformer).
- They run along the chassis perimeter to reach the fuse post (rear chassis) and the on-off switch (rear chassis).
- Keeping them close to the chassis minimizes the loop area for the AC current — which reduces radiated 60 Hz magnetic field that could couple into the audio path.

## What this completes — the mains-side power path

Before this step, the PA-060's primary winding wasn't connected to anything; the amp couldn't possibly power on. After this step (combined with the power cord installation in [step 65](../driver-stage/step-65-power-cord.md)):

1. **Mains hot** (BLACK from the power cord, step 65) → on-off switch lug 2 → switch lug 1 (when ON) → this BLACK PA-060 lead → primary winding
2. **Other end of primary** → other BLACK PA-060 lead → fuse post lug A → fuse → fuse post lug B → **mains neutral** (WHITE from the power cord, step 65)

So the AC current path through the primary is: hot → switch → primary → fuse → neutral. When the switch is OFF, the circuit is broken at the switch and no current flows through the primary at all.

## Why the fuse is in series with the primary

The 3 A slow-blow fuse protects against **catastrophic primary-side faults**:

- A shorted primary winding (rare but possible after decades of insulation breakdown).
- An accidental short of the BLACK leads to chassis or to each other (during repair work).
- A massive overcurrent from a downstream short (e.g., a filter cap fails as a dead short — the rectifier tries to dump huge current, which reflects back through the transformer as elevated primary current).

The fuse blows before any of these can damage the wall wiring, the transformer, or you. The 3 A rating is sized for normal operation (~1.5 A at full output) plus inrush margin (the cold-start surge can hit 5-6 A briefly — slow-blow tolerates that).

A fuse on the **secondary side** would protect downstream components but not the transformer itself or the building wiring. Primary-side fusing is universal for safety-critical equipment.

## Why the switch on the primary side (not after the transformer)

Three reasons:

1. **Safety**: with the switch OFF, the transformer secondary is completely de-energized. There's no B+, no heater AC, nothing. Service work is much safer.
2. **Tube life**: leaving the secondary energized while the primary is interrupted is impossible (the transformer is a single inductive system; you can't power one side without the other). But if you had a secondary-side switch, switching it would cause large voltage transients as the transformer's inductance tries to maintain current — bad for caps and tubes.
3. **Energy savings (minor)**: no idle transformer hum when off.

## Lug numbering

- **Fuse post lug A** = the lug closer to the chassis-mounting end (insulated from the rubber-washer side that faces outside). One PA-060 BLACK goes here.
- **On-off switch lug 1** = one of the two switch terminals (the other is lug 2, which gets wired to the power cord's BLACK lead in [step 65](../driver-stage/step-65-power-cord.md)).

## Modification touchpoints

The mains-side wiring is where two common modifications interact with the build:

- **[3-prong cord modification](../../modifications/3-prong-cord.md)**: the cord's GREEN earth lead lands on a solder lug at the PA-060's mounting stud (also wired in step 65). The earth lead is a third wire that doesn't affect this step but is part of the same general mains area.
- **[Anti-click cap modification](../../modifications/anti-click-cap.md)**: a small RC snubber across the on-off switch (between lugs 1 and 2) suppresses the inductive-kickback spike when the switch opens, eliminating the loud "click" on power-off. If you're installing the mod, do it now while the switch lugs are accessible — once the chassis fills up with later steps, getting back to the switch is harder.

## See also

- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — the primary winding being wired here
- [Step M8 — Fuse post mounting](../mechanical-assembly/step-m08-fuse-post.md) — where the fuse holder got installed
- [Step M9 — On-off switch mounting](../mechanical-assembly/step-m09-on-off-switch.md) — where the switch got installed
- [Step 65 — Power cord](../driver-stage/step-65-power-cord.md) — what completes the mains-side wiring
- [3-prong cord modification](../../modifications/3-prong-cord.md) — adds the earth-ground safety path
- [Anti-click cap modification](../../modifications/anti-click-cap.md) — suppresses the power-off click
- [Previous: Step 9](step-09-choke.md) · [Next: Step 11 — Right OPT secondaries](step-11-right-opt-secondaries.md)
