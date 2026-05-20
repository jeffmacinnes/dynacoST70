---
title: Silicon diode (historical context)
---

# Silicon diode for the bias supply — historical context

**This isn't actually a modification anymore — modern DynakitParts kits ship with a silicon diode as a stock component** (part #544042 in the manual's parts list, installed in mechanical-assembly step 6). This page exists for historical context: explaining what the *original* 1959 ST-70 used and why the modern kit changed.

If you're building from a modern DynakitParts kit, you already have the silicon diode. Nothing to do.

## What the original 1959 kit used

The original ST-70 used a **selenium rectifier** for the bias supply. Selenium rectifiers were the standard rectifying element in the late 1950s — they predate cheap silicon diodes. A selenium "stack" is a series of thin selenium-coated metal plates pressed together; current flows through it one way only, like any diode.

## Why every modern build replaces it (or has it replaced already)

Two reasons:

1. **Reliability** — old selenium rectifiers slowly increase in forward voltage drop as the selenium layer degrades. The bias supply drifts over time. Eventually they fail open.
2. **Safety** — when selenium fails catastrophically (overload, near-end-of-life), it can release **toxic selenium oxide fumes**. Modern silicon diodes have no such failure mode; they just go open or shorted with no smoke.

The 1N4007 is the universally-chosen modern replacement: 1000V PIV, 1A continuous, ~$0.10, sized exactly right for the bias supply's load. DynakitParts ships its current kits with a 1N4007-class diode pre-supplied; the part number in the parts list is `544042`.

## The voltage-drop side effect

Silicon has a lower forward voltage drop than selenium (~0.7V vs. ~1.5V). Modern kits compensate for this in the surrounding circuit values. If you're restoring a *vintage* ST-70 by replacing the original selenium with a 1N4007, your bias supply will produce a slightly higher (more negative) voltage, and you may need a small series dropping resistor to bring it back to the original target. For builders working from a modern kit, the math already works out — nothing to adjust.

## When you'd actually do this as a mod

The only real "modification" use case today: you have a 1960s-era ST-70 with an original selenium rectifier still in place. In that case:

1. Cut the selenium stack out at its leads.
2. Solder a 1N4007 in its place, banded end where the cathode of the selenium was.
3. Power up, verify bias supply voltage at the diode's banded end is sensibly negative (-50 to -70VDC range).
4. Re-bias the output tubes.

For a new build from a modern kit, this is already done — you literally cannot tell the difference because the kit never had a selenium rectifier in the first place.

## See also

- [1N4007 diode component page](../components/1n4007-diode.md) — specs, failure modes, banding
- [Step 1 — Bias diode](../build/power-supply/step-01-bias-diode.md) — the wiring step where the diode goes in
- [Individual bias pots](individual-bias-pots.md) — what consumes the bias supply
