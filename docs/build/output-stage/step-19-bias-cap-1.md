---
title: 'Step 19: First 100 µF bias filter cap'
---

# Step 19: 100 µF cap with negative end to lug 4, positive to lug 1

> *Connect the negative end (-) of a 100 MFD capacitor to lug #4 of the seven lug strip. Connect the positive (+) capacitor lead to lug #1.* — manual page 7

## What you're doing physically

Take one of the two **100 µF electrolytic capacitors** (DynakitParts #284506). Electrolytics are polarized — they have a distinct positive and negative end, marked on the body. Look for the band or "−" symbol; that's the negative side.

Solder the **negative end to lug 4** of the seven-lug strip. Solder the **positive end to lug 1** of the same strip.

Neither lug is soldered final at this step — both will get more components before they're sealed.

## What this cap does

This is one of two filter capacitors for the **bias supply**. The bias supply produces a negative DC voltage (~−65 V), and like any DC supply derived from rectified AC, it has ripple. The 100 µF cap smooths the ripple to milliVolt-level cleanliness.

The polarity is critical because:

- Lug 4 will carry the **negative bias voltage** (about −65 V relative to lug 1).
- Lug 1 will be at chassis ground (via the jumper from step 18 → lug 6 → ground in step 23).
- So negative DC at lug 4, ground at lug 1.
- The cap's negative side faces the more-negative node (lug 4).

Reverse-polarity electrolytics fail spectacularly under voltage — they balloon, sometimes explode, and definitely stop filtering. Always check the polarity marking before soldering.

## See also

- [Step 21 — Second bias cap](step-21-bias-cap-2.md) — the partner of this cap
- [Step 25 — Bias from diode](step-25-bias-from-diode.md) — what feeds the negative voltage
- [Filter capacitors](../../components/filter-capacitors.md) — electrolytic theory
