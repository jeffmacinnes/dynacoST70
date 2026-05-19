---
title: Reading this manual
---

# Reading this manual

This manual is organized to be navigated, not read cover-to-cover. Each page has a clear scope, and pages cross-link aggressively. You're meant to drill into whatever you need from wherever you are.

## How the sections relate

- **[Build](../build/index.md)** is the procedural spine: step-by-step wiring, in manual order.
- **[Components](../components/index.md)** pages are referenced *from* build steps. Click a component name in any step and you'll get the full story on that part.
- **[Theory](../theory/index.md)** chapters are referenced *from* both build steps and component pages. Click a concept (rectification, push-pull, etc.) and you get the conceptual deep-dive.
- **[Modifications](../modifications/index.md)** are the planned departures from stock — each gets its own page describing what changes and why.
- **[Bring-up](../bring-up/index.md)** is the post-build procedural section: powering up, checking voltages, setting bias.
- **[Test equipment](../test-equipment/index.md)** is reference material for the instruments you'll use — mostly during bring-up.

## Conventions

### Quoting the original manual

Verbatim text from the Dynaco manual is set in blockquotes with italics:

> *Connect the red-black power transformer lead to the banded side of the diode at the (2) lug terminal strip (S)*

After each verbatim instruction comes the explainer: what you're doing physically, what it accomplishes electrically, and the design reasoning.

### (S) markers

**(S)** at the end of a step means *solder this connection now*. A pin number without (S) means *make the connection but leave it unsoldered* — another wire will land on the same pin in a later step, and you'll solder them all together at once.

### Pin numbering

Pin numbers refer to the tube socket as viewed from the **wiring side** (bottom of the chassis), using standard octal or 9-pin socket numbering. This is the orientation you'll be working from while wiring.

### Voltages

- All voltages are **AC** unless explicitly noted as DC.
- "B+" refers to the high-voltage DC rail that powers the output tube plates (~450V DC nominal).

### Tube designations

This kit's manual uses a non-standard tube numbering — see the [home page](../index.md#tube-layout-this-manuals-numbering) for the full table. Always defer to this convention; some online references will differ.

## Voice and tone

- Second person ("you connect the lead..."), instructional.
- Level-2 conceptual depth: what each step accomplishes, why the circuit is designed that way.
- Tangents and "why not" alternatives are valuable, not digressions.
- Honest acknowledgment of uncertainty; defer to the manual when in doubt.

## Page anatomy: build steps

Each step page includes:

1. The verbatim manual instruction (blockquote, italics)
2. **What you're doing physically** — concrete description of the wire path
3. **What this accomplishes** — the circuit-level role of this connection
4. **Why [some design choice]** sections — the deeper reasoning
5. Cross-references: components touched, theory chapters relevant, related steps
6. Diagrams where they materially help understanding

## Page anatomy: components

Each component page includes:

1. **What it is** — physical description, where it sits in the amp
2. **Specs** — table format
3. **How it works** — brief, with links to deeper [theory](../theory/index.md) pages
4. **In this build** — where this specific component lives, what it does
5. **Failure modes** — what goes wrong, how to diagnose
6. **Alternatives and mods** — relevant substitutions or modifications
7. **References** — links to every step that touches this component, plus external resources
