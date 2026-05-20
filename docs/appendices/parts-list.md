---
title: Parts list
---

# Parts list

Per the kit manual (page 17). Use the part numbers when ordering replacements from DynakitParts.

## Major components

| Qty | Part | DynakitParts # |
|---|---|---|
| 1 | Chassis | 711004 |
| 1 | Bottom plate | 711005 |
| 1 | Cover (optional) | 711007 |
| 1 | Power transformer — PA-060 | 464006 |
| 2 | Output transformer — A-470 | 454326 |
| 1 | Choke — C-354 | 423354 |
| 7 | Octal socket | 398008 |
| 1 | Printed circuit assembly — PC-3 | 557003 |
| 1 | Quad filter capacitor (525 V) | 298906 |

## Capacitors

| Qty | Part | DynakitParts # |
|---|---|---|
| 2 | Capacitor 100 µF | 284506 |
| 2 | Disc capacitor 0.02 µF | 224403 |

The PC-3 driver board has its own components soldered to it (coupling caps, etc.) — those aren't separately listed.

## Diode

| Qty | Part | DynakitParts # |
|---|---|---|
| 1 | Diode (silicon, 1N4007-class) | 544042 |

This is the stock part — replaces the original 1959 selenium rectifier. See [historical context](../modifications/1n4007-replacement.md).

## Switches and connectors

| Qty | Part | DynakitParts # |
|---|---|---|
| 2 | Four-screw terminal strip | 374004 |
| 1 | Fuse holder | 341004 |
| 1 | Fuse — 3 A slow-blow | 342030 |
| 1 | Line cord | 322092 |
| 1 | On-off switch (SPST) | 331101 |
| 1 | Input switch (SPDT, mono/stereo) | 332202 |
| 1 | Input socket insulator | 875002 |
| 1 | Dual input socket (RCA) | 355002 |
| 2 | Potentiometer 10 kΩ (bias control) | 145103 |
| 1 | Seven-lug terminal strip | 377207 |
| 1 | Hook-up wire (bulk) | TCW-BLK |

## Resistors

| Qty | Part | DynakitParts # | Value |
|---|---|---|---|
| 2 | Cathode sense | 120150 | 15.6 Ω |
| 4 | Grid stopper | 111102 | 1 kΩ |
| 2 | Bias divider | 115103 | 10 kΩ |
| 2 | Input grid leak | 111474 | 470 kΩ |
| 1 | B+ chain dropping | 114682 | 6.8 kΩ |
| 1 | B+ chain dropping | 114223 | 22 kΩ |

## Hardware

| Qty | Part | DynakitParts # |
|---|---|---|
| 4 | Rubber feet | 859002 |
| 32 | Screw #4-40 | 611245 |
| 32 | Nut #4-40 | 614245 |
| 5 | Screw #6-32 | 612365 |
| 1 | Kep nut #6-32 | 612366 |
| 10 | Screw #8-32 | 611465 |
| 18 | Kep nut #8-32 | 614465 |
| 1 | Rubber grommet | 895003 |
| 4 | Isolation bushing | BR-T1B |
| 3 | Solder lug | 639308 |
| 2 | Cable clamp | 713001 |
| 1 | Two-lug terminal strip | 613002 |

## Tubes (not included with kit)

| Tube | Quantity | Role |
|---|---|---|
| EL-34 (or 6CA7) | 4, matched pairs | Output, V2 / V3 / V6 / V7 |
| 7199 (Type A kit) or 6GH8A (Type B kit) | 2 | Driver / phase splitter (on PC-3 board) |
| GZ-34 / 5AR4 | 1 | Rectifier, V1 |

Per page 15 of the manual, acceptable substitutes:

- **5881** or **KT-66** for the EL-34 (re-bias to 1.56 V Biaset).
- **5U4G** for the GZ-34 (note: cuts maximum power slightly).
- **6U8** or **7687** for the 6GH8A (Type B kit only). Type A kit only takes the 7199 unless you install the SA-6GH8A socket adapter.

## When ordering replacements

The manual notes that *"parts of similar type which do not change performance may sometimes be included as a matter of expediency. This will account for slight variations in value and appearance."* In practice this means the kit may ship with parts whose markings or color don't exactly match the parts-list description — as long as the value matches, it's the right part.

**Always specify Type (A) or Type (B)** when ordering replacement kits or driver boards — the two have different PC-3 board pinouts and tube specs.

## See also

- [Components](../components/index.md) — per-component deep dives
- [Tube pinouts](tube-pinouts.md) — pin-by-pin function reference
- [Transformer specs](transformer-specs.md) — full PA-060 / A-470 / C-354 data
