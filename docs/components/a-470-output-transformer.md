---
title: A-470 output transformer
---

# A-470 output transformer

The A-470 is the output transformer in the ST-70 — the part that turns the high-impedance, high-voltage AC swing on the EL34 plates into a low-impedance current that can drive a speaker. There are two A-470s in the amp, one per channel.

This build uses the Dynakit-branded Pacific Transformer reproductions, which are widely considered faithful to the original 1959 Dynaco specs.

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../assets/diagrams/a-470-windings.svg" aria-label="A-470 output transformer winding diagram">
    A-470 winding diagram (your browser does not support inline SVG).
  </object>
  <figcaption>Push-pull primary on the left (BLUE / RED CT / BROWN-primary, plus the GREEN ultralinear screen taps); speaker secondary on the right (BLACK common, BROWN 4 Ω, ORANGE 8 Ω, YELLOW 16 Ω). Hover any lead for its role. Click to zoom.</figcaption>
</figure>

*Page to be expanded.* Planned coverage:

- Primary: center-tapped, push-pull, two plate connections (blue + brown) and a B+ feed (red center tap).
- Secondary: multiple impedance taps (4Ω, 8Ω, 16Ω) plus a common (black) — different speaker loads use different tap pairs.
- The ultralinear screen tap (green) — what UL operation is and why this transformer supports it.
- Interleaving: see [how transformers work](../theory/how-transformers-work.md#what-separates-a-good-output-transformer-from-a-great-one) for why this matters.
- The original spec: −1dB from 6Hz to 30kHz at full power.
- Pacific Transformer reproductions vs. original Dynaco vs. third-party clones.
- Failure modes (very rare; output transformers in well-treated Dynacos last forever).

## Lead colors

| Lead | Purpose |
|---|---|
| Blue | Plate, one side of push-pull primary |
| Brown (primary side) | Plate, other side of push-pull primary |
| Red | Primary center tap (B+ feed) |
| Green | Ultralinear screen tap |
| Black (secondary side) | Speaker common (0Ω reference) |
| Brown (secondary side) | 4Ω secondary tap |
| Orange | 8Ω secondary tap |
| Yellow | 16Ω secondary tap |

!!! warning "Two brown leads"
    The A-470 has *two* brown leads — one is a primary plate, one is the 4Ω secondary tap. They are physically distinguishable by which end of the transformer they exit, but it's worth labeling them before installation.

## See also

- [How transformers work](../theory/how-transformers-work.md) — general theory, with focus on output transformer interleaving
- [Push-pull topology](../theory/push-pull-topology.md) — how the center-tapped primary is driven
- [Feedback](../theory/feedback.md) — the 16Ω tap is where the global feedback loop originates
- [Transformer specs](../appendices/transformer-specs.md) — at-a-glance reference
