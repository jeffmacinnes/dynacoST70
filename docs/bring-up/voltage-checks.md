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

These vary depending on whether the EL34s are biased to their normal idle current (~50 mA each, ~200 mA total) or running cooler:

| Node | Type | Expected at idle | Notes |
|---|---|---|---|
| V1 pin 8 (5AR4 cathode) = filter cap +1 | DC | 460-490 V | First filter cap |
| After choke (filter cap +2) | DC | 440-470 V | Second filter cap; ~15 V drop across choke |
| Screen feed (filter cap +3, after dropping R) | DC | 400-430 V | EL34 screens, 6GH8A pentode plate |
| Input/bias feed (filter cap +4, after dropping R) | DC | 200-250 V | 6GH8A pentode plate, input stage |

If B+ is consistently ~50 V low everywhere: your line voltage might be low, or the EL34s are biased too hot. Check bias.

If B+ is consistently ~50 V high: line voltage might be high, or the EL34s aren't drawing current (bias too cold, dead tube). Check bias.

### Bias supply

| Node | Type | Expected |
|---|---|---|
| 1N4007 cathode (after diode + filter) | DC | −45 to −60 V |
| At each EL34 grid (pin 5, with tube installed) | DC | −36 to −42 V |
| At each individual bias pot wiper | DC | adjustable, somewhere between −30 and −55 V |

The grid voltage is what actually sets the tube's idle current. The bias supply itself is just the source.

### EL34 voltages (with tubes warm, biased to ~50 mA)

| Pin | Function | Expected |
|---|---|---|
| 3 | Plate (anode) | 450 V DC (= B+ to plate) |
| 4 | Screen (g2) | 400-430 V DC |
| 5 | Control grid (g1) | −36 to −42 V DC (the bias) |
| 8 | Cathode | ~0 V (across the small sense resistor: ~50 mV) |
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

### B+ low on one cap only (e.g., +3 is low but +1 is normal)

The dropping resistor between caps is wrong value or open. Measure across the resistor with the amp powered (carefully) — voltage drop should match (current × resistance).

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

### EL34 plate voltage MUCH higher than nominal (e.g., 480 V)

The tube isn't drawing its rated current. Bias is too cold (too negative grid), or the tube is dying.

### EL34 plate voltage LOWER than nominal (e.g., 420 V)

The tube is drawing too much current. Bias is too hot (not negative enough), or the tube is gassy / shorted internally. Watch the plate carefully — if it glows red, power off immediately.

## When voltages all check out

Proceed to [bias adjustment](bias-adjustment.md) to dial each EL34 to its ideal idle current.

## See also

- [High-voltage safety](../test-equipment/high-voltage-safety.md) — required reading
- [Multimeter](../test-equipment/multimeter.md) — knowing your instrument's limits
- [Probes](../test-equipment/probes.md) — CAT-III rating matters for these voltages
