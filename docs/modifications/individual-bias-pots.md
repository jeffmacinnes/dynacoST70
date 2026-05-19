---
title: Individual bias pots
---

# Individual bias pots per output tube

The stock ST-70 has **one** bias trimmer that sets the operating point of **all four** [EL34s](../components/el34-output-tube.md) at the same time. That worked acceptably in 1959 when "matched quad" meant the same factory and similar test-bench numbers. Modern reality: tubes drift, even matched ones drift apart over months, and one trimmer can only find the *average* — leaving some tubes overbiased (running hot, eating themselves) and others underbiased (distorting, weak).

The fix is four independent bias trimmers — one per output tube — plus a small cathode sense resistor on each tube. You can then set each EL34 to its own ideal idle current.

## Why a shared bias is a problem

In the stock circuit, the bias supply (see [1N4007 mod](1n4007-replacement.md) for the supply itself) feeds a single voltage divider, whose wiper drives all four EL34 control grids through 470 kΩ grid stoppers in parallel. The four tubes see the same DC bias, but no two real tubes have identical transconductance — so they pull different idle currents at the same grid voltage.

Concretely: if your "matched quad" has Tube A drawing 45 mA, Tube B drawing 50 mA, Tube C drawing 48 mA, and Tube D drawing 52 mA at the same bias point, you can either:

- Set bias for the average (≈ 49 mA) — tubes A and C run cool, B and D run hot.
- Bias for the hottest tube (52 mA target → set bias so D draws 52 mA) — the others now all run cooler than they could.
- Bias for the coolest — D red-plates.

Most builders end up doing a compromise, and the amp lives with non-ideal bias on at least two of the four tubes. With individual pots, you set each tube to exactly 50 mA (or whatever target you pick), and that's that.

## What the mod looks like

Two parts:

**1. Cathode sense resistors.** Each EL34's pin 8 (cathode) connects to ground through a small precision resistor — 1 Ω 1 % is the most common choice, sometimes 10 Ω. The voltage across this resistor is the cathode current via Ohm's law:

$$I_{cathode} = V_{measured} / R_{sense}$$

For a 1 Ω resistor and a 50 mA target: V = 0.050 × 1 = **50 mV** across the resistor. That's a comfortable measurement for any DMM.

**2. Four trimpots feeding four bias resistors.** The shared divider is replaced with four parallel paths:

- Bias supply → fixed series resistor → trimpot → 470 kΩ grid stopper → EL34 grid.

Each trimpot sets its tube's grid voltage independently. Common values: 25 kΩ or 50 kΩ trimpots, with a 100 kΩ or so fixed series resistor that keeps the adjustment range sane.

## Mechanical layout

The four trimpots need to be accessible — you'll be adjusting them periodically. Typical placements:

- Bottom of chassis, accessible through holes (need a small screwdriver to reach).
- Top of chassis, sometimes mounted in a small bracket next to the tubes.
- The "VTA" driver board (Tubes4HiFi) includes per-tube bias pots in its design.

Right next to each tube's socket is the cleanest layout, but accessibility from the top can be awkward. Underside access is the most common.

## Measurement points

For the cathode sense resistors, bring out test points to where you can probe them safely:

- A small turret terminal on the side or top of the chassis.
- A test jack (banana socket) next to each tube.
- Just the cathode lead of the EL34 socket itself (pin 8), probed from below.

Whichever approach, the goal is: probe each cathode resistor without dismantling the amp.

## Bias-up procedure

See [bias adjustment](../bring-up/bias-adjustment.md) for the detailed bring-up. Outline:

1. Power on, let everything warm up for at least 5 minutes.
2. DMM on DC mV range, leads on the cathode sense resistor for tube #1.
3. Adjust trimpot #1 until DMM reads the target voltage (e.g., 50 mV for 50 mA at 1 Ω).
4. Repeat for tubes #2, #3, #4.
5. Go back and re-check tube #1 — bias drifts slightly as the tubes warm fully. Iterate once or twice.

## Target idle current

The stock ST-70 idles its EL34s at around **50 mA** per tube. This is conservative — the tubes can handle more — and it's a good starting point.

Going hotter (60-70 mA): more class-A operation, marginally better linearity, much shorter tube life.

Going cooler (35-40 mA): longer tube life, more class-AB crossover distortion.

50 mA is the canonical Dynaco-era target and what most people use.

## Failure-mode bonus

With individual pots, a dying tube is obvious in two ways:

- Its trimmer ends up at a very different setting than the others (you have to crank it WAY more — or less — than its neighbors to hit the same idle current).
- Its bias creeps over the course of an hour. Healthy tubes settle within a few minutes; a dying cathode keeps drifting.

In the stock single-bias circuit, you have no way to see this without pulling each tube and testing it on a tube tester. With per-tube pots, you can spot a fading tube from the bias adjustment alone.

## Hum considerations

Four trimpots add four potential noise sources. To keep hum low:

- Use sealed trimpots (Bourns 3296 or similar) — not the open carbon-comp ones.
- Keep the wiper-side wiring short.
- Twist any wire pair that runs near heater AC wiring.
- Mount the pots on a piece of grounded copper or aluminum if hum is bad.

In practice, well-built individual bias pot mods are no noisier than the stock single-bias design.

## Parts list (approximate)

- Four 1 Ω 1 % 1 W cathode resistors
- Four 25 kΩ or 50 kΩ multi-turn cermet trimpots (Bourns 3296W is the standard pick)
- Four 100 kΩ fixed resistors (series with the trimpots)
- Four 470 kΩ grid stoppers (often already in the stock circuit)
- Hookup wire, terminal lugs, mounting hardware

Total parts cost: ~$10. Time to install: an afternoon if you're confident with the layout, more if you're working it out for the first time.

## See also

- [EL34 output tube](../components/el34-output-tube.md) — the tubes being biased
- [Bias adjustment](../bring-up/bias-adjustment.md) — the procedure that uses these pots
- [1N4007 modification](1n4007-replacement.md) — the upstream bias supply
- [Multimeter](../test-equipment/multimeter.md#working-around-the-missing-functions) — how to read bias current without an ammeter
