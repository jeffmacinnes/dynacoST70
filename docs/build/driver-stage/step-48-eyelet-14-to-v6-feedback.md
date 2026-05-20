---
title: 'Step 48: Eyelet #14 to V6 pin 4 (feedback path)'
---

# Step 48: 5½" wire from eyelet #14 (S) to V6 pin 4 (S)

> *Connect one end of a 5 ½" wire to eyelet #14 (S), and connect the other end to pin #4 of V6 (S).* — manual page 9

## What you're doing physically

A 5½" wire from PC-3 eyelet #14 to V6 pin 4. Both ends soldered.

V6 pin 4 now has: the GREEN UL screen tap (from OPT primary, step 14) + this wire. Soldered final.

## What this is — the feedback wire

This is the **channel A feedback path**. Eyelet #14 is the on-board landing point for the global negative feedback signal coming back from the OPT.

Tracing the feedback loop for channel A:

1. Audio signal at the EL-34 plates (V6 + V7) → through OPT primary → induces voltage in the OPT secondary.
2. The secondary's 16 Ω tap (or sometimes the BLU/WHT and GRN/WHT UL primary points themselves) provides a sample of the output.
3. This wire takes that sample (from V6 pin 4 = GREEN UL tap) and brings it back to eyelet #14 on the PC-3 board.
4. On the board, eyelet #14 routes through a resistor + capacitor network to the **6GH8A pentode cathode** (the input stage).
5. The feedback voltage at the pentode cathode opposes the input signal's effect on the same cathode → net gain is reduced, but distortion is also reduced.

This is **global negative feedback** — see [feedback](../../theory/feedback.md) for the full theory.

## Why through V6 pin 4 (UL tap) instead of the 16 Ω secondary

The Dynaco design samples feedback at the *UL screen tap* rather than the *speaker secondary*. The UL tap is closer to the EL-34 plate and has a different impedance characteristic — it provides effective feedback without loading the speaker output.

Sampling at the 16 Ω secondary would also work and is more common in some other amp designs (e.g., Williamson topology). Dynaco's choice gives slightly different feedback characteristics — more emphasis on lowering output distortion vs. speaker-impedance-correction.

## Lead routing matters

The manual notes (step 58 — the channel B equivalent): *"It is important to keep this wire close to the chassis and carried around the printed circuit board as shown in the pictorial."*

The feedback wire carries low-level audio with feedback content — it's sensitive to inductive pickup from nearby AC signals (heaters, power transformer). Route it close to the chassis to minimise its loop area and use the chassis as a partial shield.

## See also

- [Step 58 — V3 to eyelet #11 (channel B feedback)](step-58-v3-to-eyelet-11-feedback.md) — the mirror
- [Feedback](../../theory/feedback.md) — what this wire is doing electrically
- [Step 14 — Left OPT primary](../output-stage/step-14-left-opt-primary.md) — where the UL tap is initially landed
