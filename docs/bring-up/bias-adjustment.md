---
title: Bias adjustment
---

# Bias adjustment

"Setting bias" means adjusting the negative DC voltage on each [EL34](../components/el34-output-tube.md)'s control grid so the tube draws the right idle plate current — not too hot (which kills the tube), not too cold (which sounds bad). It's the single most important user-adjustable setting in the amp's life. Get it right at the start, recheck periodically, and your tubes last for years.

## What "bias" actually is

The EL34's control grid (pin 5) needs to sit at a negative voltage relative to its cathode (pin 8) for the tube to operate in its linear region. The relationship between that voltage and the plate current is steep — a few volts of difference is the difference between "barely on" and "red-plating."

Typical operating point for the ST-70:

- **Grid-to-cathode bias**: −36 to −42 V DC
- **Idle plate current**: ~50 mA per tube
- **Idle plate dissipation**: ~50 mA × 450 V = 22.5 W (well under the EL34's 25 W max plate rating)

Hot/cold tradeoff:

- **Too hot** (grid less negative, e.g., −30 V → ~70 mA): tube glows visibly red on the plate, runs short on life, plate dissipation may exceed rating, can damage the tube in minutes.
- **Too cold** (grid more negative, e.g., −50 V → ~25 mA): tube runs in class B more of the time, more crossover distortion, less "class A" sweetness at low listening volumes.

The sweet spot is roughly 50 mA — far enough below max dissipation for tube longevity, hot enough for class A operation at quiet listening levels.

## Measurement method

Direct measurement of cathode current is hard because the EL34 cathode is internally connected (no separate test point). The trick: put a small precision resistor (the **cathode sense resistor**) between cathode and ground, then measure the **voltage** across it. Use Ohm's law to convert to current:

`I_cathode = V_measured / R_sense`

For the [individual bias pots mod](../modifications/individual-bias-pots.md), this build uses 1 Ω 1 % cathode sense resistors. So:

- 50 mA target × 1 Ω = **50 mV across the resistor**
- Read this with the DMM on its 4000 mV (or 200 mV) range
- Adjust the trimpot to dial in 50 mV per tube

Without the individual bias pots mod, you have one shared bias adjustment for all four EL34s. In that case, the procedure measures the average current across all four tubes and you compromise on a single setting — see the stock Dynaco manual.

## Setup

- Amp powered on, fully warmed up (~5 minutes from cold).
- All four EL34s installed and biased at maximum NEGATIVE (least current) at first.
- DMM on **DC volts, 200 mV or 4000 mV range**.
- Probe leads with alligator clips (preferred — leaves both hands free, follows the [one-hand rule](../test-equipment/high-voltage-safety.md#one-hand-rule)).
- Small flathead or Phillips screwdriver (for trimpot adjustment — match the type your trimpots use).

## Procedure

Work through one tube at a time. Don't try to adjust multiple tubes simultaneously.

### Step 1 — Probe across the sense resistor for tube #1 (V2)

Clip the black DMM lead to chassis ground. Touch the red probe to the test point that gives you the voltage across V2's cathode sense resistor (in practice: the cathode side of the resistor, with the other side at ground).

DMM should read 0-50 mV — somewhere in that range depending on starting bias.

### Step 2 — Adjust V2's bias pot

With the DMM still reading V2's cathode voltage:

- Turn the V2 bias pot SLOWLY in the "less negative grid" direction. The cathode voltage rises (tube conducts more).
- Stop when the voltage reads **50 mV** (= 50 mA cathode current = 50 mA target plate current).

Take your time. The reading may drift over a few seconds as the tube responds to the change. Let it settle, re-adjust if needed.

### Step 3 — Move to V3, V6, V7

Repeat steps 1-2 for the other three EL34s. Each tube has its own bias pot and its own sense resistor.

### Step 4 — Iterate

Once all four tubes are at ~50 mV, go back to V2 and check it again. The tubes interact slightly via the shared B+ supply (one tube drawing more current sags B+ slightly, which changes the others' operating points). So expect to do 1-2 rounds of small adjustments to settle all four at 50 mV.

### Step 5 — Let it cook

Leave the amp running for 30-60 minutes. Tubes drift somewhat as their internals reach full thermal equilibrium. After this longer warm-up:

- Recheck each tube's cathode voltage.
- Touch up if needed (usually 1-3 mV of drift, which equals 1-3 mA — within tolerance).

This longer-soak bias is more representative of normal operating conditions than the 5-minute cold bias.

## Bias values that mean something

| Reading across 1 Ω sense | Plate current | Verdict |
|---|---|---|
| 30 mV | 30 mA | Cold — class B-ish, more distortion |
| 40 mV | 40 mA | Cooler than ideal but workable |
| 50 mV | 50 mA | **Target** — class AB sweet spot |
| 60 mV | 60 mA | Hot — runs warmer, shorter tube life |
| 70 mV+ | 70+ mA | Very hot — watch for red plate, reduce bias |

If a tube's needed bias setting is wildly different from its mates (e.g., V2 hits 50 mA at the trimpot wide open while V3 reaches 50 mA at the trimpot half-way), that tube is weak — its transconductance has dropped, and it needs more drive to reach the same current. Time to replace.

## What can go wrong

### A tube red-plates as you bias it

Stop. Reduce bias to maximum negative for that tube. Power off, let it cool, investigate.

Possible causes:

- You went past the target. Bring back down.
- The tube has a gas leak or internal short — replace.
- The bias supply itself failed (no negative grid voltage). Recheck [voltage checks](voltage-checks.md).

### Bias drifts over an hour

A small drift (1-3 mA over 30 minutes) as the tube fully warms is normal. A large drift (10 mA or more) means the tube isn't stable — usually a sign of:

- Heater-cathode insulation breakdown.
- Cathode emission failing (the cathode is depleted; tube has limited remaining life).
- Bias supply itself is unstable (less common — would affect all four tubes similarly).

If one tube drifts and the others don't, that one tube is the problem.

### The pot doesn't have enough range

You can't get the cathode voltage down to 50 mV even at maximum-negative bias setting. The tube is too hot at all available settings.

Causes:

- Tube has very high transconductance (new and "strong" — common with fresh tubes).
- The fixed series resistor in the bias divider is wrong value.
- The bias supply is producing too little negative voltage (1N4007 partially shorted, dropping voltage, etc.).

You may need to add a series resistor in the bias path, or replace the diode.

### One channel sounds different

Re-bias both channels. Then if it persists, check that the OPT secondary leads are correct (different impedance taps in use, or BLUE/BROWN primary swapped on one channel).

## Re-checking bias

Tubes drift slowly. Plan to re-bias:

- **After ~50 hours** of use (initial burn-in period).
- **Every 6 months** thereafter, or whenever you notice the amp sounding different.
- **Immediately** after any tube replacement (the new tube will be at whatever bias the previous tube was — usually wrong).
- **After any major work** on the amp (cap replacement, rectifier swap, etc.).

The procedure each time is the same as above. Should take 10 minutes once you've done it a few times.

## Why per-tube bias matters

With one shared bias adjustment (stock ST-70, no [individual bias pots mod](../modifications/individual-bias-pots.md)), all four tubes get the same grid voltage. But real tubes have ±10-20 % variation in transconductance — so the four tubes draw different currents at the same grid voltage. Half are biased too hot, half too cold.

With individual pots, every tube gets dialed to its own target. The amp:

- Runs more linearly (each tube in its sweet spot).
- Cancels distortion better in push-pull (matched currents = better even-harmonic cancellation).
- Tells you when a tube is dying (its trimpot needs much more or less than the others).

The mod is one of the most worth-doing on the ST-70 platform.

## See also

- [Individual bias pots modification](../modifications/individual-bias-pots.md) — the mod this procedure depends on
- [EL34 output tube](../components/el34-output-tube.md) — what we're biasing
- [Multimeter — bias measurement](../test-equipment/multimeter.md#working-around-the-missing-functions) — DMM technique
- [Push-pull topology](../theory/push-pull-topology.md) — why matched bias matters
- [Functional testing](functional-testing.md) — what to do after bias is set
