---
title: 'Step 58: V3 pin 4 to eyelet #11 (channel B feedback)'
---

# Step 58: 8" wire from V3 pin 4 (S) to eyelet #11 (S)

> *Connect one end of an 8" wire to pin #4 of V3 (S). Connect the other end to eyelet #11 (S). It is important to keep this wire close to the chassis and carried around the printed circuit board as shown in the pictorial.* — manual page 10

## What you're doing physically

An 8" wire from V3 pin 4 to PC-3 eyelet #11. Both ends soldered.

V3 pin 4 now has: the GREEN UL screen tap (from step 13) + this wire. Soldered final.

**Route this wire close to the chassis**, around the PC-3 board following the pictorial. This is the feedback wire — sensitive to inductive pickup. Routing close to the chassis uses the chassis as a partial magnetic shield and minimises loop area.

## What this is

The **channel B feedback path**. Mirror of [step 48](step-48-eyelet-14-to-v6-feedback.md).

Eyelet #11 is the channel B feedback return point on the PC-3 board. This wire delivers a sample of the OPT primary signal (from V3's UL screen tap, which is electrically the GREEN lead of the **left** A-470 primary — V3 is a left-channel tube) back to the input stage, where it provides the high-frequency compensation leg of the feedback network through a 390 pF cap.

The feedback reduces gain in the input stage by ~20 dB (about a factor of 10), at the cost of less distortion and tighter frequency response. See [feedback](../../theory/feedback.md) for the full picture.

## Lead routing

The manual is explicit: keep this wire close to the chassis and route it around the PC-3 board. The reason:

- Feedback wires carry low-level audio. The signal level here is comparable to the input audio (~10s of millivolts).
- Nearby high-current AC wires (heaters, PA-060 primary, OPT primaries) radiate magnetic fields.
- A feedback wire that loops away from the chassis exposes itself to that radiation — and any AC pickup gets fed BACK into the input stage as noise (hum, buzz, sometimes oscillation).
- Chassis-hugging keeps the feedback wire's loop area small and uses the chassis as a partial shield against external fields.

Sloppy routing of feedback wires is a common cause of inexplicable hum in tube amps. Get this one right.

## See also

- [Step 48 — Channel A feedback](step-48-eyelet-14-to-v6-feedback.md) — the mirror
- [Feedback](../../theory/feedback.md) — what the wire is doing electrically
- [Grounding and hum](../../theory/grounding-and-hum.md) — why routing matters
