---
title: 'Step 49: Input switch lug 3 to right RCA long lug'
---

# Step 49: 2" wire from input switch lug 3 (S) to right RCA "long" lug

> *Connect a 2" wire from lug #3 of the input switch (S) to the (long) lug of the right input socket.* — manual page 9

## What you're doing physically

A 2" wire from lug 3 of the SPDT slide switch (from [M3](../mechanical-assembly/step-m03-input-switch.md)) to the **long lug** of the right RCA input socket. The switch end is soldered (S); the RCA end stays unsoldered for [step 52](step-52-eyelet-17-to-right-rca.md).

The "long lug" of an RCA socket is the **center pin** = signal hot (the audio source's positive output).

## What this builds

The SPDT mono/stereo switch has three lugs:

- Lug 1: the unused throw (open in STEREO)
- Lug 2: pole — the left channel signal hot (wired from the left RCA in [step 54](step-54-left-rca-to-input-switch.md))
- Lug 3: right channel signal hot — connects to the right RCA in this step

The switch's job is mono/stereo selection:

It's a single-pole (SPDT) switch, so the mono/stereo function is simple:

- **STEREO** position: the pole (lug 2, the left input hot) is left independent of lug 3, so the left and right inputs stay separate.
- **MONO** position: the pole connects lug 2 to lug 3, shorting the left and right input hots together so one source drives both channels.

## See also

- [Step M3 — Input switch](../mechanical-assembly/step-m03-input-switch.md) — physical mounting
- [Step 51 — Left grid leak resistor](step-51-left-grid-leak.md) — channel B's input wiring continues
- [Operating modes](../../bring-up/operating-modes.md) — how the mono/stereo switch is used
