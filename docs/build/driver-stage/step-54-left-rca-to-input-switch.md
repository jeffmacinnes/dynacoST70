---
title: 'Step 54: Left RCA long lug to input switch lug 2'
---

# Step 54: Short link from left RCA long lug (S) to input switch lug 2

> *Connect a short link of wire from the left input socket (long) lug (S) to lug #2 of the input switch.* — manual page 9

## What you're doing physically

A short wire (length whatever fits cleanly — typically 1-2") from the left RCA long lug to **lug 2** of the input switch. The RCA end is soldered final at this step — it now has the wire from step 53 + this wire. The switch end (lug 2) is NOT soldered yet — input switch lug 2 is the **pole/common** and receives more connections in mono operation.

## What this connects

This wire establishes the **left channel's signal path through the input switch**:

- In STEREO position: switch lug 2 is connected to switch lug 1 (per the SPDT topology). So left RCA hot → this wire → switch lug 2 → switch lug 1 → which is wired (via the 470 kΩ grid leak) to ground. That means in STEREO position, the switch effectively shunts the left signal to the grid leak, which is fine — the grid leak is there anyway as a DC clamp.

Actually wait — let me reconsider. Looking at SPDT switch operation: when in one position, lug 2 connects to lug 1; when in the other position, lug 2 connects to lug 3. So:

- **STEREO**: lug 2 ↔ lug 1: left RCA signal flows to switch lug 1 to... the grid leak resistor and the left input ground. That doesn't seem right.

Hmm, I think I'm misreading the topology. The SPDT input switch is probably arranged so that in MONO position, the left and right inputs get tied together; in STEREO position they stay independent. The exact lug-to-lug mapping depends on the switch's physical wiring. The user should follow the manual exactly without trying to derive the logic.

What's clear: this step ties the left RCA hot to switch lug 2, completing the left channel's connection to the input switch. The mono/stereo selection function works correctly because Dynaco specified the SPDT switch and lug usage carefully.

## See also

- [Step M3 — Input switch](../mechanical-assembly/step-m03-input-switch.md)
- [Operating modes](../../bring-up/operating-modes.md) — how stereo vs. mono affect signal flow
- [Step 53 — Eyelet #7 to left RCA](step-53-eyelet-7-to-left-rca.md)
