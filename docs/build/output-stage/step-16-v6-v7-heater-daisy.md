---
title: 'Step 16: V6 ↔ V7 heater daisy-chain'
---

# Step 16: Twist a pair of 6" wires and daisy V6 and V7 heaters

> *Twist together a pair of 6" wires except for 1 ½" at each end. Connect one end of one wire to pin #2 of V7 (S). Connect the other wire to pin #7 of V7 (S). Connect one of the other ends to pin #2 of V6. Connect the remaining end to pin #7 of V6.* — manual page 7

## What you're doing physically

Cut two pieces of hookup wire, each 6" long. Strip ¼" from each end of each wire. Lay them parallel and twist them together along their middle 3", leaving 1½" untwisted at each end. The untwisted ends make it easy to land each wire on a separate pin.

Then connect:

- One wire from V7 pin 2 (S) → V6 pin 2 (NOT soldered yet)
- Other wire from V7 pin 7 (S) → V6 pin 7 (NOT soldered yet)

V6 pins 2 and 7 will get more wires later (the heater feed FROM the PA-060 in [step 5](../power-supply/step-05-v7-heater.md) already lands at V7; the V6 daisy gets soldered later when its heater pins are fully populated).

## What this completes

The channel A heater string is now:

1. **PA-060 BRN pair** → V7 pins 2 and 7 (from [step 5](../power-supply/step-05-v7-heater.md))
2. **V7 pin 2** → V6 pin 2 (this step)
3. **V7 pin 7** → V6 pin 7 (this step)

So V6 and V7 share the same heater AC — fed once from the PA-060, daisied between the two tubes.

## Why twist the pair

The two wires carry 6.3 V AC and the return current (or rather, the AC waveform on each wire is 180° out of phase relative to the CT, which lands at lug 7 of the seven-lug strip and is AC-referenced to ground through a 0.02 µF disc cap — not hard-grounded). When the two wires are twisted, the magnetic field from one wire cancels the magnetic field from the other — minimising radiated hum.

A twisted heater pair also looks neater than two separate wires and is mechanically more stable.

## See also

- [Step 5 — V7 heater](../power-supply/step-05-v7-heater.md) — where the PA-060 brown pair lands at V7
- [Step 17 — V2/V3 heater daisy](step-17-v2-v3-heater-daisy.md) — mirror for the other channel
- [Heater circuits](../../theory/heater-circuits.md) — how the channels are separated
