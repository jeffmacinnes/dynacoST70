---
title: 'Step 44: Input ground returns to PC-3 board'
---

# Step 44: Two short links from RCA grounded lugs to circuit-board input pads

> *Cut (2) short lengths of wire (to suit) and strip ends 1/4". Connect (S) one wire to circuit board input [L] and connect (S) other end to the "Left" grounded (short) lug of the RCA input socket. Now, connect (S) the other wire to circuit board input [R] and connect (S) other end to the "Right" grounded (short) lug of the RCA input socket.* — manual page 8

## What you're doing physically

Two short wires (length whatever fits cleanly — typically 2-3"). Each wire connects:

- One end: PC-3 board's "input [L]" or "input [R]" pad (the board has these labelled — they're the signal-ground pads for each channel's audio input).
- Other end: the **grounded (short) lug** of the left or right RCA jack respectively.

The grounded lug of an RCA jack is the outer "barrel" connection — it's electrically shorter than the center-pin (signal "hot") lug. Hence "short" lug.

All four ends are soldered (S) at this step.

## Why "grounded" lugs go to the board, not chassis

This is critical for hum-free operation.

The RCA jack has two terminals:

- **Long lug** = center pin = signal hot
- **Short lug** = outer barrel = signal ground (the shield side of the input cable)

You'd think "ground = chassis" and the shield should just bolt to the chassis. But that creates a **ground loop**: signal ground current flowing through the chassis past other circuit grounds picks up voltage differences across the chassis's small resistance, which appear as hum.

Instead: the signal ground from the RCA shield goes to the PC-3 board's input pad, which is electrically the **signal ground reference for the input stage**. From the board, the signal ground eventually ties to chassis ground at exactly ONE point (the star ground, completed in step 64).

So the signal ground current path is: RCA shield → board → board's internal ground network → eyelet #9 → step 59 wire → main ground lug. Single path, no loops.

## The Bakelite insulator's role here

The Bakelite insulator from [M2](../mechanical-assembly/step-m02-input-connector.md) is what makes this single-point-ground work. It prevents the RCA jack frames from directly contacting chassis metal — if they did, signal ground would be tied to chassis at the RCA jack AND at the star ground, creating exactly the loop you're trying to avoid.

## See also

- [Step M2 — Input connector](../mechanical-assembly/step-m02-input-connector.md) — the Bakelite insulator that makes this work
- [Step 59 — Eyelet #9 to ground](step-59-eyelet-9-to-ground.md) — where the board's signal ground meets chassis
- [Grounding and hum](../../theory/grounding-and-hum.md) — full theory
