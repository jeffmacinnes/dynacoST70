---
title: 3-prong cord
---

# 3-prong grounded power cord

*Page to be written.* Planned coverage:

- The original ST-70 shipped with a 2-prong unpolarized cord. By modern safety standards this is **inadequate** — there's no chassis-to-earth bond.
- Replace with a 3-prong IEC inlet (or fixed cord) where the earth pin bonds firmly to the chassis at a single dedicated bolt.
- Why a *single* bolt (no daisy-chained chassis grounds): a loose connection in a multi-point earth path defeats the safety guarantee.
- Where the earth pin lands relative to the [seven-lug terminal strip](../components/seven-lug-terminal-strip.md) and the rest of the [grounding architecture](../theory/grounding-and-hum.md).
- IEC inlet vs. fixed cord: IEC is more user-serviceable but adds a chassis cutout; fixed cord is simpler but locks in a specific cord.
- Polarized vs. earthed: a "polarized" 2-prong cord is *not* the same thing. Earth bonding is what matters for safety.
- Testing: AC voltage between chassis and known earth should read 0V, not the "floating ~60V" of an unbonded chassis.

## See also

- [Step 10 — Primary fuse & switch](../build/power-supply/step-10-primary-fuse-switch.md) — where the primary side of the mains lands; the earth pin joins this network.
- [Grounding and hum](../theory/grounding-and-hum.md)
