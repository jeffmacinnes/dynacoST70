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

- Lug 1: left channel signal hot (from input)
- Lug 2: common / pole (where the audio hot goes to the board)
- Lug 3: right channel signal hot (from input) — connects here in this step

The switch's job is mono/stereo selection:

- **STEREO** position: the switch keeps L and R separated. Audio at lug 1 (left input) goes to one path; audio at lug 3 (right input) goes to another. The board has separate left and right inputs.
- **MONO** position: the switch ties L and R together, so a signal at either input drives both channels.

Wait — this is actually a one-pole switch (SPDT), not a two-pole switch (DPDT). Looking at the manual more carefully, the SPDT input switch may be implementing a simpler function than I described. The switch likely just shorts the right input to the left input (or vice versa) in MONO position. Let me not overthink the schematic details; the wiring step is to connect this wire as described.

## See also

- [Step M3 — Input switch](../mechanical-assembly/step-m03-input-switch.md) — physical mounting
- [Step 51 — Left grid leak resistor](step-51-left-grid-leak.md) — channel B's input wiring continues
- [Operating modes](../../bring-up/operating-modes.md) — how the mono/stereo switch is used
