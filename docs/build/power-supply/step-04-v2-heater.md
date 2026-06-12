---
title: Step 4 — V2 heater
---

# Step 4: Twist the green pair of leads and connect to V2 pins #2 and #7

> *Twist the pair of green leads together and dress to socket V2. Connect one green lead to pin #2 of V2. Connect the other green lead to pin #7 of V2.*

Note: **no (S) markers** on either pin. Both connections are left unsoldered for now — more wires will land on these pins in later steps (the heater "daisy chain" continues from V2 to other tubes), and you'll solder them all together when each pin is fully populated.

## What you're doing physically

Connecting the **first 6.3V @ 5A heater winding** of the [PA-060](../../components/pa-060-power-transformer.md) (the green-green pair) to the **filament pins of V2** — one of the [EL34 output tubes](../../components/el34-output-tube.md).

This is the moment you start wiring up the heaters for the signal-carrying tubes (versus the rectifier's heater, which got wired in [step 2](step-02-5ar4-heater.md)).

## Why pins #2 and #7 on the EL34

The EL34 is an octal-base tube (8 pins). On an EL34, pins 2 and 7 are the heater pins. The full pinout, for reference:

```
        Pin 1  ─  suppressor grid (g3) — strapped to the cathode externally in this build
        Pin 2  ─  heater
        Pin 3  ─  plate (anode)   ←── HV B+ comes in here via OPT
        Pin 4  ─  screen grid     ←── fed from the OPT's ultralinear taps
        Pin 5  ─  control grid    ←── negative bias from bias supply
        Pin 6  ─  no internal connection (used as a tie point)
        Pin 7  ─  heater
        Pin 8  ─  cathode         ←── usually grounded via small R
```

Pins 2 and 7 are the two ends of the filament wire that runs inside the tube. 6.3V AC across that filament dissipates roughly 9 watts of heat (the EL34 spec is 1.5A at 6.3V), bringing the cathode up to operating temperature.

## Why this heater pair gets no center-tap consideration here

You might notice we're connecting the two ends of the green winding (the two GRN leads) to the tube, but **not the green-yellow center tap**. Where does the CT go?

That's the subject of [step 6](step-06-heater-cts.md), two steps from now. The CT gets routed to a separate location on the [seven-lug terminal strip](../../components/seven-lug-terminal-strip.md) for grounding purposes. So:

- Steps 4 and 5 wire the **active ends** of each 6.3V winding to its tube heater
- Step 6 wires both **center taps** to a grounding reference

This is intentional separation of concerns. The active leads carry the heater current; the CTs serve a different electrical purpose entirely (hum balancing, covered in [step 6](step-06-heater-cts.md)).

## Why no solder yet

V2's heater pins are part of a **chain** that distributes 6.3V AC to multiple tubes' heaters in parallel. In a later step (you'll see it on subsequent manual pages), short jumper wires will go from V2's pin 2 to the corresponding pins on V3 and the [driver board tubes](../../components/pc-3a-driver-board.md) — wherever else needs the same 6.3V source.

When you eventually solder pin 2, you'll be soldering the green lead from the transformer *plus* the jumper to the next tube *plus* possibly other connections, all at once. Soldering now would just mean having to re-flow the joint later, which weakens it.

## See also

- [EL34 output tube](../../components/el34-output-tube.md) — pin functions
- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — the green heater winding
- [Heater circuits](../../theory/heater-circuits.md) — why we twist, why we dress along the chassis
- [Previous: Step 3](step-03-5ar4-anodes.md) · [Next: Step 5 — V7 heater](step-05-v7-heater.md)
