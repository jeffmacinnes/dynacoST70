---
title: Voltage source vs current path
---

# Voltage source vs current path

A useful framing for understanding any electrical system is the distinction between voltage *available* and current *flowing*. They're not the same thing, and confusing them is the root cause of most "but I thought it was safe" wiring catastrophes.

**The big picture:** every voltage source in this amp — the wall outlet, each transformer secondary, the B+ rail — is just *potential*. Nothing happens until you give it a path. The amount of current that flows is decided entirely by the resistance of whatever path you provide, via Ohm's law ($I = V/R$ — the same law you measured directly in [bench primer exercise 1](../bench-primer/01-ohms-law-and-power.md)). Design the path well and the circuit works; provide the wrong path (a mis-wire, a stray strand, your body) and the same "harmless" voltage becomes destructive. That's the entire page in two sentences — everything below is examples.

!!! note "In plain words: pressure vs. flow"
    Think of the plumbing analogy the bench primer uses. Voltage is **water pressure** in a pipe; current is **water actually flowing**. A capped pipe at high pressure has zero flow — nothing moves, nothing gets wet. Open a small faucet and a trickle flows; cut the pipe wide open and you flood the room. The pressure was the same the whole time. What changed was the *path* you gave it. Voltage is the push that's available; current is what actually moves, and only when there's somewhere to go.

## The mental model

A wall outlet has 120V available between hot and neutral, but no current flows when nothing's plugged in. The voltage just sits there, ready to push current through whatever you connect. Plug in a 100W lamp (with about 144Ω of resistance), and 120V / 144Ω = 0.83A flows. Plug in a piece of copper wire across the slots (essentially 0Ω), and the current spikes catastrophically until something gives — usually the breaker.

The same logic applies to every secondary on the [PA-060](../components/pa-060-power-transformer.md):

| State of the 5V heater winding | Resistance | Current |
|---|---|---|
| No tube installed | Infinite (open circuit) | 0 A |
| 5AR4 installed | ~2.6Ω hot | 1.9 A (tube's draw; the winding is rated for 4 A) |
| Two leads tied directly together | ~0Ω | 100A+ theoretical, transformer destroyed |

!!! note "In plain words"
    Same winding, same 5 V, three wildly different outcomes — and the *winding* did nothing different in any of them. The only thing that changed between the rows is the resistance of the path you connected. That's the whole lesson: a voltage source doesn't decide how much current flows. **The load decides.** The source just pushes as hard as its voltage allows, and $I = V/R$ does the rest.

    Why does the middle row work out fine? Because the tube designer chose a heater resistance that draws 1.9 A, and the transformer designer built a winding rated for 4 A. The current is *designed*, not accidental. Every safe circuit in this amp is a deliberately-chosen path; every dangerous fault is an accidental one.

## Why this matters for wiring errors

This is why **wiring errors are taken seriously** in tube amp construction. The energy stored in even a modest tube amp's transformers is enough to destroy components, start fires, or hurt people. Continuity testing each wiring section before powering up is mandatory; catching a mis-wire with the meter is free, catching it with smoke is expensive.

Here's the *why* behind that rule: before power is applied, a mis-wire is invisible — it's just a wire in the wrong place, sitting at 0 V, doing nothing. The voltage source hasn't met its path yet. The moment you flip the power switch, every winding simultaneously "tests" every path you've built, at full voltage, all at once. A continuity check with the meter is you running that same test *first*, with a harmless 1.5 V meter battery instead of the transformer. Same question ("where can current flow?"), consequence-free answer.

## Worked example: shorting the 5V heater leads

If you accidentally connected the two white leads of the [PA-060](../components/pa-060-power-transformer.md) directly together (instead of routing them to V1 pins 2 and 8), the transformer's 5V secondary would try to push 5V across essentially zero resistance, with current limited only by the transformer's internal impedance and saturation.

Theoretical current: 5V / 0.05Ω ≈ 100A — vastly more than the 4A rating.

In practice, the wire would heat up rapidly, the transformer would saturate and limit the current to something less, but still enough to either:

- Burn through one of the white leads (lucky outcome — the wire acts as a fuse)
- Blow the AC mains fuse (designed-for outcome)
- Damage the transformer itself if neither of the above happens fast enough (worst outcome — you've destroyed a $200 component)

This is why the AC mains fuse exists, and why continuity-checking before power-up is mandatory.

??? note "Why doesn't the full 100 A actually flow?"
    Because no real voltage source is ideal. Every source has some internal resistance of its own — the winding's copper, the core's limits — and that internal resistance is in series with whatever you connect. When the external path is nearly 0 Ω, the source's *own* resistance becomes the thing limiting current, and the source's terminal voltage collapses ("sags") while it dumps everything it has into the short. You measured exactly this behavior on the bench in [E4 — source impedance and sag](../bench-primer/extras/e4-source-impedance-and-sag.md): load a source hard enough and its output voltage droops. A dead short is just the extreme end of that curve — maximum sag, maximum internal heating. The transformer survives *briefly* because its internal impedance limits the current, but it's converting all that energy to heat inside itself, which is why "briefly" is the operative word.

## Why voltage alone doesn't tell you whether something is dangerous

A van de Graaff generator can produce 400,000V and won't kill you — the current capability is so limited that your body's resistance instantly drops the voltage to nothing. A car battery produces only 12V but can melt a wrench welded across its terminals.

!!! note "In plain words"
    In the plumbing analogy: the van de Graaff is enormous pressure behind a pipe the width of a human hair — impressive number, trivial flow. The car battery is modest pressure behind a fire main — small number, enormous flow. Danger isn't a property of the voltage alone; it's a property of *how much current the source can sustain into the path you become*. That's why the two questions you should ask about any terminal in this amp are always asked together: "how many volts?" **and** "how much current can the thing behind it deliver?"

What matters is the **product of voltage and the path's conductivity**. High voltage *across a low-resistance path* is what creates dangerous current.

The ST-70's B+ rail is ~435V, but more importantly the supply behind it can deliver well over 100mA of current. That combination — high voltage *and* high current capability — is what makes it lethal. Skin resistance of 1000Ω at 435V would push 435mA through your body, well past the ~100mA threshold that can stop the heart.

This is why the safety practices in [high-voltage safety](../test-equipment/high-voltage-safety.md) are about *paths* — discharging caps before touching, keeping one hand in your pocket to avoid creating a chest-crossing path, using insulated probes to avoid creating any path at all.

Notice that every one of those rules is really the same rule stated three ways: **don't become the low-resistance path.** Discharging caps removes the stored voltage before you can touch it; one-hand-in-pocket ensures that even if you do touch something live, the current path stays out of your chest; insulated probes mean the meter — not you — is the only thing bridging two points. None of the rules reduce the voltage in the amp. They all manage the path.

## What to remember

- **Voltage is potential; current is what flows.** A high voltage with no path does nothing — it's pressure in a capped pipe.
- **The load sets the current, not the source.** The source pushes; $I = V/R$ decides how much actually moves.
- **Every fault is an unplanned path.** Continuity testing before power-up is running the "where can current flow?" test with a harmless meter battery instead of 435 V.
- **Danger = volts × current capability.** Ask both questions about every terminal. The ST-70's B+ rail scores high on both, which is what makes it lethal.
- **All safety practice is path management** — you never lower the voltage; you make sure your body is never the path.

## See also

- [High-voltage safety](../test-equipment/high-voltage-safety.md) — concrete consequences of failing to think in terms of current paths
- [How transformers work](how-transformers-work.md) — what determines a transformer secondary's current capability
- [Step 2 — 5AR4 heater](../build/power-supply/step-02-5ar4-heater.md) — where this mental model first appears in the build
