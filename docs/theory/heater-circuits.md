---
title: Heater circuits
---

# Heater circuits

The 6.3V and 5V heater windings of the [PA-060](../components/pa-060-power-transformer.md) are the simplest parts of the power supply — but they're also where careless wiring most commonly introduces audible hum. This chapter covers what the heaters do, why they're AC, and the techniques used to keep their magnetic fields from leaking into the audio signal.

## The big picture

Heaters are the amp's pilot lights: low-voltage, high-current windings whose only job is to keep each tube's cathode hot enough to emit electrons. Electrically they're trivial — raw AC straight into a resistance wire, no rectifier, no filter. The *entire* engineering challenge is elsewhere: those wires carry amps of 60 Hz AC through a chassis full of millivolt-level audio signals, and every technique on this page (twisting, dressing, center-tap grounding) exists for one reason — **keeping the heaters' 60 Hz out of the music.** If you remember one thing, remember that the hum tricks all work the same way: arrange the two heater wires so their effects on nearby circuitry are equal and opposite, and let them cancel.

!!! note "Diagram placeholders"
    A planned interactive diagram will show magnetic field cancellation in parallel vs. twisted wire pairs. See [diagram roadmap](../index.md).

## Why tubes need heaters at all

All vacuum tubes need their cathodes heated to function. Electrons don't spontaneously leave a cold piece of metal — they're held there by atomic bonds. To get them to "boil off" the cathode surface (thermionic emission), you have to heat the metal until thermal energy overcomes those bonds. For oxide-coated cathodes (the standard for audio tubes), that's around 800°C.

**No heat = no electron flow = the tube is just an empty glass bulb.**

!!! note "In plain words"
    A tube works by throwing a cloud of free electrons across a vacuum from cathode to plate, with the grid as a valve in between. But you can't throw electrons that are still stuck to the metal — heat is what shakes them loose, the same way heat turns water into steam. The heater is literally the boiler. Every other voltage in the amp (B+, bias, signal) controls *where the electrons go*; the heater is the only thing that produces electrons *to control* in the first place. That's why a tube amp does nothing for the first several seconds after power-on: no glow, no cloud, no amp.

## Why the heaters use AC

The heater windings produce **AC**, not DC. The tubes' filaments are heated by 5V or 6.3V *alternating* current, swinging back and forth 60 times per second.

A filament is just a piece of resistance wire. Power dissipation is `V² / R` regardless of whether V is AC or DC. The wire heats up the same way. There's no rectification or smoothing needed for heaters. (This is the same P = V²/R you burned into a resistor in [power and heat](../bench-primer/extras/e1-power-and-heat.md) — a heater is just that experiment run on purpose, all day.)

!!! note "In plain words"
    Why doesn't the heater care about direction? Because its only product is *heat*, and a wire gets just as hot whether current flows left-to-right or right-to-left — friction doesn't care which way you rub. Squaring V in the power formula is the math saying the same thing: (+6.3)² and (−6.3)² are both ≈ 40, so the heating is identical on both halves of the AC cycle. Contrast that with the plate supply, where direction is everything — which is why B+ needs the whole rectify-and-smooth chain and the heaters need nothing at all.

So the WHY of AC heaters is economics: the transformer already produces AC, and the heaters can use it *raw*. Skipping a rectifier and filter for the heater circuit saves real money and chassis space — the heaters draw several amps, and smoothing amps of current takes big, expensive parts.

DC heaters *are* sometimes used in very high-end designs to eliminate any chance of heater hum, but they require their own rectifier, filter cap, and regulator — extra cost and complexity that Dynaco didn't think was justified for the ST-70. Instead, Dynaco spent a few cents on the hum-cancellation tricks below and got most of the benefit.

## Why 5V (for the 5AR4) and 6.3V (for everything else)

The 5AR4 was designed for a **5V heater** — the same 5V standard as the directly-heated rectifiers it descended from (5U4, 5Y3, 5R4, etc.), though the 5AR4 itself is *indirectly* heated, with a separate cathode tied to the heater at pin 8. The number is right there in the tube name: the "5" in "5AR4" tells you it's a 5V heater tube.

Most signal tubes from the same era — the EL34 outputs, 6GH8A drivers, 12AX7s, etc. — were designed for **6.3V filaments**. Again the number is in the name: 12AX7, 6V6, 6L6, 6SN7 — the leading "6" or "12" means 6.3V.

Why the difference? Originally, 6.3V was chosen for compatibility with car batteries (6V batteries actually run at ~6.3V in operation). 5V was a separate standard for power supply rectifier tubes.

You can't share these. Running an EL34 on 5V would underheat it (cold cathode, no emission, distorted/quiet sound, eventual cathode poisoning). Running a 5AR4 on 6.3V would overheat it (shortened life, eventual filament burnout). So the PA-060 has separate windings for the two voltage standards.

## The hum problem

There's a downside to AC heaters: any current flowing through a wire generates a magnetic field around it. AC current generates an *oscillating* magnetic field at 60Hz. If those fields reach into the audio signal circuitry, they induce **60Hz hum** — the audible enemy of every tube amp.

!!! note "In plain words"
    Remember how a transformer works: a changing magnetic field near a wire induces a voltage in that wire — that's the whole point of [the transformer chapter](how-transformers-work.md). The heater wires and your signal wires form an *accidental transformer*: heater wire as primary, signal wire as secondary, air as the (bad, but not bad enough) core. The heater current is big — amps, not milliamps — so even terrible coupling can induce enough 60 Hz into a signal wire to hear. And it lands at the amp's *input*, so it gets amplified by every stage after it. The hum tricks below don't try to make the coupling zero (impossible); they arrange for the induced voltages to **cancel**.

## How twisting the leads helps

The heater wires carry the same current in *opposite* directions (current flows out one wire of the winding and back the other). The magnetic fields around the two wires are also in opposite directions. At any point a few inches away, the field from one wire largely cancels the field from the other.

This cancellation is **dramatically better with twisted pairs than with parallel wires**. A loose pair of parallel wires lets the fields radiate outward; a twisted pair forces them to cancel locally. The tighter the twist, the better the cancellation.

!!! note "In plain words"
    Why does twisting beat parallel? With parallel wires, a victim signal wire is always slightly closer to one heater wire than the other — so it feels one field a bit more strongly, and the cancellation is incomplete. Twisting swaps which wire is closer, over and over, every half-twist. Whatever imbalance the victim picks up in one half-twist, the next half-twist hands it the *opposite* imbalance, and they average out to nearly zero. It's the same reason you alternate which arm carries the heavy grocery bag: any one stretch is lopsided, but the trip totals out even.

You see this same principle at work in:

- Twisted-pair Ethernet cable (CAT5/6/7)
- Speaker cables sometimes
- Heater wiring throughout every well-built tube amp

## Why we "dress them along the chassis"

"Dressing" wires means routing them neatly along the chassis edge or pressed down against the metal. Two reasons:

1. Mechanically tidy and out of the way of other components
2. Keeping AC heater wires close to the grounded chassis further reduces their radiated magnetic field reaching nearby signal circuitry — the chassis acts as a partial shield

So the seemingly trivial instructions in the manual — *twist them, dress them along the chassis* — are doing real work to keep your amp quiet. A poorly-dressed heater pair can audibly add hum to the output.

## The center-tap-to-ground trick

Most heater windings (the green and brown 6.3V windings, but not the white 5V one) have a center tap brought out as a separate lead (GRN/YEL or BRN/YEL).

!!! note "In plain words"
    This is the same seesaw idea as the rectifier's center tap ([rectification](rectification.md)), used for a different purpose. A heater winding is a little seesaw: the two ends always swing equal-and-opposite around the midpoint. Twisting handled the *magnetic* coupling; the CT trick handles the *capacitive* coupling (wires sitting near each other act like tiny capacitors and leak AC voltage into each other). The cancellation only works if the seesaw's pivot is bolted to the amp's own zero — otherwise the whole seesaw floats up and down as a unit, and that common motion is what leaks into the signal.

A heater winding without a CT-to-ground reference is **floating** with respect to the amp's signal ground. Its absolute voltage relative to the rest of the amp is undefined — it could drift anywhere within the limits of the transformer's insulation. In practice, capacitive coupling between the windings ties the heater leads to some imperfect reference, but it's not a clean one.

The two heater leads swing symmetrically around the floating reference: at any instant, one is positive relative to the midpoint and the other equally negative (3.15 V RMS each, ±4.45 V at the peaks). But that floating midpoint itself wanders around, picking up stray noise.

When you reference the **center tap to ground**, you anchor that midpoint at 0V relative to the amp's signal reference. (That's the textbook version — a hard wire from CT to ground, which many amps use. This build does something slightly different: the CT is *capacitor-coupled* to ground through a 0.02 µF disc cap, which holds the midpoint at 0 V for AC purposes — the only thing hum cancellation needs — while leaving the winding DC-floating to avoid ground loops.) Now:

- One heater lead is at **+3.15V relative to ground** at any instant
- The other heater lead is at **−3.15V relative to ground** at the same instant
- 1/120th of a second later, they swap

The two leads now swing **symmetrically around zero**, which is the amp's reference.

??? note "Why a 0.02 µF cap instead of a plain wire to ground?"
    A capacitor blocks DC and passes AC — exactly what you established on the bench in [capacitors at DC](../bench-primer/04-capacitors-dc.md) and [caps with AC](../bench-primer/extras/e5-caps-with-ac.md). The hum-cancellation job only needs the midpoint anchored *for AC*: the cap does that. Meanwhile, at DC the winding stays disconnected from ground, which means no DC current can ever circulate between the heater CT and the rest of the ground network — one less possible ground loop (see [grounding and hum](grounding-and-hum.md) for why extra DC ground paths are trouble). A hard wire would work for hum too, and many amps do it that way; the cap is the belt-and-suspenders version: full AC anchoring, zero DC entanglement.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/heater-ct-comparison.svg" alt="Heater winding floating midpoint vs CT grounded comparison">
  <figcaption>Panel A: floating midpoint drifts under stray pickup, both leads ride along. Panel B: CT tied to ground anchors the midpoint at 0 V, so the two leads' induced voltages into nearby signal wiring cancel cleanly. Click to zoom.</figcaption>
</figure>

When the midpoint is held at 0V, any voltage induced into nearby signal-carrying wires (via capacitive coupling between the heater wires and the signal wires running through the chassis) is **balanced** — the +3.15V wire induces a small positive voltage, and the −3.15V wire induces an equal and opposite negative voltage, and they cancel.

When the midpoint is floating, this cancellation is imperfect. The induced voltages don't fully cancel because the reference is wandering. Result: 60Hz hum gets into the audio signal.

The 5AR4's 5V winding doesn't get this treatment for a more dramatic reason: its heater and cathode share pin 8, so the whole 5V winding rides at B+ — roughly 435 V above ground. Grounding a center tap there wouldn't reduce hum; it would short the B+ supply to ground. The winding must float at the cathode's potential, which is why the white 5V winding has no center tap to ground.

!!! note "In plain words"
    The 5AR4's heater isn't just heating the cathode — it's electrically *bolted to* the cathode, and the cathode is the point where the freshly rectified B+ leaves the tube. So the entire 5 V winding is a little 5 V seesaw riding on top of a ~435 V platform. Ground any part of it and you've connected the B+ rail straight to ground: fireworks, not hum reduction. This is also why the transformer's 5 V winding needs insulation rated for hundreds of volts even though it only *produces* five — the whole winding sits at B+ height, and only its own insulation separates it from the other windings and the core. And it's why the 5AR4 gets a private winding instead of sharing the 6.3 V ones (beyond the voltage mismatch): the signal tubes' heaters must stay near ground, not ride at B+.

## Why the heater AC frequency matters

Heater AC is at the mains frequency — 60Hz in the US. If hum couples from the heaters into the audio signal, it appears as 60Hz hum at the output. This is exactly the kind of low-frequency hum that's audible (the human ear is quite sensitive in the 60–120Hz range) and that audiophiles obsess over eliminating.

A well-designed tube amp with CT-grounded heaters can achieve hum levels 60–80dB below full output — quiet enough that you have to put your ear up to the speaker to hear it.

A poorly-grounded heater chain can produce visible-on-a-scope hum at the output. The CT-to-ground trick is one of the most cost-effective improvements in tube amp design: a single connection from each CT to the ground network (in this build, through a 0.02 µF bypass cap), and your hum floor drops dramatically.

## What to remember

- Heaters exist to **boil electrons off the cathode** — no heat, no electron cloud, no amplification. They're the only part of the tube that *produces* the electrons everything else controls.
- Heaters run on **raw AC** because heat doesn't care about current direction (P = V²/R) — so Dynaco skipped an entire rectifier/filter chain the heaters don't need.
- **5 V vs 6.3 V is not negotiable**: the first digit of the tube name tells you its heater standard, and swapping them underheats or burns out the tube.
- Every hum trick is the same trick — **make the two heater wires' effects equal and opposite so they cancel**: twisting cancels the magnetic fields, the grounded center tap balances the capacitive leakage around the amp's own zero.
- The CTs are anchored **through 0.02 µF caps**: AC-grounded (all the cancellation needs) but DC-floating (no ground loop).
- The 5 V winding gets none of this because it **rides at B+ (~435 V)** — grounding it would short the supply.

## See also

- [How transformers work](how-transformers-work.md) — what's happening upstream of the heater secondaries
- [Grounding and hum](grounding-and-hum.md) — where the heater CT eventually ties into the amp's star ground
- [PA-060 power transformer](../components/pa-060-power-transformer.md) — the specific heater windings in this build
- [Step 2 — 5AR4 heater](../build/power-supply/step-02-5ar4-heater.md) — wiring the 5V heater
- [Step 4 — V2 heater](../build/power-supply/step-04-v2-heater.md) and [step 5](../build/power-supply/step-05-v7-heater.md) — wiring the 6.3V heaters
- [Step 6 — Heater CTs](../build/power-supply/step-06-heater-cts.md) — the center-tap-to-ground trick in practice
