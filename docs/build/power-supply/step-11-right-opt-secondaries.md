---
title: Step 11 — Right OPT secondaries
---

# Step 11: Right output transformer secondary leads to 4-screw terminal strip

> *Connect the black lead from the right output transformer to lug #4 of the 4 screw terminal strip. Connect the brown lead to lug #3 (S). Connect the orange lead to lug #2 (S). Connect the yellow lead to lug #1.*

!!! info "Explainer pending"

*Topics to cover when written:*

- These are the [A-470 secondary leads](../../components/a-470-output-transformer.md) — the speaker output.
- Color decode (per A-470 spec sheet): black = common, brown = 4Ω, orange = 8Ω, yellow = 16Ω.
- Why multiple impedance taps exist (matching different speaker loads).
- Why some are soldered now and some aren't:
  - Lug #4 (black, common) — no (S), awaiting the global feedback wire that lands here from the input stage.
  - Lug #3 (brown, 4Ω) — soldered now.
  - Lug #2 (orange, 8Ω) — soldered now.
  - Lug #1 (yellow, 16Ω) — no (S), awaiting the global feedback wire from this tap.
- The relationship to [feedback](../../theory/feedback.md): the 16Ω tap is where the global feedback loop is sampled from.
- Why this is the *right* OPT only — the left OPT secondaries get wired in a later step on a different page.

## See also

- [A-470 output transformer](../../components/a-470-output-transformer.md)
- [Feedback](../../theory/feedback.md) — what the unsoldered leads are waiting for
- [Previous: Step 10](step-10-primary-fuse-switch.md)
