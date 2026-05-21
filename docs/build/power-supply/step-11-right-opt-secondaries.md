---
title: Step 11 — Right OPT secondaries
---

# Step 11: Right output transformer secondary leads to 4-screw terminal strip

> *Connect the black lead from the right output transformer to lug #4 of the 4 screw terminal strip. Connect the brown lead to lug #3 (S). Connect the orange lead to lug #2 (S). Connect the yellow lead to lug #1.* — manual page 6

## What you're doing physically

The right A-470 output transformer has 4 leads on its secondary side. Each one wires to a specific lug on the right 4-screw terminal strip (the one installed in [M4](../mechanical-assembly/step-m04-rear-terminal-strips.md), mounted on the chassis rear).

| Lead color | Strip lug | Speaker tap | Solder now? |
|---|---|---|---|
| BLACK | Lug 4 | Common (0 Ω reference) | No (S) — feedback wire from [step 63](../driver-stage/step-63-right-strip-4-to-ground.md) joins here |
| BROWN | Lug 3 | 4 Ω | **(S)** — solder now |
| ORANGE | Lug 2 | 8 Ω | **(S)** — solder now |
| YELLOW | Lug 1 | 16 Ω | No (S) — feedback wire from [step 62](../driver-stage/step-62-right-strip-1-to-eyelet-13.md) joins here |

The secondary leads exit the A-470 through the chassis rear hole (per [M13](../mechanical-assembly/step-m13-output-transformers.md) orientation). Route each to its assigned lug, keeping the bundle tidy.

## Why these four leads

The A-470's secondary has multiple impedance taps because speakers come in different impedance ratings:

- **8 Ω**: by far the most common modern speaker rating. Use the ORANGE tap + BLACK common.
- **4 Ω**: some modern speakers and many vintage horn speakers. Use BROWN tap + BLACK common.
- **16 Ω**: classic Klipsch, JBL, some vintage British speakers. Use YELLOW tap + BLACK common.

The amp doesn't "know" which tap your speaker uses — you just connect the speaker leads to the COM lug and the matching impedance tap. The transformer's primary impedance (4300 Ω plate-to-plate, the load the EL-34s see) stays constant regardless of which secondary tap is used; the secondary's turns ratio is what determines the impedance transformation.

## Why some leads are soldered now and others aren't

**BROWN (4 Ω) and ORANGE (8 Ω)** get soldered final at this step because nothing else lands on those lugs. The audio comes out of those taps directly to your speaker wires.

**BLACK (common) and YELLOW (16 Ω)** stay unsoldered because they each get one more wire later:

- **Lug 4 (BLACK)** will receive the speaker-common-to-chassis-ground wire in [step 63](../driver-stage/step-63-right-strip-4-to-ground.md) — this is what ties the speaker's reference to the amp's signal ground.
- **Lug 1 (YELLOW)** will receive the **global negative feedback wire** in [step 62](../driver-stage/step-62-right-strip-1-to-eyelet-13.md), which samples a small portion of the speaker-level signal and feeds it back to the input stage. See [feedback](../../theory/feedback.md).

Don't seal these lugs prematurely — adding the second wire later is much easier with the lug still "open."

## Why the 16 Ω tap (not 8 Ω) for feedback

The 16 Ω tap has the **highest voltage** for a given speaker signal, because it's the highest turns ratio relative to the primary. Higher signal voltage at the feedback sample point = better signal-to-noise ratio in the feedback loop.

Using the 8 Ω tap would also work but the feedback signal would be smaller and slightly more susceptible to ambient noise. Dynaco's choice of the 16 Ω tap for feedback is one of those "small details that add up" design decisions that contribute to the ST-70's low noise floor.

## Why only the right OPT at this step

The manual splits the OPT secondary wiring across two steps: this one (right OPT) and [step 12](../output-stage/step-12-left-opt-secondaries.md) (left OPT, on manual page 7). Doing them in two steps lets the manual cleanly transition to page 7 — where it picks up the **output stage** wiring (OPT primaries, bias network, etc.).

This is the **last wiring step on manual page 6**. Once it's done, the power supply phase is complete and you move on to the output stage.

## See also

- [A-470 output transformer](../../components/a-470-output-transformer.md) — full secondary lead spec
- [Step M4 — Rear terminal strips](../mechanical-assembly/step-m04-rear-terminal-strips.md) — where the strips got mounted
- [Step M13 — OPT mounting](../mechanical-assembly/step-m13-output-transformers.md) — how the leads exit through the rear hole
- [Step 12 — Left OPT secondaries](../output-stage/step-12-left-opt-secondaries.md) — the mirror, on manual page 7
- [Step 62 — Right strip 1 to eyelet 13](../driver-stage/step-62-right-strip-1-to-eyelet-13.md) — where the YELLOW feedback wire eventually arrives
- [Step 63 — Right strip 4 to ground](../driver-stage/step-63-right-strip-4-to-ground.md) — where the BLACK common gets its ground wire
- [Feedback](../../theory/feedback.md) — what the 16 Ω feedback tap is doing
- [Previous: Step 10](step-10-primary-fuse-switch.md) · [Next: Step 12 — Left OPT secondaries](../output-stage/step-12-left-opt-secondaries.md)
