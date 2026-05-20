---
title: 'Step 45: V6 heater pins to board eyelets #15 and #16'
---

# Step 45: Twisted pair from board eyelets #15/#16 (S) to V6 pin 7/pin 2 (S)

> *Twist together a pair of wires with length to suit (see pictorial). Strip and connect one pair of ends to eyelets #15 (S) and #16 (S). Strip and connect other wire ends to socket V6, Pin #7 (S) and Pin #2 (S).* — manual page 9

## What you're doing physically

A **twisted pair** of hookup wires, length to suit (typically 4-5"). One pair of ends goes to PC-3 eyelets #15 and #16. The other pair goes to V6 pin 7 and pin 2. All four soldered (S).

## What this carries

This is the **6.3 V heater AC** to the channel A 6GH8A on the PC-3 board. The heater current comes from the EL-34 channel A heater string (V6 + V7), which is fed from the PA-060 BRN pair:

- PA-060 BRN pair → V7 pins 2 and 7 (step 5)
- V7 daisy to V6 (step 16)
- **V6 pins 2 and 7 also feed up to the PC-3 board** via this step

So the 6GH8A heater taps off the EL-34 heater bus. One PA-060 winding powers two EL-34 heaters + one 6GH8A heater — total ~3 A which is comfortably under the 5 A winding rating.

## Why daisy off V6 instead of the PA-060 directly

Two reasons:

1. **Wire length**: the PC-3 board is in the middle of the chassis; V6 is closer than the PA-060.
2. **Hum minimization**: keeping the heater wire run short reduces the loop area for stray AC magnetic-field pickup. A long heater wire would couple more hum into the input stage.

## Twisting matters

The heater pair carries AC, and AC currents in single wires radiate magnetic fields. Twisted pairs cancel almost all the radiation. Critical for a low-hum amp — see [heater circuits](../../theory/heater-circuits.md).

## See also

- [Step 5 — V7 heater](../power-supply/step-05-v7-heater.md) — where the heater string starts
- [Step 16 — V6/V7 heater daisy](../output-stage/step-16-v6-v7-heater-daisy.md) — chain continuation
- [Step 46 — V3 heater to board](step-46-v3-heater-to-board.md) — channel B's equivalent
- [Heater circuits](../../theory/heater-circuits.md) — twisted-pair theory
