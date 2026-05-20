---
title: 'Step 13: Right OPT primary leads to V3 and V2'
---

# Step 13: Wire the right output transformer primary to V3 and V2

> *Twist the blue and green leads from the left output transformer together and connect the green lead to pin #4 of V3. Connect the blue lead to pin #3 of V3 (S). Twist blue-white and green-white together and connect the blue-white lead to pin #3 of V2 (S). Connect the green-white lead to pin #4 of V2 (S).* — manual page 7

!!! note
    The manual says "left output transformer" but means the one wired to V3 and V2 — the convention is that the V3/V2 pair sits on the *right* side of the chassis as you look at it from the back, but the manual's "left" refers to the wiring schematic side. Match the leads to V3 and V2 as shown; the physical chassis side doesn't matter here.

## What you're doing physically

The A-470 primary has 5 leads exiting one end. Four of them wire to the two EL-34s on V3 and V2:

| Lead | Goes to | Function |
|---|---|---|
| BLUE | V3 pin 3 (S) | Plate of V3 |
| GREEN | V3 pin 4 | UL screen tap of V3 |
| BLUE/WHITE | V2 pin 3 (S) | Plate of V2 |
| GREEN/WHITE | V2 pin 4 (S) | UL screen tap of V2 |

The 5th primary lead (RED, center tap) is already wired to filter cap lug 1 in [step 8](../power-supply/step-08-opt-b-plus.md).

## Twist the pairs

Before routing, twist each pair of wires together:

- **BLUE + GREEN** twisted tightly along their length, then routed as a pair to V3.
- **BLUE/WHITE + GREEN/WHITE** twisted tightly, routed as a pair to V2.

Why twist: each twisted pair carries the audio signal for one EL-34 (a plate + its matching UL screen tap). Twisting cancels external magnetic pickup and minimises hum coupling between the two tubes.

## Why the BLU-with-GRN pairing matters

Each EL-34's plate is wired to ONE end of the OPT primary, and its screen tap comes from a point on the SAME end of the primary winding. So BLUE plate must pair with GREEN UL tap (same end of the winding); BLU/WHT plate must pair with GRN/WHT UL tap (other end).

If you cross-wire (e.g., BLUE plate with GREEN/WHITE screen tap), the screen sees the signal from the *opposite* half of the primary — wrong polarity, wrong amplitude. The ultralinear feedback breaks and the amp will likely oscillate or distort badly.

## Pin 4 is NOT soldered yet at V3

Note pin 4 of V3 is **not** soldered on this step (no S after V3 pin 4). The GREEN lead lands there and waits — pin 4 will get more wires in [step 48](../driver-stage/step-48-eyelet-14-to-v6-feedback.md) (the feedback path back to the driver board). Solder when all wires are present.

Pin 4 of V2 IS soldered now (S after V2 pin 4) because it's the only wire landing there.

## See also

- [A-470 output transformer](../../components/a-470-output-transformer.md) — lead colors and primary structure
- [Step 14 — Left OPT primary](step-14-left-opt-primary.md) — mirror of this step for V6/V7
- [EL34 output tube](../../components/el34-output-tube.md) — pin 3 (plate) and pin 4 (screen) function
- [Push-pull topology](../../theory/push-pull-topology.md) — why the primary is wired this way
