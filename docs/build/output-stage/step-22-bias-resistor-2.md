---
title: 'Step 22: Second 10 kΩ resistor between lugs 2 and 1'
---

# Step 22: 10 kΩ resistor from lug 2 to lug 1 (S)

> *Select another 10,000 ohm resistor and connect one end to lug #2 of the seven lug strip. Connect the other end to lug #1 of the strip (S). Trim and form leads as needed.* — manual page 7

## What you're doing physically

The second 10 kΩ resistor between lug 2 and lug 1 of the seven-lug strip. Trim leads to fit cleanly. The end at lug 1 is **soldered (S)** at this step — lug 1 now has the positive ends of both bias caps + the jumper from step 18 + this resistor. All four connections get soldered together in one joint.

Lug 2 stays unsoldered for now — it'll receive one more wire in [step 26](step-26-bias-pot-distribution-2.md) before final soldering.

## What this resistor + lug 2 do

This 10 kΩ resistor is the **shunt (bottom) leg of the bias-setting voltage divider**: it runs from lug 2 down to ground (lug 1 is tied to ground via the lug-6 jumper). With the divider's other resistances above it, lug 2 settles at roughly −22 V — the least negative node of the divider, and the node that feeds the less negative ends of the bias pots in [step 26](step-26-bias-pot-distribution-2.md). Without this resistor there would be no defined divider bottom, and the pots couldn't set the grid voltage in the right range.

## Why solder lug 1 now (S)

Lug 1 has FOUR things landed on it by this point:

1. The 5" jumper from lug 6 ([step 18](step-18-bias-jumper.md)).
2. The positive end of the first 100 µF cap ([step 19](step-19-bias-cap-1.md)).
3. The positive end of the second 100 µF cap ([step 21](step-21-bias-cap-2.md)).
4. This 10 kΩ resistor's lug-1 end.

All four are present, so solder them together now in one good joint. Hot work — use a higher-wattage iron for a few seconds to get all four wires + the lug itself hot enough that solder flows around everything cleanly.

## See also

- [Step 18 — Bias jumper](step-18-bias-jumper.md) — what else is on lug 1
- [Step 19, 21 — Bias caps](step-19-bias-cap-1.md) — positive ends on lug 1
- [Step 26 — Bias to left pot](step-26-bias-pot-distribution-2.md) — lug 2 gets soldered there
