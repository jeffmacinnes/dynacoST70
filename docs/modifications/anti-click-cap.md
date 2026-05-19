---
title: Anti-click cap
---

# Anti-click capacitor

The stock ST-70 produces a loud **click** — sometimes a thump that can sound alarming through speakers — when you flip the power switch off. There's usually a smaller click on turn-on. This isn't a defect in the amp; it's basic physics of switching an inductive load. A small RC snubber across the power switch makes it go away.

## What's actually happening

The power switch is a simple mechanical contact in series with the PA-060 primary winding. The primary is a big inductor (it's literally a coil of wire on an iron core).

When you open a switch carrying current through an inductor, the inductor *resists* the change in current. Its voltage spikes — V = L·dI/dt, and dI/dt can be enormous when contacts separate fast. The result is an arc across the opening contacts, and a huge transient voltage spike on the primary side that briefly couples capacitively (through the inter-winding capacitance) into the secondaries and from there into the audio chain.

That spike is what you hear: a fast wide-spectrum pulse that the audio circuit translates into a "click" or "thump" at the speakers.

## What the snubber does

An RC snubber is a small capacitor + resistor in series, wired across the switch contacts. When the contacts open and the voltage tries to spike, the cap absorbs the energy by charging up (instead of the energy going into an arc + radiated transient). The resistor in series limits the *inrush* current when the switch closes again (capacitor sees the AC line through R, not directly), and also damps any oscillation between the cap and the transformer's primary inductance.

The combined effect:

- No (or much smaller) arc when opening.
- Slower voltage transition across the contacts.
- Less RF radiated into the chassis from the switching event.
- Less transient coupled into the audio circuit.

Result: turning the amp off is silent, or nearly so.

## Typical values

The textbook starting point: **0.01 µF capacitor + 100 Ω resistor**, in series.

Why these values:

- At 60 Hz, 0.01 µF is about 265 kΩ impedance — high enough that essentially no current flows through the snubber in normal operation.
- The RC time constant is 1 µs, fast enough to absorb the inductive transient (which happens over tens of microseconds).
- The 100 Ω resistor limits inrush to ~1.2 A peak when the switch closes at the worst phase angle (120 V / 100 Ω) — small enough that the switch contacts handle it without arcing.

Some people use 0.022 µF / 100 Ω or 0.047 µF / 220 Ω — the exact values aren't critical. Any RC pair with a roughly 1–10 µs time constant in this range works.

## Safety class — this is critical

This capacitor sits **across the mains**. If it fails short, you have 120 V AC right across the switch contacts (i.e., the switch becomes useless, and any leakage current goes wherever it wants). If it fails open, no protection but no hazard.

Use a properly-rated **X1 or X2 safety capacitor**. These are designed for across-the-line use and fail safely (typically open, not short). DO NOT use a generic film cap rated only for 600 V DC — those aren't qualified for sustained AC line operation.

Common Y/X cap types you'll see in catalogs:
- **X1**: rated for line-to-line, up to higher transient peaks. Less common in this small value.
- **X2**: rated for line-to-line, up to 2.5 kV transient peaks. Most common, plenty for this application.

Don't substitute Y-class (line-to-ground) — wrong rating for this position.

## Physical placement

The snubber goes **directly across the switch contacts**, not somewhere else in the mains wiring. Two leads of the snubber assembly tie onto the two switch terminals.

If you wire it across the switch from a distance (long leads), you partly defeat the point — the snubber needs to be electrically close to the contacts to suppress the arc. Solder leads short, dress them so they can't move.

See [step 10](../build/power-supply/step-10-primary-fuse-switch.md) for the surrounding wiring.

## What you should NOT do

- Don't use a non-safety-rated film cap "just because it has a 600 V rating." Voltage rating alone isn't the issue; safety qualification is.
- Don't omit the series resistor. A bare capacitor across the switch causes inrush surges that can weld the contacts shut.
- Don't make the cap large (e.g., 1 µF). The bigger the cap, the bigger the inrush surge and the more it interacts with the transformer at the line frequency.

## Testing

There's no easy DMM test for snubber function. The proof is in the listening: power the amp off through the speakers. If the click is gone, the snubber works. If it's much quieter than before but still there, the snubber values might want tweaking, but you're 90 % of the way there.

## See also

- [Step 10 — Primary fuse & switch](../build/power-supply/step-10-primary-fuse-switch.md) — where this mod gets installed
- [3-prong cord modification](3-prong-cord.md) — the other primary-side modification
