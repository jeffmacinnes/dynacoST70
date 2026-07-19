---
title: Rectification
---

# Rectification: turning AC into DC

Rectification is the bridge between what the wall provides (AC) and what tubes need on their plates (DC). This chapter covers half-wave vs. full-wave rectification, the 5AR4 specifically, smoothing, and the 180° phase relationship across a center tap — a concept that shows up everywhere in tube audio.

## The big picture

The power supply is a three-step assembly line, and this page is step 2:

1. **Transform** — the [PA-060](../components/pa-060-power-transformer.md) steps the wall's 120 V AC up to 360 V AC per half-winding (tubes need hundreds of volts on their plates).
2. **Rectify** — the 5AR4 forces the current to flow in one direction only. The output is now DC, but *bumpy* DC: a train of humps, not a flat line.
3. **Smooth** — capacitors and a choke iron out the humps into the steady B+ rail the tubes actually run on.

Why can't the tubes just run on AC directly? Because a tube amplifies by letting a small grid voltage control a one-way stream of electrons from cathode to plate — and that stream only flows when the plate is *positive*. On AC, the plate would be positive only half the time, and the "amplified" output would carry a huge 60 Hz wobble mixed into your music. The plate supply must be steady DC so that the *only* thing changing at the plate is the music.

!!! note "Diagram placeholders"
    ASCII waveforms here will be replaced with matplotlib-generated graphics. Interactive rectification animations are planned — see [diagram roadmap](../index.md).

## The problem

Tubes need DC on their plates. The wall provides AC. Something has to bridge that.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/rectification-waveforms.svg" alt="Rectification waveforms at each stage">
  <figcaption>What the waveform looks like at each stage: raw AC from the transformer, after one diode (half-wave), after the 5AR4's two anodes (full-wave). Hover any panel for the physics. Click to zoom.</figcaption>
</figure>

## What "rectify" means

The word comes from the Latin *rectus* (straight, right, correct) — same root as "rectangle" and the everyday "rectify" meaning to fix or straighten out. In electronics it specifically means **converting alternating current (AC) into direct current (DC)** by forcing the current to flow in only one direction.

## How a diode rectifies

A diode is a one-way valve for current. It conducts when voltage is applied in one direction (forward-biased) and blocks when applied the other way (reverse-biased). You've already handled these on the bench — the one-way conduction and the forward voltage drop are exactly what you measured in [LEDs and diodes](../bench-primer/extras/e3-leds-and-diodes.md).

!!! note "In plain words"
    A diode is the electrical version of a check valve in a plumbing system — the kind with a hinged flap that swings open when water pushes one way and slams shut when it tries to flow back. Push AC through a check valve and the back-and-forth slosh becomes a series of one-way squirts. That's rectification, the whole idea of it, in one sentence.

Putting a diode in line with the AC source produces **half-wave rectification** (panel 2 of the diagram above): the negative halves are blocked. What remains is a series of positive humps — current flowing in only one direction. It's still bumpy DC, not smooth, but it's now *unidirectional*, which is the essential first step.

## Full-wave rectification (what the 5AR4 does)

Half-wave wastes half the energy and produces dirty DC that's hard to smooth. **Full-wave rectification** uses additional diodes (or, in the [5AR4](../components/5ar4-rectifier-tube.md)'s case, two diodes in one tube envelope) to flip the negative halves up — panel 3 of the diagram above. Both halves contribute positive pulses, and the output frequency doubles from 60 Hz to 120 Hz, which makes it far easier to filter.

Why is 120 Hz "far easier to filter" than 60 Hz? Two reasons, both about the filter cap downstream:

- **Shorter gaps to bridge.** The cap charges at each peak and then coasts, supplying the amp from stored charge, until the next peak refills it (the reservoir behavior you explored in [capacitors at DC](../bench-primer/04-capacitors-dc.md)). With full-wave the refills come every 1/120 s instead of every 1/60 s — half the coasting time, so the voltage droops half as far between refills. Same cap, half the ripple, for free.
- **No dead half-cycle.** In half-wave, the cap must carry the entire load alone for a full half-cycle in which the diode delivers *nothing*. Full-wave never leaves the cap unsupported that long.

!!! note "In plain words"
    Half-wave is one worker filling a leaky bucket, but only allowed to pour every *other* trip to the well. Full-wave is two workers alternating trips — the bucket gets topped up twice as often, so its level barely dips. Same well, same bucket, much steadier water level.

??? note "Why a center tap instead of a 4-diode bridge?"
    If you've seen modern power supplies, you may know the **bridge rectifier**: four diodes that achieve full-wave rectification from a simple two-lead winding, no center tap needed. So why did Dynaco use a center-tapped winding instead? Because with *tube* diodes, every diode is expensive: it's a big glass envelope, a socket, and a power-hungry heater winding. A bridge would need four tube diodes (or two dual-diode tubes) plus their heaters. The center-tap trick gets full-wave rectification from just **two** diodes — which fit in a single 5AR4 — at the cost of some extra copper in the transformer. In 1959, copper was cheaper than tubes. With silicon diodes at pennies each, the economics reversed, which is why modern gear uses bridges.

The 5AR4 has two anodes (pins 4 and 6 on the tube socket) connected to the two ends of the high-voltage transformer winding. The center tap of that winding (the RED/YEL lead) provides the ground reference. On the positive half-cycle, current flows through one anode; on the negative half-cycle, current flows through the other anode. The cathode (pin 8 — also where the heater is, since the 5AR4 is indirectly heated) sees both halves as positive pulses.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/full-wave-rectifier-topology.svg" alt="Full-wave rectifier topology">
  <figcaption>The complete circuit: PA-060 HV secondary with center tap, 5AR4 dual-anode rectifier, filter cap, B+ rail to load. Hover any component for its role and wiring details. Click to zoom.</figcaption>
</figure>

See [step 3](../build/power-supply/step-03-5ar4-anodes.md) for the actual wiring that creates this topology, and [step 7](../build/power-supply/step-07-hv-ct.md) for the center-tap connection that completes it.

## The 180° phase relationship across a center tap

Full-wave rectification depends on a deep fact about center-tapped windings: **the two ends are always exactly 180° out of phase** with each other relative to the center tap.

!!! note "In plain words"
    Picture a seesaw with the pivot in the middle. When one end is up, the other end is down — always, automatically, by construction. The center tap is the pivot; the two RED winding ends are the seats. "180° out of phase" is just the electrical way of saying "perfect seesaw": at every instant, one end is exactly as far *above* the center tap voltage as the other end is *below* it. This is why two diodes are enough for full-wave rectification — at any moment, **one of the two ends is guaranteed to be positive**, so one of the 5AR4's two anodes always has something to conduct.

The center tap is exactly halfway through the high-voltage coil. Both halves of the secondary are wound around the same core, share the same magnetic field, and have the same number of turns. So they produce equal-magnitude voltages.

But because we measure each half "from the center tap outward," the two ends end up with opposite polarities at any instant:

```
       RED (one end)
        │
        ║  ← top half of winding
        ║
        ║
   RED/YEL (center tap)
        ║
        ║  ← bottom half of winding (same number of turns)
        ║
        │
       RED (other end)
```

Each half of the winding produces 360 V RMS, which peaks at about ±509 V at the instant of maximum field. When the magnetic field is rising in one direction:

??? note "Where does 509 V come from? (RMS vs. peak)"
    "360 V RMS" is the *effective* value of the sine wave — the DC voltage that would deliver the same heating power. But a sine wave spends its time swinging between peaks that are higher than its RMS value by a factor of $\sqrt{2} \approx 1.414$:

    $$V_{peak} = V_{RMS} \cdot \sqrt{2} = 360 \cdot 1.414 \approx 509\ \text{V}$$

    This matters for two very practical reasons. First, the filter cap charges to the **peak**, not the RMS — which is why B+ starts near 500 V, well above 360. Second, every insulation and voltage rating in the supply must survive the peak, not the average. Your DMM reads RMS; your scope shows peaks. Both are telling the truth.

- **Top RED end:** up to +509V relative to CT
- **Bottom RED end:** down to −509V relative to CT

Half a cycle later (1/120th of a second), the field reverses and so does the polarity:

- **Top RED end:** down to −509V relative to CT
- **Bottom RED end:** up to +509V relative to CT

The two ends are **always opposite** — at any instant, whatever voltage one end sits at, the other is its mirror image.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/phase-180-degrees.svg" alt="180 degree phase relationship across a center-tapped winding">
  <figcaption>Two sine waves measured at the two RED leads relative to the center tap. They cross zero at the same instants; their peaks are exact mirror images. Click to zoom.</figcaption>
</figure>

### The deeper physics: Faraday's law

The 180° phase relationship comes from **Faraday's law of electromagnetic induction**. The voltage induced in a coil is proportional to the rate of change of magnetic flux through it:

`V = −N · (dΦ/dt)`

where N is the number of turns and Φ is the magnetic flux. The negative sign in Faraday's law is what gives us the phase relationship — voltage opposes change, and the geometry of the winding determines the sign convention.

Both halves of the secondary share the same dΦ/dt (same flux going through the same core). They have the same N (same number of turns). So they produce equal-magnitude voltages. The 180° phase relationship comes from how we define their positive terminals: if we measure each half "from CT outward," they appear in series, and the polarity at the far end of one is opposite to the polarity at the far end of the other.

### Why this matters beyond the rectifier

The "two halves of a center-tapped winding are 180° out of phase" relationship shows up everywhere in tube audio:

- **Full-wave rectification** (here, in the power supply)
- **[Phase splitter circuits](phase-splitting.md)** (the driver tube generates two signals 180° apart to drive the push-pull output stage)
- **[Push-pull output transformers](push-pull-topology.md)** (the output transformer's primary has a center tap, and the two output tubes drive opposite halves)
- **Differential / balanced audio circuits**

The same trick — using a center tap as a reference point and exploiting the natural opposite-phase relationship across the two halves — is foundational to how push-pull tube amps work end-to-end. The output stage uses this same principle, just for audio signals instead of 60Hz mains.

## The 5AR4 specifically

The 5AR4 (also called GZ34 in European nomenclature) is an **indirectly heated** rectifier, which is somewhat unusual. The filament heats a separate cathode sleeve, rather than the filament itself being the cathode. This gives it two desirable properties:

!!! note "In plain words"
    "Directly heated" means the glowing filament wire *is* the electron-emitting surface — like cooking directly over the flame. "Indirectly heated" means the filament is a heater tucked inside a metal sleeve, and the *sleeve* emits the electrons — like cooking on a pan over the flame. The pan takes longer to come up to temperature (that's the slow warm-up) and it keeps the food away from the flame itself (that's the isolation from heater AC).

1. **Slow warm-up** (~10 seconds before it conducts). This is a *feature*: the rectifier comes online *after* the signal tubes have warmed up, so the high-voltage B+ doesn't slam onto cold output tubes (which causes "cathode stripping" damage over time).
2. **Quieter operation** — directly-heated rectifiers can inject AC ripple from the filament into the DC output. Indirect heating isolates the cathode from the AC heater current.

When you fire up the ST-70 and there's a delay before sound starts, that's the 5AR4 doing its job — letting everything else stabilize first.

See the [5AR4 component page](../components/5ar4-rectifier-tube.md) for tube specifics: pinout, dual-anode topology, specs, failure modes.

## Smoothing: from pulsating DC to clean DC

After rectification, you have unidirectional but bumpy DC. The next stages smooth it:

1. **[Filter capacitors](../components/filter-capacitors.md)** charge up during the peaks and discharge during the valleys, filling in the gaps. They act as energy reservoirs.
2. **[Chokes (inductors)](../components/choke.md)** resist *changes* in current, further smoothing the ripple.

!!! note "In plain words"
    The filter cap is a water tower. The rectifier is a pump that only runs in short bursts, 120 times a second — but the town needs steady water pressure all the time. The tower absorbs the pump's bursts and delivers a smooth flow; the bigger the tower (more µF), the less the level dips between bursts. The choke is a heavy flywheel in the pipe: it hates changes in *flow*, so it passes the steady DC current while fighting the 120 Hz surges. Cap smooths voltage; choke smooths current — together they're far more effective than either alone.

Why a choke instead of just a resistor between the two caps? A resistor would also help the second cap filter (that's the RC filtering you built in [caps with AC](../bench-primer/extras/e5-caps-with-ac.md)) — but a resistor big enough to kill the ripple would also drop a huge chunk of DC voltage at the amp's ~200 mA draw. The choke cheats: it has a *small* DC resistance (spec 62 Ω; this one measures 71 Ω, dropping only ≈ 15 V at the full 212 mA load) but a *large* impedance at 120 Hz. It fights the ripple hard while barely taxing the DC. Full-wave rectification helps it, too: doubling the ripple frequency to 120 Hz doubles the choke's impedance to the ripple.

Here's the smoothing chain doing its job, measured on this build:

| Point on the rail | Measured ripple | Why |
|---|---|---|
| First filter cap (lug 2) | ~40 Vp-p, 120 Hz sawtooth | The raw charge/coast cycle — the cap alone against the full load |
| After the choke (lug 1) | ~2–3 Vp-p | The choke + second cap knock ripple down ~15× |
| Driver rail (lug 4) | ~110 mVp-p | Another RC stage; the driver draws little current, so a resistor is fine here |
| Input-stage rail (lug 3) | < 1 mV | One more RC stage — quietest rail for the most sensitive stage |

Notice the pattern: **each stage of the amp gets a cleaner supply than the last, in order of sensitivity.** The output tubes tolerate a couple volts of ripple (push-pull cancels most of it — see [push-pull topology](push-pull-topology.md)); the input stage, whose signal is millivolts, gets a rail with less than a millivolt of ripple. That's why the supply is a *chain* of filters rather than one giant cap: each stage only needs to be as clean as its consumer, and the RC stages get cheap once the current is small.

One more real-world effect: the B+ voltages sag below the manual's chart under load — the rectifier and transformer have source impedance, exactly the behavior you measured in [source impedance and sag](../bench-primer/extras/e4-source-impedance-and-sag.md). On this build (mains ~116 V), lug 2 measures 428 V against the chart's 435, and lug 4 measures 349 V against the chart's 375, mostly because the driver board draws ~9.4 mA rather than the ~6 mA the chart assumes.

<figure class="diagram-fig" markdown="span">
  <img src="../../assets/diagrams/smoothing-chain.svg" alt="Smoothing chain — what each filter stage does to the waveform">
  <figcaption>Same vertical scale on all four panels, in approximate ST-70 volts (B+ ≈ 435 V, V_peak ≈ 509 V). Ripple amplitudes are exaggerated so each stage's shape is visible — measured on this build, the ripple is ~40 Vp-p at the first cap, ~2–3 Vp-p on the main B+ rail after the choke (and push-pull cancels most of that at the speaker), and under a millivolt by the input-stage rail. Click to zoom.</figcaption>
</figure>

The ST-70 uses a two-stage filter: rectifier → filter cap → choke → second filter cap → output tubes. This produces clean enough B+ that no audible hum reaches the output.

## What to remember

- Tubes need **steady DC** on their plates so the only thing changing there is the music; the wall gives AC, and rectification is the bridge.
- A diode is a **check valve**: it turns AC's back-and-forth slosh into one-way pulses.
- The center-tapped winding is a **seesaw**: the two ends are always mirror images around the CT, so one of the 5AR4's two anodes always has a positive voltage to conduct. Two diodes buy you full-wave.
- Full-wave doubles the ripple to **120 Hz**, which halves the cap's coasting time between refills — cleaner DC from the same parts.
- The cap charges to the **peak** (509 V), not the RMS (360 V) — $\sqrt{2}$ apart.
- Smoothing is a **chain**: big cap, then choke, then RC stages — each rail cleaner than the last, matched to how sensitive its stage is (40 Vp-p at the first cap down to < 1 mV at the input stage on this build).

## See also

- [How transformers work](how-transformers-work.md) — what's happening on the AC side before the rectifier
- [5AR4 rectifier tube](../components/5ar4-rectifier-tube.md) — the specific rectifier in this build
- [1N4007 diode](../components/1n4007-diode.md) — the small silicon diode used for bias supply rectification
- [Step 3 — 5AR4 anodes](../build/power-supply/step-03-5ar4-anodes.md) — wiring the rectifier inputs
- [Step 7 — HV center tap](../build/power-supply/step-07-hv-ct.md) — completing the rectifier topology
