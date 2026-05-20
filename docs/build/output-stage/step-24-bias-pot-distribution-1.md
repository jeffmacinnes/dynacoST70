---
title: 'Step 24: Lug 3 to left bias pot lug 1'
---

# Step 24: 6" wire from lug 3 (S) to left pot lug 1

> *Connect one end of a 6" wire to lug #3 of the 7 lug strip (S). Connect the other end to lug #1 of the left bias potentiometer.* — manual page 7

## What you're doing physically

A 6" wire connects lug 3 of the seven-lug strip to lug 1 of the **left bias pot** (the 10 kΩ potentiometer for channel A bias). Lug 3 is soldered final at this step — by now it has: the negative end of the second bias cap (step 21), the 10 kΩ resistor (step 20), and this distribution wire. All three get soldered together.

The pot's lug 1 is NOT soldered yet — it'll get more wires before being sealed.

## What this carries

Lug 3 of the seven-lug strip carries the **filtered −65 V bias DC** (the output of the two RC filter stages from steps 19-22). This wire delivers that voltage to one end of the left bias pot's resistance element.

## Why "lug 1" of the pot

A 3-lug potentiometer has:

- Lug 1: one end of the resistance element
- Lug 2: the wiper (center contact, moves as you rotate)
- Lug 3: the other end of the resistance element

For the bias adjustment to work:

- Lug 1 sits at the most-negative voltage (−65 V from this wire).
- Lug 3 sits at chassis ground (will be wired in step 27/28).
- Lug 2 (wiper) sits somewhere between, depending on the pot's position.

Turning the pot moves lug 2's voltage between ~−65 V and ~0 V. That voltage drives the EL-34 grids through the rest of the bias network — controlling tube bias.

## See also

- [Step 26 — Lug 2 distribution](step-26-bias-pot-distribution-2.md) — wires the pot wiper down the chain
- [Step M5 — Bias pots](../mechanical-assembly/step-m05-bias-pots.md) — where these pots got mounted
- [Bias adjustment](../../bring-up/bias-adjustment.md) — how the pots get used
