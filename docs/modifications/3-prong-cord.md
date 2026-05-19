---
title: 3-prong cord
---

# 3-prong grounded power cord

The original 1959 ST-70 shipped with a **2-prong unpolarized** power cord. By 1959 standards this was acceptable; by modern safety standards it isn't. A failure between the primary winding and the chassis would leave the chassis at line voltage with no safety path to trip the breaker.

The fix is a 3-prong cord (or an IEC inlet plus detachable cord) where the third pin — earth — bonds to the amp's chassis at a single dedicated point.

## What the third wire does

In a 3-prong outlet:

- **Hot** (black) — carries current to the load.
- **Neutral** (white) — carries current back, nominally at 0 V relative to earth.
- **Earth** (green or bare) — connected to the building's grounding electrode. Carries *no current* in normal operation. Its job is to provide a low-resistance path for *fault* current.

In the amp:

- Hot and neutral go through the **fuse** and the **power switch** (see [step 10](../build/power-supply/step-10-primary-fuse-switch.md)) and then to the PA-060 primary.
- Earth bonds directly to the **chassis** at one dedicated bolt.

The reason this matters: if any primary-side wire ever shorts to chassis (insulation failure, cracked solder joint touching metal, etc.), without earth bonding the entire chassis floats up to line voltage. With earth bonding, the fault current goes earth → breaker → trips. Safe.

## The single-bolt rule

The earth wire should connect to **exactly one** chassis bolt, dedicated to that purpose. Reasons:

- A loose ground introduces a non-deterministic fault path. One firm dedicated bolt is far more reliable than several "also kind of grounded" connections.
- The single point should be electrically separate from the [audio star ground](../theory/grounding-and-hum.md) — earth carries fault current (potentially very high transients), and tying it to your low-level audio ground creates a hum loop.

In practice: pick a bolt that doesn't already do anything else (sometimes a tab is added specifically for this), strip the green wire, ring-terminal it, bolt it down with a star washer for bite, and don't loop any other ground onto that bolt.

## IEC inlet vs. fixed cord

Two implementation styles:

**Fixed 3-prong cord.** Replace the original cord with a modern 18 AWG SJT cord with molded plug. Simpler, fewer parts, cheaper. The downside is the cord is permanently attached — if it gets damaged you're replacing the whole thing.

**IEC inlet + detachable cord.** Cut a rectangular hole in the chassis and mount an IEC C13/C14 socket. Use a standard kettle-style cord. More work to install, but the cord becomes a consumable that's easy to swap (or upgrade — some people enjoy fancy aftermarket cords).

For a build that's going to live on a shelf and rarely move, the fixed cord is fine. For something that travels or shares cords with other gear, IEC is nicer.

## Polarized vs. earthed — they're not the same

A "polarized" 2-prong cord (one blade wider than the other) ensures that hot and neutral don't get swapped — that's a small safety win, but it does **not** earth the chassis. It's strictly inferior to a 3-prong cord.

If you're tempted to leave the original 2-prong cord because it "looks period-correct" — don't. The safety risk is real, and a tasteful 3-prong IEC + cloth-covered cord can keep the vintage aesthetic.

## Wire gauge and current rating

The ST-70 draws about 1 A from the mains at full operation. 18 AWG cord is more than adequate. Don't overthink this — the original wire was probably 20 AWG.

## Testing the install

After installing the 3-prong cord but *before* powering the amp up:

1. **Continuity** between the third pin of the plug and any chassis bolt → should beep continuously (resistance < 1 Ω).
2. **No continuity** between the third pin and either of the other two pins.
3. **No continuity** between the chassis and either hot or neutral (with the switch off).
4. With the switch on, **no continuity** between the chassis and hot or neutral *through the primary winding* either — the transformer's primary should be galvanically isolated from the chassis.

If step 1 fails: the earth bond isn't actually bonding. Tighten the bolt, check the ring terminal. If steps 2–4 fail: stop and figure out where the unintended path is before powering up.

## See also

- [Step 10 — Primary fuse & switch](../build/power-supply/step-10-primary-fuse-switch.md) — where the primary side of the mains is wired
- [Grounding and hum](../theory/grounding-and-hum.md) — why the safety earth must NOT be tied to the audio star ground
- [Anti-click capacitor mod](anti-click-cap.md) — the other primary-side modification
