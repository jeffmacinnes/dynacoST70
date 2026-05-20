---
title: 'Step 59: Eyelet #9 to main ground lug'
---

# Step 59: 5" wire from eyelet #9 (S) to solder lug near filter cap

> *Connect one end of a 5" wire to eyelet #9 (S). Connect the other end to solder lug near filter capacitor.* — manual page 10

## What you're doing physically

A 5" wire from PC-3 eyelet #9 to the **main ground solder lug** near the filter capacitor (from [M15](../mechanical-assembly/step-m15-ground-lugs.md)). The eyelet end is soldered (S); the ground-lug end is NOT yet — more wires arrive in steps 61, 63, 64 before final soldering.

## What this completes

Eyelet #9 is the **signal ground reference for the entire PC-3 board**. All on-board signal grounds (the 6GH8A cathode returns, the coupling cap negative ends, the input grid leak returns, etc.) tie together at this eyelet internally on the board.

This wire connects that whole signal-ground network to the **star ground** at the filter cap. After step 59:

- Board signal ground = main ground lug = chassis = star ground point.

Combined with [step 44](step-44-input-grounds-to-board.md) (RCA shields → board input pads → board signal ground) and the other ground-bearing wires (heater CTs to lug 5/7 of seven-lug strip → step 23 wire → star ground), the entire amp's signal ground is concentrated at one chassis point.

This is the moment the **star-ground architecture** is electrically realised. See [grounding and hum](../../theory/grounding-and-hum.md).

## See also

- [Step M15 — Main ground lug](../mechanical-assembly/step-m15-ground-lugs.md)
- [Step 23 — Bias network ground](../output-stage/step-23-bias-ground.md) — another ray of the star
- [Step 64 — Star ground completion](step-64-star-ground-completion.md) — where this lug finally gets soldered
- [Grounding and hum](../../theory/grounding-and-hum.md)
