---
title: M5 — Bias potentiometers
---

# M5: Mount the two 10,000 ohm potentiometers

> *Mount the two 10,000 ohm potentiometers in the ⅜" holes near the center of the chassis. Locate with the three connecting lugs facing the front of the chassis. Put a ⅜" lockwasher on each shaft, insert from the inside and fasten with a ⅜" nut.* — manual page 5

## What you're doing physically

The kit supplies two **10 kΩ linear-taper potentiometers** for setting the **stock bias**. One per channel.

Insert each pot's threaded shaft from the **inside** of the chassis, through the ⅜" hole near the chassis center, with the three solder lugs facing **forward**. From outside, put on the ⅜" lockwasher and tighten the ⅜" nut.

The shaft typically protrudes about ¼" outside the chassis — long enough to grip with pliers or a screwdriver slot for adjustment.

## How the stock bias circuit uses them

The stock ST-70 has **one 10K pot per channel**, shared between the two EL-34s in that channel:

- The pot's outer lugs connect to a fixed +/- voltage divider (one end to bias supply −65 V, the other end to ground or a higher reference).
- The pot's wiper (center lug) drives BOTH EL-34s' grids in that channel through their respective 1 kΩ grid stoppers.
- Turning the pot moves the wiper, which moves the grid voltage of both tubes together.

This is the **"Dyna Biaset"** arrangement (see [bias adjustment](../../bring-up/bias-adjustment.md)). Both tubes in a channel get the same bias; per-tube adjustment requires the [individual bias pots modification](../../modifications/individual-bias-pots.md).

## Why face the lugs forward

Convenience for wiring. The connecting lugs need to reach:

- The bias 2-lug strip with diode (next step, [M6](step-m06-bias-2lug-strip.md))
- The seven-lug terminal strip (mounted in [M12](step-m12-seven-lug-strip.md))
- Each other (with a short jumper between the two pots' #1 and #3 lugs)

Facing forward keeps these wiring runs short and well-routed. If you mount the pot rotated, the lugs face a wall and the wires have to take a much longer path.

## If you've installed the individual bias pots modification

The mod replaces these two 10K pots with four smaller trimpots — one per EL-34. The mod kit usually comes with new mounting hardware that takes over these mounting holes (often via a small bracket that holds all four trimpots). In that case, you skip the stock-pot installation entirely and follow the mod's instructions.

## See also

- [Bias adjustment](../../bring-up/bias-adjustment.md) — how these pots get used
- [Individual bias pots modification](../../modifications/individual-bias-pots.md) — the per-tube alternative
- [Step M6](step-m06-bias-2lug-strip.md) — the bias diode mounted between the two pots
