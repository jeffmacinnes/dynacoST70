---
title: Filter capacitors
---

# Filter capacitors

The ST-70 uses a multi-section filter capacitor (often called a "quad cap" or "FP cap") — a single can containing four separate capacitors with a shared negative terminal. These caps are the energy reservoirs that smooth the 5AR4's rectified output into clean B+.

*Page to be written.* Planned coverage:

- Multi-section can construction: four electrolytics, one envelope, one ground stud.
- Typical values for the ST-70 (commonly 30μF + 20μF + 20μF + 10μF or similar; exact value depends on era and replacement choice).
- How the four sections distribute across the B+ chain: rectifier output → choke input → choke output → driver/screen supply.
- Voltage ratings (must exceed expected B+ with headroom — typically 500V or 525V working voltage).
- Why electrolytics specifically (high capacitance per unit volume, polarized).
- Failure modes:
  - Drying out (loss of capacitance, increased ESR, hum)
  - Shorting (sudden — usually destroys whatever rectifier is feeding them)
  - Leakage (slow DC current, ineffective filtering, distortion)
- Reforming old caps and why it's controversial.
- Modern replacements: F&T, JJ, Sprague Atom, CE Manufacturing.
- The discharge habit: see [high-voltage safety](../test-equipment/high-voltage-safety.md#discharging-filter-caps).

## In this build

The quad filter cap sits on the chassis between the rectifier and the choke. Its lugs are referenced from multiple steps:

- [Step 7](../build/power-supply/step-07-hv-ct.md) — red/yellow CT lands at the cap's ground area
- [Step 8](../build/power-supply/step-08-opt-b-plus.md) — OPT red leads land at lug #1
- [Step 9](../build/power-supply/step-09-choke.md) — choke connects between lugs #1 and #2

## See also

- [Rectification](../theory/rectification.md#smoothing-from-pulsating-dc-to-clean-dc) — what filter caps do conceptually
- [Choke](choke.md) — the inductor that pairs with the filter caps for two-stage smoothing
- [High-voltage safety](../test-equipment/high-voltage-safety.md) — *required reading* before touching these caps in a powered-down amp
