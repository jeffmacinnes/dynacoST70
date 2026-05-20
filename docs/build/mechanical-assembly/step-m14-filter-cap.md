---
title: M14 — Quad filter capacitor
---

# M14: Mount the quad filter capacitor

> *Mount the quad filter capacitor in the special cutout. Fasten by twisting each of the (4) mounting tabs one-quarter turn. Note that the four connecting lugs are identified by markings at the base of the lugs. Be sure to orient the capacitor properly, with the lugs positioned as in the pictorial.* — manual page 5

## What you're doing physically

The **quad filter capacitor** is the big aluminum can with four electrolytic sections inside, mounted on TOP of the chassis. It contains four separate capacitor sections in one can, each rated 525 V.

Mounting is unique to this part — it doesn't use screws. Instead:

1. Set the cap into its dedicated rectangular cutout on the chassis top.
2. The cap has **four metal mounting tabs** sticking down through slots in the chassis.
3. From underneath, twist each tab **one quarter turn** (90°) with pliers. This locks the tab against the chassis like a key turning in a lock.
4. The cap is now held firmly in place; no nuts, no screws.

The orientation is critical: the four connecting lugs (A, B, C, D — also numbered 1, 2, 3, 4 in the wiring procedure) must match the pictorial. There's only one way the cap fits in the cutout because the tabs are arranged asymmetrically, but double-check.

## What's inside the can

Four electrolytic capacitor sections sharing a common aluminum can (which is the shared negative terminal — grounded via the chassis through M15's solder lug).

| Section | Capacitance | Voltage at this lug | Role |
|---|---|---|---|
| 30 µF | First stage filter | Lug **D** (435 V DC) | Direct from rectifier output |
| 20 µF | Second stage filter | Lug **C** (415 V DC) | After choke, main B+ rail |
| 20 µF | Third stage filter | Lug **B** (375 V DC) | After 6.8 kΩ dropping R, screen feed |
| 20 µF | Fourth stage filter | Lug **A** (305 V DC) | After 22 kΩ dropping R, input stage feed |

These four sections together implement the **B+ chain** that smooths and progressively drops the rectified DC voltage. See [filter capacitors](../../components/filter-capacitors.md) and [rectification — smoothing](../../theory/rectification.md#smoothing-from-pulsating-dc-to-clean-dc) for the theory.

## Why a single can instead of four separate caps

Mid-century manufacturing economy. A single multi-section can:

- Saved real estate (4 caps in 1 mounting area).
- Shared the negative terminal (the can itself), simplifying ground wiring.
- Standardized the part — easier to source one quad cap than four matched discretes.

Modern restorations sometimes replace the quad can with four separate caps (which can be physically smaller, cheaper, and easier to source). The electrical behavior is identical if the values match.

## The "common negative" tradeoff

Since all four cap sections share the can (= shared negative terminal), they ALL ground at the same point. If the can isn't grounded properly (the [M15](step-m15-ground-lugs.md) solder lug under it), the entire B+ chain has no return path → amp doesn't work.

This is one reason why the manual emphasises good torque on the can's mounting in the next step.

## Lug identification

The four lugs sticking up from the top of the can are marked at their bases:

- A small letter or shape stamped into the can next to each lug (A, B, C, D — sometimes shown as ▢ △ ◯ ● in older kits)
- The wiring procedure also refers to them as "lug 1, 2, 3, 4" — same physical lugs, dual naming convention

Verify the identification before any wiring lands on these lugs.

## See also

- [Filter capacitors](../../components/filter-capacitors.md) — what's electrically inside this can
- [Step M15](step-m15-ground-lugs.md) — the ground lug right next to this cap that's the star ground point
- [Step 8 — OPT red leads to B+](../power-supply/step-08-opt-b-plus.md) — first wiring that uses the filter cap lugs
