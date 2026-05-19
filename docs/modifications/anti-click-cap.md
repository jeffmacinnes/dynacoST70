---
title: Anti-click cap
---

# Anti-click capacitor

*Page to be written.* Planned coverage:

- The stock ST-70 produces a loud "click" (sometimes a damaging *pop*) through the speakers when you turn it off. Sometimes a smaller click on turn-on.
- The cause: the power switch is a simple mechanical contact in series with the primary. When the contacts open with current flowing, an inductive kickback transient appears across the contacts (and capacitively couples into the audio circuit).
- The fix: a small RC snubber across the switch contacts. Typical values: 0.01μF cap in series with 100Ω resistor.
- How the snubber works: the cap absorbs the inductive kick, the resistor limits the inrush current when the switch closes (avoiding contact bounce damage).
- Voltage rating: the cap needs to handle line voltage continuously plus inductive transients — minimum 600V (X-class safety cap recommended).
- Where it lands physically: across the switch terminals, near the [primary fuse & switch wiring](../build/power-supply/step-10-primary-fuse-switch.md).
- Safety class: this cap sits across the mains. Use a properly-rated X1 or X2 class safety capacitor, not a generic film cap.

## See also

- [Step 10 — Primary fuse & switch](../build/power-supply/step-10-primary-fuse-switch.md) — where this mod gets installed
