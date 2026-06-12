---
title: 'Step 54: Left RCA long lug to input switch lug 2'
---

# Step 54: Short link from left RCA long lug (S) to input switch lug 2

> *Connect a short link of wire from the left input socket (long) lug (S) to lug #2 of the input switch.* — manual page 9

## What you're doing physically

A short wire (length whatever fits cleanly — typically 1-2") from the left RCA long lug to **lug 2** of the input switch. The RCA end is soldered final at this step — it now has the wire from step 53 + this wire. The switch end (lug 2) is NOT soldered yet — input switch lug 2 is the **pole/common** and receives more connections in mono operation.

## What this connects

This wire ties the left RCA hot to switch lug 2 — the **pole** of the SPDT mono/stereo switch. It's the mirror of [step 49](step-49-input-switch-to-right-rca.md), which wired the right RCA hot to lug 3:

- **STEREO** position: the pole (lug 2, left input hot) is not connected to lug 3, so the left and right inputs stay independent.
- **MONO** position: the pole connects lug 2 to lug 3, shorting the left and right input hots together so one source drives both channels.

This step completes the left channel's connection to the input switch.

## See also

- [Step M3 — Input switch](../mechanical-assembly/step-m03-input-switch.md)
- [Operating modes](../../bring-up/operating-modes.md) — how stereo vs. mono affect signal flow
- [Step 53 — Eyelet #7 to left RCA](step-53-eyelet-7-to-left-rca.md)
