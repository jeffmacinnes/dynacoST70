---
title: 'Step 36: V6 pin 8 to right Biaset socket pin 8'
---

# Step 36: 4½" wire from V6 pin 8 (S) to right power take-off pin 8 (S)

> *Connect one end of a 4 ½" wire to pin #8 of V6 (S). Connect the other end to pin #8 of the right power take-off socket (S).* — manual page 8

## What you're doing physically

Mirror of [step 33](step-33-v3-to-left-biaset.md). A 4½" wire from V6 pin 8 to **pin 8 of the RIGHT Biaset socket** (V5 on the front panel). Both ends soldered.

V6 pin 8 is now soldered final (cathode daisy from step 35 + this wire).

## What this completes

Channel A's cathode voltage is now routed to V5 pin 8 — the right Biaset socket. Stick the positive DMM probe into V5 pin 8 during bias adjustment, read 1.56 V when channel A is correctly biased.

After steps 33 and 36 together, **bias measurement is fully wired**:

- V4 pin 8 → channel B (V2 + V3) cathode voltage
- V5 pin 8 → channel A (V6 + V7) cathode voltage

You can now follow the stock [bias adjustment](../../bring-up/bias-adjustment.md) procedure once the rest of the amp is wired and powered up.

## See also

- [Step 33 — V3 to left Biaset](step-33-v3-to-left-biaset.md) — the channel B mirror
- [Bias adjustment](../../bring-up/bias-adjustment.md) — the procedure that uses these sockets
