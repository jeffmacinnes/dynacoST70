---
title: 'Step 17: V2 ↔ V3 heater daisy-chain'
---

# Step 17: Repeat step 16 for V2 and V3

> *Repeat Step 16 for connection of V2 and V3.* — manual page 7

## What you're doing physically

Mirror of [step 16](step-16-v6-v7-heater-daisy.md) but for the channel B heater string.

Two 6" wires, twisted in the middle, 1½" untwisted at each end. Connect:

- One wire from V2 pin 2 (S) → V3 pin 2 (NOT soldered yet)
- Other wire from V2 pin 7 (S) → V3 pin 7 (NOT soldered yet)

## What this completes

The channel B heater string:

1. **PA-060 GRN pair** → V2 pins 2 and 7 (from [step 4](../power-supply/step-04-v2-heater.md))
2. **V2 pin 2** → V3 pin 2 (this step)
3. **V2 pin 7** → V3 pin 7 (this step)

V2 and V3 share heater AC — fed once from the PA-060, daisied between them.

After this step, all four EL-34 heaters are wired. They draw 6.3 V AC × 1.5 A each = ~9 W of heat per tube, distributed across two separate PA-060 windings (one per channel pair).

## See also

- [Step 4 — V2 heater](../power-supply/step-04-v2-heater.md) — where the PA-060 green pair lands at V2
- [Step 16 — V6/V7 heater daisy](step-16-v6-v7-heater-daisy.md) — the mirror
- [Heater circuits](../../theory/heater-circuits.md) — heater AC theory
