---
title: Tube pinouts
---

# Tube pinouts

Pin functions for every tube in this build. All views are from the **wiring side** (bottom of the socket).

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/tube-pinouts.svg" alt="Tube pinout reference chart">
  <figcaption>Three tube types in this build, viewed from below the socket. Color coding: heater orange, plate blue, screen yellow, control grid purple, cathode brown, NC/IC grey. Hover any pin for spec. Click to zoom.</figcaption>
</figure>

## 5AR4 rectifier (V1)

Octal base, 8 pins.

| Pin | Function |
|---|---|
| 1 | NC |
| 2 | Heater |
| 3 | NC |
| 4 | Plate (anode) #1 |
| 5 | NC |
| 6 | Plate (anode) #2 |
| 7 | NC |
| 8 | Cathode + heater |

See [5AR4 page](../components/5ar4-rectifier-tube.md) for the dual-anode topology.

## EL34 output tube (V2, V3, V6, V7)

Octal base, 8 pins.

| Pin | Function |
|---|---|
| 1 | Internal connection / shield |
| 2 | Heater |
| 3 | Plate (anode) |
| 4 | Screen grid (g2) |
| 5 | Control grid (g1) |
| 6 | Internal connection |
| 7 | Heater |
| 8 | Cathode |

See [EL34 page](../components/el34-output-tube.md).

## 6GH8A driver / phase splitter

9-pin compactron. Mounts in board sockets on the PC-3A driver board (no chassis V-number). One per channel. *Pinout details to be filled in when this section gets fleshed out.* See [6GH8A page](../components/6gh8a-driver-tube.md).

| Pin | Function |
|---|---|
| TBD | TBD |
