---
title: 'Step 40: Eyelet #22 to V7 pin 6'
---

# Step 40: 3" wire from eyelet #22 (S) to V7 pin 6 (S)

> *Connect a 3" wire from eyelet #22 (S) to pin #6 of V7 (S).* — manual page 8

## What you're doing physically

A 3" wire from PC-3 eyelet #22 to V7 pin 6. Both ends soldered.

V7 pin 6 now has: the 1 kΩ grid stopper from [step 37](../output-stage/step-37-grid-stoppers.md) + this wire.

## What this wire carries

Eyelet #22 is the **other phase-splitter output** of the channel A 6GH8A — 180° opposite phase to eyelet #23. Together with [step 39](step-39-eyelet-23-to-v6.md), this completes the push-pull drive for channel A:

- Eyelet #23 → V6 → audio at one phase
- Eyelet #22 → V7 → audio at the opposite phase

V6 and V7 push and pull current through the A-470 primary, producing the full audio output. See [push-pull topology](../../theory/push-pull-topology.md).

## See also

- [Step 39 — Eyelet #23 to V6](step-39-eyelet-23-to-v6.md) — the other half of the push-pull pair
- [Push-pull topology](../../theory/push-pull-topology.md) — why two opposite-phase signals
- [Step 37 — Grid stoppers](../output-stage/step-37-grid-stoppers.md)
