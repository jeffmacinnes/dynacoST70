---
title: Audio signal path
---

# Audio signal path

The trace of one channel's audio signal from the RCA input jack on the rear panel to the speaker terminals (also on the rear). Six stages, two tube envelopes (one 6GH8A + two EL34s), one output transformer.

The right channel is the mirror of the left: same topology, different parts, no signal crossing between channels except through the (per-channel) feedback loop. This page describes the **left channel** for concreteness — for the right channel, substitute V6/V7 for V2/V3 and the right [6GH8A](../components/6gh8a-driver-tube.md) for the left.

## At a glance

<figure class="diagram-fig" markdown="span">
  <img src="../assets/diagrams/audio-signal-path.svg" alt="Audio signal path through one channel of the ST-70">
  <figcaption>One channel, end to end: RCA input through the 6GH8A pentode (gain), the cathodyne phase splitter, the EL34 push-pull pair, the A-470 OPT, to the speaker. Solid blue = positive-phase signal; dashed blue = the 180°-shifted signal after the phase splitter. Dashed red = the global feedback wire returning to the pentode cathode. Hover any stage for details. Click to zoom.</figcaption>
</figure>

## Stage by stage

### Stage 1 — RCA jack → input switch

Audio enters the amp on the rear panel left RCA jack (mounted in [step M2](../build/mechanical-assembly/step-m02-input-connector.md)). The center pin carries the audio signal; the shell ties to chassis-side ground.

From the RCA, the signal goes to the **input switch** ([step M3](../build/mechanical-assembly/step-m03-input-switch.md)), which selects between input modes for that channel. The switch's selected output goes to the input of the [PC-3A driver board](../components/pc-3a-driver-board.md) — wired in [step 54](../build/driver-stage/step-54-left-rca-to-input-switch.md) (RCA-to-switch) and [step 53](../build/driver-stage/step-53-eyelet-7-to-left-rca.md) (switch-to-board).

Typical signal level at this point: line level, around 1 V peak-to-peak with a "loud" source. Source impedance is whatever the source supplies (commonly a few hundred ohms from a CD player or DAC).

### Stage 2 — 6GH8A pentode (gain)

The signal arrives at the **control grid of the pentode section** of the left 6GH8A on the PC-3A board. A **1 MΩ grid leak resistor** ([step 51](../build/driver-stage/step-51-left-grid-leak.md)) ties the grid to ground — this gives the grid a DC reference at 0 V so it doesn't drift with leakage current, while presenting a high enough impedance to the source that the signal isn't loaded down.

Inside the pentode, the control grid modulates the plate current. With a plate-load resistor to B+ (~330 V), the AC swing on the grid becomes a much larger AC swing on the plate — **gain of roughly 50×**, depending on the specific tube and the operating point. See [6GH8A](../components/6gh8a-driver-tube.md#pentode-input-stage) for the topology.

The pentode's **cathode is also where the global negative feedback returns**, mixed in with the local cathode bias. See [negative feedback](negative-feedback.md) for the loop.

### Stage 3 — coupling cap to the triode

The pentode's plate sits at high DC voltage (~150–200 V), so a **coupling capacitor** is needed to pass the AC signal to the next stage while blocking that DC. The coupling cap lives on the PC-3A board between the pentode plate output and the triode section's grid input.

This is one of the components most likely to age into a problem — see [PC-3A failure modes](../components/pc-3a-driver-board.md#failure-modes). A leaky coupling cap puts DC on the next grid and skews the bias, sometimes audibly, sometimes not.

### Stage 4 — 6GH8A triode (phase splitter)

The triode section is wired as a **cathodyne** (split-load) phase splitter: equal-value resistors above and below the triode (~22 kΩ each), with the signal taken from both the plate (one output) and the cathode (the other output).

Because the same current flows through both resistors, the two outputs have **equal amplitude but opposite phase** — exactly what the push-pull output stage needs. See [phase splitting](../theory/phase-splitting.md) for the full derivation and why cathodyne self-balances.

After the triode, the signal exists as **two complementary copies, 180° out of phase**, ready to drive the two EL34 grids.

### Stage 5 — coupling caps + grid stoppers → EL34 grids

Each of the triode's two outputs goes through its own coupling cap (blocking the high triode-section DC) and out of the PC-3A board to an EL34 grid:

- One output → V2 grid, via [eyelet 1 → V2](../build/driver-stage/step-56-eyelet-1-to-v2.md)
- The other output → V3 grid, via [eyelet 2 → V3](../build/driver-stage/step-55-eyelet-2-to-v3.md)

Just before each grid pin (pin 5), there's a **1 kΩ grid stopper resistor** ([step 37](../build/output-stage/step-37-grid-stoppers.md)) directly across pins 5 and 6 of the EL34 socket. These suppress parasitic RF oscillation, which the EL34s are otherwise prone to under high-gain conditions.

The EL34 grids also receive a **negative DC bias** (~−40 to −55 V) from the [bias supply](bias.md) — the AC signal rides on top of this DC bias, swinging the grid above and below its quiescent point.

### Stage 6 — EL34s push-pull → A-470 primary → speaker

The two EL34s (V2 and V3) operate in **push-pull**: when V2's grid goes positive, V3's grid is going negative by the same amount, and vice versa. Their plate currents swing oppositely. See [push-pull topology](../theory/push-pull-topology.md).

The plates connect to opposite ends of the **A-470 primary winding**:

- V2 plate (pin 3) → A-470 BLUE lead ([step 14](../build/output-stage/step-14-left-opt-primary.md))
- V3 plate (pin 3) → A-470 GREEN lead (same step)
- A-470 RED (center tap) → B+ via the choke (see [B+ path](b-plus.md))

EL34 screen grids (pin 4) connect to the **ultralinear taps** on the A-470 (BLUE/WHITE and GREEN/WHITE), each tap matched to the half of the winding driven by the corresponding plate. UL operation is a compromise between pentode (high power, more distortion) and triode (low distortion, less power) — see [A-470](../components/a-470-output-transformer.md).

The push-pull currents in the primary's two halves cancel any common-mode contribution and **reinforce the audio signal in the secondary**. The secondary is a low-voltage, low-impedance winding with three impedance taps (4 Ω BROWN, 8 Ω ORANGE, 16 Ω YELLOW) plus a common (BLACK), wired to the **left 4-screw rear terminal strip** in [step 12](../build/output-stage/step-12-left-opt-secondaries.md).

Speaker wires connect to the appropriate tap pair (most modern speakers: ORANGE 8 Ω + BLACK common), completing the path.

## Per-channel notes

| | Left channel | Right channel |
|---|---|---|
| Input jack | Left RCA | Right RCA |
| 6GH8A | Left socket on PC-3A | Right socket on PC-3A |
| EL34 pair | V2, V3 | V6, V7 |
| OPT | Left A-470 | Right A-470 |
| Speaker strip | Left 4-screw (back) | Right 4-screw (back) |
| Feedback loop | independent | independent |

The two channels are wholly separate from input to speaker. They only share the **power supply** (B+, heaters, bias) and the **chassis ground**. Crosstalk between channels comes from coupling through these shared supplies — minimized by good filtering (the multi-stage [B+ path](b-plus.md)) and good grounding ([grounding and hum](../theory/grounding-and-hum.md)).

## Where it can break

| Symptom | Likely cause | DMM probe |
|---|---|---|
| Channel is dead | Coupling cap open, grid leak open, broken solder joint in input wiring | Inject a 1 kHz tone at the RCA; probe AC voltage at the pentode plate, then triode plate/cathode, then EL34 grids — the signal stops where the path broke |
| Channel is distorted at low volume | EL34 bias too low (grid not negative enough), driving the EL34s into clipping early | Measure bias voltage at EL34 pin 5; should be around −40 to −55 V |
| Distortion + low gain | Leaky coupling cap putting DC on the next grid | DC probe at triode grid: should be near 0 V; if positive, the previous coupling cap is leaking |
| 60 Hz hum on one channel | Heater-cathode leakage in the 6GH8A | Swap channels' 6GH8As; if hum follows the tube, replace it |
| One side of push-pull silent | Coupling cap to one EL34 open, or grid stopper failed | Probe AC voltage at each EL34 grid; should be roughly equal magnitudes |
| Sounds boomy / loose at LF | Bad coupling cap, or filter cap section feeding that stage dried out | Scope the stage; LF cutoff should be < 20 Hz |

## See also

- [6GH8A driver tube](../components/6gh8a-driver-tube.md) — what's inside the envelope
- [EL34 output tube](../components/el34-output-tube.md) — the push-pull pair's specs and pinout
- [A-470 output transformer](../components/a-470-output-transformer.md) — primary topology and secondary taps
- [PC-3A driver board](../components/pc-3a-driver-board.md) — what's on the PCB and what's not
- [Phase splitting](../theory/phase-splitting.md) — the cathodyne topology in detail
- [Push-pull topology](../theory/push-pull-topology.md) — what the EL34 pair is doing
- [B+ signal path](b-plus.md) — what feeds the plates and screens
- [Negative feedback](negative-feedback.md) — the closed loop riding alongside this signal path
