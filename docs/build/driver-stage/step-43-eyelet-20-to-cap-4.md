---
title: 'Step 43: Eyelet #20 to filter cap lug 4'
---

# Step 43: 3½" wire from eyelet #20 (S) to filter cap lug 4 (S)

> *Connect a 3 ½" wire from eyelet #20 (S) to capacitor lug #4 (S).* — manual page 8

## What you're doing physically

A 3½" wire from PC-3 eyelet #20 to filter cap lug 4. Both ends soldered.

Lug 4 is now soldered final — it has the 6.8 kΩ resistor from [step 30](../output-stage/step-30-b-plus-dropping-resistor.md), the 22 kΩ resistor from [step 42](step-42-22k-dropping-resistor.md), and this wire.

## What this wire carries

Lug 4 = "lug B" = **375 V DC** at idle. This wire delivers 375 V to PC-3 eyelet #20, which feeds the **6GH8A pentode screen grid** and the **triode plate** (the cathodyne phase splitter).

The pentode screen wants ~150-180 V; the on-board screen-dropping resistor takes 375 V down to the right operating point.

The triode (phase splitter) plate wants a slightly higher voltage than the pentode screen — somewhere around 250-300 V. Again, an on-board dropping resistor brings 375 V down to the right value.

## After step 43

The driver board has both B+ feeds (eyelet #19 = 305 V, eyelet #20 = 375 V). Combined with the heaters (coming in steps 45-46), the board has everything it needs to operate — once the audio input and output wires are also connected.

## See also

- [Step 41 — Eyelet #19 to cap 3](step-41-eyelet-19-to-cap-3.md) — the other B+ feed
- [Step 42 — 22 kΩ dropping resistor](step-42-22k-dropping-resistor.md)
- [6GH8A driver tube](../../components/6gh8a-driver-tube.md) — pentode/triode voltage targets
