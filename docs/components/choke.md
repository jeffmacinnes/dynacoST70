---
title: Choke
---

# Choke

The ST-70's choke is a single-winding inductor in the B+ supply, sitting between the first and second filter capacitor stages. It's the "L" in the classic LC pi-filter topology — its inductance resists changes in current and smooths the supply far better than capacitance alone.

*Page to be written.* Planned coverage:

- What a choke is: a coil of wire on an iron core, basically a transformer with only one winding.
- Why it's here: a two-stage filter (cap → choke → cap) has much lower ripple than either stage alone.
- The ST-70's choke specs (commonly 1.5H or similar, with a DC resistance that drops a few volts).
- Why a gapped core: the choke carries DC current, which would saturate a non-gapped core.
- Mechanical vibration ("choke hum" you can sometimes hear from the metal).
- Failure modes:
  - Open winding (uncommon, but ends the amp's operation)
  - Shorted turns (reduces inductance, increases ripple, hum returns)

## In this build

The choke is wired during [step 9](../build/power-supply/step-09-choke.md), connecting filter cap lug #1 (input) to lug #2 (output).

## See also

- [Filter capacitors](filter-capacitors.md) — the caps the choke sits between
- [Rectification](../theory/rectification.md#smoothing-from-pulsating-dc-to-clean-dc) — the smoothing chain
