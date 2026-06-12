---
title: Continuity checks
---

# Continuity checks

Before the amp is powered for the first time, methodically verify every electrical path with a DMM. This catches wiring errors while they're free — a shorted secondary found here costs nothing; the same short discovered by smoke costs a transformer.

## What a continuity check actually tells you

A DMM in continuity mode applies a small voltage (~1 V) and measures the resulting current. It reports:

- **Continuous beep (or low resistance)**: the two probes are electrically connected, resistance below some threshold (often <50 Ω).
- **No beep (high resistance / OL)**: the probes are not connected — open circuit.

For an unpowered amp, this lets you trace every wire and verify:

1. **Things that SHOULD be connected** are connected (low resistance).
2. **Things that SHOULD NOT be connected** are not (open / high resistance).

[Voltage source vs current path](../theory/voltage-vs-current.md) explains why mis-wiring matters — current finds whatever path you give it, regardless of intent. Continuity testing makes intent visible.

## Setup

- Amp UNPOWERED, unplugged.
- All filter caps DISCHARGED (probe across each cap with the DMM on DC volts first, confirm <10 V before continuing). See [HV safety](../test-equipment/high-voltage-safety.md#discharging-filter-caps).
- DMM set to continuity mode (beep symbol).
- One alligator-clip lead for the negative probe (clip it to a known chassis ground point — typically a chassis bolt or the seven-lug strip's grounded lug).
- Your free hand on the positive probe, working through each test.

## Tests, organised by what they verify

### 1. Heater windings end-to-end

For each heater winding on the PA-060, probe between its two leads at their landing points. Should be low resistance — the winding is just a coil of copper wire.

| Winding | Probe between | Expected resistance |
|---|---|---|
| 5V (5AR4 heater) | V1 pin 2 ↔ V1 pin 8 (white pair) | ~0.5 Ω |
| 6.3V #1 (channel B) | V2 pin 2 ↔ V2 pin 7 (green pair) | ~0.3 Ω |
| 6.3V #2 (channel A) | V7 pin 2 ↔ V7 pin 7 (brown pair) | ~0.3 Ω |

If any reads OL: open winding (broken). Replace the PA-060.

### 2. Heater CT to its grounding lug

| Winding | Probe between | Expected |
|---|---|---|
| 6.3V #1 CT | Either GRN pin ↔ seven-lug strip lug #5 | <1 Ω |
| 6.3V #2 CT | Either BRN pin ↔ seven-lug strip lug #7 | <1 Ω |

If OL: the GRN/YEL or BRN/YEL CT lead isn't connected to its lug. Recheck [step 6](../build/power-supply/step-06-heater-cts.md).

### 3. HV secondary end-to-end

Probe between V1 pin 4 and V1 pin 6 (the two red leads of the 720 V winding).

- **Expected:** ~80-150 Ω (the full HV winding's DC resistance).
- **OL:** open winding. PA-060 is dead.
- **<1 Ω:** secondary is shorted. Stop, don't power up.

### 4. HV CT to ground reference

Probe between V1 pin 8 (5AR4 cathode), the [filter cap +1 lug](../components/filter-capacitors.md), and chassis ground:

| Probe between | Expected |
|---|---|
| V1 pin 4 ↔ RED/YEL CT landing point (filter cap area) | ~40-75 Ω (half the winding) |
| V1 pin 6 ↔ RED/YEL CT landing point | ~40-75 Ω (other half) |
| RED/YEL CT landing point ↔ chassis | varies (depends on whether step 7 is wired) |

### 5. Filter cap sections

For each section of the quad filter cap, probe between its positive lug and chassis (the can body):

- **Expected:** initially OL, then slowly drops as the cap charges from the DMM's small current. After 10-20 seconds, climbs back to OL as the cap saturates.

This rising/falling pattern indicates a healthy electrolytic.

- **If the resistance stays constant (e.g., 5-50 kΩ):** the cap is leaky. Won't hold charge properly.
- **If it stays at 0 Ω:** the cap is shorted. WILL destroy your rectifier on power-up.

Do this for all four sections of the quad cap before powering on.

### 6. Chassis safety earth (3-prong cord)

| Probe between | Expected |
|---|---|
| Third pin of mains plug ↔ chassis (any bolt) | <1 Ω |
| Third pin of mains plug ↔ hot pin | OL |
| Third pin of mains plug ↔ neutral pin | OL |
| Chassis ↔ hot pin (switch OFF) | OL |
| Chassis ↔ neutral pin (switch OFF) | OL |

If the first test fails: your earth bond isn't bonding. See [3-prong cord modification](../modifications/3-prong-cord.md).

If any of the others fail: there's an unintended path between mains and chassis. STOP and find it.

### 7. Output transformer windings

For each A-470 output transformer:

| Probe between | Expected |
|---|---|
| BLUE ↔ BLUE/WHITE (primary) | ~150-250 Ω (full primary) |
| BLUE ↔ RED (one half of primary) | ~75-125 Ω |
| BLUE/WHITE ↔ RED (other half) | ~75-125 Ω |
| BLACK ↔ BROWN (4Ω secondary) | <0.5 Ω |
| BLACK ↔ ORANGE (8Ω) | <0.5 Ω |
| BLACK ↔ YELLOW (16Ω) | <0.5 Ω |
| Any primary lead ↔ any secondary lead | OL (no continuity!) |

The last test is critical: primary and secondary must be electrically isolated. Any continuity means insulation breakdown — OPT is dead.

### 8. No shorts to chassis from HV nodes

This is the most important "things should NOT be connected" test.

| Probe between | Expected |
|---|---|
| V1 pin 4 (anode 1) ↔ chassis | OL |
| V1 pin 6 (anode 2) ↔ chassis | OL |
| V1 pin 8 (cathode / B+) ↔ chassis | OL or very high resistance (>1 MΩ) |
| Each filter cap + lug ↔ chassis | initially OL, then transient |
| EL34 plate pins (3 on each socket) ↔ chassis | OL |
| OPT primary leads ↔ chassis | OL |

If any HV node has continuity to chassis: there's a short. DO NOT POWER UP. Find and fix it first.

### 9. Bias supply path

| Probe between | Expected |
|---|---|
| PA-060 RED/BLK lead ↔ 1N4007 cathode (banded end) | <1 Ω |
| 1N4007 anode ↔ bias filter cap (after the diode) | <1 Ω |
| 1N4007 cathode ↔ anode | shows ~600 mV drop on diode test |

The diode test confirms the 1N4007 is oriented correctly. If the diode shows OL in BOTH directions: it's blown. If it shows continuity in both: it's shorted.

### 10. The shotgun check

After working through all the above, do one final pass with the amp totally cold:

- Set DMM to continuity.
- Clip one probe to chassis ground.
- Tap the other probe on every HV-bearing node in turn (anodes, plates, filter cap +s).
- All should show OL.

If anything beeps, stop. There's a path that shouldn't exist.

## When to skip ahead

If you've been wiring carefully and have been continuity-checking each section as you went, the steps above are mostly confirmation. You don't have to repeat every test.

The MINIMUM continuity tests before first power-on:

- Heater windings end-to-end (catches a broken transformer).
- HV secondary end-to-end (catches a shorted secondary — fatal).
- No HV-to-chassis shorts (catches the most common wiring error).
- Chassis earth bonded (catches a safety hazard).

These four cover the failure modes that cost real money or hurt people.

## Next step

When continuity passes: [first power-on](first-power-on.md).
