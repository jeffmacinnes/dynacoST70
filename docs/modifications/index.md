---
title: Modifications
---

# Modifications

This build incorporates several well-known, widely-recommended modifications to the stock ST-70 design. Each is its own page, covering what changes, what it costs (in parts, time, and reversibility), and why it's worth doing.

- [3-prong grounded power cord](3-prong-cord.md) — safety; chassis-to-mains-earth bonding.
- [1N4007 silicon diode](1n4007-replacement.md) — replaces the original selenium rectifier in the bias supply (already incorporated in [step 1](../build/power-supply/step-01-bias-diode.md)).
- [Rectifier diode mod](rectifier-diode-mod.md) — two 1N4007s in series with the 5AR4 plates to protect the rectifier tube from warm-up failure. Shipped with current DynakitParts kits on a separate sheet; not in the original manual.
- [Anti-click capacitor](anti-click-cap.md) — small RC snubber across the power switch to eliminate the loud pop on power-off.
- [Individual bias pots per output tube](individual-bias-pots.md) — replaces the stock shared bias network with one trimmer per tube.

## Deferred mods (future)

- **VTA driver board upgrade** — replaces the [PC-3A board](../components/pc-3a-driver-board.md) with a modern long-tail-pair phase splitter. Significant performance improvement, but it's a non-trivial change and we want to bring up the stock-style amp first.
