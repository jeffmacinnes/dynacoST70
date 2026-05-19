---
title: First power-on
---

# First power-on

The first time mains voltage reaches the amp. This is the scariest moment of the build — but if [pre-power](pre-power-checklist.md) and [continuity](continuity-checks.md) checks passed, it should also be the most boring. The point is to ramp up slowly, in stages, watching for anything wrong. A variac makes this safe; without one, you go right from "off" to "full mains" with no way to back out.

!!! danger "Required reading first"
    [High-voltage safety](../test-equipment/high-voltage-safety.md). The amp's B+ rail reaches ~450 V DC after this procedure, and the filter caps hold lethal charge for minutes after power-off.

## Equipment for the bring-up

- **Variac** (variable autotransformer). Adjustable from 0 to ~130 V AC. See [variac page](../test-equipment/variac.md). Mandatory for safe first power-on; if you don't have one, borrow one.
- **DMM**, set to AC volts (600 V range) for line checks, DC volts (600 V range) for B+ checks.
- **Insulated probes**, CAT III 600 V or better. See [probes](../test-equipment/probes.md).
- **Discharge tool** — a 10 kΩ 5 W resistor with insulated leads, for safely draining filter caps between tests. See [HV safety](../test-equipment/high-voltage-safety.md#discharging-filter-caps).
- **Safety glasses** — filter caps can rupture; arc flash is bright.

## The general procedure

There are FOUR distinct power-on sessions, in order, each verifying more of the amp:

| Session | Tubes installed | What it tests |
|---|---|---|
| 1 | NONE | Transformer + filter caps under no load |
| 2 | 5AR4 only | Rectifier works; B+ comes up |
| 3 | 5AR4 + 6GH8As | Driver stage works; B+ sags slightly under driver load |
| 4 | All 7 tubes (output tubes bias set MAX NEGATIVE) | Full operation |

Don't skip sessions — each one catches a different category of failure, and skipping risks destroying things in a way the earlier session would have caught cheaply.

## Session 1 — no tubes

Goal: verify the power transformer and filter caps work, without any tubes loading the circuit.

### Setup

- All tube sockets empty.
- Amp plugged into the variac.
- Variac plugged into the wall.
- Variac dialed to **0 V**.
- Power switch ON.
- DMM ready.

### The ramp

1. **Dial variac up to ~25 V AC.** You should hear a faint transformer hum (varies by transformer; some are nearly silent).
2. **Check for any smoke or smell.** None? Continue. Anything? STOP, discharge caps, find the problem.
3. **Measure on the filter cap +1 lug** (DC volts, 600 V range): should read ~0 V (no tubes = no rectification = no DC).
4. **Measure on the 6.3 V heater pins** (AC volts, ~30 V range): should read ~1.3 V AC (proportional to variac dial position, 25/120 × 6.3 V).
5. **Dial up to 50 V.** Repeat checks. Heater AC should now read ~2.6 V.
6. **Continue ramping** in 25 V steps to full mains voltage. At each step, listen and look for problems, recheck the heater AC.
7. **At full mains (~120 V),** the 6.3 V heater windings should read 6.3 V AC; the 5 V winding should read 5 V AC.

### What this confirms

- The primary is taking mains.
- All heater secondaries are intact and outputting the right voltage.
- No insulation breakdown anywhere (no smoke, no arc).
- Filter caps don't have shorts (no current spike during ramp).

### What this does NOT yet test

- The HV rectification (no rectifier tube).
- Any tube biasing.
- The amplifier signal path.

Power off. Discharge filter caps. Wait at least 30 seconds before installing the next tube.

## Session 2 — 5AR4 only

Goal: verify the rectifier works and B+ comes up to the right voltage.

### Setup

- Install only the **5AR4** (in socket V1).
- Other tube sockets still empty.
- Variac back to **0 V**, power switch ON.

### The ramp

1. **Dial up to 25 V.** Wait 30 seconds (the 5AR4 has a slow indirectly-heated warm-up — it doesn't start rectifying until the cathode is hot enough).
2. **Measure on filter cap +1** (DC volts, 600 V): should be a few volts (just starting to rectify with low input).
3. **Dial to 50 V, then 75 V, then 100 V, then full mains.**
4. At each step, give 10-15 seconds for the cap to settle, then measure +1 lug.
5. **At full mains, +1 lug should read 480-520 V DC.** Higher than the nominal 460 V because there's no load drawing current down.

### What this confirms

- 5AR4 is healthy.
- HV winding produces the expected voltage.
- Rectification works.
- Filter caps charge to the right level.

### What to watch for

- **B+ much lower than expected** (e.g., 200 V at full mains): rectifier issue or HV winding problem. Probably one of the red leads isn't connected properly.
- **B+ at expected level but rapidly drops to zero**: a filter cap is shorting under voltage. Power off immediately.
- **Smoke or smell at any point**: power off immediately, discharge, find the problem.
- **5AR4 glows brilliantly blue**: gas inside, tube is dying. Replace.

Power off. Discharge filter caps. Wait 30 seconds.

## Session 3 — driver tubes added

Goal: verify the driver stage works under load. The 6GH8As will draw some current, which slightly loads the supply.

### Setup

- 5AR4 still installed.
- Install both **6GH8As** (in sockets V4 and V5).
- Output tube sockets (V2/V3/V6/V7) still empty.
- Variac back to **0 V**.

### The ramp

1. Same as before — 25 V, 50 V, 75 V, 100 V, full.
2. At each step, give the driver tubes time to warm up (~15-20 seconds).
3. **At full mains:** B+ should be 450-490 V DC (slightly lower than session 2 because the drivers are drawing ~10 mA each).

### What to check

- 6GH8A heaters glowing (you can see a soft orange glow from inside the tube).
- Plate voltages on the 6GH8As are roughly in their normal range (you can measure these against the schematic if you want; for now, "non-zero" is OK).
- No arcing or smoke.

Power off, discharge, wait.

## Session 4 — all tubes, bias maximum negative

Goal: full operation, but the EL34s start in a "barely conducting" state so you can dial them in safely.

### Setup

- All previous tubes installed.
- **Bias pots set to maximum NEGATIVE.** This makes the EL34s nearly cut off — minimal idle current. If you have individual bias pots ([modification](../modifications/individual-bias-pots.md)), set ALL four to maximum negative. Turn the pot fully counter-clockwise (typical) or whichever way produces the most negative grid voltage.
- Install the four EL34s (V2, V3, V6, V7).
- Variac at **0 V**.
- **DMMs on bias measurement points** — DC volts, 4000 mV range, probing across one of the EL34 cathode sense resistors. See [bias adjustment](bias-adjustment.md).

### The ramp

1. Dial up slowly, 25 V, 50 V, etc.
2. Watch the EL34 cathode voltage as it comes up. With bias maximum negative, you should see almost no cathode voltage (i.e., almost no current).
3. At full mains, the cathode reading should still be very low — maybe 5-20 mV across a 1 Ω resistor (5-20 mA per tube). That's "barely on."
4. **Watch the EL34 plates.** They should NOT be glowing red. If any plate starts glowing red, IMMEDIATELY power off and recheck the bias setup. Red-plating destroys EL34s in minutes.

### What this confirms

- All four EL34s are alive and respond to bias.
- B+ holds up under the (still light) output stage load.
- Bias supply is producing negative voltage at the grids.

### Next step

When session 4 succeeds, proceed to [bias adjustment](bias-adjustment.md) to dial the EL34 idle currents to their proper values.

## What to do if anything goes wrong

At any point during any session, if you observe:

- Smoke
- Burnt smell
- Audible arcing or popping
- A tube glowing brilliant blue (gas)
- An EL34 plate going red-hot
- The DMM reading wildly wrong values
- The variac drawing way more current than expected (>1 A typical, >2 A is suspicious)

**...immediately:**

1. Power off (the variac switch and / or the wall switch).
2. **Wait at least 60 seconds** for the filter caps to drain.
3. **Verify caps are discharged** with the DMM before reaching inside.
4. **Investigate** with the amp cold. Look for visible damage, retraced connections, smell-locate the problem.

Don't reapply power until you understand what went wrong. "Try again and see" is the wrong move when there's been smoke.

## See also

- [Variac](../test-equipment/variac.md) — the slow-ramp tool
- [High-voltage safety](../test-equipment/high-voltage-safety.md) — required reading
- [Voltage checks](voltage-checks.md) — the next step after first power-on
- [Bias adjustment](bias-adjustment.md) — the procedure that follows session 4
