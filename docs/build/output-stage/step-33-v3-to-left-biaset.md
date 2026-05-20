---
title: 'Step 33: V3 pin 1 to left Biaset socket pin 8'
---

# Step 33: 4½" wire from V3 pin 1 (S) to left power take-off pin 8 (S)

> *Connect one end of a 4 ½" wire to pin #1 of V3 (S). Connect the other end to pin #8 of the left power take-off socket (S).* — manual page 8

## What you're doing physically

A 4½" wire from V3 pin 1 to **pin 8 of the LEFT Biaset socket** (the front-panel V4 socket installed in [M1](../mechanical-assembly/step-m01-octal-sockets.md)). Both ends are soldered (S).

V3 pin 1 is now soldered final — it has the cathode daisy wire (step 32) + this wire.

## What this completes

This is the wire that brings the **channel B cathode voltage** out to a meter-probe point on the front panel.

Tracing the path:

- V2 + V3 cathodes (tied together) sit at some voltage above ground (1.56 V at correct bias, per [step 31](step-31-v2-cathode-sense.md))
- That voltage appears at V2 pin 1, V2 pin 8, V3 pin 1, V3 pin 8 — same potential.
- This wire takes that voltage from V3 pin 1 over to V4 pin 8.
- The Biaset socket on the front panel has "BIASET 1.56V" labeled near it.
- During bias adjustment, you stick the positive DMM probe into pin 8 of V4 and read the voltage.

The Biaset sockets are also "preamp power take-off sockets" — they can be wired (with additional wiring beyond this step) to provide power to a vintage Dynaco preamp. But the bias-measurement role is what 99% of users care about.

## Why V3 pin 1 specifically

Could have been any of the four EL-34 cathode pins (V2 pin 1, V2 pin 8, V3 pin 1, V3 pin 8). The manual picks V3 pin 1 because it's physically closest to V4 (the left Biaset socket), giving a short 4½" wire.

## See also

- [Step 31 — V2 cathode sense](step-31-v2-cathode-sense.md) — what voltage gets sampled
- [Step 36 — V6 to right Biaset](step-36-v6-to-right-biaset.md) — the mirror for channel A
- [Bias adjustment](../../bring-up/bias-adjustment.md) — the procedure that uses this wire
- [Step M1 — Octal sockets](../mechanical-assembly/step-m01-octal-sockets.md) — where the Biaset sockets are
