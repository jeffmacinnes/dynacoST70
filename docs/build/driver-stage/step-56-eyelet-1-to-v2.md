---
title: 'Step 56: Eyelet #1 to V2 pin 6'
---

# Step 56: 3½" wire from eyelet #1 (S) to V2 pin 6 (S)

> *Connect one end of a 3 ½" wire from eyelet #1 (S). Connect the other end to pin #6 of V2 (S).* — manual page 10

## What you're doing physically

A 3½" wire from PC-3 eyelet #1 to V2 pin 6. Both ends soldered.

V2 pin 6 now has: the 1 kΩ grid stopper from step 37 + this wire. Soldered final.

## What this is

The other phase-splitter output of the channel B 6GH8A, 180° opposite of eyelet #2. Together with [step 55](step-55-eyelet-2-to-v3.md), this completes the push-pull drive for channel B.

After steps 39, 40, 55, 56: all four EL-34 grids have signal drive from the PC-3 board. The audio signal path is electrically complete:

- Input RCA → grid leak → board input → 6GH8A pentode → coupling cap → 6GH8A triode (phase splitter) → coupling caps → V2/V3/V6/V7 grids (via grid stoppers) → EL-34 plates → OPT primary → OPT secondary → speaker terminals.

## See also

- [Step 55 — Eyelet #2 to V3](step-55-eyelet-2-to-v3.md) — the other half of the channel B push-pull
- [Push-pull topology](../../theory/push-pull-topology.md)
