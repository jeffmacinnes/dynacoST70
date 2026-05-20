---
title: M13 — A-470 output transformers
---

# M13: Mount the two A-470 output transformers

> *Mount both A-470 output transformers with #8 hardware. Note: the (4) output wire leads come through the rear hole.* — manual page 5

## What you're doing physically

Two **A-470 output transformers** mount on the **top of the chassis**, one on each side — left A-470 for the left channel, right A-470 for the right. Each weighs about 2 lbs.

Mounting:

1. Set each A-470 on its mounting tabs (the iron-core can has integral mounting feet with bolt holes).
2. Insert four **#8-32 screws** from underneath the chassis up through the chassis into the transformer's mounting tabs.
3. From the top of the transformer mounting tab, thread #8 kep nuts onto the screws.
4. Tighten firmly. These are heavy components on a chassis that will be carried around — they need to be solid.

## Lead orientation matters

The A-470 has 9 leads total:

- **5 primary leads** (BLUE plate, GREEN plate, RED CT, BLU/WHT UL tap, GRN/WHT UL tap) exit one end of the transformer
- **4 secondary leads** (YELLOW 16Ω, ORANGE 8Ω, BROWN 4Ω, BLACK common) exit the OTHER end

Mount each A-470 so:

- **Secondary leads** exit toward the REAR of the chassis (and pass through the rear hole, where they reach the 4-screw terminal strips from [M4](step-m04-rear-terminal-strips.md))
- **Primary leads** exit toward the FRONT (where they reach the EL-34 sockets and the filter cap)

If you get this backwards, you'll be routing the primary leads around the back of the transformer to reach the front-of-chassis components — adding distance, adding hum coupling, making the build ugly.

## How to identify the two transformers

The two A-470s are physically identical. There's no "LEFT" vs. "RIGHT" stamping. Mount whichever in whichever position — the wiring is mirror-symmetric.

Just remember: once mounted, that A-470 is now "the left A-470" (because it's on the left of the chassis). Its 5 primary leads will eventually connect to V2 and V3 (the left channel EL-34s); its 4 secondary leads will go to the left 4-screw terminal strip.

## Lead routing through the rear hole

The four secondary leads of each A-470 (YELLOW, ORANGE, BROWN, BLACK) pass through a hole in the chassis rear flange near each A-470. The leads enter the chassis interior through this hole, then route a short distance to the corresponding 4-screw terminal strip.

## A-470 specs

Per the [A-470 page](../../components/a-470-output-transformer.md):

| Parameter | Value |
|---|---|
| Primary impedance | 4300 Ω plate-to-plate |
| Power rating | 35 W |
| Bandwidth | −1 dB from 6 Hz to 30 kHz at full power |

## See also

- [A-470 output transformer](../../components/a-470-output-transformer.md) — full specs and lead colors
- [Step 11 — Right OPT secondaries](../power-supply/step-11-right-opt-secondaries.md) — wiring the BLACK/BROWN/ORANGE/YELLOW leads to the rear terminal strip
- [Push-pull topology](../../theory/push-pull-topology.md) — why this transformer is center-tapped
