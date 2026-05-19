---
title: Individual bias pots
---

# Individual bias pots per output tube

*Page to be written.* Planned coverage:

- The stock ST-70 has a single bias adjustment (one trimmer) that sets the bias for *all four* [EL34s](../components/el34-output-tube.md) at once.
- Problem: real-world tubes drift apart over time. Even matched quads gradually lose their match. With a single bias control, the only optimum you can find is the *average* — some tubes overbiased, some underbiased, and you can't tell which without removing them and measuring individually.
- The mod: replace the shared bias network with four independent trimmers — one per output tube. Each tube can be set to its own ideal idle current.
- Bonus: failed tubes are easier to spot. If one trimmer needs much more adjustment than the others, that tube's cathode is dying.
- Mechanical: typically four 25kΩ or 50kΩ trim pots mounted somewhere accessible, with the wipers feeding the four individual grid networks.
- The cathode resistor: each EL34 gets a small (1Ω or 10Ω) cathode resistor to ground, providing a measurement point. Bias is set by measuring the DC voltage across each cathode resistor and using Ohm's law (see [bias adjustment](../bring-up/bias-adjustment.md)).
- Hum tradeoff: more variability in individual bias pots can introduce slight hum differences between tubes; mitigated by using sealed trimmers and good wiring.

## See also

- [EL34 output tube](../components/el34-output-tube.md)
- [Bias adjustment](../bring-up/bias-adjustment.md) — the procedure that uses these pots
- [1N4007 modification](1n4007-replacement.md) — the upstream bias supply
