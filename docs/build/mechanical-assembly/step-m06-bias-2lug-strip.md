---
title: M6 — Bias 2-lug strip with diode
---

# M6: Mount the small 2-lug terminal strip + bias diode

> *Mount the small 2 lug terminal strip between the (2) potentiometers with 4/40 hardware. Position as shown in pictorial. Connect the diode between each lug with banded end to the left as shown in the pictorial.* — manual page 5

## What you're doing physically

The kit supplies a small **2-lug terminal strip** (about ¾" long, two solder lugs sticking up from a phenolic base) and a **silicon diode** (the 1N4007-class part, #544042 in the parts list).

Mount the strip between the two bias pots from [M5](step-m05-bias-pots.md), using #4-40 hardware. The two lugs should sit between the pots with the diode bridging them.

Solder the diode between the two lugs, with the **banded end (cathode) on the LEFT** per the pictorial diagram. The banded end is where the RED/BLK AC input from the PA-060 will land (step 1); the negative DC output emerges from the non-banded (anode) end.

## What this circuit is

This is the **bias supply rectifier**. It takes the 50 V AC from the PA-060's bias winding (RED/BLK lead) and converts it to filtered DC at about −65 V.

Circuit flow:

1. RED/BLK lead (AC bias winding output, ~50 V AC) comes in to the banded (cathode) end of the diode.
2. The diode rectifies (half-wave) — only the negative half-cycles pass.
3. The non-banded (anode) end of the diode outputs pulsing DC at about −60 to −70 V.
4. From the non-banded end, filtering and dropping resistors smooth this into the −65 V DC the bias network needs.

The 2-lug strip provides anchor points for the diode and the wires landing on either side of it. It also provides physical clearance — the diode hangs in mid-air between two lugs rather than touching anything else.

## Why "banded end to the left"

It's a convention. The banded end matches the schematic symbol's cathode (the line with the bar across the arrow). If you reverse the diode, the rectifier is backwards — it would block the negative half-cycles instead of passing them — and the bias supply would output a positive voltage, which would destroy the EL-34s on first power-on by removing all grid bias.

This is one of the few wiring orientations that has a "you have one chance to get this right" quality. Double-check the band before soldering.

## The diode's role in the modified kit

In the original 1959 kit, this was a selenium rectifier (a small stack of metal plates). Modern kits ship with a silicon diode (1N4007-class) — see [historical context](../../modifications/1n4007-replacement.md) for why. The mounting and wiring is the same; only the part changed.

## See also

- [1N4007 historical context](../../modifications/1n4007-replacement.md) — what changed and when
- [Step 1 — Bias diode wiring](../power-supply/step-01-bias-diode.md) — the first wiring step connects to this diode
- [Bias adjustment](../../bring-up/bias-adjustment.md) — what the −65 V output eventually drives
