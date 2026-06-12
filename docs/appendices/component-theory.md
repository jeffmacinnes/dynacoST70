---
title: Component theory deep dives
---

# Component theory deep dives

Things that are too specific for the per-component pages but apply broadly across the build. Reference material, mostly — not required reading for building, but useful when you're picking replacement parts or wondering "why does X work the way it does?"

## Capacitor types

A capacitor stores energy in an electric field between two conductors separated by a dielectric. The differences between types come down to what's used as the dielectric and how it's physically constructed.

### Electrolytic

Two thin aluminium foils with a paper soaked in conductive electrolyte between them. One foil has been **anodised** — its surface oxidised into a thin insulating layer of aluminium oxide. That oxide is the actual dielectric.

- **Pros**: huge capacitance per unit volume (the oxide is incredibly thin → huge capacitance for a given area). Cheap.
- **Cons**: polarised (wrong polarity = catastrophic failure). Limited lifespan (electrolyte dries). High ESR compared to other types. Not great at high frequencies.
- **Used for**: bulk filtering (B+ filter caps), bypass on power supplies.

### Film (polypropylene, polyester, polystyrene)

A thin plastic film coated with metal, rolled into a cylinder. The plastic is the dielectric.

- **Pros**: very stable over temperature and time. Low ESR. Non-polarised. Long life (decades). Good high-frequency response.
- **Cons**: much larger than electrolytic for the same capacitance. Generally limited to <1 µF for reasonable sizes.
- **Used for**: signal coupling caps, bypass caps in the signal path, anywhere precision matters more than capacitance density.

The ST-70's audio-path coupling caps (between stages on the PC-3A) are an obvious candidate for film. Originally they were paper-in-oil or film; replacements should be high-quality film.

### Ceramic (multilayer / disc)

Alternating layers of ceramic and metal, fired into a solid block.

- **Pros**: very small, very cheap, decent high-frequency performance.
- **Cons**: capacitance varies wildly with voltage and temperature (the dielectric is non-linear). Sounds "harsh" in signal-path applications. Microphonic (mechanical vibrations modulate the capacitance).
- **Used for**: RF bypass, decoupling on high-frequency circuits. Rarely in tube audio.

If you find a ceramic cap in an audio signal path of a tube amp, it's there to bypass RF interference, not as a deliberate audio choice. They're acceptable in that role.

### Paper-in-oil (PIO)

Paper soaked in oil, between two metal foils. The oil is the dielectric.

- **Pros**: famous for "warmer" sound (debate about whether this is real or psychosomatic). Stable.
- **Cons**: heavy, large, expensive. Oil can leak as they age.
- **Used for**: vintage tube amp coupling caps. Audiophile-grade replacements.

Original 1960 Dynacos used PIO caps; they're long expired. Modern PIO replacements exist and are expensive.

## Capacitor ESR

**Equivalent Series Resistance** (ESR) is the parasitic resistance of a capacitor — what you'd measure if you could probe inside the cap. It includes:

- The wire/foil resistance.
- The contact resistance between leads and foils.
- Loss in the dielectric.

For an ideal capacitor, ESR is zero. For a real cap, it's a small fraction of an ohm (good electrolytic) to tens of ohms (aged or low-quality electrolytic).

ESR matters because:

- **Power dissipation** under ripple current. An electrolytic with 1 Ω ESR carrying 100 mA RMS dissipates 0.01 W internally — not much, but it heats the cap, accelerating drying.
- **Filtering effectiveness**. Higher ESR means more ripple voltage developed across the cap → less smoothing.
- **Aging signal**. ESR is a leading indicator of cap aging — it rises (sometimes 10×) before capacitance starts dropping.

An ESR meter is the right tool for diagnosing tired electrolytics. A regular DMM only measures capacitance and DC characteristics, missing the ESR rise.

## Resistor types

### Carbon composition (vintage)

A solid rod of graphite mixed with binder, with axial leads pressed into the ends.

- **Pros**: simple, cheap, durable under transient overload (carbon doesn't crack from short pulses).
- **Cons**: noisy (excess noise — see below). Drift upward in value over time. Tolerance was originally ±10 %, drifts to ±20 % or worse over decades.
- **Why ST-70 used them**: 1959 — they were the cheapest option that worked.

### Carbon film

A film of carbon deposited on a ceramic rod, with spiral grooves cut to set the resistance.

- **Pros**: lower noise than composition. Better tolerance (±5 % new). Cheaper than metal film.
- **Cons**: less robust under transient overload. Worse temperature coefficient than metal film.
- **Usage**: common in 1970s-80s consumer electronics.

### Metal film

Similar to carbon film but with a metal alloy instead of carbon.

- **Pros**: very low noise. Tight tolerance (±1 % standard). Stable over time and temperature.
- **Cons**: somewhat fragile under transient overload (the thin film can vaporise).
- **Usage**: modern signal-path electronics.

### Wirewound

A coil of resistance wire (nichrome or similar) wound on a ceramic former, encased in cement or aluminium.

- **Pros**: very precise. High power handling (a wirewound resistor is essentially a heater you can ignore). Stable.
- **Cons**: inductive (a wirewound is also a small coil). Expensive.
- **Usage**: power supply dropping resistors, cathode bias resistors at high current.

### When to use which

For replacement parts in the ST-70:

- **Signal path** (grid stoppers, plate loads in input stage): metal film, ±1 %.
- **Power supply** (dropping resistors): wirewound or metal-oxide film, with margin on the wattage.
- **Cathode bias resistors** for output tubes: high-watt metal-oxide or wirewound (1 W or higher).
- **Carbon composition replacements**: only if you're doing a period-correct restoration; modern metal film performs better in every measurable way.

## Resistor noise

Resistors don't just resist — they also generate noise. Two kinds:

### Johnson (thermal) noise

Random thermal motion of electrons. Unavoidable, present in every resistor at every temperature above absolute zero. Magnitude (RMS voltage):

`V_noise = √(4 k T R Δf)`

For a 1 MΩ resistor at room temperature with 20 kHz bandwidth: ~18 µV RMS.

This is the noise floor below which you can't go. It's all the noise present in a metal-film or wirewound resistor.

### Excess noise (carbon composition specifically)

Carbon composition resistors have additional noise on top of Johnson — a flicker-noise component that's proportional to the DC current through the resistor. Typically 5-30 dB above the Johnson floor.

This is why old tube amps with carbon comp resistors are often hissier than they need to be. Replacing the carbon comp resistors in the signal path with metal film drops the noise floor measurably.

For the ST-70, the candidates for noise-improvement-by-resistor-swap are the carbon comp resistors in the input stage and phase splitter. The output stage is so much noisier that resistor noise there is irrelevant.

## Tube physics

### Thermionic emission

A heated cathode releases electrons into the vacuum. The relationship between cathode temperature and emission current is the **Richardson-Dushman equation**:

`J = A · T² · exp(−W / (k T))`

where W is the work function of the cathode material. The exponential dependence means emission rises very rapidly with temperature.

For oxide-coated cathodes (the standard in audio tubes), W is small (~1 eV), so usable emission starts around 700-800°C cathode temperature. Below that, the tube is "cold" and barely conducts.

### Space charge

Electrons emitted from the cathode pile up in the space between cathode and anode — a cloud of negative charge. This **space charge** repels further electrons trying to leave the cathode. In steady state, only as many electrons leave as are pulled toward the anode.

The space charge is what makes the grid effective: a small change in grid voltage modulates the *available* current through the cloud, not the total emission. That's why tube transconductance can be high even with limited cathode emission.

### Plate dissipation

The plate (anode) absorbs all the electrons that don't go elsewhere. Each electron arrives with kinetic energy = e × V_plate (where V_plate is the potential the electron fell through). Power dissipated in the plate:

`P_plate = I_plate × V_plate`

For an EL34 at 450 V plate, 50 mA idle current: P_plate = 22.5 W. The plate is rated for 25 W — comfortable margin.

If plate dissipation exceeds the rating, the plate gets hot enough to **out-gas** (release adsorbed gases from the metal). The gas ionises, the tube shorts, end of tube.

### The pentode "knee"

The pentode's plate-current-vs-plate-voltage curve has a characteristic shape:

- Below the "knee" (low plate voltage, like <30 V): current rises steeply with plate voltage.
- Above the knee: current is nearly constant — depends mostly on grid voltage, weakly on plate voltage.

That flat region above the knee is what makes the pentode useful: it acts like a current source (high output impedance) driven by grid voltage. The plate voltage barely affects the current.

For audio: the pentode's output impedance is high (≈15 kΩ for an EL34), which is what makes it want a transformer-coupled load. The OPT steps that down to the speaker's 8 Ω.

## Transformer leakage inductance

In an ideal transformer, all magnetic flux generated by the primary couples perfectly to the secondary. In reality, some flux "leaks" — escapes the iron core, returns through the air, doesn't link the secondary.

The unlinked flux behaves like an inductor in **series with** the transformer, between primary and secondary. This is **leakage inductance**.

At low frequencies, leakage inductance has negligible impedance (jωL is small). At high frequencies, it acts as a rolloff — series inductance + load capacitance = first-order low-pass filter at the band edge.

The fix: **interleave** the primary and secondary windings. Instead of "all primary, then all secondary" stacked on the bobbin, do "primary-secondary-primary-secondary-primary" in alternating layers. The closer the primary turns are to the secondary turns, the better the magnetic coupling, the lower the leakage inductance.

The A-470 uses 5+ interleaved sections, which is why it has such extraordinary high-frequency response (−1 dB at 30 kHz at full power, in 1959).

## Dielectric absorption

A capacitor that's been charged, then discharged through a short, will gradually "recover" some voltage on its own — even with no input. This phenomenon is **dielectric absorption** (DA), and it's caused by dipoles in the dielectric realigning slowly after the field changes.

DA varies dramatically by dielectric type:

- **Polypropylene**: ~0.01 % (negligible).
- **Polystyrene**: ~0.05 %.
- **Mica**: ~0.05 %.
- **Polyester (Mylar)**: ~0.2-0.5 %.
- **Ceramic (X7R)**: ~2.5 %.
- **Electrolytic**: very high, ~10 %.

In audio: DA is what's blamed for some capacitors "sounding different." The theory is that DA causes a small delayed signal — an echo at very low level — that smears micro-detail.

The science here is murky. Measurable DA effects in well-designed audio circuits are below the threshold of audibility for most listeners. But choosing polypropylene over polyester for signal-path caps costs little extra and removes one variable.

For the ST-70 coupling caps: polypropylene is the canonical modern choice. Polystyrene is also excellent (and traditionally favored by audiophiles) but limited to smaller values.

## See also

- [Filter capacitors](../components/filter-capacitors.md) — the specific electrolytics in this build
- [How transformers work](../theory/how-transformers-work.md) — including interleaving in the A-470
- [EL34 output tube](../components/el34-output-tube.md) — concrete tube specs
- [PC-3A driver board](../components/pc-3a-driver-board.md) — the signal-path caps + resistors worth upgrading
