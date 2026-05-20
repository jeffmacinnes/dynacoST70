---
title: 'Step 15: Two 0.02 µF disc capacitors on 7-lug strip'
---

# Step 15: Two 0.02 µF disc caps from lug 6 to lugs 5 and 7

> *Connect one lead of each of the two (.02) disc capacitors to lug #6 of the 7 lug terminal strip. Connect one of the outside leads to lug #5 of the strip (S) and the other outside lead to lug #7 of the strip (S). "Refer to Pictorial".* — manual page 7

## What you're doing physically

Take two ceramic disc capacitors (0.02 µF each). Solder one lead of each cap to lug 6 of the seven-lug terminal strip — both caps share this single lug. Then the other lead of one cap goes to lug 5 (S), and the other lead of the other cap goes to lug 7 (S).

Visually: the two caps form a "V" shape with their tips meeting at lug 6.

Lug 6 itself is NOT soldered at this step — it'll get one more wire in step 23 before being soldered.

## What this network does

These two ceramic disc caps are **RF / high-frequency bypass caps** for the heater center taps:

- Lug 5 has the **GRN/YEL heater CT** (channel B heater AC midpoint).
- Lug 7 has the **BRN/YEL heater CT** (channel A heater AC midpoint).
- Lug 6 will eventually be wired to chassis ground (in step 23).

The 0.02 µF cap presents low impedance at RF frequencies (above ~10 kHz) and high impedance at audio frequencies. So:

- **At audio**: the caps look like an open circuit. Heater CTs see their normal grounding scheme.
- **At RF**: the caps look like a short to ground. Any RF noise that gets onto the heater windings (from nearby switching power supplies, dimmers, fluorescent lights, etc.) gets shunted to ground before it can couple into the audio path.

Ceramic discs are perfectly adequate for this RF-bypass duty. They're cheap, small, and don't need to be precise (the value 0.02 µF is approximate — anything 0.01 to 0.1 µF works).

## See also

- [Step 6 — Heater CTs](../power-supply/step-06-heater-cts.md) — wired the CTs to lugs 5 and 7 earlier
- [Seven-lug terminal strip](../../components/seven-lug-terminal-strip.md) — the strip these caps land on
- [Heater circuits](../../theory/heater-circuits.md) — why CT grounding matters
