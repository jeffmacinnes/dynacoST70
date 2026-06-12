---
title: 'Step 47: Eyelet #21 to right bias pot lug 2'
---

# Step 47: 2½" wire from eyelet #21 (S) to right pot lug 2 (S)

> *Connect one end of a 2 ½" wire to eyelet #21 (S). Connect the other end to lug #2 of the right potentiometer (S).* — manual page 9

## What you're doing physically

A 2½" wire from PC-3 eyelet #21 to lug 2 (the **wiper**) of the right bias pot. Both ends soldered (S).

## What this completes

Lug 2 of the right pot is the **wiper** — the moving contact that taps a voltage off the pot's resistance element. Turning the pot moves the wiper, and that voltage is what eventually controls the EL-34 grid bias.

This wire delivers the wiper voltage from the right (channel A) pot **up to the PC-3 board** at eyelet #21.

On the PC-3 board, eyelet #21 connects through resistors to the appropriate eyelet outputs (#22 and #23 — the phase splitter outputs for channel A), so that the bias voltage gets distributed to both V6 and V7 grids through the coupling caps.

## How the bias actually arrives at the EL-34 grid

The audio signal AC and the bias DC share the same path:

1. Bias voltage at right pot wiper (lug 2) → through this wire → eyelet #21.
2. From eyelet #21 → through PC-3 board's internal resistor network → eyelet #22 (and eyelet #23).
3. From eyelet #22 → through a coupling cap on the board → out to V7 pin 6.
4. From V7 pin 6 → through the 1 kΩ grid stopper → V7 pin 5 (grid).

The bias is injected on the **grid side** of the on-board coupling caps: from eyelet #21, the wiper voltage feeds through the two 270 kΩ grid-return resistors to the output side of each coupling cap. The grids see the negative DC through those resistors, while the coupling caps (which block DC) keep the bias voltage out of the driver stage upstream. The key takeaway: turning the right pot moves the bias voltage applied to V6 and V7 grids.

## See also

- [Step 28 — Inter-pot wire (lug 1)](../output-stage/step-28-bias-pot-interconnect-2.md) — what completes the bias supply to the pot
- [Step 57 — Eyelet #6 to left pot](step-57-eyelet-6-to-left-pot.md) — the channel B equivalent
- [Bias adjustment](../../bring-up/bias-adjustment.md) — the user-facing procedure
