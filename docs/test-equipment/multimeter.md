---
title: Multimeter (DMM)
---

# Digital Multimeter (DMM)

## The IDEAL 61-327

This build uses the IDEAL 61-327, a CAT III 600V manual-ranging DMM. Key specs:

| Function | Range | Notes |
|---|---|---|
| AC voltage | up to 600V | ±(1.3% + 5) accuracy |
| DC voltage | up to 600V | ±(1.3% + 5) accuracy |
| Resistance | up to 4MΩ | for continuity and component checks |
| Continuity | ✓ | with audible beep |
| Diode test | ✓ | shows forward voltage drop |
| Battery test | ✓ | basic battery check |

Notably absent:

- No current measurement (no amp clamp, no in-line ammeter)
- No capacitance measurement
- No true RMS (averaging only — fine for sine waves, less accurate for distorted waveforms)
- No temperature
- No frequency

## Is the 61-327 adequate for the ST-70?

**Yes, with caveats.**

The amp's main high-voltage rail (B+) runs around 415–445V DC at the first filter caps depending on line voltage and load. That's *under* the 600V meter limit, so technically within spec. But there's only ~150V of headroom. CAT III 600V means the meter is rated to handle voltage transients up to that level on a circuit normally operating below it. Be conservative about probe placement to avoid touching points that might exceed 600V.

## Specific cautions for tube amp work

**Don't measure across both 5AR4 plate pins.** Pin 4 to pin 6 sees the full 720V RMS across the high-voltage secondary — roughly 1,018V at the peaks. That's far above the 600V rating. Always measure each pin to chassis ground separately (around 360V RMS each), never plate-to-plate.

**Be aware of transformer voltage during start-up.** Voltage transients during power-on can briefly exceed steady-state values. Measure with the amp warmed up and stable, not during the first few seconds.

**Use the 600V DC range for B+ measurements.** Don't auto-range or use a lower range — locking the range avoids the brief overrange transient when the meter is figuring out what to do.

## Working around the missing functions

**No current measurement?** Not actually a problem for tube bias work. Bias is set by measuring the DC voltage across each output tube's cathode resistor (often 1Ω or 10Ω) and using Ohm's law: I = V / R. If the cathode resistor is 10Ω and the meter reads 600mV DC across it, the cathode current is 60mA. The 4000mV DC range on the 61-327 is perfect for this. See [bias adjustment](../bring-up/bias-adjustment.md) for the procedure.

**No capacitance?** Annoying for verifying filter caps before installation, but workable. You can do a rough check by measuring the diode drop in continuity mode while the cap charges (a working cap will show climbing resistance; a shorted cap will read 0Ω; an open cap will read OL immediately).

**No true RMS?** Matters mainly for measuring distorted AC waveforms (audio, ripple). For pure 60Hz sine wave from the transformer secondaries, an averaging meter reads accurately. For ripple measurement on the B+ rail, you'll want a [scope](oscilloscope.md) eventually anyway.

## When to consider upgrading

The 61-327 will get you through the build. Reasons you might want a more capable DMM later:

- **Higher CAT rating** for more headroom on high-voltage measurements (the IDEAL 61-337 or 61-347 in the same product line are CAT III 1000V or CAT IV 600V)
- **Capacitance** for filter cap verification
- **True RMS** for measuring distorted waveforms
- **Higher resolution display** — the 61-327's 4000-count display means 1V resolution at the 600V range. A 6000-count or 60000-count meter is more precise
- **Dual display** showing two related quantities (e.g., AC and DC simultaneously)

For the build itself, none of these are required. They become more useful for ongoing diagnostic work after the amp is running.

## See also

- [Probes](probes.md) — your DMM is only as safe as its probes
- [High-voltage safety](high-voltage-safety.md) — what to do (and not do) with the DMM
- [Bias adjustment](../bring-up/bias-adjustment.md) — the main DMM-driven measurement during bring-up
