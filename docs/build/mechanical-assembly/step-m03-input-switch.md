---
title: M3 — Input switch (mono/stereo)
---

# M3: Mount the SPDT slide switch (mono/stereo selector)

> *Mount the SPDT slide switch (with three lugs) next to the input connector with 4/40 hardware.* — manual page 4

## What you're doing physically

The kit includes a small **SPDT** (Single Pole, Double Throw) slide switch with three solder lugs on the bottom. It mounts on the chassis front panel, just next to the dual RCA input from [M2](step-m02-input-connector.md). Two #4-40 screws hold it from the outside; kep nuts secure it from inside.

## What the switch does

This switch selects between **STEREO** and **MONO** modes:

- **STEREO**: the left RCA input feeds the left channel; the right RCA input feeds the right channel. Each channel's signal is independent.
- **MONO**: both channels are tied together at the input, so a signal applied to either RCA jack drives both channels in parallel. Used for the [mono 70-watt mode](../../bring-up/operating-modes.md#monophonic-70-w).

The three lugs:

- **Lug 1**: common (signal-ground side of one channel — left input grounded shield)
- **Lug 2**: pole (input "hot" — switches between left or right when paralleled)
- **Lug 3**: throw (signal-ground side of the other channel — right input grounded shield)

In STEREO position, the switch sees each input on its own ground path. In MONO position, the switch ties the two channels' input paths together.

For day-to-day stereo use, leave this in STEREO and ignore it.

## Why it lives on the front panel

The mono/stereo selector is a user-facing control — you might flip it occasionally when listening to a mono recording or feeding from a mono source. Putting it on the front panel makes it accessible. The other controls (bias pots, fuse) live elsewhere because they're set-once or rarely-touched.

## See also

- [Operating modes](../../bring-up/operating-modes.md) — when you'd use STEREO vs. MONO position
- [Step M2 — Input connector](step-m02-input-connector.md) — the RCA jacks this switch is next to
