---
title: 'Step 18: 5" jumper from lug 1 to lug 6'
---

# Step 18: 5" wire from 7-lug lug 1 to lug 6

> *Connect one end of a 5" wire to lug #1 of the 7 lug strip. Connect the other end to lug #6.* — manual page 7

## What you're doing physically

A 5" piece of hookup wire (stripped ¼" at each end). One end at lug 1 of the seven-lug terminal strip, the other end at lug 6. Neither end is soldered at this step — both lugs will receive more components before final soldering.

## What this builds

This jumper electrically connects lugs 1 and 6 of the seven-lug strip. After [step 23](step-23-bias-ground.md) wires lug 6 to chassis ground, this jumper means lug 1 is ALSO at chassis ground — important because the next several steps land bias-network components on lug 1 expecting it to be the ground side of those components.

Effectively this step creates an extension of the "ground" node from lug 6 to lug 1, even though they're physically separated on the strip.

## See also

- [Step 23 — Bias ground to chassis](step-23-bias-ground.md) — completes the ground path
- [Seven-lug terminal strip](../../components/seven-lug-terminal-strip.md) — the strip layout
