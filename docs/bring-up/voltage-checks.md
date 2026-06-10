---
title: Voltage checks
---

# Voltage checks

After [first power-on](first-power-on.md) succeeds (all four sessions ran without smoke), it's time to systematically measure voltages at every accessible node and confirm they match what the schematic says. This catches subtle issues that don't trip the "burst into flames" alarm but will cause real problems downstream — drifted resistors, weak tubes, miswired bias.

## Setup

- Amp at full mains, fully warmed up (~5 minutes from power-on).
- All tubes installed, bias pots set near final values (or maximum negative if you haven't biased yet).
- DMM, leads on **CAT III 600 V or better probes**.
- [One-hand rule](../test-equipment/high-voltage-safety.md#one-hand-rule) — keep one hand in your pocket, work with the other.
- Negative probe clipped (alligator) to chassis ground — a known clean reference point. The seven-lug strip's grounded lug or a dedicated chassis bolt works.
- Positive probe in your free hand — touch and read.

## Manual reference (page 19 — Voltage Test Points)

The Dynaco manual provides a canonical voltage table on page 19. Tolerance per page 16: **"Departures of more than 10% from these values may indicate a malfunctioning of one or more of the circuit components."** Anything inside that 10% band is normal.

### Tube pins (with all tubes warm, biased at 1.56 V Biaset)

| Pin | EL-34 (each) | GZ-34 (V1) | 6GH8A (on board) |
|---|---|---|---|
| 1 | 1.56 V DC (cathode) | — | * |
| 2 | — | 435 V DC (plate) | 0 V (g1 / signal node) |
| 3 | 410 V DC (plate) | — | * |
| 4 | 415 V DC (screen) | 360 V AC (HV anode) | 6.4 V AC heater (pins 4-5) |
| 5 | −32 V DC (control grid) | — | 6.4 V AC heater (pins 4-5) |
| 6 | −32 V DC (suppressor, tied to g1) | 360 V AC (HV anode) | 1.0 V (cathode region) |
| 7 | — | — | 1.2 V (cathode region) |
| 8 | 1.56 V DC (cathode) | 435 V DC (plate) | * |

\* = measurements at these points vary tube-to-tube and don't reliably indicate normal performance.

EL-34 pin 5 and pin 6 should read **identically** between the two tubes in a pair — if they don't, that pair has a wiring or bias problem.

### Quad filter capacitor lugs

The four sections of the can-mounted filter cap have lugs labeled A, B, C, D at their bases (the same physical lugs are also numbered 1-4 in the wiring instructions; the letter naming is what the voltage table uses).

| Lug | Voltage | Role |
|---|---|---|
| A | 305 V DC | After 22 kΩ dropping resistor — feeds 6GH8A pentode plate / input stage |
| B | 375 V DC | After 6.8 kΩ dropping resistor — feeds EL-34 screen network |
| C | 415 V DC | After the choke — main B+ rail to OPT primary CT |
| D | 435 V DC | Direct from rectifier — first filter cap, highest voltage in the amp |

### Other test points

| Node | Expected | Notes |
|---|---|---|
| Diode rectifier, (A) lug | 50 V AC | The bias winding AC input to the diode |
| Diode rectifier, (B) lug | −65 V DC | Bias supply output (filtered) |
| PC-3 eyelets #3 and #18 | 370 V DC | After board's internal dropping network — supply to driver tube |
| Biaset sockets V4 / V5, pin 8 | 1.56 V DC | Per-channel bias measurement (when bias is correctly set) |

---

## Reference voltage table

All voltages are RELATIVE TO CHASSIS GROUND unless noted otherwise. Tolerances are typical — ±5 % is normal across tubes, ±10 % is "still working." Larger deviations warrant investigation.

### Mains side (primary)

| Node | Type | Expected | Tolerance |
|---|---|---|---|
| Wall outlet (Hot ↔ Neutral) | AC | 120 V | ±5 % |
| Across primary winding | AC | 120 V | ±5 % |
| Hot ↔ chassis (switch ON) | AC | 60-120 V (capacitive) | varies |
| Neutral ↔ chassis | AC | ~0 V | <5 V |
| Earth pin ↔ chassis | AC | 0 V | <0.5 V |

### Heater windings (secondaries)

| Winding | Probe between | Expected |
|---|---|---|
| 5 V (5AR4 heater) | V1 pin 2 ↔ V1 pin 8 | 5.0 V AC ±5 % |
| 6.3 V #1 (CHAN A heaters) | V2 pin 2 ↔ V2 pin 7 | 6.3 V AC ±5 % |
| 6.3 V #2 (CHAN B heaters) | V7 pin 2 ↔ V7 pin 7 | 6.3 V AC ±5 % |
| 6.3 V #1 either pin ↔ chassis | (with CT grounded) | 3.15 V AC |
| 6.3 V #2 either pin ↔ chassis | (with CT grounded) | 3.15 V AC |
| 55 V (bias winding) | RED/BLK lead ↔ RED/YEL CT | 55 V AC ±10 % |

### HV winding

| Probe between | Expected |
|---|---|
| V1 pin 4 ↔ V1 pin 6 (full secondary, **don't measure! exceeds DMM rating**) | 720 V AC |
| V1 pin 4 ↔ chassis (CT grounded) | 360 V AC ±5 % |
| V1 pin 6 ↔ chassis (CT grounded) | 360 V AC ±5 % |
| RED/YEL CT ↔ chassis | 0 V |

**Don't probe pin-to-pin across the full HV secondary.** 720 V AC peak-to-peak exceeds the 600 V rating of most CAT III DMMs and probes. Always measure each end to ground (chassis) separately.

### B+ rail (after rectifier and filter)

Per the manual's voltage table (page 19), with all tubes warm and biased to 1.56 V Biaset (~50 mA per tube):

| Node | Type | Expected at idle | Notes |
|---|---|---|---|
| Filter cap lug D | DC | 435 V | First filter cap (direct from rectifier) |
| Filter cap lug C | DC | 415 V | After choke; B+ to OPT primary CT |
| Filter cap lug B | DC | 375 V | After 6.8 kΩ — feeds EL-34 screen network |
| Filter cap lug A | DC | 305 V | After 22 kΩ — feeds 6GH8A pentode plate / input stage |
| PC-3 eyelets #3 and #18 | DC | 370 V | On-board dropping network output |

10% tolerance applies. If B+ is consistently low everywhere: line voltage might be low, or the EL-34s are biased too hot. If consistently high: line voltage is high, or EL-34s aren't drawing current (bias too cold, dead tube). Check bias either way.

!!! tip "4-ch scope: ripple across the B+ cascade"
    DMMs read average DC and average AC separately; they don't show you the *ripple riding on top of DC* unless you switch to AC mode (which is a peak-detection measurement, not RMS, on most cheap DMMs). A scope shows everything.

    Probe (AC-coupled, 50 mV/div, time base 5 ms/div — covers ~12 cycles at 120 Hz):

    - **Ch1**: Filter cap lug D (~435 V DC + heavy ripple)
    - **Ch2**: Filter cap lug C (after choke)
    - **Ch3**: Filter cap lug B (after 6.8 kΩ)
    - **Ch4**: Filter cap lug A (after 22 kΩ)

    What you should see: a 120 Hz sawtooth-ish ripple decreasing dramatically from ch1 → ch2 → ch3 → ch4. Typical magnitudes at idle:

    - **Lug D**: 15–25 Vp-p ripple (lots, expected — this is right after rectification)
    - **Lug C**: 0.5–1.5 Vp-p (choke + cap drops it by ~25 dB)
    - **Lug B**: 50–200 mVp-p
    - **Lug A**: 10–50 mVp-p (essentially flat — input-stage grade B+)

    What it tells you: each filter stage is doing its job. If lug C has 5+ Vp-p ripple, the choke isn't filtering (open inductor) OR the lug-1 cap is dry. If lug A has ~100 mVp-p, the 22 kΩ resistor between lugs is fine but the lug-3 cap may have lost capacitance.

    **Use AC coupling on the scope** so the input attenuator can handle the small ripple signal without your big DC level pinning the trace off-screen. The 10:1 probe still applies — for 50 mVp-p ripple riding on 400 V DC, you want headroom.

### Bias supply

| Node | Type | Expected |
|---|---|---|
| Diode (B) lug — bias supply output | DC | −65 V |
| At each EL34 grid (pin 5, with tube biased to target) | DC | −32 V |
| At each individual bias pot wiper | DC | adjustable, somewhere between −20 and −55 V |

The grid voltage is what actually sets the tube's idle current. The bias supply itself is just the source.

### EL34 voltages (with tubes warm, biased to ~50 mA per tube)

| Pin | Function | Expected |
|---|---|---|
| 1 | Cathode (joined with pin 8) | 1.56 V DC (= 100 mA per pair × 15.6 Ω) |
| 3 | Plate (anode) | 410 V DC |
| 4 | Screen (g2) | 415 V DC |
| 5 | Control grid (g1) | −32 V DC (the bias) |
| 6 | Suppressor (internally tied to g1 region) | −32 V DC (same as pin 5) |
| 8 | Cathode (joined with pin 1) | 1.56 V DC |
| 2 / 7 | Heater pins | 3.15 V AC each (relative to CT-grounded reference) |

If a tube has a plate voltage WAY different from its mate (V2 vs V6, V3 vs V7): something is wrong with that tube or its socket.

### 6GH8A voltages

These vary more by version and adapter, but rough expectations:

| Section | Plate | Cathode | Grid |
|---|---|---|---|
| Pentode | 180-220 V DC | 1-3 V DC | ~0 V (signal node) |
| Triode | 150-200 V DC | 110-150 V DC | varies (mid-point of cathode for cathodyne) |
| Heater | 6.3 V AC across the heater pins | | |

The pentode and triode share the same envelope, so if one section is off, both might be affected.

## Procedure

Work through the table in order, top to bottom. Mains side first (safest), heaters next, HV last. At each measurement:

1. **Confirm DMM is on the right range** (600 V AC for line, 600 V DC for B+, etc.) before touching the probe.
2. **Touch the probe to the node** with your free hand.
3. **Read the value.** Compare to the table.
4. **Lift the probe** before adjusting DMM settings or moving.

If a value is wildly off (>20 % from expected):

1. **Power off, discharge filter caps.** Don't troubleshoot with HV present.
2. **Continuity-check** the path leading to that node. Look for a bad solder joint, a miswired component, a drifted resistor.
3. **Power up again** and re-measure. If still off, the affected component (tube, resistor, capacitor) needs replacement.

## Common voltage issues

### B+ low across the board (~10-15 % low)

Possible causes:

- Mains voltage is low (check the wall first).
- 5AR4 cathode emission is weak (replace).
- One of the HV winding leads has a bad joint, effectively running half-wave.
- A filter cap is leaky (drawing current it shouldn't).

### B+ low on one lug only (e.g., lug A is low but D is normal)

The dropping resistor between lugs is wrong value or open. Measure across the resistor with the amp powered (carefully) — voltage drop should match (current × resistance). The two key dropping resistors are the 6.8 kΩ between lugs C and B, and the 22 kΩ between lugs B and A.

### Heater voltages low

- Mains voltage low.
- Too many tubes on that winding (shouldn't happen in a stock build).
- Transformer winding partly shorted (rare but catastrophic).

### Heater voltages OK but only one side is grounded

The CT wire isn't connecting to ground properly. Recheck [step 6](../build/power-supply/step-06-heater-cts.md).

### Bias voltage too low (less negative than expected)

- 1N4007 is shorted (showing AC on output).
- Bias filter cap is leaky.
- The bias supply network has a wrong resistor value.
- If using [individual bias pots](../modifications/individual-bias-pots.md): the pot is at its less-negative extreme.

### EL34 plate voltage MUCH higher than nominal (e.g., 450 V instead of 410 V)

The tube isn't drawing its rated current. Bias is too cold (too negative grid), or the tube is dying.

### EL34 plate voltage LOWER than nominal (e.g., 380 V instead of 410 V)

The tube is drawing too much current. Bias is too hot (not negative enough), or the tube is gassy / shorted internally. Watch the plate carefully — if it glows red, power off immediately.

## When voltages all check out

Proceed to [bias adjustment](bias-adjustment.md) to dial each EL34 to its ideal idle current.

## See also

- [High-voltage safety](../test-equipment/high-voltage-safety.md) — required reading
- [Multimeter](../test-equipment/multimeter.md) — knowing your instrument's limits
- [Probes](../test-equipment/probes.md) — CAT-III rating matters for these voltages
