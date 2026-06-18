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

The single best AC source on your bench: the 6.3 V heater winding of the ST-70 itself, when powered. But you don't need to power the amp to do this exercise. Instead, use a **signal generator** if you have one, or an unloaded transformer's secondary (like a 9 V wall wart, which is actually ~9 V AC at the secondary before its internal rectifier).

If you don't have either: use the scope's calibrator (it's a square wave, not a sine, but the exercise is about *triggering* and that works on any waveform).

**Setup with the calibrator (and the probe still on it):**

1. Time base: 200 µs/div (faster than 5A).
2. V/div: 1 V/div.
3. Coupling: DC.
4. Trigger source: **channel 1** (the channel you're using).
5. Trigger mode: **Auto** (vs. Normal).
6. Trigger slope: **Rising**.
7. Trigger level: **about half-way up the visible wave**. Adjust the level knob — watch a line move up and down on the screen — and put it at the middle of the wave's vertical range.

A clean square wave should appear, locked in place. As you adjust the trigger level, the rising edge moves left/right (the scope is triggering at a slightly different point on the wave), but the picture stays stable.

Now move the trigger level **above** the top of the wave or **below** the bottom. The picture loses sync and slides around. That's the trigger never finding a rising edge that crosses its level — the scope falls back to Auto mode and shows you free-running garbage.

This is the single most common scope problem: **the trigger level is set somewhere the signal never crosses.** Fix is always the same: set the level into the middle of the signal's range.

## Bench exercise 5D — AC vs DC coupling

If you have a signal generator: set it to a 1 kHz sine, 2 Vp-p, **with a 2 V DC offset** (so the wave swings from 1 V to 3 V).

If you don't have one: take a 9 V battery and a function generator app on your phone playing through a small speaker, then measure the speaker terminals (it'll have an AC signal riding on a small DC offset from the speaker's coil).

Probe the signal with the scope. In **DC coupling**, you see the wave centered on its DC offset (between 1 V and 3 V). In **AC coupling**, the DC is blocked and the wave centers on 0 V (between −1 V and +1 V).

Use cases:

- **DC coupling** when you want to know the actual voltage including any DC offset. Default mode for tracing what's happening in a circuit.
- **AC coupling** when you want to see small AC variations on top of a large DC level. Example: measuring B+ ripple — the rail is at 415 V DC with maybe 100 mV of 120 Hz ripple. In DC coupling on a 100 V/div range, the ripple is invisible (less than a pixel). Switch to AC coupling, drop to 50 mV/div, and the ripple is now full screen.

The classic AC-coupling trick for the ST-70: at bring-up, AC-couple a probe to a B+ rail and read the ripple amplitude directly. <100 mV at lug 1 = excellent supply; >1 V = ailing.

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
