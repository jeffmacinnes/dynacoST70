---
title: PC-3A driver board
---

# PC-3A driver board

The **PC-3A** is the ST-70's small printed circuit board — about 3" × 2" — that hosts both [6GH8A driver tubes](6gh8a-driver-tube.md), one per channel, plus all the passive components for voltage amplification and phase splitting. Audio enters the board from the input jacks, gets amplified by the pentode sections, gets phase-split by the triode sections, and exits as four signals (two per channel, 180° apart) that drive the [EL34 output tube](el34-output-tube.md) grids.

It's the only printed circuit board in an otherwise point-to-point amplifier. Dynaco's reasoning was straightforward: this part of the circuit is small, dense, and identical across every amp — a PCB is the right tool for the job. The rest of the chassis stays point-to-point because it's high-voltage, high-current, and varies between chassis.

## What's on the board

| Component | Quantity | Role |
|---|---|---|
| 6GH8A tube sockets | 2 | One per channel (board-mounted 9-pin miniature; no chassis V-number) |
| Resistors | ~20 | Plate loads, cathode bias, grid stoppers, dividers |
| Coupling caps | ~6 | Between pentode plate and triode grid; between triode outputs and EL34 grids |
| Screen-feed network | 1 set per channel | Drops B+ down to the 6GH8A pentode screen voltage |
| Feedback resistor + RC | 1 per channel | Sets feedback amount and high-frequency compensation |

Modest parts count, very dense layout. Every component has only one possible location.

## Signal flow

For each channel:

1. **Input** arrives via a coupling cap at the pentode's control grid.
2. **Pentode amplifies** (gain ~50×). Its plate is loaded by a resistor going to B+ (~250-350 V), and its cathode has a bias resistor + bypass cap.
3. **Coupling cap** carries the amplified signal to the next stage's grid, blocking DC.
4. **Triode phase splitter** takes that signal and produces two outputs 180° apart. Equal-value resistors above and below the triode (~22 kΩ each) give automatic balance — see [phase splitting](../theory/phase-splitting.md).
5. **Two coupling caps** carry the two phase-split signals (one from the triode plate, one from the cathode) out to the EL34 grids.
6. **Feedback resistor** brings a fraction of the OPT 16 Ω secondary signal back to the pentode's cathode (see [feedback](../theory/feedback.md)).

That's the whole driver stage, all on this one PCB.

## Why a PCB here when the rest is point-to-point

Hafler's design philosophy was "use the right tool for each section":

- **Power supply, output tube sockets, output transformer connections** — high voltage, high current, varies between builds (tube types, mods). Point-to-point on heavy terminal lugs. Servicable forever.
- **Driver stage** — low-voltage, low-current signal path, identical in every ST-70, lots of small parts in a small space. PCB. Cheap to manufacture, consistent results.

Modern audiophile kits sometimes do the entire driver and input stage point-to-point ("turret board" or eyelet board construction) for ideological reasons. The PC-3A approach is the pragmatic one: a PCB for the dense small-signal stuff, point-to-point for the heavy lifting.

## Versions

The original Dynaco ST-70s shipped with several PC-3A revisions over the years. The two most-cited:

- **PC-3A "Version A"** — uses 7199 tubes (also a pentode + triode, different pinout).
- **PC-3A "Version B"** — uses 6GH8A tubes (this build).

The boards aren't electrically identical — different tubes have different pinouts and component values. If you're rebuilding a vintage ST-70, identify which version you have BEFORE ordering parts.

This build uses Version B with 6GH8A tubes.

## Failure modes

After 40+ years of thermal cycling and capacitor aging, *every* original PC-3A has issues. Common ones, in order of likelihood:

### Coupling caps gone leaky (the #1 issue)

The coupling caps between stages were originally paper-in-oil or early film caps. After decades, the dielectric breaks down slightly, letting a tiny DC current flow through. That DC current shows up at the next stage's grid — which is supposed to be biased to a specific negative voltage. Even a small leakage current through a high-value grid resistor drops a meaningful voltage and shifts the operating point.

Symptoms:

- EL34 bias drifts upward (tubes run hot).
- One channel sounds different than the other.
- Distortion at low signal levels.
- In bad cases, EL34s red-plate within minutes of warm-up.

Fix: **replace all coupling caps**. This is the FIRST thing to do on any vintage PC-3A. Modern polypropylene or polystyrene caps are inexpensive and last essentially forever. Use 600 V rated parts for the inter-stage couplings; the actual voltages are nowhere near that, but headroom is free insurance.

### Drifted resistors

Carbon composition resistors (the originals) drift in value over time — usually up, sometimes down. A 470 kΩ grid-stopper that's drifted to 600 kΩ throws off the bias network.

Fix: measure every resistor on the board (with the tube out and power off). Replace any that's ±10 % off marked value. Use modern metal-film or carbon-film parts.

### Cracked solder joints

The PCB sees a lot of thermal cycling — tubes get hot, board expands; tubes cool, board contracts. Solder joints develop tiny fatigue cracks over decades. The classic symptom: intermittent crackling that goes away when you touch a particular tube or wiggle the chassis.

Fix: **reflow every solder joint on the board.** This sounds tedious; it takes maybe 30 minutes and is the cheapest reliability upgrade you can do. Use 60/40 leaded solder for ease (lead-free flows badly when reworking old joints).

### Tube socket pin tension

The PCB-mounted sockets have spring-loaded contacts that grip the tube pins. After many tube swaps, the springs lose tension and the pins make intermittent contact.

Fix: a small jeweller's screwdriver can be used to GENTLY squeeze the socket contacts back into shape. Don't overdo it — pins shouldn't be hard to insert, just snug.

## Standard rebuild workflow

If your PC-3A is original and untouched, the canonical rebuild is:

1. **Photograph the board** before doing anything. You'll want this reference.
2. **Replace all coupling caps** (3 per channel, 6 total) with modern polypropylene 0.022-0.1 µF / 600 V.
3. **Replace any resistor that measures ±5 % or worse** off its marked value.
4. **Reflow all solder joints** on the board (every joint, no exceptions).
5. **Inspect tube sockets** for pin tension.
6. **Vacuum the board** — decades of dust is an electrical insulator that traps moisture.
7. **Reinstall and check bias** before reinstalling the EL34s.

This is a 2-3 hour job and transforms the amp. Most "this ST-70 sounds amazing now" stories are about a freshly-rebuilt PC-3A.

## The VTA driver board alternative

Tubes4HiFi sells a **VTA driver board** that's a drop-in replacement for the PC-3A. It uses different tubes (12AU7s configured as a long-tail-pair phase splitter — see [phase splitting](../theory/phase-splitting.md)) and provides:

- Wider drive voltage swing (more headroom for high-output speakers).
- Better-matched outputs to the EL34 grids.
- 12AU7 is a current-production audio tube with much wider availability than 6GH8A.
- Built around modern components (no 40-year-aged caps).

The VTA is the most popular ST-70 upgrade. It changes the amp's character somewhat — more "modern" sounding, less "Dynaco classic." Whether that's an upgrade depends on what you're after.

This build keeps the PC-3A for now. If/when we move to VTA, it's a separate documentation effort.

## In this build

The PC-3A board sits roughly centred on the chassis, between the input jacks and the EL34 sockets. It mounts on standoffs. Connections to and from the board are via short hookup wires to nearby terminal points.

Wiring steps that touch the PC-3A area come in a later section of the manual — the page-6 wiring we're doing now is power supply only. Stay tuned for the driver-stage build pages.

## See also

- [6GH8A driver tube](6gh8a-driver-tube.md) — the tubes on this board
- [Phase splitting](../theory/phase-splitting.md) — the topology the triode section uses
- [Feedback](../theory/feedback.md) — the loop that lands back at the pentode's cathode
- [EL34 output tube](el34-output-tube.md) — what the PC-3A's outputs drive
