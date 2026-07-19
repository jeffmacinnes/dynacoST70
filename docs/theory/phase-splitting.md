---
title: Phase splitting
---

# Phase splitting

[Push-pull output stages](push-pull-topology.md) need two copies of the audio signal that are 180° out of phase. The job of producing them from the single-ended input signal is called **phase splitting**, and the circuit that does it is a **phase splitter** (or "phase inverter," depending on the era of textbook).

The ST-70 uses the simplest reasonable topology: a **cathodyne** (also called "split-load") phase splitter, built around one triode section of the [6GH8A driver tube](../components/6gh8a-driver-tube.md) on the [PC-3A board](../components/pc-3a-driver-board.md).

**The big picture:** the [push-pull page](push-pull-topology.md) showed that everything good about push-pull depends on the two output tubes receiving *equal and opposite* copies of the signal. This page answers "where do those two copies come from?" The cathodyne's answer is elegant: run one current through two equal resistors and tap the signal off both. Because it's literally the same current through matched resistors, the two outputs *can't* be unequal — balance is enforced by physics, not adjustment. The price is that this stage adds no voltage gain (it only *splits*), which is why the ST-70 puts a high-gain pentode stage in front of it.

!!! note "In plain words: one current, two taps"
    Think of the plumbing version: one pipe with a single flow of water through it, and two identical flow meters — one upstream of the valve, one downstream. Whatever the flow does, both meters *must* read the same change, because it's the same water. Now notice the trick: the upstream meter reads relative to the supply (so more flow reads as a *drop* from the top), while the downstream one reads relative to the drain (more flow reads as a *rise* from the bottom). Same event, two gauges swinging by the same amount in opposite directions. That's the cathodyne: one tube current, two equal resistors, and the two outputs are opposite by construction.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/cathodyne-phase-splitter.svg" alt="Cathodyne phase splitter schematic">
  <figcaption>Equal resistors above and below a single triode. The plate output swings opposite to the input; the cathode output swings with it. Same current, same R, same magnitude — perfectly balanced. Click to zoom.</figcaption>
</figure>

## The geometry

A triode has three working electrodes: plate, grid, cathode. In a normal voltage amplifier:

- The grid receives the input signal.
- The plate connects to B+ through a load resistor.
- The cathode connects to ground (often through a small bias resistor + bypass cap).
- The output is taken from the plate, inverted and amplified.

A cathodyne phase splitter changes one thing: it makes the **plate load resistor and the cathode resistor equal value**, and removes the cathode bypass cap so the cathode swings with the signal. Then it takes TWO outputs — one from the plate, one from the cathode.

Now consider what happens when the grid swings positive:

- The tube conducts more (positive grid → more current).
- The same current flows through both resistors (Kirchhoff's law — current in a series path is the same everywhere).
- More current × same resistance = more voltage dropped across each.
- The plate, which was sitting at some positive voltage relative to B+, drops DOWN as more voltage is dropped across R_plate.
- The cathode, which was sitting at some positive voltage relative to ground, rises UP as more voltage is dropped across R_cathode.

Two outputs, swinging in opposite directions, with **identical magnitude** because the same current flowed through equal resistors.

That's it. The whole circuit. No matching, no calibration, no trim adjustments. The physics gives you balance for free.

!!! note "This is just a voltage divider you've already built"
    If the "plate drops while cathode rises" step feels slippery, connect it to the bench: B+ → R_plate → tube → R_cathode → ground is a three-element series stack, exactly like the [voltage dividers you built in bench primer exercise 2](../bench-primer/02-voltage-dividers.md) — except the middle element (the tube) is a resistor whose value the grid signal wiggles. When the tube "resistor" shrinks (grid swings positive, tube conducts harder), more current flows through the whole stack, so *both* fixed resistors drop more voltage. Dropping more across R_plate pulls the plate node down away from B+; dropping more across R_cathode pushes the cathode node up away from ground. One knob (grid voltage), two nodes moving equally in opposite directions. If you can predict a divider's midpoint with a pot, you already understand this circuit.

??? note "Why the cathodyne has (almost) no gain — and why that's fine"
    Notice something the circuit gives up: each output can only swing as much voltage as the tube's current change drops across *one* resistor, and the cathode's rise actually fights the input (as the cathode rises with the grid, the grid-to-cathode voltage — the thing that actually controls the tube — barely changes). The result is that each output is very slightly *less* than the input: gain ≈ 1 (unity), not the ~15–70× you'd get from the same triode as a normal amplifier.

    Why is that acceptable? Division of labor. The ST-70 doesn't ask this stage for gain — the pentode section in front of it supplies all the voltage amplification the amp needs. The cathodyne is asked for exactly one thing: *two perfectly balanced opposite copies*, and its unity gain is a direct consequence of the same built-in feedback (the un-bypassed cathode) that makes it so linear and stable. You're trading gain you didn't need for balance you can't buy. A stage that tried to split *and* amplify would need two matched amplifying paths — which is precisely the complication the long-tail-pair takes on (see below).

## Why it works without calibration

The "magic" is that the current through both resistors is identical — it's the same physical current, flowing through a series path. Mismatches in:

- The tube's transconductance — irrelevant, same tube for both outputs.
- Power supply variations — irrelevant, same B+ feeds both.
- Temperature drift — affects R_plate and R_cathode equally if they're the same type.

The only thing that needs to match is the resistor values themselves. With 1 % tolerance resistors (cheap and standard), you get within 1 % balance for free.

Compare to a long-tail-pair phase splitter (the alternative — see below), which requires a matched tube pair AND has a balance trimpot. Cathodyne wins on simplicity.

## Where this lives in the ST-70

The 6GH8A is a 9-pin noval miniature with two separate tube sections in one envelope. One section is a pentode (the voltage-amplifying gain stage), the other is a triode (used here as the phase splitter).

Signal chain through the PC-3A driver board:

1. Audio input arrives at the RCA jack, passes through the mono/stereo switch, and is referenced to ground by a 470 kΩ grid leak resistor (the ST-70 is a power amp — there are no volume or balance controls).
2. The pentode section of the 6GH8A amplifies the input (voltage gain ~50× open-loop).
3. The triode section configured as a cathodyne splits the amplified signal into two phases.
4. Those two phases drive the grids of the [EL34 push-pull pair](push-pull-topology.md).

Two 6GH8As total in the ST-70 — one per channel.

!!! note "Why the pentode comes first — and what you'll actually measure"
    The ordering isn't arbitrary. The cathodyne contributes no gain (see above), and the EL34 grids need tens of volts of swing to reach full power, so *something* upstream has to do all the voltage amplification — that's the pentode's whole job. Pentode for gain, triode for splitting: each tube section doing the one thing it's best at, in one envelope.

    One measurement trap to be aware of: that "~50×" is the pentode's *open-loop* stage gain. On a working amp, the [global feedback loop](feedback.md) returns a fraction of the output to this pentode's cathode, and the loop deliberately throttles the gain. Probe input-to-plate on this build with feedback connected and you'll measure about **19×** (anywhere in the 15–25× range is healthy) — not 50×. Both numbers are "right"; they're answers to different questions. Measuring ~19× is the feedback loop working, not a weak tube.

## Output impedance — the cathodyne's weakness

The plate output and cathode output have different output impedances:

- **Plate output impedance** ≈ R_plate ≈ 47 kΩ (looking back into the plate, it's the parallel combination of R_plate and the tube's plate resistance r_p, but r_p >> R_plate so it's roughly R_plate).
- **Cathode output impedance** ≈ R_cathode / (1 + µ) ≈ ~500 Ω (the cathode follower has much lower output impedance due to the inherent feedback of cathode degeneration).

So the cathode output drives its load *much* harder than the plate output. The two EL34 grids see different source impedances, which can subtly unbalance the high-frequency response.

In practice this asymmetry is small enough at audio frequencies that the ST-70 sounds fine. But it's the main reason serious amplifiers (and the VTA upgrade) use a long-tail-pair instead.

!!! note "In plain words: why 'output impedance' matters here"
    Output impedance is the "stiffness" of a source — how much its voltage sags when something loads it, exactly what you measured in [E4 — source impedance and sag](../bench-primer/extras/e4-source-impedance-and-sag.md). The cathodyne's two outputs are equal *voltage* signals, but one comes from a stiff source (~500 Ω, cathode) and one from a soft source (~47 kΩ, plate). At mid frequencies the EL34 grids draw essentially no current, so both sources deliver their full voltage and the balance holds — nothing loads them, so stiffness doesn't matter.

    The catch is at high frequencies: each EL34 grid has a few tens of picofarads of input capacitance, and a capacitor's opposition falls as frequency rises (see [E5 — caps with AC](../bench-primer/extras/e5-caps-with-ac.md)). Each output impedance forms an RC low-pass with its grid capacitance — and 47 kΩ into that capacitance rolls off at a much lower frequency than 500 Ω into the same capacitance does. So the balance, perfect through the audio band, starts to slip in the ultrasonic range. That's tolerable here (it's above audibility, and the feedback loop's compensation handles the region anyway), but it's the cathodyne's genuine weakness.

## Alternative: long-tail-pair

The "long-tail-pair" (LTP) phase splitter uses two triodes with their cathodes tied together to a shared cathode resistor (the "tail" — often biased through a constant-current source).

Layout:

- Triode A grid receives the input signal.
- Triode B grid is held at AC ground (or tied to a balance trimpot for fine adjustment).
- Both plates have equal load resistors to B+.
- Both cathodes tie together through a shared resistor (the "long tail").

When the input swings positive on triode A's grid, A conducts more. The shared cathode wants to rise (more current through the tail). But triode B's grid is held fixed, so B's grid-to-cathode voltage drops — triode B conducts LESS. The plates of A and B swing in opposite directions.

Advantages over cathodyne:

- **Equal output impedance** at both plates (both are plate outputs).
- **Better PSRR**: power supply noise tends to common-mode at both outputs and gets cancelled by the push-pull stage.
- **More headroom**: each side can swing a larger fraction of B+.

Disadvantages:

- Uses TWO tube sections instead of one (most LTPs use both halves of a 12AX7 or similar).
- Needs a balance trimpot (or matched tubes).
- More parts overall.

The **VTA driver board** upgrade for the ST-70 (Tubes4HiFi) replaces the PC-3A's cathodyne with an LTP — one of several reasons people prefer that upgrade.

!!! note "In plain words: the seesaw"
    The LTP is two kids on a seesaw. The shared cathode resistor (the "tail") is the pivot: it carries a roughly constant total current, so the two triodes are always dividing a fixed pie between them. Push one kid down (drive triode A's grid) and the other kid *must* go up (triode B gets less of the pie) — the pivot enforces the opposition. Compare the two philosophies: the cathodyne gets balance from *one current read twice*; the LTP gets it from *two currents forced to trade off*. The cathodyne's version is more perfect and cheaper (one tube section, no trimming) but has unity gain and mismatched output stiffness. The LTP's version needs matched parts and a trim, but both outputs come from identical-looking plates *and* the stage amplifies while it splits. Dynaco chose the cathodyne because for a kit amp, "perfectly balanced with zero adjustments, forever" beats "slightly better on paper if you trim it correctly."

## Why the 180° relationship matters

The two output signals must be EXACTLY 180° apart for push-pull's even-harmonic cancellation to work. Any imbalance — say, one output is 95% of the other's amplitude, or shifted in time by a fraction of a cycle — means:

- Common-mode signals don't fully cancel (hum and 2nd-harmonic distortion leak through).
- The two EL34s are unequally driven, so their plate currents don't perfectly cancel in the OPT core.

The cathodyne's free balance is what makes it work in the ST-70 design. With careful component selection (1 % resistors, low-leakage coupling caps), the balance is good enough that the push-pull cancellation properties hold up well.

## Connection to other 180° relationships

The cathodyne's two outputs being 180° apart is the **same physics** as:

- The two halves of a [center-tapped transformer winding](rectification.md#the-180-phase-relationship-across-a-center-tap) being 180° apart.
- The two halves of the [push-pull primary on the A-470](push-pull-topology.md) being 180° apart.

In all three cases, opposite-phase signals enable the push-pull cancellation properties that make the system sound clean.

## What to remember

- **The splitter exists because push-pull demands two equal, opposite drive signals.** Everything push-pull cancels, it cancels only as well as these two signals are balanced.
- **The cathodyne is a series stack — one current, two equal resistors, two taps.** The same current through matched resistors makes imbalance physically impossible; that's why there's no trim adjustment.
- **It splits but doesn't amplify (gain ≈ 1), and that's by design** — the pentode ahead of it does all the voltage gain. Expect to measure ~19× input-to-plate on this build with feedback connected, not the pentode's ~50× open-loop figure.
- **Its one real weakness is unequal output stiffness** (~500 Ω cathode vs ~47 kΩ plate), which only matters at ultrasonic frequencies where grid capacitance loads the outputs unevenly.
- **The LTP alternative trades the cathodyne's free perfection for gain and symmetric outputs** — more parts, needs trimming; that's the swap the VTA upgrade makes.

## See also

- [Push-pull topology](push-pull-topology.md) — what the phase-split signals drive
- [6GH8A driver tube](../components/6gh8a-driver-tube.md) — the specific tube
- [PC-3A driver board](../components/pc-3a-driver-board.md) — the board that implements the phase splitter in this build
- [Feedback](feedback.md) — the global feedback loop wraps around the splitter + push-pull stage
- [Rectification — 180° phase relationship](rectification.md#the-180-phase-relationship-across-a-center-tap) — same physics, different application
