---
title: B+ signal path
---

# B+ signal path

**B+** is the high-voltage DC supply that every tube plate and screen in the amp depends on. It starts as 720 V peak-to-peak AC across the PA-060's high-voltage secondary, gets rectified by the 5AR4, then cascades through a multi-stage filter network that produces progressively cleaner, progressively lower-voltage DC for each load.

By the time the build is at idle, the rail looks something like:

| Filter node | Approx. DC | Feeds |
|---|---|---|
| Just after rectifier (cap lug 2) | ~480 V | (input of the choke) |
| After choke (cap lug 1) | ~450 V | OPT primary center taps (EL34 plates + UL screens) |
| After 6.8 kΩ drop (cap lug 4) | ~370 V | first PC-3A B+ node, 6GH8A triode plates |
| After 22 kΩ drop (on PC-3A) | ~250 V | 6GH8A pentode plates and screens |

Numbers are typical — see [voltage checks](../bring-up/voltage-checks.md) for what to expect at bring-up time. The key thing is that each downstream load gets a **lower, smoother** voltage than the one upstream — the filter cap + dropping resistor cascade buys both regulation and ripple rejection at each stage.

## At a glance

```
                                  PA-060 HV secondary
                                  (~720 Vpp across)
                                       │
                            RED ─┐           ┌─ RED
                                 │ RED/YEL CT │
                                 │     │      │
                                 ↓     ↓      ↓
                              V1 pin 4 │  V1 pin 6      (optional: 1N4007 mod
                                       ↓                 in series with each plate)
                                    [ground]
                                       │
                              [5AR4 rectifier]
                                       ↓
                                  V1 pin 8 (cathode)
                                       ↓
                              [cap lug 2]  ←─ first filter section (≈480 V DC)
                                       ↓
                                   [choke]
                                       ↓
                              [cap lug 1]  ←─ second filter section (≈450 V DC)
                                  │       │
                                  ↓       └─→ to BOTH A-470 primary center taps
                                  ↓             (red leads — EL34 plates + UL screens)
                              [6.8 kΩ]   ← dropping resistor
                                  ↓
                              [cap lug 4]  ←─ third filter section (≈370 V DC)
                                  ↓
                              to PC-3A board (eyelet 19)
                                  │
                                  ↓
                              [22 kΩ on board]
                                  ↓
                              [cap lug 3]  ←─ fourth filter section (≈250 V DC)
                                  ↓
                              6GH8A pentode plates + screens
```

## Stage by stage

### Stage 1 — PA-060 HV secondary

The PA-060 [power transformer](../components/pa-060-power-transformer.md) has a center-tapped high-voltage secondary winding: two red leads at the ends of the winding, one red/yellow lead at the center tap. Across the full winding, ~720 V peak-to-peak AC at 60 Hz. From either red lead to the CT, ~510 V peak (~360 V RMS), shifted 180° between the two halves.

The CT establishes the **return reference** for the rectified current — every electron that flows out one half of the winding has to come back through the CT.

### Stage 2 — 5AR4 plates (V1 pins 4 and 6)

Each red lead wires to one of the 5AR4's anodes ([step 3](../build/power-supply/step-03-5ar4-anodes.md) — or, with the optional [rectifier diode mod](../modifications/rectifier-diode-mod.md), via a series 1N4007).

The 5AR4 is a **dual-anode full-wave rectifier**: each anode conducts during the half-cycle when its red lead is positive relative to the CT, taking turns 120 times per second. See [rectification](../theory/rectification.md) for the topology.

### Stage 3 — 5AR4 cathode → first filter cap (lug 2)

Both anodes share a single cathode at V1 pin 8. The cathode swings positive on every half-cycle of the line frequency — producing **120 Hz pulsating DC**.

A short heavy wire from V1 pin 8 to **filter cap lug 2** ([step 29](../build/output-stage/step-29-rectifier-to-filter-cap.md)) is the first place the rectified DC lands. The cap section attached to lug 2 (~30 µF, see [filter capacitors](../components/filter-capacitors.md)) starts smoothing those pulses — current is dumped *into* the cap on the peak of each pulse and drawn *out* between pulses, integrating the waveform toward a DC level.

The red/yellow CT lands at the ground reference next to the filter cap ([step 7](../build/power-supply/step-07-hv-ct.md)) to complete the loop.

### Stage 4 — choke → second filter cap (lug 1)

A wire from lug 2 goes to one end of the **choke** ([step 9](../build/power-supply/step-09-choke.md)); the other end of the choke lands on **lug 1** of the filter cap. The choke is a large inductor (~1.5 H) that resists rapid changes in current — together with the cap on lug 1 (~20 µF), it forms an **LC filter** that removes essentially all of the 120 Hz ripple.

The voltage on lug 1 sits a bit lower than lug 2 due to the choke's DC resistance (~100 Ω) and the steady current draw, but it's much smoother. This is the **clean B+ rail that feeds the output transformer primaries** — both A-470 red leads (center taps) land on lug 1 in [step 8](../build/power-supply/step-08-opt-b-plus.md).

### Stage 5 — to the OPT primary center taps

Each [A-470 output transformer](../components/a-470-output-transformer.md) has a center-tapped primary, with the center tap (RED lead) drawing B+. Current flows from lug 1 → A-470 red → through both halves of the primary → out the BLUE and GREEN plate leads → into the EL34 plates (pin 3 of V2/V3 for left, V6/V7 for right).

Because the two halves of the primary are driven by **push-pull** plate currents (one half going up while the other goes down), the *quiescent* current draw on the B+ is steady, and only the *AC* signal swings oppositely in the two halves. This is what makes push-pull so efficient at rejecting B+ ripple — see [push-pull topology](../theory/push-pull-topology.md).

The EL34 **screen grids** (pin 4) get their voltage from the UL taps (BLU/WHT and GRN/WHT), which sit at ~43% of the way from the CT to each plate — they see B+ minus some signal swing, not B+ minus a fixed drop.

### Stage 6 — 6.8 kΩ drop → third filter cap (lug 4)

A 6.8 kΩ resistor ([step 30](../build/output-stage/step-30-b-plus-dropping-resistor.md)) hops from cap lug 1 to **cap lug 4** — together with the cap on lug 4 (~20 µF), this forms an **RC filter** that drops the voltage and smooths it further. The third B+ stage typically sits around 350–380 V.

This rail is the **first PC-3A B+ feed** — wired from cap lug 4 to PC-3A eyelet 19 ([step 41](../build/driver-stage/step-41-eyelet-19-to-cap-3.md)) and then to the 6GH8A triode-section plate loads.

### Stage 7 — 22 kΩ drop on the board → fourth filter cap (lug 3)

The PC-3A board itself has another dropping resistor (22 kΩ, [step 42](../build/driver-stage/step-42-22k-dropping-resistor.md)) that feeds the **fourth filter section** at cap lug 3 via [step 43](../build/driver-stage/step-43-eyelet-20-to-cap-4.md). This is the cleanest, lowest-voltage B+ rail — ~250 V, and it powers the **6GH8A pentode plates and screens** plus the screen of the driver tube's pentode section.

Putting the input stage on the cleanest, most heavily-filtered rail is deliberate: any ripple here gets amplified by the full gain chain and ends up as audible hum at the speaker. So the input gets the "premium" supply, the EL34s (which are at the end of the chain and benefit from push-pull ripple rejection) get the "raw" supply.

## How the cascade works

Each stage is the same pattern: **drop voltage, smooth voltage**. The dropping element (choke for the first stage, resistor for the rest) plus the capacitor on the receiving lug forms a low-pass filter that:

- Reduces ripple by ~20–40 dB per stage
- Drops the DC level by an amount proportional to the load current and the dropping element's resistance
- Provides energy storage so transient current draws (like a kick drum hitting full-power) don't pull the rail down

By the time B+ has been through four stages, what arrives at the pentode plates is ~30+ dB cleaner than what came off the rectifier cathode.

## Where it can break

| Symptom | Likely cause | DMM probe |
|---|---|---|
| No B+ anywhere | 5AR4 not lit, rectifier tube failed, primary fuse open | Check primary fuse continuity; verify 5AR4 heater is glowing |
| B+ very low (e.g., 200 V at lug 2) | Filter cap shorted, or one half of HV secondary open | Disconnect lug 2 wire, measure DC across just the cap; should match HV secondary loaded behavior |
| Loud 120 Hz hum | Choke not filtering (open) or lug 2 cap dried out | Measure ripple at lug 1 with scope; should be < 1 V AC. If much higher, choke or lug 2 cap is bad |
| Hum on one channel only | Cap lug 3 or 4 section failed | Channel signals share later filter stages but EL34s share lug 1 — by elimination, hum on one channel implicates the PC-3A B+ rails |
| EL34s red-plating | B+ way too high (shorted choke leg, lost CT, etc.) OR bias too low (separate issue) | Measure B+ at lug 1: > 500 V is suspect. Also check bias supply (-50 V at EL34 pin 5) |
| Voltage at lug 4 = voltage at lug 1 | 6.8 kΩ resistor open or shorted | Measure across the resistor — should drop ~80 V at idle |
| No signal from input stage even with B+ on lug 1 | 22 kΩ on board open, or eyelet wire missing | Measure DC at the pentode plate (PC-3A); should be ~150–200 V |

For the full bring-up sequence and what to measure where, see [voltage checks](../bring-up/voltage-checks.md).

## Why the chain looks like this

It's tempting to think "just put one big cap after the rectifier and feed everything from it." It doesn't work for two reasons:

1. **Different loads want different voltages.** The EL34 plates want ~440 V; their screens (in UL) want similar; the 6GH8A triode plates want ~330 V; the 6GH8A pentode plates want ~200–250 V. You need to drop voltage between stages, which means dropping resistors, which means an RC filter at each drop.
2. **Different loads tolerate different ripple.** The EL34 plates can tolerate ~1 V ripple — it's at the end of the gain chain and the push-pull cancels much of it anyway. The pentode plates cannot — any ripple here gets multiplied by the full gain chain (50× per stage × 50× per stage × push-pull gain) and ends up as hum. So the input stage gets the most heavily filtered rail.

The cascade gives you both at once: each stage drops voltage *and* smooths it, scaling the protection to where it's needed most.

## See also

- [PA-060 power transformer](../components/pa-060-power-transformer.md) — what produces the raw HV AC
- [5AR4 rectifier tube](../components/5ar4-rectifier-tube.md) — full-wave rectification details
- [Filter capacitors](../components/filter-capacitors.md) — the quad cap that hosts lugs 1–4
- [Choke](../components/choke.md) — the inductor between the first two filter stages
- [Rectification](../theory/rectification.md) — theory behind stage 2
- [Voltage source vs current path](../theory/voltage-vs-current.md) — what "B+" actually is
- [Audio signal path](audio.md) — what this rail ultimately powers
- [Voltage checks (bring-up)](../bring-up/voltage-checks.md) — measuring all of this for real
- [Rectifier diode mod](../modifications/rectifier-diode-mod.md) — the optional 1N4007 series-diode mod that sits between stages 1 and 2
