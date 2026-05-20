---
title: 'Step 65: Power cord installation'
---

# Step 65: Install the power cord

> *Strip back and remove outer jacket of power cord exposing approx. 5" of all (3) insulated wires. Insert power cord from outside through the chassis grommet with the outer cord jacket protruding ½" inside of the chassis. Now, install the cord stop bushing on the cord and position on the ½" extended cord jacket and tighten securely with the provided cable tie. (See pictorial). Now, cut the white lead 3", strip end and connect to (B) lug of fuse holder (S). Cut black wire 4 ½", strip end and connect to lug (2) of on-off switch (S). Mount solder lug to L/H 8/32 extended threaded stud at power transformer. Cut green lead 2 ¾" and connect to solder lug (S). This completes wiring of your amplifier.* — manual page 10

## What you're doing physically

The final step. Install the 3-conductor mains cord through the chassis grommet (from [M7](../mechanical-assembly/step-m07-grommet.md)) and wire each lead to its destination.

**Cord preparation**:

1. Strip back the outer jacket about 5" from the chassis end of the cord. You should now see three insulated wires (BLACK, WHITE, GREEN).
2. Pass the cord through the grommet from outside, with the outer jacket protruding ½" *inside* the chassis (the jacket should fully cover the cord up to the strain-relief location).
3. Install the **cord stop bushing** (the small strain-relief clamp) on the ½" of exposed jacket inside the chassis. Tighten with the supplied cable tie. The cord is now mechanically locked — pulling on it from outside won't disturb the internal wires.

**Wire connections**:

| Cord wire | Cut to | Goes to | Role |
|---|---|---|---|
| WHITE (neutral) | 3" | Fuse holder (B) lug (S) | Mains return |
| BLACK (hot) | 4½" | On-off switch lug 2 (S) | Mains hot (switched) |
| GREEN (earth) | 2¾" | Solder lug at PA-060 left mounting stud (S) | Safety ground / chassis |

For the green earth lead, first **mount a solder lug** under the left-hand 8/32 threaded stud at the power transformer's mounting bolt. Then solder the green lead to that lug. This is the **safety earth path** — see [3-prong cord modification](../../modifications/3-prong-cord.md).

## What's now electrically complete

- **Mains power path**: wall outlet → cord → fuse → switch → PA-060 primary (already wired in [step 10](../power-supply/step-10-primary-fuse-switch.md)).
- **Safety earth**: cord green → chassis at PA-060 mounting stud. Any internal short to chassis trips the wall breaker via earth.
- **Strain relief**: cord can't be yanked out — the bushing clamps the jacket.

This is the moment when the kit becomes a functioning amplifier (electrically). Time for **bring-up** — [pre-power checklist](../../bring-up/pre-power-checklist.md).

## A note on the 2-prong vs 3-prong cord

The 2017 DynakitParts kit ships with a 3-prong cord, so the GREEN earth lead exists. If you're restoring an older ST-70 with a 2-prong cord, the green lead won't exist — and the [3-prong cord modification](../../modifications/3-prong-cord.md) is what adds it. Modern safety practice strongly favors 3-prong even on tube amps.

## Final words from the manual

> *This completes wiring of your amplifier.*

After step 65 you're done with the manual's wiring procedure. The amp is electrically built. Next: visual inspection, continuity checks, and the gradual first power-on procedure.

## See also

- [Step 10 — Primary fuse & switch wiring](../power-supply/step-10-primary-fuse-switch.md) — the mains path upstream of step 65
- [Step M7 — Grommet](../mechanical-assembly/step-m07-grommet.md) — the cord routing hole
- [3-prong cord modification](../../modifications/3-prong-cord.md) — the safety upgrade
- [Pre-power checklist](../../bring-up/pre-power-checklist.md) — what comes next
- [Bring-up](../../bring-up/index.md) — the path from here to working amp
