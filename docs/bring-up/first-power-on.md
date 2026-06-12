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

There are FIVE distinct power-on sessions, in order, each verifying more of the amp:

| Session | Tubes installed | What it tests |
|---|---|---|
| 1 | NONE | Transformer + filter caps under no load |
| 1B (optional) | All signal tubes (EL34s + 6GH8As), but **NO 5AR4** | Heaters under load — visible glow + measured current. No B+ can develop. |
| 2 | 5AR4 only | Rectifier works; B+ comes up |
| 3 | 5AR4 + 6GH8As | Driver stage works; B+ sags slightly under driver load |
| 4 | All 7 tubes (output tubes bias set MAX NEGATIVE) | Full operation |

Don't skip sessions — each one catches a different category of failure, and skipping risks destroying things in a way the earlier session would have caught cheaply. Session 1B is optional but informative; it's a richer heater check than Session 1 because you actually see the tubes light up and verify the daisy chain works under real heater current.

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

!!! tip "4-ch scope: verify the heater windings under no load"
    With the variac at full mains and no tubes installed, probe (DC-coupled, 50 V/div):

    - **Ch1**: V2 pin 2 (one end of the green pair)
    - **Ch2**: V2 pin 7 (other end of the green pair)
    - **Ch3**: V7 pin 2 (one end of the brown pair)
    - **Ch4**: V7 pin 7 (other end of the brown pair)

    With both windings' CTs grounded at the 7-lug strip, you should see all four channels as **clean 60 Hz sine waves at ~9 Vp-p** (6.3 Vrms = 8.9 Vp-p), with **ch1 ↔ ch2 in antiphase** and **ch3 ↔ ch4 in antiphase**. The pairs are symmetric about ground — at any instant, one end of a pair is +4.5 V and the other is −4.5 V.

    What it tells you: the CT-grounding scheme (which is what keeps heater AC from coupling hum into the cathodes) is working. If one end of a pair is at 0 V instead of swinging, the CT is grounded but the other end of the winding is open. If both ends ride the same way (in phase), the CT is open and the winding is floating.

Power off. Discharge filter caps. Wait at least 30 seconds before installing the next tube.

## Session 1B — signal tubes in, NO rectifier (optional but informative)

Goal: verify the heater windings under realistic load and visually confirm every signal tube lights up. Without the 5AR4, no B+ can develop — so even if there's a wiring error in the HV path, nothing dangerous happens. The tubes just sit there with hot filaments and no plate voltage.

This is a strictly more informative version of Session 1: same B+ safety (none), but you actually get to see the heater chain work end-to-end and measure heater voltage under real current.

### Setup

- **NO 5AR4** in V1.
- **All four EL34s** in V2/V3/V6/V7.
- **Both 6GH8As** in their PC-3A sockets.
- Bias pots set to **maximum negative** (a precaution — even with no B+, this leaves the EL34s in a known state when you eventually install the 5AR4).
- Variac at 0 V, power switch ON.

### The ramp

1. **Dial up to ~25 V AC.** Filaments are too cold to glow visibly. No B+ anywhere because no 5AR4. Measure heater AC: ~1.3 V per the variac ratio.
2. **Dial to 50 V, then 75 V, 100 V, full mains.** Same as Session 1.
3. **At full mains**, take a slow look at the tubes:
    - All four EL34s should show a soft orange glow at the filament structure (visible through the glass top-down).
    - Both 6GH8As should show a fainter glow (their heaters are physically smaller).
    - **No EL34 plate should be glowing red.** Without B+ this is impossible, but it's worth getting in the habit of looking.
4. **Measure heater AC across each EL34 socket** (pins 2 and 7): ~6.3 V AC on every socket.
5. **Measure heater AC at the PC-3A 6GH8A sockets** (pins 4 and 5): also ~6.3 V AC.
6. **Measure heater current draw** via the variac's ammeter (if it has one). Expected: ~6.9 A on the 6.3 V rails (4 × 1.5 A EL34 + 2 × 0.45 A 6GH8A = 6.9 A draw, but the variac's ammeter reads PRIMARY current, which scales by the turns ratio — for a typical PA-060 you'd see ~0.5 A on the primary side at full draw).

### What this confirms

- Both 6.3 V windings deliver full voltage under real load (a winding with a high-resistance joint or shorted turn will sag here, where it didn't in Session 1).
- The heater daisy chains (V2↔V3 and V6↔V7) are intact end-to-end; if one were open, that side's tubes would be dark.
- The PC-3A board's heater wiring reaches the 6GH8A sockets correctly.
- No wiring fault that would draw catastrophic current at full mains.

### What this does NOT yet test

- The HV rectification (no 5AR4).
- The 5 V winding under load (no 5AR4 to draw it).
- Any tube biasing or audio operation.

!!! tip "4-ch scope: heaters under load + the 180° CT relationship"
    Probe (AC-coupled, 5 V/div):

    - **Ch1**: V2 pin 2
    - **Ch2**: V3 pin 2 (the daisy-chained side of the green pair)
    - **Ch3**: V7 pin 2
    - **Ch4**: V6 pin 2

    What you should see: clean 60 Hz sine waves at ~9 Vp-p on all four channels. **Ch1 ↔ ch2 in phase** (V2 and V3 share the same heater node via the daisy), **ch3 ↔ ch4 in phase** (V7 and V6 likewise), and the two channel pairs (left vs right) **independent in phase** (no relationship between green-winding and brown-winding waveforms because they're separate windings).

    What it tells you: the daisies are continuous (V2↔V3 in phase confirms that wire isn't open), and the two channels' heater rails are isolated from each other (which is why heater hum doesn't couple between channels). If V2 and V3 were *out of phase*, the daisy would be wrong (you'd have connected V2 pin 2 to V3 pin 7 or similar).

Power off. Discharge any residual charge on the heater rails (none should accumulate, but discipline matters). Wait 30 seconds. Install V1 and proceed to Session 2.

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
5. **At full mains, +1 lug should read 480-520 V DC.** Higher than the nominal 435 V because there's no load drawing current down.

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

!!! tip "4-ch scope: see rectification happen in real time"
    This is *the* showcase 4-channel measurement of the build. You can see the [B+ signal path](../signal-paths/b-plus.md) in one screen. Probe (DC-coupled — and **use HV-rated probes**, at least 10:1 attenuation; consider 100:1 for the secondary):

    - **Ch1**: V1 pin 4 (one HV plate / red lead from PA-060) — set to 200 V/div, AC-coupled is fine here
    - **Ch2**: V1 pin 6 (the other HV plate / other red lead) — same settings
    - **Ch3**: V1 pin 8 (5AR4 cathode = filter cap lug 2) — set DC-coupled, 200 V/div
    - **Ch4**: filter cap lug 1 (after the choke) — DC-coupled, 200 V/div

    What you should see (with the variac at full mains, 5AR4 warmed up):

    - **Ch1 and ch2** are sine waves at 60 Hz, ~510 Vp (~360 Vrms) — **180° out of phase** with each other (the center-tapped HV secondary).
    - **Ch3** is **nearly smooth DC just under the ~500 V peak** of the half-winding. With no load, the lug 2 cap charges up to the peak and barely discharges between cycles — the textbook "120 Hz pulsating DC" humps only appear once the amp is drawing real current. At idle you'll see just a faint 120 Hz ripple riding on the DC.
    - **Ch4** sits at essentially the **same ~500 V level** as ch3. With no load current there's no drop across the choke, and the choke + lug 1 cap filter the already-faint ripple down further (mV-level).

    What it tells you: the rectifier is doing full-wave rectification (the faint ripple on ch3 is at 120 Hz — two charging events per 60 Hz cycle), and the LC filter is doing its job (the difference in residual ripple between ch3 and ch4 is the suppression). If the ch3 ripple is at *60 Hz* instead, one anode is dead (or its diode connection is broken — see the [rectifier diode mod](../modifications/rectifier-diode-mod.md) for series-diode failure modes).

Power off. Discharge filter caps. Wait 30 seconds.

## Session 3 — driver tubes added

Goal: verify the driver stage works under load. The 6GH8As will draw some current, which slightly loads the supply.

### Setup

- 5AR4 still installed.
- Install both **6GH8As** in their 9-pin sockets on the PC-3A board.
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

!!! tip "4-ch scope: B+ cascade with the driver loaded"
    Probe (DC-coupled, all channels):

    - **Ch1**: filter cap lug 1 (~415 V at idle now, since drivers draw current)
    - **Ch2**: filter cap lug 4 (~375 V — after the 6.8 kΩ drop)
    - **Ch3**: filter cap lug 3 (~305 V — after the 22 kΩ drop)
    - **Ch4**: 6GH8A pentode plate (PC-3A eyelet for plate-load top) (~150–200 V at idle)

    What you should see: four cleanly-stratified DC levels, each ~50-100 V lower than the one above, each essentially ripple-free at this point (the cascade has done its work). The drop from one to the next equals (load current) × (dropping resistor) — about 40 V across the 6.8 kΩ, about 70 V across the 22 kΩ, plus the pentode plate-load drop on the board.

    What it tells you: the entire B+ cascade is wired and working. If ch2 = ch1 (no drop across the 6.8 kΩ), the 22 kΩ on the cap may be missing or shorted. If ch4 reads 305 V (same as ch3), the on-board pentode plate-load resistor is open. The cascade is the place to spot which dropping element is misbehaving — you don't need to take the chassis apart to find it.

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
3. At full mains, the cathode reading should still be very low — in the stock build you read across the shared 15.6 Ω per channel pair, and it should sit far below the 1.56 V target. (With the [individual bias pots mod](../modifications/individual-bias-pots.md) and its per-tube 1 Ω sense resistors, expect maybe 5-20 mV per tube = 5-20 mA.) That's "barely on."
4. **Watch the EL34 plates.** They should NOT be glowing red. If any plate starts glowing red, IMMEDIATELY power off and recheck the bias setup. Red-plating destroys EL34s in minutes.

### What this confirms

- All four EL34s are alive and respond to bias.
- B+ holds up under the (still light) output stage load.
- Bias supply is producing negative voltage at the grids.

!!! tip "Scope: see both EL34 pairs quiescent simultaneously"
    Probe (DC-coupled) at the cathode-sense resistors. In the stock build there are **two** probe points — one shared 15.6 Ω per channel pair (easiest at the Biaset sockets, which mirror them):

    - **Ch1**: left pair (V2/V3) cathode sense
    - **Ch2**: right pair (V6/V7) cathode sense

    (Per-tube sense points — four channels, 1 Ω each — exist only if you've done the [individual bias pots mod](../modifications/individual-bias-pots.md).)

    What you should see (with bias maximum negative, no signal): flat DC levels near 0 V — barely-conducting tubes. The two pairs should be **roughly equal** to each other.

    What it tells you: one pair being substantially different from the other means that channel is biased differently — usually a wiring fault on that pot's wiper or a grid-stopper. The multi-channel display makes the asymmetry obvious without bouncing the DMM between sockets.

    Keep this scope setup for [bias adjustment](bias-adjustment.md) — watching the cathode-sense voltage rise as you turn each pot is much more intuitive than reading single-channel DMM updates.

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
