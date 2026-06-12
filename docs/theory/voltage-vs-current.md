---
title: Voltage source vs current path
---

# Voltage source vs current path

A useful framing for understanding any electrical system is the distinction between voltage *available* and current *flowing*. They're not the same thing, and confusing them is the root cause of most "but I thought it was safe" wiring catastrophes.

## The mental model

A wall outlet has 120V available between hot and neutral, but no current flows when nothing's plugged in. The voltage just sits there, ready to push current through whatever you connect. Plug in a 100W lamp (with about 144Ω of resistance), and 120V / 144Ω = 0.83A flows. Plug in a piece of copper wire across the slots (essentially 0Ω), and the current spikes catastrophically until something gives — usually the breaker.

The same logic applies to every secondary on the [PA-060](../components/pa-060-power-transformer.md):

| State of the 5V heater winding | Resistance | Current |
|---|---|---|
| No tube installed | Infinite (open circuit) | 0 A |
| 5AR4 installed | ~2.6Ω hot | 1.9 A (tube's draw; the winding is rated for 4 A) |
| Two leads tied directly together | ~0Ω | 100A+ theoretical, transformer destroyed |

## Why this matters for wiring errors

This is why **wiring errors are taken seriously** in tube amp construction. The energy stored in even a modest tube amp's transformers is enough to destroy components, start fires, or hurt people. Continuity testing each wiring section before powering up is mandatory; catching a mis-wire with the meter is free, catching it with smoke is expensive.

## Worked example: shorting the 5V heater leads

If you accidentally connected the two white leads of the [PA-060](../components/pa-060-power-transformer.md) directly together (instead of routing them to V1 pins 2 and 8), the transformer's 5V secondary would try to push 5V across essentially zero resistance, with current limited only by the transformer's internal impedance and saturation.

Theoretical current: 5V / 0.05Ω ≈ 100A — vastly more than the 4A rating.

In practice, the wire would heat up rapidly, the transformer would saturate and limit the current to something less, but still enough to either:

- Burn through one of the white leads (lucky outcome — the wire acts as a fuse)
- Blow the AC mains fuse (designed-for outcome)
- Damage the transformer itself if neither of the above happens fast enough (worst outcome — you've destroyed a $200 component)

This is why the AC mains fuse exists, and why continuity-checking before power-up is mandatory.

## Why voltage alone doesn't tell you whether something is dangerous

A van de Graaff generator can produce 400,000V and won't kill you — the current capability is so limited that your body's resistance instantly drops the voltage to nothing. A car battery produces only 12V but can melt a wrench welded across its terminals.

What matters is the **product of voltage and the path's conductivity**. High voltage *across a low-resistance path* is what creates dangerous current.

The ST-70's B+ rail is ~435V, but more importantly the supply behind it can deliver well over 100mA of current. That combination — high voltage *and* high current capability — is what makes it lethal. Skin resistance of 1000Ω at 435V would push 435mA through your body, well past the ~100mA threshold that can stop the heart.

This is why the safety practices in [high-voltage safety](../test-equipment/high-voltage-safety.md) are about *paths* — discharging caps before touching, keeping one hand in your pocket to avoid creating a chest-crossing path, using insulated probes to avoid creating any path at all.

## See also

- [High-voltage safety](../test-equipment/high-voltage-safety.md) — concrete consequences of failing to think in terms of current paths
- [How transformers work](how-transformers-work.md) — what determines a transformer secondary's current capability
- [Step 2 — 5AR4 heater](../build/power-supply/step-02-5ar4-heater.md) — where this mental model first appears in the build
