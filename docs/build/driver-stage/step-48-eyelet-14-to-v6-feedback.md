---
title: 'Step 48: Eyelet #14 to V6 pin 4 (feedback path)'
---

# Step 48: 5½" wire from eyelet #14 (S) to V6 pin 4 (S)

> *Connect one end of a 5 ½" wire to eyelet #14 (S), and connect the other end to pin #4 of V6 (S).* — manual page 9

## What you're doing physically

A 5½" wire from PC-3 eyelet #14 to V6 pin 4. Both ends soldered.

V6 pin 4 now has: the GREEN UL screen tap (from OPT primary, step 14) + this wire. Soldered final.

## What this is — the feedback wire

This is part of the **right channel's feedback network**. The main global negative feedback loop runs from the OPT's 16 Ω secondary tap → rear strip lug 1 → eyelet #13 → 1 kΩ → the 6GH8A pentode cathode (wired in [step 62](step-62-right-strip-1-to-eyelet-13.md)). The feedback voltage at the pentode cathode opposes the input signal → net gain drops, but distortion drops with it.

This wire is the **high-frequency compensation leg** of that network: it takes the signal at V6 pin 4 (the GREEN UL screen tap of the right A-470) back to eyelet #14, where a 390 pF capacitor couples it into the feedback node. That small cap adds extra feedback at high frequencies, stabilizing the loop against phase shift in the output transformer.

This is **global negative feedback** — see [feedback](../../theory/feedback.md) for the full theory.

## Lead routing matters

The manual notes (step 58 — the channel B equivalent): *"It is important to keep this wire close to the chassis and carried around the printed circuit board as shown in the pictorial."*

The feedback wire carries low-level audio with feedback content — it's sensitive to inductive pickup from nearby AC signals (heaters, power transformer). Route it close to the chassis to minimise its loop area and use the chassis as a partial shield.

## See also

- [Step 58 — V3 to eyelet #11 (channel B feedback)](step-58-v3-to-eyelet-11-feedback.md) — the mirror
- [Feedback](../../theory/feedback.md) — what this wire is doing electrically
- [Step 14 — Right OPT primary](../output-stage/step-14-right-opt-primary.md) — where the UL tap is initially landed
