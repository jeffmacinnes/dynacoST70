---
title: Feedback
---

# Feedback

**Negative feedback** is a single design decision with outsized consequences: take a small fraction of the output signal, invert it, and add it back to the input. The amplifier then "sees" its own output and corrects for any difference between input and output. That correction reduces distortion, lowers output impedance, and flattens bandwidth — in exchange for some gain and some new stability constraints.

The ST-70 uses **global negative feedback**: a single resistor (1 kΩ, per channel) from the [A-470](../components/a-470-output-transformer.md)'s 16 Ω secondary tap back to the [input stage](../components/pc-3a-driver-board.md) pentode's cathode. That one wire wraps the entire amplifier — every stage, the OPT, everything — in a feedback loop.

**The big picture:** an amplifier without feedback is like a driver with their eyes closed — it applies gain and *hopes* the output came out right, with no way to know. Feedback gives the amp eyes: it continuously compares a sample of the actual output against the input and steers to close the gap. The amp stops being a "multiply by A and hope" machine and becomes a "make the output track the input, whatever it takes" machine. Everything on this page — lower distortion, tighter bass, flatter response, and the new risk of oscillation — falls out of that one change.

!!! note "In plain words: cruise control"
    Feedback is cruise control for signal. You set 65 mph (the input signal says what the output *should* be, scaled up). The car constantly measures its actual speed (the feedback resistor samples the actual output at the speaker terminals) and compares it to the target. Hit a hill — a tube gets non-linear, the transformer sags, the supply ripples — and the instant the actual speed droops below target, the error grows and the system automatically feeds in more throttle to close the gap. The correction isn't programmed for hills specifically; it corrects *any* disturbance, from *any* cause, because all it ever looks at is the difference between "what I asked for" and "what I'm getting." That's why one wire fixes tube non-linearity, transformer roll-off, and supply hum all at once: to the loop, they're all just "the output isn't matching the input," and it fights them all the same way.

    The catch, previewed: cruise control only works if the correction arrives *promptly and in the right direction*. If the throttle responded to where the car was two seconds ago, it would over-correct, then over-correct the correction — surging endlessly. That's exactly the stability problem covered below.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/feedback-loop.svg" alt="Global negative feedback loop in the ST-70">
  <figcaption>The full signal path with the feedback wire shown in red. Hover any stage for what feedback does to it. Click to zoom.</figcaption>
</figure>

## The mechanism in one paragraph

Without feedback, an amplifier's job is open-loop: take the input, multiply by gain A, hope the output is a faithful copy. Any non-linearity in the tubes, any phase shift in the OPT, any DC drift — all of it shows up on the output.

With feedback, a fraction β of the output is subtracted from the input *before* the amplifier sees it. The amp now sees `input − β·output`. Whatever the amp does to that input shows up as the output. Solve for output:

`output = A · (input − β·output)`
`output · (1 + Aβ) = A · input`
`output = (A / (1 + Aβ)) · input`

The effective gain is `A / (1 + Aβ)` instead of `A`. With Aβ much greater than 1 (which it is in a real tube amp), the closed-loop gain becomes approximately `1/β` — set by the feedback resistor, not by the tubes. Tube non-linearity is dramatically attenuated because *any* deviation between actual output and the expected output gets corrected.

This is the core trade: you give up gain (which you have plenty of) in exchange for linearity, low output impedance, and wide bandwidth (which you want).

!!! note "In plain words: why giving up gain buys accuracy"
    Read the final line again with words instead of symbols. When `Aβ` is large,

    $$ A_{cl} = \frac{A}{1 + A\beta} \approx \frac{1}{\beta} $$

    and the tube gain `A` has *vanished from the answer*. That's the deepest idea on this page: the closed-loop gain no longer depends on the tubes — sloppy, drifting, non-linear, aging tubes — but only on β, which is set by a **resistor divider**. And resistors are the most boringly reliable, linear, drift-free components you can buy. Feedback is a trade of quality: you swap gain that came from unreliable parts for gain defined by reliable ones.

    Why does the tube gain stop mattering? Because with lots of raw gain in the loop, the amp only needs a *microscopic* error signal at its input to produce the full output. Whether the tubes deliver 45× or 55× on a given day just changes how microscopic that error is — the output still lands almost exactly where `1/β` says. It's why your cruise control holds 65 mph whether the engine is cold or warm: as long as there's throttle to spare, the *set point* rules, not the engine's mood.

    You can build β with your own hands: [E7 — the feedback divider](../bench-primer/extras/e7-feedback-divider.md) has you construct exactly this network on the bench and watch it set a loop's gain. It's the single best exercise for making this page click. And β itself is nothing exotic — it's a plain [voltage divider](../bench-primer/02-voltage-dividers.md): on this amp, the 1 kΩ feedback resistor and the small resistance at the input pentode's cathode divide down the 16 Ω tap's signal, and that ratio *is* β.

    You can also see this on the real amp with a scope. The input pentode's raw stage gain is ~50× open-loop, but probe input-to-plate on this build with the loop connected and you'll measure about **19×** (15–25× is the healthy range). The "missing" gain isn't lost — it's been spent, deliberately, as the loop's error-correcting muscle. Measuring ~19× instead of 50× is the proof that feedback is working.

## What feedback buys you, concretely

For the ST-70 with about **20 dB of feedback** (loop gain ~10×):

### Lower distortion

Distortion in any stage is reduced by a factor of `1 + Aβ` — the "loop gain." For 10× loop gain, total harmonic distortion drops by ~10×. An open-loop ST-70 might produce 5 % THD at full output; with feedback, more like 0.5 %.

This applies to *every* source of distortion inside the loop: tube non-linearity, screen-grid effects, output transformer saturation. Everything gets pulled toward "what the input said."

### Lower output impedance

The amp looks much more like an ideal voltage source to the speaker. Output impedance drops by `1 + Aβ`. A typical open-loop tube amp has Z_out ≈ 5-10 Ω at the 8 Ω tap; with the ST-70's feedback, it drops to ~0.5 Ω or less.

The practical effect: better **damping factor** — the amp resists motion of the speaker cone caused by stored energy in the voice coil or cabinet. Tighter bass, less mushy low-mid range.

!!! note "In plain words"
    Why does feedback lower output impedance at all? Because output impedance *is* sag — how much the output voltage droops when the load pulls current (the thing you characterized in [E4 — source impedance and sag](../bench-primer/extras/e4-source-impedance-and-sag.md)). But the loop is watching the output. The instant the speaker's current draw tries to drag the output voltage down, that droop shows up as an error, and the loop drives the tubes harder to cancel it. The sag still "wants" to happen; the loop just refuses to allow it. An output that refuses to sag under load is, by definition, a low-impedance source.

    And why care? A speaker isn't a passive resistor — it's a moving mass on a spring that generates voltage of its own as the cone overshoots and rings after each bass note (a motor run backwards is a generator). A low-impedance amp output short-circuits that generated voltage, braking the cone's unwanted motion — like the difference between stopping a swing with a firm grip versus a loose one. That braking is what "tight bass" literally means. [E6 — driving a speaker](../bench-primer/extras/e6-driving-a-speaker.md) explores what a speaker really looks like as a load.

### Wider, flatter bandwidth

The A-470 by itself rolls off at the band extremes — its open-loop response is maybe ±0.5 dB from 25 Hz to 25 kHz. With feedback compensating for the roll-off, the closed-loop response is ±0.2 dB over a wider window. The amp's measured response becomes essentially determined by the feedback network, not by transformer characteristics.

### Reduced sensitivity to supply variation

Hum and ripple in the B+ rail show up as additive noise on the output. Feedback subtracts the same hum from the input, so the amp's output is *less* sensitive to supply noise. This is part of why a well-designed feedback amp tolerates a sloppier power supply than a no-feedback amp would.

On this build you can put numbers on it: the main B+ rail still carries ~2–3 Vp-p of ripple after the choke (down from ~40 Vp-p at the first cap). The [push-pull output stage](push-pull-topology.md) cancels most of that before it ever reaches the speaker, and the feedback loop mops up what leaks past the cancellation. Two independent defenses, which is *why* the ST-70 gets away with a straightforward power supply: the designer didn't need a laboratory-grade rail because the topology forgives an imperfect one.

## What feedback costs you

### Stability is now a design problem

Open-loop, the amp's bandwidth is whatever it is — phase shifts at the band extremes don't matter. With feedback, those phase shifts come back through the loop. If at some frequency the total phase shift through the loop reaches 180°, the *negative* feedback becomes *positive* feedback — and the amp oscillates.

!!! note "In plain words: the shower with slow plumbing"
    Why does phase shift flip helpful feedback into runaway? Think of adjusting a shower where the pipes are long: the water hitting you now reflects the knob position from five seconds ago. Too cold → you turn it up → still cold (the hot water hasn't arrived) → you turn it up more → suddenly scalding → you slam it down → freezing → and now you're oscillating, hot-cold-hot-cold, forever. Nothing is broken; the *correction is arriving late*, so every fix lands after the problem has already reversed, amplifying the swing instead of damping it.

    In the amp, "late" means phase shift. Every stage and especially the OPT delays the signal a little, and the delay (measured as a fraction of a cycle) grows at frequency extremes. At some frequency, the accumulated shift reaches 180° — a half cycle — which means the "corrective" signal arrives perfectly inverted: pushing exactly when it should pull. If the loop still has gain ≥ 1 at that frequency, each round trip makes the swing bigger, and the amp sings a note of its own with no input at all (usually ultrasonic — you won't hear it, but your tweeters and output tubes will feel it). Stability design is simply arranging for the loop's gain to fall below 1 *before* its lateness reaches half a cycle.

The ST-70 handles this with three techniques:

1. **The A-470 has very low phase shift** in its passband — extending well into the inaudible high-frequency range.
2. **Modest loop gain** (20 dB instead of, say, 30 dB). Less correction, but more margin.
3. **Compensation capacitor** somewhere in the loop (often across a plate resistor) that rolls off the high frequencies inside the loop before they accumulate enough phase shift to oscillate.

On this build, technique 3 is concrete: alongside the main 1 kΩ feedback resistor from the 16 Ω tap, there is a **second, HF-only feedback path — a 390 pF capacitor from the OPT's ultralinear primary tap into the same input-stage cathode**. Why a cap, and why from the *primary*? A 390 pF cap is effectively invisible at audio frequencies (its impedance is huge there — the same reactance-falls-with-frequency behavior you measured in [E5 — caps with AC](../bench-primer/extras/e5-caps-with-ac.md)) but becomes a low-impedance path at the ultrasonic frequencies where oscillation threatens. And it taps the *primary* side because that signal hasn't yet picked up the OPT's high-frequency phase lag — it's the "earlier," less-delayed copy. So at exactly the frequencies where the main loop's correction starts arriving dangerously late, this path quietly supplies a prompt one. It's a bypass lane for the corrections that can't afford to be late.

This is why "more feedback is always better" is wrong — beyond a certain point, the amp becomes hard to keep stable across all loads (a partially-blown speaker, a long cable, a different speaker impedance) and starts oscillating into ultrasonic territory. That's bad for tubes, bad for speakers, bad for everyone.

### Even-harmonic "warmth" gets cancelled

This is the audiophile argument against feedback: the second-harmonic distortion characteristic of single-ended tube amps is widely considered "pleasing" — it adds a slight harmonic richness to the signal. Negative feedback works hard to cancel that distortion. The result is a more accurate, less colored amp — which is what the engineering side wants, but not always what the listener prefers.

The push-pull EL34s in the ST-70 already cancel a lot of 2nd-harmonic distortion *via the push-pull arrangement* itself (see [push-pull topology](push-pull-topology.md)). Feedback removes whatever push-pull cancellation missed.

If you want more "warmth": reduce or eliminate the global feedback. The amp's distortion will go up but so will the audible 2nd-harmonic content. This is the "zero-feedback" school of design.

### Constraints on the entire signal chain

Once you commit to a feedback loop, every component in that loop has to behave well at every frequency the loop sees. The OPT can't have weird resonances at 50 kHz. The coupling caps must not introduce phase shift below the cutoff. The driver stage has to swing enough to drive the output tubes through the corrections.

This is why tube amp design is a system-level problem, not a stage-by-stage problem.

## Damping factor

Damping factor is just the ratio of speaker impedance to amplifier output impedance:

`damping_factor = Z_speaker / Z_out`

The ST-70's spec is a damping factor of **at least 15**, which means Z_out ≤ ~0.5 Ω at the 8 Ω tap:

`damping_factor = 8 / 0.5 ≈ 16`

!!! note "In plain words"
    Damping factor is just "how much stiffer is the amp than the speaker?" A DF of 16 means the amp's output looks 16× more rigid than the speaker's own impedance — so when the cone rings and generates its own unwanted voltage, the amp's low impedance absorbs it 16× more effectively than the speaker can sustain it. Why is "at least 15" the spec rather than "as high as possible"? Because DF is bought with loop gain, and loop gain is rationed (see the stability section) — past DF ≈ 20 or so the audible improvement in a tube amp is marginal, but the stability margin you spent to get it is real.

By solid-state amp standards (DF often > 100) that's low. By tube amp standards it's good — most tube amps have damping factors in the 5-20 range. Higher than that and you start losing the "tube character" people associate with bass.

The 16 Ω tap gives somewhat lower output impedance referred to the speaker (more feedback amplitude) — using a 4 Ω speaker on the 4 Ω tap gives a similar damping factor as 16 Ω on 16 Ω. The taps are designed to keep DF roughly constant across speaker impedances.

## Why the 16 Ω tap specifically

The ST-70's feedback resistor goes to the **16 Ω secondary tap**. Why not 8 or 4?

The 16 Ω tap has the largest voltage swing of the secondary (you can derive this: same power, P=V²/Z, so higher Z means higher V). That gives the feedback network the strongest signal to sample, which improves signal-to-noise in the feedback path. Lower-impedance taps would require a smaller feedback resistor to maintain the same loop gain, which would also draw more current from the speaker into the feedback path.

The 16 Ω tap is the canonical choice; the ST-70 uses it regardless of which tap your speaker is connected to.

!!! note "In plain words"
    Two ideas hiding in that paragraph, unpacked. First: all three secondary taps carry the *same signal* at different sizes — they're points along one winding, so the 16 Ω tap is just the "loudest copy" available ($P = V^2/Z$ at equal power means the highest-impedance tap swings the most volts). When you're sampling a signal to measure it, you take the biggest, cleanest copy you can get, for the same reason you'd photocopy from the original rather than from another copy. Second, and easy to miss: the feedback samples the **secondary** — the *speaker side* — of the OPT, not the tube side. That's a deliberate choice with a big consequence: it puts the output transformer *inside* the loop, so every imperfection the OPT adds (roll-off, phase wiggle, slight distortion) is seen and corrected too. Sample on the primary side and the loop would happily perfect the tube stages while remaining blind to whatever the transformer does afterward. The cost of enclosing the OPT is that its phase shift now lives inside the loop — which is exactly the stability problem the 390 pF compensation path exists to solve.

## Local vs. global feedback

Global feedback wraps the whole amplifier. **Local feedback** is feedback applied within a single stage — most commonly, a cathode resistor *without* a bypass capacitor, which feeds back the cathode current to oppose grid voltage changes (cathode degeneration).

Local feedback:

- Reduces stage gain
- Improves linearity of that stage
- Lowers that stage's output impedance
- No global stability issues (the loop is small and short)

Global feedback:

- Reduces overall gain
- Corrects errors *anywhere* in the loop
- Sets overall closed-loop characteristics
- Introduces global stability constraints

Most tube amps use both: cathode degeneration in selected stages plus a global loop. The ST-70 follows this pattern.

Why both? Think of local feedback as each worker double-checking their own output, and global feedback as final inspection at the loading dock. Final inspection catches everything but arrives late and can only say "the whole product is wrong" — it can't fix a stage's bad habit at the source. Local feedback is small, fast, and unconditionally stable (the loop is too short to accumulate dangerous phase shift), and it makes each stage better-behaved *before* the global loop has to deal with it. A well-behaved open-loop amp needs less global correction — which means the global loop gain can stay modest (20 dB), which keeps the stability margins comfortable. The two kinds of feedback aren't redundant; each makes the other's job easier. Incidentally, you've already met local feedback twice in this manual without the name: the [cathodyne's](phase-splitting.md) un-bypassed cathode resistor (which trades its gain to unity for perfect balance) is cathode degeneration, and the global loop itself injects into the input pentode's cathode — the same node local feedback uses — because a signal arriving at the cathode naturally *opposes* one arriving at the grid, which is exactly what subtraction requires.

## What to remember

- **Feedback is cruise control**: sample the actual output (16 Ω tap, through a 1 kΩ resistor into the input pentode's cathode), compare it to the input, and correct the difference — whatever caused it.
- **The trade is surplus gain for accuracy.** $A_{cl} \approx 1/\beta$: the amp's gain ends up set by a resistor divider instead of by tubes. On this build that shows up directly — ~50× open-loop input-stage gain becomes ~19× measured with the loop closed, and that drop is the loop *working*.
- **Everything inside the loop gets corrected** — tube non-linearity, OPT roll-off, supply ripple, output sag. That's why the loop deliberately encloses the whole amp, transformer included, by sampling at the speaker side.
- **The price is stability.** Corrections that arrive a half-cycle late become sabotage; that's why loop gain is kept to a modest 20 dB and why the 390 pF cap from the UL primary tap provides a prompt HF path.
- **Get hands-on**: [E7 — the feedback divider](../bench-primer/extras/e7-feedback-divider.md) has you build β on the bench and watch it set the gain of a real loop.

## See also

- [Push-pull topology](push-pull-topology.md) — partly cancels 2nd-harmonic distortion before feedback even sees it
- [Phase splitting](phase-splitting.md) — the stage before push-pull
- [A-470 output transformer](../components/a-470-output-transformer.md) — its phase response is part of the feedback loop
- [PC-3A driver board](../components/pc-3a-driver-board.md) — where the feedback resistor lands at the input stage cathode
- [Step 11 — Right OPT secondaries](../build/output-stage/step-11-right-opt-secondaries.md) — where the 16 Ω tap is brought out for the feedback path
