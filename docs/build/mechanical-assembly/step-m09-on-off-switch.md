---
title: M9 — On-off switch
---

# M9: Mount the SPST on-off switch

> *Mount the SPST on-off switch (two lugs) on the chassis rear. The connecting lugs should be located as shown in the pictorial diagram. Use 4/40 hardware.* — manual page 5

## What you're doing physically

The kit supplies a **SPST** (Single Pole, Single Throw) toggle switch — a small switch with two solder lugs on the bottom, an ON/OFF lever on top.

Mount it on the rear of the chassis from outside, with the toggle accessible from outside. Two #4-40 screws hold it in place.

Position the two solder lugs per the pictorial — they need to face the fuse post (from [M8](step-m08-fuse-post.md)) and the PA-060 ([M10](step-m10-pa-060.md)) so wires can route cleanly.

## What the switch does

This is the **mains power switch**. It sits in series with the **hot leg** of the mains line (the cord's BLACK wire), interrupting the AC supply when OFF. The fuse sits in the other (neutral) leg.

Position-wise: when the lever is UP, the switch is ON (closed circuit, mains flows). When DOWN, OFF.

Why rear panel? The original Dynaco design assumed the amp would be left ON most of the time (tube amps don't like frequent on/off cycles, and the 1960s norm was leaving HiFi gear powered up). A rear-mounted switch is "set it once" — the user toggles it once a day, not constantly.

Some modern users leave the rear switch ON permanently and control the amp from a preamp's switched AC outlet — which lets you turn everything on/off together from the preamp's front panel.

## Why SPST instead of DPST

A DPST switch would interrupt BOTH hot and neutral. An SPST interrupts only ONE wire — in the ST-70's case, the hot. The neutral leg runs through the fuse and is never bonded to the chassis.

Modern safety practice favors DPST (interrupting both hot and neutral) but the SPST design works fine when:

- The amp uses a polarized 2-prong plug (so the hot wire is always the same).
- Or the amp uses a 3-prong cord with proper earth (so any fault to chassis trips the breaker via earth, not via accidentally-hot neutral).

If you've added the [3-prong cord modification](../../modifications/3-prong-cord.md), the SPST is acceptable — the earth conductor provides the redundant safety path.

## Common mistake: mounting upside-down

The switch has clear "ON" and "OFF" labels on the toggle (or in some kits, just the lever position indicates state). Mount it so "ON" matches the chassis label (or with the lever UP = ON, conventionally). A backwards mount means you have to flip your mental model every time you power on.

## See also

- [Step 10 — Primary fuse and switch wiring](../power-supply/step-10-primary-fuse-switch.md) — the wiring step that uses this switch
- [3-prong cord modification](../../modifications/3-prong-cord.md) — what to know about safety with an SPST switch
- [Anti-click capacitor](../../modifications/anti-click-cap.md) — a small mod that suppresses the click at power-off
