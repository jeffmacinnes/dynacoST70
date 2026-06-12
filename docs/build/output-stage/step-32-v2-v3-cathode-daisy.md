---
title: 'Step 32: V2 ↔ V3 cathode daisy'
---

# Step 32: 5" wire daisy through V2 pin 1, V2 pin 8 (S), V3 pin 8 (S), V3 pin 1

> *Strip both ends of a 5" wire ½", Feed one end through pin #1 of V2 (S) and connect it to pin #8 of V2 (S). Feed the other end through pin #8 of V3 (S) and connect to pin #1 of V3.* — manual page 8

## What you're doing physically

This is a single 5" wire making multiple connections, threaded through tube socket pins. Strip ½" off each end of the wire (longer than usual — ¼" isn't enough for what this needs to do).

The wire path:

1. One stripped end **goes through V2 pin 1** (insert through the eyelet hole, but the wire continues past).
2. Then **lands on V2 pin 8** (where it terminates and gets soldered).
3. The OTHER stripped end **goes through V3 pin 8** (same threading-through trick).
4. **Lands on V3 pin 1** (and stays there — V3 pin 1 is NOT soldered yet in this step).

By threading the wire's stripped end through pin 1 on its way to pin 8, you electrically connect both pin 1 and pin 8 to the wire — without needing a second wire.

All four pin connections are now electrically tied together: V2 pin 1, V2 pin 8, V3 pin 1, V3 pin 8.

## Why all four pins together

On the EL-34, pin 8 is the **cathode** and pin 1 is the **suppressor grid (g3)** — they are NOT internally tied. The suppressor needs to sit at cathode potential for the tube to work properly, and this daisy wire is what makes that connection: by threading through pin 1 on the way to pin 8, the wire straps g3 to the cathode externally. That's the whole reason the manual has you thread pin 1 rather than going straight to pin 8.

By daisy-chaining V2 and V3 through this single wire, the two tubes' cathodes are tied together. Combined with the 15.6 Ω from step 31 (also at V2 pin 8 = same node), both V2 and V3 cathodes return to chassis through the SAME 15.6 Ω resistor.

That's the stock-bias setup: one resistor measures combined cathode current of the channel B pair.

## Solder discipline

Pins V2 pin 8 and V3 pin 8 are both soldered (S) at this step:

- V2 pin 8 has the 15.6 Ω from step 31 + this wire — all soldered.
- V3 pin 8 has this wire only — soldered.

V2 pin 1 is soldered too (the wire passes through it; you solder it at this point).

V3 pin 1 is NOT soldered yet — the **Biaset socket wire** lands there in [step 33](step-33-v3-to-left-biaset.md).

## See also

- [Step 31 — V2 cathode sense](step-31-v2-cathode-sense.md) — the 15.6 Ω that this network feeds into
- [Step 33 — V3 to left Biaset](step-33-v3-to-left-biaset.md) — what V3 pin 1 will connect to next
- [EL34 output tube](../../components/el34-output-tube.md) — pinout showing pin 1 ↔ pin 8 ↔ cathode
