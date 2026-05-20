---
title: 'Step 38: Mount the PC-3 board'
---

# Step 38: Mount the PC-3 printed circuit board

> *Mount the printed circuit board PC-3 from the bottom of the chassis. Note the numbers of the eyelets are upright when looking from the front of the chassis. Use a 4/40 screw and nut at each mounting hole. In making solder connections (See above illustration) to the PC board, all connections are made to the square solder pads. The lead wires are stripped back about ¼" and inserted into the appropriate solder pad hole. With soldering iron, heat both the exposed lead and solder pad while introducing the solder at this junction. Allow solder to flow into the solder pad hole and remove solder iron tip allowing connection to set. Insure that top board side components are clear of exposed lead and all connections are made from bottom side of the PC board. Trim extended leads after soldering.* — manual page 8

## What you're doing physically

The **PC-3 board** (the only printed circuit in the otherwise point-to-point ST-70) mounts to the underside of the chassis with two **#4-40 screws and nuts**. The board hangs in the chassis interior with its components facing DOWN (toward the chassis bottom) and its eyelets facing UP (so the eyelet numbers are readable when you flip the chassis to wire it).

**Orientation**: the eyelet numbers should read **upright when viewed from the front of the chassis**. If you mount the board rotated, all the eyelet-numbered wiring instructions become positional puzzles.

Tighten both screws firmly — the board carries the 6GH8A driver tubes and any vibration could loosen the contacts.

## What's on the PC-3 board

The board pre-soldered components include:

- Two 9-pin miniature sockets (for the 6GH8A driver tubes)
- ~20 resistors (plate loads, screen drops, cathode bias, grid stoppers)
- ~6 coupling caps
- Phase splitter network
- Feedback compensation network

For full details see the [PC-3A page](../../components/pc-3a-driver-board.md).

## Eyelet numbering

The board has **23 numbered eyelets** (small holes for solder connections to the rest of the chassis). The numbers are printed (or etched) on the board itself.

Eyelet roles (which wires land on them) get sorted out over the next 27 wiring steps. Some examples:

- Eyelets #1, #2: outputs of the phase splitter → coupling caps → V2, V3 grid stoppers
- Eyelets #22, #23: outputs of the other channel's phase splitter → V6, V7 grid stoppers
- Eyelets #19, #20: B+ feeds in (from filter cap lugs A and B)
- Eyelets #4, #5, #15, #16: heater connections to/from EL-34 sockets
- Eyelets #7, #17: input signal in from RCA jacks
- Eyelets #11, #14: feedback returns from OPT primary screen taps
- Eyelets #21, #6: bias distribution to the per-channel pots
- Eyelet #9: chassis ground (signal ground tie)
- Eyelets #12, #13: feedback origins (from OPT secondary 16 Ω taps)

## Soldering technique on PC boards

PC-board soldering is different from chassis-mount terminal soldering:

1. Strip the wire ¼" — slightly less than for terminal-mount.
2. Insert the stripped end into the eyelet hole from the bottom (component-side-up arrangement is unusual — the PC-3 has components on the *top* but is mounted with that side facing down).
3. Touch the iron to **both the wire and the solder pad simultaneously**, heating them together.
4. Apply solder at the wire/pad junction. It should flow around the wire into the pad hole quickly (1-2 seconds).
5. Remove the iron and let the joint cool without movement.
6. Trim excess lead with flush-cut wire cutters.

A bad PC-board joint looks **dull and grainy** instead of shiny and smooth. If you see that, reheat with the iron and re-flow.

## See also

- [PC-3A driver board](../../components/pc-3a-driver-board.md) — what's on the board
- [6GH8A driver tube](../../components/6gh8a-driver-tube.md) — the tubes that go on the board
- [Step 39 — Eyelet 23 to V6 pin 6](step-39-eyelet-23-to-v6.md) — the first wire to the board
