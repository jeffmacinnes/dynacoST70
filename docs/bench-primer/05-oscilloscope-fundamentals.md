---
title: 5. The oscilloscope
---

# Exercise 5 — The oscilloscope

## The concept

A DMM gives you one number, averaged over some time window. A scope shows you the **voltage waveform** — how a signal varies with time. It is the single most powerful diagnostic tool on the bench, and almost every "is this circuit doing what I think?" question is answered by a scope picture in five seconds.

The four knobs that matter most:

1. **Time base (s/div)** — sets the horizontal axis. How many seconds (or ms, µs) each grid division represents. Bigger numbers = wider time window, slower-looking signals.
2. **Vertical sensitivity (V/div)** — sets the vertical axis. How many volts each grid division represents. Smaller numbers = more zoom on small signals.
3. **Coupling (DC / AC / GND)** — DC shows the actual voltage (signal + DC offset). AC blocks DC and shows just the AC variation. GND shows nothing (used to find the 0 V reference line).
4. **Trigger** — tells the scope *when* to start drawing a sweep. A correctly-set trigger gives you a still picture instead of a smeared jumble.

The most important thing to internalize: **without a stable trigger, the picture is useless.** Most "my scope is broken" calls turn out to be trigger problems.

## The probe — start here

Use a **10× passive probe** for almost everything. The probe attenuates the input by 10× (so a 100 V signal looks like 10 V to the scope) but presents a 10 MΩ impedance to the circuit being measured (vs. 1 MΩ for a direct lead). On most scopes you tell it the probe ratio in the channel menu, and it shows you the *actual* (un-attenuated) voltage on screen.

Probe rating matters. A typical 10× probe is rated for **300–400 V CAT II at DC**, derating with frequency. Don't probe the ST-70's B+ rail (435 V) without checking your probe's spec — and if you need to measure higher than the probe is rated for, use a **100× HV probe** (rated 1.5 kV+ typical). See [probes](../test-equipment/probes.md).

The probe also has a **compensation adjustment** — a small screw on the probe body. If it's miscompensated, square waves look like roofs (rising) or U-shapes (falling). Every scope has a built-in square-wave calibration output (usually a 1 kHz square wave at a few hundred mV); touch the probe to it, adjust the compensation screw with a small screwdriver until the square wave has sharp, flat edges. Do this once when you set up the scope and you can forget about it.

## Bench exercise 5A — first probe, the calibrator

**Setup:**

1. Power on the scope. Set channel 1 to 10× probe, DC coupling, 0.5 V/div, 500 µs/div.
2. Find the calibration test point on the scope (often a small metal tab labeled "CAL" or "1 kHz / 5 Vp-p" or similar — look near the bottom front).
3. Clip the probe ground to the chassis ground point near the test point.
4. Touch the probe tip to the calibrator.

You should see a clean square wave: 5 V peak-to-peak (or whatever your scope's cal is rated), about 2 cycles across the screen (since 1 kHz period = 1 ms = 2 divisions at 500 µs/div).

If the wave looks tilted (corners not crisp), adjust the **compensation screw** on the probe body until the corners are sharp. Done.

**Now play with the knobs:**

- Change V/div. Watch the wave get taller or shorter.
- Change time base. Watch more or fewer cycles fit on screen.
- Change coupling to AC. The wave should look the same (it's already centered on 0 V, so AC and DC look identical). On a signal with a DC offset (next exercise), they'll differ.
- Change coupling to GND. The trace should snap to a horizontal line — that's the 0 V reference. Use this often to remind yourself where 0 V is on the screen.

## Bench exercise 5B — measure a DC voltage with the scope

Yes, the scope can measure DC. It just measures the *vertical position* of the trace relative to the 0 V baseline.

**Setup:**

1. Probe ground to battery −, probe tip to battery +.
2. Set DC coupling, time base 500 µs/div, V/div 2 V/div.

The trace should jump up to **4.5 divisions above the 0 V baseline** = 9 V. That's it.

This is sometimes useful for noisy DC signals — you can see if the "DC" you're measuring has hum or ripple riding on it.

## Bench exercise 5C — first AC waveform

The single best AC source on your bench is the 6.3 V heater winding of the ST-70 itself, when powered. But you don't need to power the amp to do this exercise. Two paths below depending on whether you have a signal generator (or a software equivalent). Both arrive at the same goal: a clean, stable waveform on screen, and confidence with the trigger.

### Path A — If you have a signal generator (hardware or software)

A "signal generator" here can be any of:

- A bench function generator (BNC output).
- A USB function generator (Analog Discovery, OWON, etc.).
- A **software signal generator running on your Mac**: REW (Room EQ Wizard) or Audacity will produce a clean sine on the headphone output. See [test equipment / signal sources](../test-equipment/index.md) for setup notes.

**Settings:**

- **1 kHz sine wave**, amplitude **~0.5 V to 2 V peak-to-peak** (whatever your source can give you).
- Output it via the appropriate connector for your scope: BNC-to-BNC, BNC-to-banana, or **3.5 mm headphone jack → TRS-to-dual-RCA adapter cable → exposed RCA** if you're using your Mac.

**Where to clip the scope probe's ground:** to the **return / shield / sleeve of the signal source itself**, NOT to chassis ground or wall earth or "anywhere convenient."

- **BNC source** → the BNC's outer shell. Easiest: use a BNC-to-BNC coax cable straight into the scope channel (no probe needed), or a BNC-to-clip adapter and clip the ground to the BNC shell.
- **Mac → TRS-to-RCA adapter** → the RCA's **outer ring** (the shield) is the ground. The center pin is the signal. Probe tip on center pin, ground clip on the outer ring.
- **Bare wires from a pigtail** → identify the signal wire and the ground/shield wire from the cable's wiring (or from the source's manual). Ground clip to the shield wire.

The rule beneath this rule: **the scope probe's ground clip is *electrically the scope's chassis*, which is at mains earth.** Whatever you clip it to gets tied to earth. So it must be a node that is *supposed* to be at ground potential. The signal source's own ground qualifies — it's already at or near earth. A node that is NOT at ground (a tube plate, a hot side of a floating transformer secondary, the +B rail) is *never* a valid place to put the ground clip; you'll short that node to earth through the probe and either pop the probe, damage the source, or worse. We'll revisit this rule at bring-up.

**Scope setup:**

1. Time base: **500 µs/div** (so ~2 cycles of 1 kHz fit on screen).
2. V/div: **0.2 V/div** (start sensitive; adjust to fit the wave).
3. Coupling: **DC**.
4. Trigger source: the channel you're probing on (usually CH1).
5. Trigger mode: **Auto**.
6. Trigger slope: **Rising**.
7. Trigger level: **mid-amplitude of the wave** (turn the level knob and put the indicator line through the middle of the sine).

A clean, stable sine should lock in place. Confirm: amplitude matches what the generator is set to (within probe ratio); period is 1 ms (1 / 1 kHz); 2 cycles visible. Then proceed to **the trigger experiment** below.

### Path B — If you don't have a signal generator

Use the scope's built-in **calibration output** as the test signal. It's a square wave (typically 1 kHz, a few hundred mV to 5 Vp-p — check your scope's spec), but that's perfectly fine for the trigger exercise — triggering works on any waveform with a clean crossing.

The probe should already be on the calibrator from exercise 5A. If not: probe tip on the calibration test point, ground clip on the chassis ground tab next to it.

**Scope setup:**

1. Time base: **200 µs/div**.
2. V/div: **1 V/div**.
3. Coupling: **DC**.
4. Trigger source: the channel you're probing.
5. Trigger mode: **Auto**.
6. Trigger slope: **Rising**.
7. Trigger level: **mid-amplitude of the wave**.

A clean square wave should lock in place. Now proceed to **the trigger experiment**.

### The trigger experiment (do this regardless of path)

With the wave locked stable, slowly adjust the **trigger level** knob. Watch the indicator line move up and down across the wave; the picture stays still but the rising edge shifts left or right because the scope is triggering at a slightly different point on the same wave each sweep.

Now move the trigger level **above the top** of the wave (or **below the bottom**). The picture loses sync and slides around. That's the trigger never finding a rising edge that crosses its level — the scope falls back to Auto mode and shows you free-running garbage.

This is the single most common scope problem: **the trigger level is set somewhere the signal never crosses.** Fix is always the same: set the level into the middle of the signal's range.

## Bench exercise 5D — AC vs DC coupling

Goal: see what AC coupling actually *does* by comparing the same signal on both settings. You need a signal that has an AC component riding on a DC offset.

### Path A — If you have a signal generator with DC offset capability

Bench function generators and most software signal generators include a DC offset control.

- **Settings:** 1 kHz sine, 2 Vp-p, **with a 2 V DC offset** (the wave swings from +1 V to +3 V).
- Probe the source the same way as 5C (signal at the source, ground clip on the source's ground/shield).

### Path B — If your sig gen has no DC offset (most software gens)

Build a tiny adder circuit on the breadboard that sums a software-generated AC signal with a DC source from a battery.

- Software gen produces an AC sine on the Mac's headphone output.
- Run the signal through a **10 µF film cap** (or any non-electrolytic, the polarity doesn't matter), then to your breadboard node X.
- Tie node X through a **100 kΩ resistor** to a fresh **9 V battery's +** terminal. Tie the **battery's −** terminal to the same ground as the signal generator (Mac audio sleeve).
- Probe node X with the scope.

That circuit gives you the AC signal centered on a non-zero DC level — about **+9 V offset** with the AC riding on top. The 100 kΩ + 10 µF pair is a high-pass filter from the AC source side and a "DC injection" from the battery side; node X averages the two.

### Path C — If you have no sig gen at all

Skip 5D's quantitative exploration for now and read on. The concept is straightforward enough to grok without a personal demo, and you'll see AC vs DC coupling in action at bring-up when you measure B+ ripple (described below). If you want to try something approximate, use the scope's calibrator (a square wave) and watch how AC coupling shifts its average to zero — the square's DC offset to ground goes away in AC mode.

### What you should see (path A or B)

In **DC coupling**, the wave sits centered on its DC offset (between +1 V and +3 V for path A, or between roughly +8 V and +10 V for path B). The whole wave is shifted up by the offset.

In **AC coupling**, the DC is blocked at the scope's input by an internal series capacitor, and the wave centers on **0 V** (between −1 V and +1 V for path A, between −1 V and +1 V for path B — the offset goes away, leaving only the AC swing).

Use cases:

- **DC coupling** when you want to know the actual voltage including any DC offset. Default mode for tracing what's happening in a circuit.
- **AC coupling** when you want to see small AC variations on top of a large DC level. Example: measuring B+ ripple — the rail is at 415 V DC with maybe 100 mV of 120 Hz ripple. In DC coupling on a 100 V/div range, the ripple is invisible (less than a pixel). Switch to AC coupling, drop to 50 mV/div, and the ripple is now full screen.

The classic AC-coupling trick for the ST-70: at bring-up, AC-couple a probe to a B+ rail and read the ripple amplitude directly. <100 mV at lug 1 = excellent supply; >1 V = ailing.

## Reading the scope's auto-measurements

Most digital scopes can compute and display measurements *from* the waveform in real time — vertical voltage stats, horizontal timing stats, and pulse-shape stats. You enable them via a **Measure** button (sometimes a "Measurements" menu). Pick which channel to measure on, then add the specific measurements you want.

These are the ones you'll actually use at the bench. Names vary slightly by manufacturer (Rigol, Siglent, Tektronix, Keysight all use different conventions), but the underlying quantities are the same.

### Vertical (voltage) measurements

| Measurement | What it tells you | Useful for |
|---|---|---|
| **Vmax** | Highest instantaneous voltage in the visible window | Spotting peak excursions and clipping |
| **Vmin** | Lowest instantaneous voltage | Same, on the negative side |
| **Vp-p** (Vpp, peak-to-peak) | Vmax − Vmin — total vertical swing of the waveform | The single most-quoted AC signal level |
| **Vamp** (Vamplitude) | Peak-to-peak of the *AC component* only, ignoring spikes — basically Vtop − Vbase, where Vtop is the steady "high" level and Vbase is the steady "low" level (smarter than Vmax − Vmin when there's ringing on the edges) | Square-wave amplitude, signal level on a noisy waveform |
| **Vmean** (Vavg, Vaverage) | Arithmetic mean voltage of the visible window — equals the DC component of the signal | DC offsets, bias voltages, the midpoint of a symmetric AC waveform riding on DC |
| **Vmid** (Vcenter) | Geometric center of the vertical excursion: (Vmax + Vmin) / 2. Equals Vmean for symmetric waveforms (sine, triangle, 50%-duty square); differs for sawtooth, narrow pulses, or signals with overshoot. Not present on every scope | "Middle of the wave" interpretation, asymmetric signal analysis |
| **Vrms** | Root-mean-square voltage — equivalent DC that delivers the same heating power into a resistor | Quoting AC voltages the way the rest of the world does (e.g., "120 V mains" means 120 V RMS) |
| **Vbase / Vtop** | Steady "low" and "high" levels on a pulse or square wave, excluding overshoot/undershoot | Square wave analysis |
| **Vovershoot / Vundershoot** | Percentage by which the wave exceeds Vtop / Vbase on transitions | Ringing on edges, damping behavior |

A few important interactions with coupling mode:

- **Vmean on a DC-coupled signal**: equals the DC component of the signal.
- **Vmean on an AC-coupled signal**: equals roughly 0 V, because the scope's AC coupling blocks the DC at the input.
- **Vrms on a DC-coupled signal**: includes both DC and AC contributions — `Vrms = √(Vmean² + Vac_rms²)`.
- **Vrms on an AC-coupled signal**: includes only the AC component — equivalent to the "AC RMS" or "Vac" that you'd get from a true-RMS DMM in AC volts mode.

This is why the coupling button matters more than it looks — switching coupling changes *which numbers the measurements report*, not just where the wave sits on screen.

### Horizontal (timing) measurements

| Measurement | What it tells you | Useful for |
|---|---|---|
| **Frequency** | Cycles per second of the fundamental | Confirming oscillator frequency, identifying hum (60 Hz line vs 120 Hz ripple), test signals |
| **Period** | Time per cycle — 1 / Frequency | Same info, reciprocal form. Useful for direct timing reads |
| **Duty cycle** | For square / pulse waves, ratio of high time to total period (50% for a symmetric square) | PWM circuits, switcher analysis |
| **Rise time / Fall time** | How long the edge takes to transition between 10% and 90% of the swing | Bandwidth-limited circuits, slew rate testing |
| **Phase** | Phase difference between two channels (requires both channels active) | Comparing input and output, identifying inversion, push-pull pair balance |

### Which measurements to enable for ST-70 work

Different tasks want different measurements active. A reasonable default loadout for general bench work:

- **Vp-p** — quick signal level check
- **Vmean** — DC bias / offset
- **Frequency** — confirm test signal frequency, identify hum source
- **Vrms** — convenient for ripple measurements

Specific use cases at bring-up:

- **Heater verification (V2/V3/V6/V7 pins 2 and 7)**: Vp-p ≈ 17.8 V, Vrms ≈ 6.3 V, Frequency = 60 Hz. Quick check that the heater winding is alive and at the right voltage.
- **B+ ripple measurement (AC-coupled, on lug 1 or 2)**: Vp-p tells you the ripple amplitude directly; Frequency should be 120 Hz (full-wave rectified) — if you see 60 Hz, one rectifier leg is dead.
- **Audio signal trace (at any node along the audio path)**: Vp-p at each stage to verify gain; Frequency to confirm it's the test signal you injected and not parasitic oscillation.
- **Cathode voltage on an EL34 (DC coupled)**: Vmean gives you the steady cathode voltage, which divided by the cathode resistor gives plate current — same trick the manual uses for bias adjustment.

### Three caveats every scope-user learns the hard way

1. **Measurements are computed from what's on the screen.** If your wave is only one cycle wide, the frequency calculation has limited data and can wobble. Use a time base setting that shows at least 3–5 full cycles for stable frequency reads.
2. **Vrms/Vmean assume a periodic waveform.** A transient (a single click, a step response) doesn't have a meaningful Vrms. The measurement will still display a number; the number isn't useful.
3. **Bandwidth limit affects measurements.** If your signal has high-frequency content beyond the scope's bandwidth, Vmax and Vp-p will underread. This rarely matters for audio frequencies on any modern scope (their bandwidth is in the MHz, audio is sub-MHz), but is worth knowing.

## A few key scope rules

- **The probe ground clip is at the same potential as the scope chassis, which is at mains earth.** Never put the ground clip on a "hot" node (e.g., one side of an isolation transformer's output, or a non-grounded chassis). You will short that node to earth through the scope. The classic blown-up scope mistake.
- **Use AC coupling when measuring small AC on a large DC offset, but switch back to DC any time you're tracing signal flow or measuring an unknown.** Forgetting which mode you're in causes wrong conclusions.
- **Always set the trigger level into the signal's range** before complaining the picture is bad.
- **Use 10× probes by default**; switch to 100× only when voltage exceeds the 10× probe's rating.
- **Probe inputs are typically rated for ~300 V max with the probe on 1×**, but 3 kV+ with a 10× HV probe. Know your probe's rating; never exceed it.

## What if my number is different?

- **Picture is sliding / smeared:** trigger isn't catching. Set the level into the wave's vertical range, choose the right source (the channel the signal is on), and set the slope (rising for most signals).
- **Wave shape is wrong (square looks like a roof):** probe compensation needs adjusting. Use the calibrator and the screw on the probe body.
- **AC coupling shows a wave but DC coupling shows just a flat line:** the DC offset is so large compared to the AC that the wave is off-screen on DC. Use the vertical position knob to bring it back, or change the V/div range.
- **Wave is way too big or too small:** wrong probe ratio set in the channel menu (1× vs 10×).

## Why this matters for the ST-70

At bring-up you'll use the scope to:

- Confirm the heater AC at 6.3 V RMS (8.9 V peak) at 60 Hz on the V2/V3/V6/V7 sockets. Probe is fine here; voltage is low.
- Measure B+ ripple at lug 1, AC-coupled, with a 10× probe — should be a few hundred mV of 120 Hz sawtooth.
- Trace a 1 kHz signal through the audio path: input jack → input switch → pentode grid → triode grid → EL34 grids → OPT secondary. The signal grows in amplitude at each stage. Visual confirmation that the amp is working — and the place to spot phase reversal, clipping, or oscillation.
- Watch the cathode of an EL34 with AC coupling at full power — should be a faint replica of the input waveform (degenerative feedback action).

Each of these requires confidence with the four knobs. Spend 30 minutes on exercises 5A–5D and you'll save yourself hours later.

[Next: From bench to amp →](06-from-bench-to-amp.md)
