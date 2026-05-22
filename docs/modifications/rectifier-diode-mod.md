---
title: Rectifier diode mod
---

# Rectifier diode mod (1N4007s in series with the 5AR4 plates)

A pair of **1N4007 silicon diodes** added in series with each plate of the [5AR4 rectifier tube](../components/5ar4-rectifier-tube.md). The red high-voltage leads from the [PA-060](../components/pa-060-power-transformer.md) no longer land directly on pins 4 and 6 of V1 — they move one lug over (to an adjacent NC pin) and the diodes bridge the gap.

This mod isn't in the original 1959 Dynaco manual, but DynakitParts now ships the two 1N4007s with current kits and recommends it as a separate add-on sheet (the one tucked into your kit box). It's purely optional.

## What problem it solves

Tube rectifiers — the 5AR4 especially — most commonly die during the **warm-up cycle** at power-on, not during steady-state operation.

Two things go wrong in the first ~30 seconds:

1. **The cathode hasn't fully heated yet**, so its emission is still ramping up. That means high *anode-to-cathode voltage* with not-yet-conducting current. If the tube is even slightly gassy, or if a plate happens to be close to the cathode mechanically, this is the moment an internal arc can strike. Once an arc starts, the tube is usually toast.
2. **The filter caps are uncharged**, so the load looks momentarily like a near-short. As soon as the cathode does start emitting, there's a slug of inrush current pulling through the plates to charge those caps. The combination of high plate voltage + sudden current surge is the worst case for a rectifier tube.

Silicon diodes don't care about either of these. They conduct in microseconds when forward-biased and block instantly when reverse-biased — no warm-up, no arc-over failure mode. Putting one in series with each 5AR4 plate transfers most of the warm-up stress to the diodes.

## What's actually happening electrically

Before the mod, current flows (on a positive half-cycle for plate 1):

```
red lead → pin 4 → plate 1 inside tube → vacuum → cathode (pin 8) → filter cap
```

After the mod:

```
red lead → NC pin (3 or 5) → 1N4007 → pin 4 → plate 1 → vacuum → cathode → filter cap
```

The 1N4007 is in series with the tube's internal diode. On the *reverse* half-cycle the tube was already blocking, but a weakened or arcing tube can fail to block cleanly. The silicon diode adds a hard backup: even if the tube arcs over internally, the silicon won't let current run backwards.

## Why 1N4007 specifically

| Spec | 1N4007 | Margin in this app |
|---|---|---|
| Peak inverse voltage | 1000 V | HV secondary peaks ~510 V (720 Vp-p across full winding ÷ 2) — 2× margin |
| Forward current | 1 A continuous | 5AR4 max DC output is 250 mA — 4× margin |
| Forward Vf | ~1 V | Negligible vs. 360 VAC per half-winding |
| Cost | ~$0.10 | — |

The 1N4007 is the cheapest reasonable choice that gives plenty of headroom in both PIV and current. The same part number is used for [the bias diode](1n4007-replacement.md) — it's the workhorse high-voltage rectifier diode of the modern era.

## Which NC pins to use as tie-points

The 5AR4 has **four NC (no-connection) pins** — 1, 3, 5, and 7 — none of which connect to anything inside the glass. They're empty socket lugs, perfect as auxiliary tie-points.

For each red lead, use whichever NC pin is immediately adjacent to its plate pin:

- **For plate 1 (pin 4):** pin 3 *or* pin 5 (both are right next to pin 4)
- **For plate 2 (pin 6):** pin 5 *or* pin 7 (both are right next to pin 6)

The pair of choices you make is purely about which routing gives the shortest, cleanest run from where the red lead naturally enters the socket area. All variants are electrically identical.

| Tie-point pair | When to choose it |
|---|---|
| Pin 5 + pin 7 | What the DynakitParts mod sheet's pictorial shows; leads enter from the pin-5/6/7 side |
| Pin 3 + pin 5 | Leads enter from the pin-2/3/4 side |
| Pin 3 + pin 7 | Leads come in from opposite sides of the socket |

**Important:** you can't use the same NC pin for *both* red leads. The two reds are opposite ends of the HV secondary winding (180° out of phase) — connecting them to the same point would short half the winding and almost certainly take out the fuse, the transformer, or both. Each red lead gets its own NC lug.

Below, examples and diagrams use the mod-sheet's pin 5 / pin 7 layout for concreteness; substitute pin 3 or pin 5 wherever pin 5 / pin 7 is shown if you've chosen a different routing.

## Diode orientation

The 1N4007's **banded end is the cathode**. The cathode goes toward the tube plate:

```
red lead ─── (pin 5) ──[ anode | cathode ]── (pin 4) ─── plate 1
                              1N4007             band end

red lead ─── (pin 7) ──[ anode | cathode ]── (pin 6) ─── plate 2
                              1N4007             band end
```

Reversed, the diode would block the *forward* half-cycle and the rectifier would do nothing. Easy to check before soldering: band end toward pins 4 and 6.

## Retrofitting after step 3 is already done

If you already completed [step 3](../build/power-supply/step-03-5ar4-anodes.md) by the book (red leads soldered to pins 4 and 6), the rework is straightforward and uses the same lead length you already have — you're just shifting each lead one lug over.

First, **decide which NC pin each red lead will move to** based on the routing you already have (see the table above). For the steps below, "the chosen NC pin" means pin 3 or pin 5 on the plate-1 side, and pin 5 or pin 7 on the plate-2 side — whichever you picked.

For each side:

1. **Desolder the red lead from pin 4** (or pin 6). Hold the lead with pliers, heat the joint, lift the lead clear. Don't yank — let the solder melt fully.
2. **Form the red lead over to the chosen NC pin.** Lead length should still reach with a little dress-routing; trim only if necessary.
3. **Hook the red lead through the chosen NC pin and crimp lightly**, but don't solder yet — the diode's anode lead also needs to land in this lug.
4. **Form the 1N4007** with its banded end toward the plate pin (4 or 6) and the unbanded end toward the chosen NC pin. Trim the leads to span the gap with a little slack — the diode should not be under tension.
5. **Insert the diode anode lead into the NC pin with the red lead**, and the diode cathode lead into the plate pin (4 or 6).
6. **Solder both lugs.** The joint at the NC pin now holds two leads (red wire + diode anode). The joint at the plate pin holds one (diode cathode).

The twist of the red pair from [step 3](../build/power-supply/step-03-5ar4-anodes.md#why-we-twist-this-pair-too) stays intact — you're only redirecting the last inch or so of each lead.

Sanity check before powering on:

- Visually confirm both diode bands face the tube plates (pins 4 and 6).
- Continuity test: from each NC tie-point lug to its plate pin, you should read low resistance in one polarity and very high in the other — that's the diode. If you read low in both polarities the diode is shorted; if high in both, it's reversed or open.

## What you'd give up

Almost nothing. The tradeoffs are:

- **A tiny voltage drop** (~1 V across each diode at the operating current). Across the full B+ supply this is in the noise — the unregulated B+ varies more than that with line voltage anyway.
- **Two extra parts** that could theoretically fail. In practice 1N4007s in this duty cycle effectively never fail — they're nowhere near their ratings.
- **Slightly busier-looking V1 socket area**. Cosmetic.

The upside: a much more forgiving warm-up, especially if you ever run with a less-than-perfect rectifier tube (NOS that's been on a shelf 60 years, current production 5AR4 from a sketchy batch, etc.).

## What this is NOT

This is **not** the same thing as replacing the 5AR4 with solid-state rectification entirely. That would be a different mod — pull the tube, jumper the diodes from pin 4/6 directly to pin 8, and you'd lose the slow warm-up that protects the output tubes from cathode stripping. This mod *keeps the tube as the rectifier* and just adds silicon insurance in series.

It's also not related to the [1N4007 bias-diode mod](1n4007-replacement.md), which sits in a completely different circuit (the bias supply) and uses one 1N4007 in place of the original selenium rectifier.

## See also

- [Step 3 — 5AR4 anodes](../build/power-supply/step-03-5ar4-anodes.md) — the original wiring this mod modifies
- [5AR4 rectifier tube](../components/5ar4-rectifier-tube.md) — pinout and failure modes
- [1N4007 diode](../components/1n4007-diode.md) — the part itself
- [1N4007 bias-diode (historical)](1n4007-replacement.md) — the other place a 1N4007 lives in this amp
