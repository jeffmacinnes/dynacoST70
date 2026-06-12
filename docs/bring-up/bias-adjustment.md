---
title: Bias adjustment
---

# Bias adjustment

"Setting bias" means adjusting the negative DC voltage on each [EL34](../components/el34-output-tube.md)'s control grid so the tube draws the right idle plate current — not too hot (which kills the tube), not too cold (which sounds bad). It's the single most important user-adjustable setting in the amp's life. Get it right at the start, recheck periodically, and your tubes last for years.

There are two procedures here: the **stock method** that ships with every modern DynakitParts kit, and a **modified per-tube method** if you've installed the [individual bias pots](../modifications/individual-bias-pots.md). Both arrive at the same operating point — ~50 mA per tube — they just give you different amounts of resolution.

## What "bias" actually is

The EL34's control grid (pin 5) needs to sit at a negative voltage relative to its cathode (pin 8) for the tube to operate in its linear region. The relationship between that voltage and the plate current is steep — a few volts of difference is the difference between "barely on" and "red-plating."

Typical operating point for the ST-70:

- **Grid-to-cathode bias**: −32 V DC (per voltage table on manual page 19, pin 5 of each EL34)
- **Idle plate current**: ~50 mA per tube
- **Idle plate dissipation**: ~50 mA × 410 V = 20.5 W (well under the EL34's 25 W max plate rating)

Hot/cold tradeoff:

- **Too hot** (grid less negative, e.g., −25 V → ~70 mA): tube glows visibly red on the plate, runs short on life, plate dissipation may exceed rating, can damage the tube in minutes.
- **Too cold** (grid more negative, e.g., −40 V → ~25 mA): tube runs in class B more of the time, more crossover distortion, less "class A" sweetness at low listening volumes.

The sweet spot is roughly 50 mA — far enough below max dissipation for tube longevity, hot enough for class A operation at quiet listening levels.

## Measurement method — why a sense resistor

Direct measurement of cathode current is hard because the EL34 cathode is internally connected (no separate test point). The trick: put a small precision resistor (the **cathode sense resistor**) between cathode and ground, then measure the **voltage** across it. Use Ohm's law to convert to current:

`I_cathode = V_measured / R_sense`

The stock and modified methods differ in *where* that sense resistor sits and *whose current* it sums.

---

## Stock method (per the manual, page 11-12) — "Dyna Biaset"

This is what you do if you built the amp as Dynaco specifies, with no bias-related modifications.

### How the stock circuit is wired

- **One 15.6 Ω 1% precision resistor per channel** — between the two EL34s' joined cathodes and chassis ground. So the resistor sees the *combined* cathode current of both tubes in the pair (V2+V3 share one resistor; V6+V7 share the other).
- **One 10K bias potentiometer per channel** — drives the grids of both EL34s in that channel from the same control. So the two tubes in a channel get the *same* grid voltage.
- The voltage across the 15.6 Ω resistor is wired over to **pin 8 of the corresponding Biaset socket** on the front panel (V4 for the left channel, V5 for the right channel). That's the probe point.

Target reading: **1.56 V DC** across the 15.6 Ω resistor.

`1.56 V / 15.6 Ω = 100 mA combined cathode current = 50 mA per tube` (assuming the two tubes in the pair are matched).

### Setup

- All four EL34s installed.
- 5AR4 installed.
- Amp powered on, fully warmed up (~15 minutes from cold per the manual).
- Both bias pots at **maximum negative** (least current) before warm-up, to be safe.
- DMM on **DC volts, 4 V or 20 V range**.
- One DMM probe to chassis ground (alligator clip preferred — keeps both hands free; follows the [one-hand rule](../test-equipment/high-voltage-safety.md#one-hand-rule)).
- Small screwdriver matched to the bias pots' adjustment slots.

### Procedure

#### Step 1 — Probe pin 8 of the left Biaset socket (V4)

Insert the positive DMM probe into the pin 8 hole of the V4 socket on the front panel (the left Biaset socket). Black probe to chassis ground.

The DMM should read somewhere between 0 V and ~1.5 V. Exactly *where* depends on where the bias pot started.

#### Step 2 — Adjust the left bias pot slowly

Turn the **left bias pot** SLOWLY in the direction that makes the reading rise (the "less negative grid voltage" direction — which way that is depends on the pot's orientation; try a small move and see which way the meter moves).

Stop when the reading is **1.56 V**.

Take your time. The reading may drift over a few seconds as the tubes respond to the change. Let it settle, re-adjust if needed.

#### Step 3 — Repeat for the right channel

Move the positive probe to pin 8 of the V5 (right Biaset) socket. Adjust the right bias pot until that reading is also 1.56 V.

#### Step 4 — Iterate

Once both channels read 1.56 V, go back and re-check the left. The two channels share the B+ supply, so adjusting one slightly affects the other. Expect 1-2 rounds of small adjustments to settle both at 1.56 V.

#### Step 5 — Let it cook

Leave the amp running for 30-60 minutes. Tubes drift somewhat as their internals reach full thermal equilibrium. After this longer warm-up:

- Recheck both Biaset socket readings.
- Touch up if needed (usually 10-30 mV of drift, which equals 1-2 mA per tube — within tolerance).

This longer-soak bias is more representative of normal operating conditions than the cold-warm-up reading.

### Limitation of the stock method

The stock method gives you **per-channel** control, not **per-tube**. If your two tubes in a channel aren't perfectly matched (and even "matched quads" sold today often have ±5-10 % spread between tubes), one tube in the pair will be a bit hotter than the other. The 1.56 V at the Biaset socket is the *average* of the two — one tube might be at 55 mA while its partner is at 45 mA, averaging to 50 mA. Audible? Barely. Measurable? Yes. Worth fixing? That's what the per-tube mod is for.

---

## Modified per-tube method (with individual bias pots installed)

If you've installed the [individual bias pots modification](../modifications/individual-bias-pots.md), the circuit changes:

- **One 1 Ω 1% precision resistor per tube** (four total, one per EL34's cathode-to-ground).
- **One bias trimpot per tube** (four total, each driving one EL34 grid independently).
- The 15.6 Ω stock resistors and the two 10 K shared pots are removed.
- The Biaset sockets no longer carry useful bias info; you probe the new per-tube sense resistors directly.

Target reading: **50 mV across each 1 Ω resistor**.

`50 mV / 1 Ω = 50 mA per tube` — same operating point, just measured per-tube.

### Procedure (per-tube)

For each EL34 in turn (V2, V3, V6, V7):

1. Probe across that tube's 1 Ω sense resistor (the cathode side relative to ground).
2. Adjust that tube's trimpot until the reading is **50 mV**.
3. Move to the next tube.

After all four are at 50 mV, iterate — the B+ supply sags slightly when one tube draws more, so the others' readings drift a few mV. 1-2 rounds normally gets them all settled.

!!! tip "4-ch scope: see all four EL34 currents at once + verify bias is *quiet* DC"
    A DMM tells you the average voltage; it doesn't tell you whether that voltage is actually DC or whether it's hiding AC ripple. A scope tells you both.

    Probe (DC-coupled, 10 mV/div, time base 5 ms/div):

    - **Ch1**: across V2's 1 Ω sense resistor (or pin 8 directly to ground)
    - **Ch2**: across V3's 1 Ω
    - **Ch3**: across V6's 1 Ω
    - **Ch4**: across V7's 1 Ω

    What you should see: four flat DC traces at 50 mV (each = 50 mA idle current). All four near-identical. **Crucially: each trace should be quiet DC**, not a fuzzy band, and *not* a slow drift over the 10-second period you watch.

    What it tells you:

    - **Trace is fuzzy / has ripple riding on it**: the cathode bypass network has a bad cap, or there's hum coupling in via the heater. A few mV of ripple is acceptable; tens of mV is a problem.
    - **One trace slowly drifting** over the period you adjust the other tubes: that pot or its connections have intermittent contact, OR the tube's thermal stability is poor (early-stage cathode aging).
    - **Two traces tracking each other** as the B+ changes (load shifts): normal, this is the sag-and-iterate dynamic mentioned above.
    - **Bias settles instantly when you let go of the pot**: good. **Slow settle over seconds**: cathode bypass cap is high-ESR or undersized.

    Once all four traces sit at 50 mV with no visible AC component, you're done. This is also a great long-warmup observation: leave the scope connected for 20 minutes and watch for slow drift.

### Why per-tube bias matters

With one shared bias adjustment per channel (stock), the two tubes in a channel both get the same grid voltage, but their currents differ if their transconductances differ. With per-tube pots:

- The amp runs **more linearly** (each tube in its individual sweet spot).
- **Distortion cancels better** in push-pull (matched cathode currents = better even-harmonic cancellation).
- **Tube aging is visible** (a tube whose trimpot needs much more travel than the others is becoming weak).

The mod is one of the most worth-doing on the ST-70 platform.

---

## Bias values that mean something

### Stock method (15.6 Ω, reading combined cathode current of a pair)

| Reading at Biaset socket | Per-tube current | Verdict |
|---|---|---|
| 0.94 V | ~30 mA | Cold — class B-ish, more distortion |
| 1.25 V | ~40 mA | Cooler than ideal but workable |
| **1.56 V** | **50 mA** | **Target — class AB sweet spot** |
| 1.87 V | ~60 mA | Hot — runs warmer, shorter tube life |
| 2.20 V+ | 70 mA+ | Very hot — watch for red plate, reduce bias |

### Per-tube mod (1 Ω, reading individual cathode current)

| Reading across 1 Ω sense | Plate current | Verdict |
|---|---|---|
| 30 mV | 30 mA | Cold |
| 40 mV | 40 mA | Cooler than ideal |
| **50 mV** | **50 mA** | **Target** |
| 60 mV | 60 mA | Hot |
| 70 mV+ | 70 mA+ | Very hot — reduce bias |

If a tube's trimpot needs much more or less travel than its mates to reach the target (e.g., V2's pot wide open at 50 mA while V3's is half-way), that tube is weak — its transconductance has dropped, and it needs more drive to reach the same current. Time to replace.

## What can go wrong

### A tube red-plates as you bias it

Stop. Reduce bias to maximum negative for that tube (or both tubes in the channel, on the stock method). Power off, let it cool, investigate.

Possible causes:

- You went past the target. Bring back down.
- The tube has a gas leak or internal short — replace.
- The bias supply itself failed (no negative grid voltage). Recheck [voltage checks](voltage-checks.md). Per manual page 19, the bias diode's (B) lug should read **−65 V DC**.

### Bias drifts over an hour

A small drift (1-3 mA over 30 minutes) as the tubes fully warm is normal. A large drift (10 mA or more) means a tube isn't stable — usually a sign of:

- Heater-cathode insulation breakdown.
- Cathode emission failing (the cathode is depleted; tube has limited remaining life).
- Bias supply itself is unstable (less common — would affect all four tubes similarly).

On the per-tube mod, you can see which tube is drifting. On the stock method, you only see the channel-average drift — if one channel drifts and the other doesn't, swap one tube between channels to localize the problem.

### The pot doesn't have enough range

You can't get the reading down to target even at maximum-negative bias setting. The tubes are too hot at all available settings.

Causes:

- Tubes have very high transconductance (new and "strong" — common with fresh tubes; they often settle in after burn-in).
- The fixed series resistor in the bias divider is wrong value.
- The bias supply is producing too little negative voltage (diode partially shorted, or filter cap leaky).

You may need to add a series resistor in the bias path, or replace the diode.

### One channel sounds different

Re-bias both channels. Then if it persists, check that the OPT secondary leads are correct (different impedance taps in use, or the BLUE/BLUE-WHITE primary plate leads swapped on one channel — getting them swapped inverts that channel's polarity; the GREEN and GREEN/WHITE leads are the UL screen taps).

## Re-checking bias

Tubes drift slowly. Plan to re-bias:

- **After ~50 hours** of use (initial burn-in period).
- **Every 6 months** thereafter, or whenever you notice the amp sounding different.
- **Immediately** after any tube replacement (the new tube will be at whatever bias the previous tube was — usually wrong).
- **After any major work** on the amp (cap replacement, rectifier swap, etc.).

The procedure each time is the same as above. Should take 10 minutes once you've done it a few times.

## See also

- [Individual bias pots modification](../modifications/individual-bias-pots.md) — the mod the per-tube path depends on
- [EL34 output tube](../components/el34-output-tube.md) — what we're biasing
- [Multimeter — bias measurement](../test-equipment/multimeter.md#working-around-the-missing-functions) — DMM technique
- [Push-pull topology](../theory/push-pull-topology.md) — why matched bias matters
- [Functional testing](functional-testing.md) — what to do after bias is set
