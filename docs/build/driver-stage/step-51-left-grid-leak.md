---
title: 'Step 51: Left channel grid leak resistor'
---

# Step 51: 470 kΩ resistor at input switch lug 1 and left RCA ground

> *Connect one end of a 470,000 ohm resistor to lug #1 of the input switch (S). Connect the other end to the ground (short) lug of the left input socket (S).* — manual page 9

## What you're doing physically

The second **470 kΩ grid leak resistor**. One end at lug 1 of the input switch (S); other end at the short (ground) lug of the LEFT RCA jack (S). Both ends soldered.

This is slightly different topology from the right channel ([step 50](step-50-right-grid-leak.md)) — the resistor doesn't span the left RCA jack directly; it spans from the input switch over to the left jack's ground.

## What this does

Same function as the right channel's grid leak — provides a DC path from the left channel's signal-hot side to ground.

The reason for the asymmetric topology (switch lug 1 instead of left RCA long lug): in MONO position, the input switch ties L and R together. The grid leak needs to be present in both stereo and mono configurations. By landing the resistor at switch lug 1 (instead of left long lug), the grid leak is **always** present regardless of switch position.

Note that step 50 has the resistor between the RCA jack's two lugs (long and short). That's because the right channel's "input hot" is also the switch lug 3 — the right RCA jack's long lug carries the signal in both stereo and mono modes, so the resistor's location works in both cases.

## See also

- [Step 50 — Right grid leak](step-50-right-grid-leak.md) — the other channel's resistor
- [Step M3 — Input switch](../mechanical-assembly/step-m03-input-switch.md)
