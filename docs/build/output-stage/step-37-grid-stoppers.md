---
title: 'Step 37: Four 1 kΩ grid stoppers'
---

# Step 37: Four 1 kΩ grid stopper resistors (one per EL-34)

> *Connect one end of a 1000 ohm resistor to pin #5 of V2 (S). Connect the other end to pin #6. Repeat for V3, V6 and V7. Keep the resistor pigtails short (about ½") for all four of these resistors.* — manual page 8

## What you're doing physically

Four **1 kΩ resistors** (DynakitParts #111102), one per EL-34. Each spans **pin 5 to pin 6** of its socket. Trim leads short (~½") and mount the resistor body close to the socket — this minimises the loop area and capacitive coupling.

For each EL-34 (V2, V3, V6, V7):

- Pin 5 (control grid): soldered (S) — the resistor lands here as the only connection to pin 5 from outside.
- Pin 6 (internal connection, also brought through to make wiring convenient): NOT soldered yet — the coupling cap from the driver board will land at pin 6 later (via steps 39-40 and 55-56).

## What grid stoppers do

A "grid stopper" is a small series resistor between the audio signal source and the tube's control grid. In a pentode/beam tetrode like the EL-34, this resistor serves a crucial role:

**Stops parasitic oscillation.** The EL-34 has small internal capacitances (plate-to-grid, grid-to-cathode, etc.) that, combined with the small inductance of the grid wiring, can form an LC resonant circuit at VHF frequencies (50-200 MHz). If that resonance has enough gain through the tube, it oscillates — produces high-frequency RF that draws extra plate current, distorts the audio, and can damage the tube.

The 1 kΩ grid stopper:

- Adds resistive damping to the resonant circuit, killing the Q below the oscillation threshold.
- Forms a low-pass filter with the grid's input capacitance (Cgs + Cgp Miller'd by stage gain), rolling off the response somewhere above the audio band (50-100 kHz typically).
- Doesn't affect audio frequencies at all — at 20 kHz, the grid input capacitance is ~50 pF, with impedance of 1/(2π × 20 kHz × 50 pF) = 160 kΩ. The 1 kΩ stopper is negligible against that.

## Why pin 5 + pin 6 specifically

Pin 5 of the EL-34 is the control grid (g1) — the input you want the audio signal on.

Pin 6 is an "internal connection" pin that's wired internally to nothing in some tube variants, or to the cathode/suppressor in others. For the ST-70's wiring topology, pin 6 is used as the **coupling-cap-to-grid junction**:

- Audio signal comes from the PC-3 board → through a 0.1 µF coupling cap on the board → out to pin 6 of the EL-34 socket.
- The 1 kΩ grid stopper lives **inside the socket**, between pin 6 and pin 5.
- Pin 5 is the actual control grid.

This routing keeps the grid stopper very close to the tube (minimising the antenna effect — the wire from pin 6 to pin 5 is internal to the socket and short). If the stopper were on the PC-3 board instead, the long wire from board to socket pin would itself act as a resonant antenna.

## Why short leads matter

The 1 kΩ resistor needs to be **physically close to the tube socket**. Long leads on this resistor would re-introduce the parasitic inductance you're trying to suppress. Trim leads to ½" max, solder directly to the pin lugs.

## After step 37

The output stage is **electrically complete** through the EL-34 control grids. Audio coming into pin 5 from the PC-3 board (via pin 6 and the stopper) will be amplified by the EL-34, pushed through the OPT primary, and emerge from the OPT secondary as speaker-level output.

The next 28 steps build the PC-3A driver board side — the audio signal path FEEDING into the EL-34 grids.

## See also

- [Step 39 — Eyelet 23 to V6 pin 6](../driver-stage/step-39-eyelet-23-to-v6.md) — what feeds pin 6 from the driver board
- [EL34 output tube](../../components/el34-output-tube.md) — pin 5/6 function
- [Driver stage](../driver-stage/index.md) — what's coming next
