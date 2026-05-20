---
title: 'Step 60: Left terminal strip lug 1 to eyelet #12 (feedback origin)'
---

# Step 60: 12" wire from left terminal strip lug 1 (S) to eyelet #12 (S)

> *Connect one end of a 12" wire to lug #1 of the left screw terminal strip (S). Connect the other end to eyelet #12 (S). See pictorial.* — manual page 10

## What you're doing physically

A long 12" wire from lug 1 of the left 4-screw terminal strip (the 16 Ω speaker tap) to PC-3 eyelet #12. Both ends soldered.

Lug 1 of the left strip is now soldered final — it has the YELLOW lead from the left A-470 secondary (step 12) + this wire.

## What this is — the channel B feedback origin

This wire taps the channel B output **at the 16 Ω secondary tap** and feeds it back to the PC-3 board (eyelet #12), where the feedback network applies it to the input stage's cathode.

This is the **other source of feedback** (alongside the UL screen tap from step 58). The Dynaco design uses both:

- **Step 48/58 feedback**: from the OPT primary's UL screen tap → direct feedback to the input stage.
- **This step (and step 62)**: from the OPT secondary's 16 Ω tap → fed through a small resistor + cap (on the board) to the input stage.

Why two feedback paths? The combination provides:

- Better high-frequency stability than either path alone would (the two paths have different phase characteristics that complement each other).
- Better speaker-impedance handling (the secondary tap feedback corrects for varying speaker impedance better than the primary tap feedback).
- More precise control of overall gain and distortion.

This is a subtle aspect of the ST-70 design — most amps use only one feedback path. Dynaco's "doubled" feedback is part of why the ST-70 has measurably better specs than its contemporaries.

## Why a long wire (12")

The left 4-screw terminal strip is on the back of the chassis; the PC-3 board is in the middle. The 12" length covers that distance with some slack for routing around the choke and PA-060.

The wire is at audio level (small voltage), so its length doesn't matter electrically. But like the other feedback wire ([step 58](step-58-v3-to-eyelet-11-feedback.md)), route it close to the chassis to minimise hum pickup.

## See also

- [Step 12 — Left OPT secondary](../output-stage/step-12-left-opt-secondaries.md) — what the YELLOW lead is doing at the same lug
- [Step 62 — Right strip 1 to eyelet #13](step-62-right-strip-1-to-eyelet-13.md) — channel A equivalent
- [Feedback](../../theory/feedback.md)
