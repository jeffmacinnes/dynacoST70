---
title: Bias path
---

# Bias path

The bias path is the **small negative-DC auxiliary supply** that holds each EL34's control grid at the right negative voltage to set its idle plate current. Without bias, an EL34 with B+ on its plate would conduct uncontrollably and melt itself within seconds.

The bias supply is the smallest power network in the amp — a few milliamps of total current — but getting it wrong has the most immediate consequences: a misbiased EL34 either red-plates (too little negative bias → tube draws too much current) or runs cold and distorts (too much negative bias → tube barely conducts).

## At a glance

```
                                                  Bias setting:
                                                  ~−40 to −55 V on each EL34 grid
                                                  (adjustable per pot)

PA-060 bias                                                   ↑
secondary (~70 Vpp)                                           │
       │                                                      │
       │ red-black lead                                       │
       ↓                                                      │
  [1N4007]   ← half-wave rectifier (step 1)                   │
       │   banded end (cathode)                               │
       │ ↓                                                    │
       │ ↑ anode                                              │
       ↓                                                      │
  ┌────────────────────────────────────────────────┐          │
  │  Seven-lug terminal strip — bias filter network│          │
  │                                                │          │
  │   lug 4 ──── [10 kΩ] ──── lug 3                │          │
  │     │                       │                  │          │
  │  [100 µF]                [100 µF]              │          │
  │     │                       │                  │          │
  │   lug 1 = ground = positive reference          │          │
  │     │                                          │          │
  │   lug 2 ──── [10 kΩ to lug 1/ground]           │          │
  └────────────────────────────────────────────────┘          │
        │              │                                      │
        │ (~−60 V DC)  │ (less-negative reference)            │
        ↓              ↓                                      │
   [bias pots: lug 1 = -60 V end, lug 3 = ground-ish end]     │
        │                                                     │
        │ wipers (lug 2)                                      │
        ↓                                                     │
   [grid-stopper 1 kΩ at each EL34] ────────────────────────→ EL34 grids (pin 5)
                                                              (V2, V3, V6, V7)
```

## Stage by stage

### Stage 1 — PA-060 bias secondary

The PA-060 has a small **bias winding** (the red-black pair) separate from the HV secondary and the heater windings. It produces ~70 V peak-to-peak AC — small compared to the 720 Vp-p HV secondary, but plenty for a bias supply.

One end of this winding goes through the 1N4007 rectifier; the other end ties to the bias-supply ground (lug 1 of the 7-lug strip, which is bonded to chassis ground via [step 23](../build/output-stage/step-23-bias-ground.md)).

### Stage 2 — 1N4007 half-wave rectifier

The bias supply uses **half-wave** rectification (one diode, conducting on every other half-cycle) because the load is tiny — a few mA of grid current at most — and the resulting ripple is easy to filter. No need for full-wave.

The 1N4007 is oriented with its **cathode (banded end) at the transformer side** and its **anode at the filter network** ([step 1](../build/power-supply/step-01-bias-diode.md) wires the cathode end, [step 25](../build/output-stage/step-25-bias-from-diode.md) wires the anode end to lug 4 of the 7-lug strip). This is "backwards" compared to a B+ rectifier — the polarity inversion is what makes the output **negative** relative to ground.

When the transformer's red-black lead swings negative on a half-cycle, the diode conducts and pulls current *out* of lug 4 (current flows lug 4 → anode → cathode → transformer). The filter cap on lug 4 charges with the negative side up, settling at approximately the negative peak of the bias winding minus a diode drop — typically **−60 to −70 V DC**.

The original ST-70 used a **selenium rectifier** here, which the kit (and this build) replaces with a 1N4007. See [silicon diode (historical context)](../modifications/1n4007-replacement.md).

### Stage 3 — RC filter network on the 7-lug strip

The filtering happens on the [seven-lug terminal strip](../components/seven-lug-terminal-strip.md), wired in [steps 18–23](../build/output-stage/step-18-bias-jumper.md). Two RC stages:

- **First stage**: 100 µF cap on lug 4 ([step 19](../build/output-stage/step-19-bias-cap-1.md)), 10 kΩ resistor between lug 4 and lug 3 ([step 20](../build/output-stage/step-20-bias-resistor-1.md)).
- **Second stage**: 100 µF cap on lug 3 ([step 21](../build/output-stage/step-21-bias-cap-2.md)).

Each cap is wired with its **negative terminal toward the bias rail and its positive terminal toward ground** (lug 1) — opposite of the B+ filter caps, because the rail is negative. Get the polarity wrong and the cap fails (usually noisily, sometimes spectacularly).

After two RC stages, the rail on lug 3 is the **clean bias rail** — typically around −55 to −60 V DC with millivolt-level ripple. This is what feeds the bias pots.

A third element, the 10 kΩ resistor between lug 2 and lug 1 ([step 22](../build/output-stage/step-22-bias-resistor-2.md)), provides a **return path to ground** for the bias-pot voltage divider — see Stage 4.

### Stage 4 — Bias pots = voltage dividers

Each bias pot is wired as a **voltage divider** between the bias rail and the divider return:

- **Pot lug 1** = bias rail (−60 V), via [step 24](../build/output-stage/step-24-bias-pot-distribution-1.md) from 7-lug strip lug 3.
- **Pot lug 3** = divider return, via [step 26](../build/output-stage/step-26-bias-pot-distribution-2.md) from 7-lug strip lug 2 (which has the 10 kΩ to ground).
- **Pot lug 2** = wiper = the adjustable output, going to the EL34's grid.

Turning the pot moves the wiper between the −60 V end (lug 1) and the less-negative end (lug 3), letting you dial in the exact bias voltage needed to hit the target idle current for that tube. Inter-pot jumpers ([step 27](../build/output-stage/step-27-bias-pot-interconnect-1.md), [step 28](../build/output-stage/step-28-bias-pot-interconnect-2.md)) tie the left and right pots together so they share the same divider rails.

The original Dynaco design uses **two shared bias pots** (one per channel — both EL34s in a channel see the same wiper voltage). This build uses the [individual bias pots](../modifications/individual-bias-pots.md) mod, which gives each tube its own pot for finer control.

### Stage 5 — Wiper → grid stopper → EL34 grid (pin 5)

Each pot wiper carries the adjustable negative voltage to its EL34's grid via:

- A wire from the wiper to the EL34 socket pin 5.
- A 1 kΩ **grid stopper** resistor at the socket itself ([step 37](../build/output-stage/step-37-grid-stoppers.md)) — between pin 5 (grid) and pin 6 (internal connection), which suppresses RF oscillation.

At pin 5, the bias voltage (−40 to −55 V depending on adjustment) is **summed with the AC audio signal** arriving from the 6GH8A phase splitter through a coupling cap. The DC bias sets the operating point; the AC signal modulates the grid around that point.

## Setting the bias

The bias voltage isn't directly measured — instead, you measure the **plate current** indirectly via a small **cathode-sense resistor** (15.6 Ω at each EL34 cathode, from [steps 31–36](../build/output-stage/step-31-v2-cathode-sense.md)). The voltage across this resistor is proportional to plate current; the target is **1.56 V** at the front-panel Biaset socket, which corresponds to 100 mA per pair (50 mA per tube).

You measure with a DMM at the front-panel Biaset socket, turn the bias pot, watch the voltage adjust, lock it in at 1.56 V. See [bias adjustment](../bring-up/bias-adjustment.md) for the procedure.

## Per-tube notes

| Tube | Channel | Cathode sense at... | Bias adjusted via... |
|---|---|---|---|
| V2 | Left | [step 31](../build/output-stage/step-31-v2-cathode-sense.md) | left bias pot (and right pot for stock; per-tube pots for individual-bias mod) |
| V3 | Left | [step 32](../build/output-stage/step-32-v2-v3-cathode-daisy.md) | same |
| V6 | Right | [step 35](../build/output-stage/step-35-v6-v7-cathode-daisy.md) | right bias pot |
| V7 | Right | [step 34](../build/output-stage/step-34-v7-cathode-sense.md) | same |

## Where it can break

| Symptom | Likely cause | DMM probe |
|---|---|---|
| EL34 red-plating immediately on power-up | Bias supply not producing voltage (open diode, open winding, shorted cap) → grids at 0 V → tubes conduct unrestricted | Probe DC at lug 4 of 7-lug strip — should be ~−60 V. If 0 V, the bias supply isn't running |
| EL34 idles way too hot | Bias voltage too low (less negative than designed) | Probe at EL34 pin 5 — should be −40 to −55 V; if less negative, suspect pot or wiring |
| EL34 idles too cold (no plate current) | Bias voltage too negative | Probe at pin 5 — if more negative than −60 V, network has a fault |
| Bias drifts over minutes | Aging filter cap (capacitance dropped, ESR up), or aging tube | Replace tubes first; if drift persists, replace bias caps |
| Won't adjust at all | Open pot, broken wiper, or broken wire from pot to grid | Probe at pot wiper while turning — voltage should change |
| Hum on output that's gone with the bias supply disabled | Bias rail not filtered enough (cap dried out) | Scope at lug 3 of 7-lug strip — should show < 50 mV AC ripple; if 1 V+, filter cap failed |

## Why bias is so easy to forget about

Bias is one of those things that's invisible until it isn't. You wire it once, set it once at bring-up, and ideally never touch it again. But two things conspire to make it drift over a tube's lifetime:

1. **Filter caps age.** Electrolytic caps lose capacitance over decades. The bias filter caps especially — they sit at relatively low voltage, but they're working caps in continuous service.
2. **Tubes age.** As a tube's cathode emission drops, its plate current at a given bias voltage drops too. You can sometimes recover by adjusting bias more positive (less negative), trading some headroom for current.

A good biennial maintenance habit: re-measure bias, re-adjust if needed. Doesn't take long; preserves the amp.

## See also

- [1N4007 silicon diode (historical)](../modifications/1n4007-replacement.md) — what replaced the original selenium
- [PA-060 power transformer](../components/pa-060-power-transformer.md) — the bias secondary winding
- [Seven-lug terminal strip](../components/seven-lug-terminal-strip.md) — the bias network's home
- [Individual bias pots modification](../modifications/individual-bias-pots.md) — the per-tube adjustment used in this build
- [Bias adjustment (bring-up)](../bring-up/bias-adjustment.md) — the procedure
- [EL34 output tube](../components/el34-output-tube.md) — what consumes the bias
- [Audio signal path](audio.md) — the AC signal that rides on top of this DC bias
