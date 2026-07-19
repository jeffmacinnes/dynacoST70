---
title: Probes
---

# Probes

The probes that ship with a DMM have their own safety rating, completely independent of the meter. **A CAT III 600V meter with CAT II 300V probes is effectively a CAT II 300V system.** You only get the protection of the weakest link.

## What to check on your DMM probes

Look for printing on the probe handles or cable insulation:

- A CAT rating (CAT II, CAT III, or CAT IV)
- A voltage rating (typically 600V or 1000V)
- A current rating (often 10A)
- Compliance markings (CE, UL, CSA)

Ideally: **CAT III 1000V** or at minimum **CAT III 600V**, matching or exceeding the [meter](multimeter.md).

## Physical features that matter

**Tip exposure.** Modern safety-rated probes have finger guards (a plastic flange between your hand and the metal tip) and only a short length of exposed metal — typically 2–4mm, sometimes with retractable shrouds. Older or cheap probes often have 19mm+ of exposed tip, which makes it much easier to slip and short two adjacent points together.

On a tube amp with 450V B+ and closely-spaced terminal lugs, a long exposed tip is a real hazard. Slip the probe sideways and you can short B+ to ground or to another circuit node, with explosive results — [filter caps](../components/filter-capacitors.md) can rupture, and arc flash can cause flash burns or eye damage.

**Cable condition.** Check for cracks, nicks, or hardened/brittle insulation. Tube amp work involves moving probes around live circuits; a compromised cable is a shock or short waiting to happen.

**Plug shrouds.** The banana plugs that go into the meter should have plastic shrouds covering the metal — exposed banana plug shafts can let you contact a live conductor while plugging in.

## Useful upgrades

**Probes with retractable tip shrouds** that expose only 2mm of tip when pressed against a contact, and retract to fully covered when removed. ~$25–40 from Pomona, Fluke, or similar quality manufacturers.

**Alligator clip leads** are extremely useful for tube amp work — clip the black lead to chassis ground with an alligator clip, then you only need one hand on the live probe ([one-hand rule](high-voltage-safety.md#one-hand-rule)). Some kits include these as accessories; if not, they're cheap (~$10–20).

**Probe replacement.** If your stock probes are unrated or low-rated, replacement CAT III 1000V silicone-insulated probes are $15–30 from Pomona or Fluke (their TL75 or TL175 lines are popular). For tube amp work, this is genuinely worth doing before bias-up.

## When this matters

For wiring with the amp powered off (most of the build), probe ratings are less critical because there's no live voltage. They become important when you start doing [voltage checks](../bring-up/voltage-checks.md) and [bias adjustment](../bring-up/bias-adjustment.md). Address probe upgrades before bias-up, not before.

## Scope probes vs. DMM probes

These are completely different and not interchangeable:

| Feature | DMM Probe | Scope Probe |
|---|---|---|
| Connector | Banana plugs | BNC |
| Cable | Simple two-wire | Coaxial with controlled impedance |
| Frequency response | DC to ~kHz | DC to MHz/GHz |
| Internal circuitry | None | Compensation network in probe head |
| Attenuation | None (1×) | Typically 10× or 100× |

DMM probes on a scope: you'd lose all high-frequency content and the probe would load the circuit unpredictably. Scope probes on a DMM: connectors don't even fit, and the BNC ground shell isn't what a DMM expects.

### What 10× means

A 10× passive probe has a built-in voltage divider that attenuates the signal by 10 before it reaches the scope. So 100V at the probe tip becomes 10V at the scope input. Reasons:

1. **Protecting the scope input** — the scope's input is typically rated for ~300V max, and the 10× division keeps large signals within it. But note: the attenuation does *not* raise what you can safely put on the probe **tip**. The tip's own rating (typically 300–400V CAT II, derating further with frequency) is the hard limit — see the high-voltage probe section below. For plate-circuit work on a tube amp, use a 100:1 probe.
2. **Lower circuit loading** — a 1× probe presents 1MΩ to the circuit. A 10× probe presents 10MΩ. The higher impedance disturbs the circuit less, which matters when measuring high-impedance nodes (like tube grids).

Tradeoff: you lose vertical resolution (everything's 10× smaller on screen) and the probe has its own bandwidth limit.

### The ground lead is an antenna

The alligator-clip ground lead that ships on a scope probe forms a **loop** with the probe tip, and any AC magnetic field passing through that loop induces a voltage the scope cannot distinguish from real signal. Next to a power transformer, this is not a subtle effect: measured on this ST-70, probing the main B+ rail with a standard ground lead showed **7.6 Vp-p of clean 60 Hz sine** that looked exactly like rectifier trouble — while the rail's true 60 Hz content, verified by FFT and a tight-loop measurement, was under 5 mV. The "signal" was the probe loop picking up the PA-060's field.

Defenses, in order of preference:

1. **Spring ground tip** — the little coiled attachment that replaces the alligator lead and grounds at the probe barrel, shrinking the loop from ~15 cm across to ~1 cm. Pickup drops by orders of magnitude.
2. **FFT mode on the scope** — separates real rail content by frequency, so induced 60 Hz stands apart from genuine 120 Hz ripple.
3. **Sanity-check the loop itself** — touch the probe tip to the same ground the clip is on; anything the scope still shows is pure pickup, and that's your measurement floor.

Rule of thumb: **any sub-volt AC measurement near the power transformer is untrustworthy through a dangling ground clip.** Tighten the loop or use FFT before diagnosing.

### High-voltage scope probes

Standard 10× passive probes are typically rated 300V CAT II or 400V CAT II. **That's not enough headroom for the B+ rail on a tube amp.**

For HV measurements on the ST-70:

- **100× passive probe**, rated 1000–2500V working voltage. ~$50–150 for decent ones (Pomona, Tektronix, quality third-party). Good for general HV work.
- **High-voltage differential probe** lets you measure floating signals (between two non-grounded points). Several hundred dollars and up. Useful for measuring across components rather than just to ground.

For ST-70 work, a 100× probe is the practical choice. It extends what you can safely measure on B+ from "don't touch" to "measure carefully."

## See also

- [Multimeter](multimeter.md) — the meter your DMM probes plug into
- [Oscilloscope](oscilloscope.md) — what scope probes connect to
- [High-voltage safety](high-voltage-safety.md) — why CAT ratings actually matter
