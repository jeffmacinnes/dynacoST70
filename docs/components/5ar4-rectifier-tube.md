---
title: 5AR4 rectifier tube
---

# 5AR4 rectifier tube

The 5AR4 (also called GZ34 in European nomenclature) is the high-voltage rectifier tube in the ST-70's power supply. In this build, it's a Sovtek 5AR4.

## What it is

An **indirectly heated dual-anode rectifier tube**. Inside the glass envelope are two plates (anodes), a shared cathode, and a heater filament that warms the cathode. The two-anode topology lets a single tube perform [full-wave rectification](../theory/rectification.md#full-wave-rectification-what-the-5ar4-does) of an AC supply with a center-tapped secondary.

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../assets/diagrams/5ar4-internal-structure.svg" aria-label="5AR4 internal structure">
    5AR4 internal structure (your browser does not support inline SVG).
  </object>
  <figcaption>Two anodes flanking a shared cathode, indirectly heated. Hover any internal element or pin for spec and wiring details. Click to zoom.</figcaption>
</figure>

## Specs

| Parameter | Value |
|---|---|
| Heater voltage | 5.0V AC |
| Heater current | 1.9A nominal |
| Peak inverse voltage | 1700V |
| Max DC output current | 250mA |
| Warm-up time | ~30 seconds |
| Base | Octal (8-pin) |

## Pinout (octal base, viewed from wiring side)

| Pin | Function |
|---|---|
| 1 | NC (no connection) |
| 2 | Heater |
| 3 | NC |
| 4 | Plate (anode) #1 |
| 5 | NC |
| 6 | Plate (anode) #2 |
| 7 | NC |
| 8 | Cathode + heater |

Note: pin 8 is **both** the cathode and one end of the heater. This is normal for indirectly heated rectifiers — the cathode and one heater pin share an internal connection.

## How it works

The 5AR4 has two separate plates inside the glass, each acting as the anode of its own diode, sharing one cathode (pin 8). When the high-voltage secondary's center tap is grounded (see [step 7](../build/power-supply/step-07-hv-ct.md)), the two plates take turns conducting on alternate half-cycles — full-wave rectification in a single envelope.

The two desirable properties of being **indirectly heated**:

1. **Slow warm-up** (~30 seconds before it conducts). This is a *feature*: the rectifier comes online *after* the signal tubes have warmed up, so the high-voltage B+ doesn't slam onto cold output tubes (which causes "cathode stripping" damage over time).
2. **Quieter operation** — directly-heated rectifiers can inject AC ripple from the filament into the DC output. Indirect heating isolates the cathode from the AC heater current.

For the deeper rectification theory, see [rectification](../theory/rectification.md).

## In this build

The 5AR4 occupies socket **V1**, the octal socket nearest the power transformer. Wiring steps that touch it:

- [Step 2](../build/power-supply/step-02-5ar4-heater.md) — white pair → pins 2 and 8 (heater)
- [Step 3](../build/power-supply/step-03-5ar4-anodes.md) — red pair → pins 4 and 6 (anodes)
- Pin 8 (cathode + heater) becomes the B+ rail output, feeding the filter capacitors after [step 7](../build/power-supply/step-07-hv-ct.md) completes the rectifier topology

## Failure modes

- **Slow or no warm-up** — heater open or weak emission. Tube needs replacement.
- **Arcing inside the envelope** — visible blue/purple flashes when powered up. Indicates internal short or gas; replace immediately or risk damage to downstream caps.
- **Reduced output / sag** — high cathode resistance from cathode poisoning. Common in old tubes. B+ drops more under load than expected.
- **Bright filament glow but no rectification** — heater works but emission has died. Replace.

## Alternatives

- **GZ34** — direct equivalent (same tube, European naming)
- **5U4G / 5U4GB** — earlier directly-heated dual-anode rectifier; lower PIV rating, instant warm-up. Not a drop-in substitute — the lack of warm-up delay defeats the cathode-stripping protection.
- **Solid-state rectifier plug-in** (e.g., Weber Copper Cap) — replaces the tube with diodes in a tube envelope. Higher B+, no warm-up delay, no sag character. Sonically controversial.

## See also

- [Rectification](../theory/rectification.md) — the underlying theory
- [PA-060 power transformer](pa-060-power-transformer.md) — what feeds the 5AR4
- [Filter capacitors](filter-capacitors.md) — what the 5AR4's cathode feeds
