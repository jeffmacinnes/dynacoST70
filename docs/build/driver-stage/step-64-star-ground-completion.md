---
title: 'Step 64: Star ground completion'
---

# Step 64: Solder all six wires at the main ground lug

> *Connect short link of wire from capacitor ground lug (S) to solder lug near capacitor. Solder all six wires which go to the pair of solder lugs.* — manual page 10

## What you're doing physically

This step actually does two things:

1. **Short link from filter capacitor's ground lug to the main ground solder lug**. The filter cap can has its own ground tab (the can itself is the cap sections' common negative terminal). Run a short wire from that ground tab to the main ground solder lug, completing the cap's ground bond.
2. **Solder all six wires** that have accumulated at the main ground lug.

By this point, the main ground lug has accumulated:

1. Filter capacitor ground link (this step)
2. PC-3 eyelet #9 wire ([step 59](step-59-eyelet-9-to-ground.md))
3. Left speaker common ([step 61](step-61-left-strip-4-to-ground.md))
4. Right speaker common ([step 63](step-63-right-strip-4-to-ground.md))
5. RED/YEL HV center tap from [step 7](../power-supply/step-07-hv-ct.md)
6. Bias network ground from [step 23](../output-stage/step-23-bias-ground.md)

Six wires (the manual's exact count — there may be small revision-dependent variations).

## This is THE soldering operation

This is the most important solder joint in the amp. Six wires + a solder lug all need to be mechanically bonded together with one good joint.

Technique:

1. Make sure all six wires are physically inserted through the lug's hole, with their stripped ends visible.
2. Use a **high-wattage soldering iron** (60+ W) or a more powerful tip. The thermal mass of six wires + the lug + the chassis behind it is substantial.
3. Touch the iron to the lug and the bundle of wires simultaneously. Wait 3-5 seconds for everything to come up to temperature.
4. Apply solder to the wire bundle (not directly to the iron). Watch for the solder to flow — when it wets all six wires and the lug uniformly, you've got it.
5. Withdraw the solder, then a moment later withdraw the iron. Don't move anything while cooling.
6. Inspect: the finished joint should be shiny, smooth, and show that solder has wetted ALL six wires (no dull "dry" wires sticking out of a half-melted blob).

If you see any wire that doesn't appear wetted, reheat and add a bit more solder. A bad joint here = the entire amp's signal ground has high resistance = hum, noise, instability.

## After step 64

The **star ground topology is electrically complete**. All chassis-ground references converge at this one lug. Time to wire the power cord ([step 65](step-65-power-cord.md)).

## See also

- [Step M15 — Main ground lug](../mechanical-assembly/step-m15-ground-lugs.md) — the lug this step solders to
- [Grounding and hum](../../theory/grounding-and-hum.md) — why this joint is so critical
- [Filter capacitors](../../components/filter-capacitors.md) — the cap whose ground bond this completes
