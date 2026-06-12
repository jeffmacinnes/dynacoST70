---
title: Bleeder resistor
---

# Bleeder resistor across the filter cap

The stock ST-70 has **no dedicated bleeder resistor**. When the amp is operating, B+ drains quickly after power-off because the tubes and the driver board's resistor chain keep pulling current as the supply collapses. The dangerous case is when that load path is missing: tubes pulled for testing or swap, a cold rectifier, or an open connection somewhere downstream. In that state the quad cap can hold **~435 V essentially indefinitely** — exactly when you're most likely to have your hands inside the chassis.

A bleeder resistor is a permanent, passive discharge path: a high-value power resistor wired straight across the first filter section, quietly draining the supply to safe levels within a minute or two of switch-off, no matter what else is connected.

## What it does electrically

The bleeder sits from **cap lug 2 (the 435 V rectifier-output section) to the ground lug at the cap**. Because the four sections are coupled — lug 2 to lug 1 through the choke, lug 1 to lug 4 through the 6.8 kΩ, lug 4 to lug 3 through the 22 kΩ — one bleeder at the head of the chain drains **all four sections**. (See the [B+ signal path](../signal-paths/b-plus.md) for the cascade.)

At idle it draws a constant trickle:

- Current: 435 V / 300 kΩ ≈ **1.5 mA** — invisible next to the amp's ~200 mA draw. No measurable effect on B+ or on the sound.
- Dissipation: 435 V² / 300 kΩ ≈ **0.65 W** — the resistor runs warm, continuously, for the life of the amp. That's why the power rating below matters.

After switch-off (worst case, no tube load): the ~50 µF on lugs 1+2 discharges through the bleeder with a time constant of ~15 s, which takes the rail from 435 V to under 10 V in **roughly a minute**. The downstream sections follow through the dropping resistors. Without the bleeder and without tubes: hours to days.

## Recommended parts

**Two 150 kΩ, 2 W metal-oxide resistors in series** (300 kΩ total).

Why two in series instead of one 300 kΩ:

- **Voltage rating.** A standard 2 W resistor is typically rated for 350–500 V *working voltage* — a single part across 435 V is at or past its limit. Two in series each see ~218 V, with comfortable margin.
- **Power margin.** ~0.33 W each on 2 W parts — running at ~16% of rating keeps them merely warm and long-lived.
- **Redundancy of failure mode.** Resistors fail open far more often than short. Two parts doesn't fix that (a series chain still fails open), but generously-derated parts make the failure much less likely in the first place.

Anything in the 220–330 kΩ / ≥4 W-total / ≥500 V-total range is fine. Don't go much lower (wasted heat, faster cap wear from ripple current is negligible but the dissipation climbs) or much higher (discharge slows proportionally).

## Physical installation

1. Power off, **discharge and verify <10 V** at all four cap lugs before touching — see [high-voltage safety](../test-equipment/high-voltage-safety.md).
2. Solder the two resistors in series (a short, stiff joint, sleeved if you like).
3. One free end to **cap lug 2**, the other to the adjacent **ground solder lug** at the cap (the main ground point from [step M15](../build/mechanical-assembly/step-m15-ground-lugs.md)).
4. Keep the body of the resistors in free air, not pressed against the cap can or a wire bundle — they dissipate ~0.7 W continuously.

Fully reversible: two solder joints, no holes, no rerouting.

## What it does NOT do

A bleeder is a backstop, not a guarantee. **Keep verifying with a meter before touching the supply.** The failure mode of a bleeder is *open* — and an open bleeder looks exactly like a working one until the day you trust it. The discharge ritual in [first power-on](../bring-up/first-power-on.md) stays exactly the same; the bleeder just means that when you check, the rail is already at a few volts instead of 435.

## See also

- [Filter capacitors](../components/filter-capacitors.md) — the quad cap this protects you from
- [B+ signal path](../signal-paths/b-plus.md) — why one bleeder drains all four sections
- [High-voltage safety](../test-equipment/high-voltage-safety.md) — the discharge-and-verify procedure that still applies
- [Step M14 — Quad filter cap](../build/mechanical-assembly/step-m14-filter-cap.md) and [Step M15 — Ground lugs](../build/mechanical-assembly/step-m15-ground-lugs.md) — the two anchor points
