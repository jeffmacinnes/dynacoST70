---
title: 'Step 46: V3 heater pins to board eyelets #4 and #5'
---

# Step 46: Twisted pair from board eyelets #4/#5 (S) to V3 pin 7/pin 2 (S)

> *Twist together a pair of wires with length to suit (see pictorial). Strip and connect one pair of ends to eyelets #4 (S) and #5 (S). Strip and connect other wire ends to socket V3, Pin #7 (S) and Pin #2 (S).* — manual page 9

## What you're doing physically

Mirror of [step 45](step-45-v6-heater-to-board.md), but for channel B. A twisted pair from PC-3 eyelets #4/#5 to V3 pin 7/pin 2. All four soldered.

## What this completes

The channel B 6GH8A on the PC-3 board now has 6.3 V AC heater power, tapped off the V3 EL-34 heater pins. The full heater chain for channel B:

- PA-060 GRN pair → V2 pins 2/7 (step 4)
- V2 daisy to V3 (step 17)
- V3 pins 2/7 to PC-3 eyelets #4/#5 (this step)

Both 6GH8A driver tubes now have heater power. Together with the B+ feeds from steps 41-43 and ground from step 59, the drivers will be electrically alive.

## See also

- [Step 45 — V6 heater to board](step-45-v6-heater-to-board.md) — the channel A mirror
- [Step 4 — V2 heater](../power-supply/step-04-v2-heater.md) — start of the channel B heater string
