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

!!! important "The chassis IS ground in this amp"
    The chassis is bonded to mains earth through the green wire of the 3-prong cord (see [3-prong cord mod](../modifications/3-prong-cord.md)), and the HV winding's RED/YEL center tap is wired to chassis at [step 7](../build/power-supply/step-07-hv-ct.md). So at the DMM:

    **chassis ≡ RED/YEL CT ≡ signal ground**

    These are the *same node* electrically. Any probe that touches "chassis" is really touching the CT.

    This matters for the next few tests: when you probe one of the red HV leads to chassis, the current flows through the winding, to the CT, to chassis. You'll see the **winding resistance**, not OL — and that's the correct outcome. A "low reading to chassis" is not automatically a short. The right diagnostic question is whether the reading **matches the expected path**. A true short shows up as a reading *lower* than the expected path, because the unintended short is in parallel with the intended one. See [grounding and hum](../theory/grounding-and-hum.md) for the conceptual treatment.

### 3. HV secondary end-to-end

!!! note "This build has the rectifier diode mod installed"
    The two RED leads land on V1 **pin 3 and pin 5** (NC pins used as anchor lugs), with 1N4007s bridging pin 3→4 and pin 5→6. See [rectifier diode mod](../modifications/rectifier-diode-mod.md). Probe at pins 3 and 5 to measure the winding directly; probing at pins 4/6 measures *through* a diode and will read OL in one direction.

Probe between V1 pin 3 and V1 pin 5 (the two ends of the 720 V HV winding).

- **Expected:** ~50–150 Ω (the full HV winding's DC resistance). The PA-060 is a beefy 300 mA transformer; ~55 Ω is normal.
- **OL:** open winding. PA-060 is dead.
- **<1 Ω:** secondary is shorted. Stop, don't power up.

### 4. HV winding halves, via the CT

The RED/YEL center tap lands somewhere in the ground network (per [step 7](../build/power-supply/step-07-hv-ct.md), at the main ground point near the filter cap — though builders sometimes route it to the star ground instead; both are electrically the same node). Either probe the CT lead directly at its landing point, **or just probe chassis**, since chassis = CT.

| Probe between | Expected | What it tells you |
|---|---|---|
| V1 pin 3 ↔ chassis | ~25–75 Ω | DC resistance of one half of the HV winding |
| V1 pin 5 ↔ chassis | ~25–75 Ω | DC resistance of the other half |
| Both halves | within ~10% of each other | CT is electrically near the middle of the winding |

The two halves should sum (within meter resolution) to the full-winding reading from Test 3.

**A truly low reading here (e.g., <1 Ω) means a red lead is shorting directly to chassis somewhere — pinched against a chassis bolt, exposed wire touching a transformer frame, etc.** Find and fix before powering up. But a value matching the winding resistance is exactly correct.

### 4a. Bias tap (RED/BLK)

The RED/BLK lead is **a tap on the HV winding** — not a separate winding — partway up from the CT toward one of the RED ends. It feeds the bias rectifier diode (banded end), per [step 1](../build/power-supply/step-01-bias-diode.md).

| Probe between | Expected | What it tells you |
|---|---|---|
| RED/BLK (at the bias diode's banded end) ↔ chassis | a few Ω to ~20 Ω | RED/BLK's resistance to the CT (and the CT is at chassis) |
| RED/BLK ↔ V1 pin 3 | small if RED/BLK taps the pin-3 side; bigger if it taps the pin-5 side | which half of the winding hosts the bias tap |
| RED/BLK ↔ V1 pin 5 | the complementary value | confirms the same |

Sanity check: the small + the bigger should sum to your half-winding values from Test 4. The ratio of (RED/BLK ↔ chassis) to (its half-winding total) should roughly match 50 V / 360 V ≈ 14% — that's how the manual's voltage spec maps to a resistance ratio.

### 4b. HV ↔ mains primary isolation

This is the one HV-side test that *must* be OL. The primary and secondary share no ground path; any continuity here means insulation breakdown inside the PA-060 — the transformer is unsafe to power up.

| Probe between | Expected |
|---|---|
| V1 pin 3 ↔ mains black (at switch) | OL |
| V1 pin 3 ↔ mains white (at fuse) | OL |
| V1 pin 5 ↔ mains black | OL |
| V1 pin 5 ↔ mains white | OL |

If any of these read a finite value: **PA-060 is dead. Replace, do not power up.** This failure is rare but catastrophic — it means the line voltage can appear on the HV secondary (and through there, on the tube sockets and B+ rail).

!!! example "Reference values from this build"
    Measured on the actual ST-70 documented in this manual (units: Ω):

    | Test | Value | Notes |
    |---|---|---|
    | Test 3 — pin 3 ↔ pin 5 | 55 | Full HV winding |
    | Test 4 — pin 3 ↔ chassis | 26 | One half of the winding |
    | Test 4 — pin 5 ↔ chassis | 28 | Other half (7% mismatch is fine) |
    | Test 4 — halves sum | 54 ≈ 55 | Confirms CT placement |
    | Test 4a — RED/BLK ↔ chassis | 4 | Bias tap, very close to CT |
    | Test 4a — RED/BLK ↔ pin 3 | 22 | (26 − 4 = 22 ✓) tap sits on pin-3 side |
    | Test 4a — RED/BLK ↔ pin 5 | 32 | (28 + 4 = 32 ✓) |
    | Test 4a — ratio 4/26 ≈ 15% | matches | 50 V / 360 V tap ratio = 14% ✓ |
    | Test 4b — all four probes | OL | Primary-to-secondary isolation intact |

    These are reference values for a healthy PA-060 in a stock-current build with the rectifier diode mod. Your numbers will differ by some, but the *relationships* (halves sum to the full winding, bias-tap ratio matching the voltage ratio, all primary-secondary OL) should hold.

### 4c. Diode-mod check (1N4007s on V1 pins 3→4 and 5→6)

With the DMM in **diode-test mode** (not resistance/continuity), probe each 1N4007:

| Probe direction | Expected |
|---|---|
| Red probe on V1 pin 3, black on pin 4 | ~0.5–0.7 V (forward) |
| Red probe on V1 pin 4, black on pin 3 | OL (reverse) |
| Red probe on V1 pin 5, black on pin 6 | ~0.5–0.7 V (forward) |
| Red probe on V1 pin 6, black on pin 5 | OL (reverse) |

The banded end (cathode) of each diode must face the **plate pin** (4 or 6). If a diode reads OL both ways → open. If it reads ~0 Ω both ways → shorted; replace. If it reads forward voltage in the *wrong* direction → installed backwards, and that half of the rectifier won't conduct (you'll get half-wave rectification: ~60 Hz hum and roughly half the expected B+).

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
