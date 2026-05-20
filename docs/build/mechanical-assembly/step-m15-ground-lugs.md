---
title: M15 — Main ground solder lug(s)
---

# M15: Mount the main ground solder lug(s)

> *Mount two solder lugs with a #4 screw and the nut next to the quad filter capacitor. This is the main ground point of the entire amplifier and should be tightened securely with the two lugs pointing as shown in the pictorial.* — manual page 5

!!! note "Marginalia from this build"
    *"Only 1 lug."* — handwritten in the manual. Your kit may ship with only **one** solder lug instead of two. The wiring works the same way; you just have one anchor point at this position instead of two. The original manual assumed two; the modern kit sometimes provides one.

## What you're doing physically

A **solder lug** is a small flat metal tab with a hole at one end (for a #4 screw) and a hole or slot at the other end (for soldering wires to). The lug provides a permanent solder anchor that's electrically bonded to whatever the screw goes into.

Procedure:

1. Take a #4 machine screw.
2. Pass it through the solder lug's screw-hole.
3. Pass it through a chassis hole next to the quad filter capacitor (from [M14](step-m14-filter-cap.md)).
4. From the underside of the chassis, screw on a #4 nut.
5. Tighten **firmly** — this connection carries all signal ground current, and a loose lug here = hum and crackle.

If you have two lugs, both share the same screw and both lugs are clamped between the chassis and the nut. They can point in different directions to make wiring reach different destinations.

## Why this is THE main ground point

The ST-70 uses a **star ground** topology — all the signal-ground connections converge at ONE physical point on the chassis. That point is this solder lug.

Why one point? Because if you have multiple chassis-to-signal-ground connections, current flowing through the chassis between them creates voltage differences (since the chassis has some resistance). Those voltage differences appear as **ground-loop hum** in the audio. One ground point eliminates the loop entirely.

What lands here:

- The signal ground from the seven-lug terminal strip ([M12](step-m12-seven-lug-strip.md))
- The HV center tap (RED/YEL lead from PA-060)
- The PC-3 board's signal ground
- Possibly the input RCA shields' ground path

All of these tie together at this one lug.

## Why right next to the filter cap

The filter cap is the source of the biggest current flow in the amp — large pulses of charging current flow from the rectifier into the cap, and the cap's return current flows through ground. Putting the main ground lug RIGHT NEXT to the filter cap minimizes the loop area for this high-current path.

Also: the filter cap can itself is grounded (the can is the shared negative terminal of all four sections). Adjacent grounding via the solder lug provides a low-impedance bond between the can and the rest of the signal-ground network.

## Why #4 hardware here (not #6 or #8)

Tradeoff. The lug + screw needs to:

- Be small enough to fit in a tight area next to the filter cap.
- Be large enough to clamp multiple wires.
- Carry significant current (the rectifier ground-return path can have peaks of several amperes).

#4 is the smallest size that still handles this current with reasonable safety margin. It's also the most common screw size in the rest of the chassis — keeps the parts inventory simple.

## Tightening matters

This is the one connection in the entire amp where a loose joint is most likely to cause audible problems. Use:

- A flat screwdriver fitting the screw head snugly (no slipping).
- Firm hand pressure — not maximum torque (you can deform the chassis), but well past "snug."
- Optional: a drop of nail polish or thread-locker on the threads to prevent slow loosening over decades.

If the amp develops mysterious hum years from now, the FIRST place to check is this connection — has it loosened?

## See also

- [Grounding and hum](../../theory/grounding-and-hum.md) — the star-ground topology explained
- [Step 7 — HV CT](../power-supply/step-07-hv-ct.md) — first wiring that uses this lug (the RED/YEL center tap lands here)
- [Filter capacitors](../../components/filter-capacitors.md) — the cap right next to this lug
