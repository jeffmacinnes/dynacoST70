---
title: 'Step 12: Left OPT secondaries to left 4-screw strip'
---

# Step 12: Repeat step 11 for the left output transformer

> *Repeat Step 11 for the left output transformer and the left screw terminal strip.* — manual page 7

## What you're doing physically

The four secondary leads from the **left** A-470 — BLACK, BROWN, ORANGE, YELLOW — wire to the left 4-screw terminal strip (the one on the LEFT side of the back panel). This is the mirror of [step 11](step-11-right-opt-secondaries.md), which you already did for the right channel.

| Lead | Goes to | Speaker tap |
|---|---|---|
| BLACK | Left strip lug 4 | Speaker common (0 Ω) |
| BROWN | Left strip lug 3 (S) | 4 Ω |
| ORANGE | Left strip lug 2 (S) | 8 Ω |
| YELLOW | Left strip lug 1 | 16 Ω + global feedback origin |

Lug 4 (BLACK common) and lug 1 (YELLOW) are left **unsoldered** at this step — lug 4 gets its ground wire later, and lug 1 stays open until the feedback wire lands in [step 60](../driver-stage/step-60-left-strip-1-to-eyelet-12.md). Don't solder until all wires are in place.

## Why these four leads matter together

The left A-470 secondary has 4 taps in total (excluding common), but only 3 are speaker taps; the 4th is implicit at lug 4 (the common/zero reference). All four leads need to land at this strip for the speaker output to work — pick whichever impedance matches your speakers when you wire them up later.

The YELLOW (16 Ω) lead is also the source of **global negative feedback** for the left channel. That feedback wire taps off here and routes back to the PC-3A driver board.

## See also

- [Step 11 — Right OPT secondaries](step-11-right-opt-secondaries.md) — the mirror image
- [A-470 output transformer](../../components/a-470-output-transformer.md) — secondary lead specs
- [Feedback](../../theory/feedback.md) — what happens with the YELLOW lead later
