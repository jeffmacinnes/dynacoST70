---
title: Troubleshooting
---

# Troubleshooting

A structured decision tree for diagnosing common problems. Use it when the amp doesn't power up cleanly, doesn't pass [bias adjustment](bias-adjustment.md), or develops a new symptom in service.

Most of these symptoms have multiple possible causes. Work down the list in order — the cheap/safe checks come first; the expensive replacements come last.

!!! danger
    All troubleshooting starts with **power off and filter caps discharged**. Never poke around inside a powered amp. See [high-voltage safety](../test-equipment/high-voltage-safety.md) — this is non-negotiable.

## Symptom-driven index

- [Amp doesn't power up at all](#amp-doesnt-power-up-at-all)
- [Fuse blows on power-up](#fuse-blows-on-power-up)
- [Tubes don't light](#tubes-dont-light)
- [Tube glows bright red / arc inside the envelope](#tube-glows-bright-red-arc-inside-the-envelope)
- [No sound out, music going in](#no-sound-out-music-going-in)
- [Hum (always present)](#hum-always-present)
- [Hum (varies with music)](#hum-varies-with-music)
- [One channel only](#one-channel-only)
- [Distortion at normal listening levels](#distortion-at-normal-listening-levels)
- [Sizzling, crackling, popping](#sizzling-crackling-popping)
- [Bias drifts excessively](#bias-drifts-excessively)
- [Bias pot has no usable range](#bias-pot-has-no-usable-range)

---

## Amp doesn't power up at all

No tube glow, no hum from the transformer, nothing. The amp is silent.

### Check in this order

1. **Mains at the wall.** Plug a lamp into the same outlet to confirm.
2. **Power cord intact.** Visually inspect for breaks or cuts. Check that the plug pins look clean and not bent.
3. **Fuse.** Pull the fuse from the rear-panel holder. Hold it up to the light or test with a DMM (continuity mode). A blown fuse will be visibly broken inside, or DMM will read OL.
4. **Power switch.** With amp UNPLUGGED, use a DMM in continuity mode across the on-off switch terminals. ON should beep; OFF should read OL. If neither beeps in either position: switch is bad. If both beep: switch is shorted.
5. **Power transformer primary continuity.** Unplug. Measure DC resistance between the two prongs of the AC plug. Should read ~10-30 Ω (the primary winding's DCR). If OL: open primary winding, broken solder joint, or bad switch/fuse upstream. If <1 Ω: short — STOP, find it before applying power.

If everything above checks out and the amp still doesn't power up: the PA-060 has likely failed (rare). See [transformer specs](../appendices/transformer-specs.md) for full lead data.

## Fuse blows on power-up

Mains is reaching the amp but the fuse pops immediately or within a few seconds.

### Most common causes

| Cause | Confirmation | Fix |
|---|---|---|
| GZ-34 rectifier is shorted | Remove the GZ-34 and re-fuse (3 A Slo-Blo only — never a larger rating). Try again. If amp now powers without blowing → rectifier was the problem. | Replace the GZ-34. |
| Filter cap is shorted | With amp unplugged, DMM in ohms between each filter cap lug and chassis: should be >100 kΩ everywhere. <1 kΩ = shorted cap. | Replace the filter cap. |
| Power transformer primary shorted | Primary DCR much lower than 10 Ω. | Replace PA-060. |
| Mis-wiring (HV crossed to mains, etc.) | Visual inspection of all wiring against schematic. | Find and fix. |

The manual notes (page 14): *"Fuses blowing with all tubes removed indicate either mis-wiring or a defective PA-060 power transformer."*

A blown fuse with the GZ-34 installed but other tubes out usually means the rectifier.

A blown fuse with EL-34s installed (but fine without) means an EL-34 has gone gassy or shorted.

## Tubes don't light

Mains arrives and the amp didn't blow the fuse — but no tube's heater glows.

### Check

1. **Heater voltage at a tube socket** (with the amp powered, very carefully — see [HV safety](../test-equipment/high-voltage-safety.md)). DMM on AC volts, 30 V range. Across pins 2 and 7 of any EL-34 socket should read **6.3 V AC ±5 %**. Across pins 2 and 8 of V1 should read **5.0 V AC ±5 %**.
2. **If heater voltage is correct but tubes don't light**: tubes are bad. Check each one — sometimes a single dead tube is the only problem. Heaters fail open occasionally.
3. **If heater voltage is 0 V**: a heater winding lead has a bad solder joint somewhere. Trace back along the heater wiring ([steps 2, 4, 5, 6](../build/power-supply/index.md)).
4. **If heater voltage is half-correct** (~3.15 V AC): the center tap is open. The CT-to-lug-5 or CT-to-lug-7 wire is broken. Recheck [step 6](../build/power-supply/step-06-heater-cts.md).

## Tube glows bright red / arc inside the envelope

The plate of an EL-34 glows visible red, or you see actual sparks/arcing inside the glass. **Power off immediately** — this destroys tubes in seconds and risks shorting the power transformer.

### Causes

- **Bias is much too hot.** The grid voltage is less negative than it should be. Tube draws much more current than rated. Common after replacing tubes without re-biasing.
- **Bias supply has failed.** Diode shorted, filter cap leaky, or the −65 V bias rail has collapsed. Check pin 5 of the EL-34: should be ~−32 V. If 0 V or positive: bias has failed.
- **EL-34 has gone gassy.** Internal short or gas leak. Tube needs replacement.
- **Plate has lost its B+ feed somehow** and the tube is conducting from screen alone (rare).

Per the manual (page 14): if one tube glows but its mate doesn't, **swap them between sockets**. If the SAME tube glows in either socket, the tube is bad. If the SAME socket glows with either tube, the wiring/bias to that socket is bad.

## No sound out, music going in

Amp powers up cleanly, tubes glow, no hum or smoke — but no music.

### Check in order

1. **Cable to the source.** Try a known-good cable. Try a different source.
2. **Speaker cable.** Touch the speaker cable to the amp's output briefly — does the speaker click? If not, bad cable or bad speaker.
3. **Source signal level.** Some preamps output extremely low level. Verify with a different source.
4. **One channel or both?** If both: check the speaker terminals' wiring (BLACK common + impedance tap). If one: see [one channel only](#one-channel-only) below.
5. **Touch the tip of a screwdriver to the input RCA jack center pin.** With moderate volume on the source, you should hear a thump or buzz through the speaker. If not: the signal path from the RCA to the EL-34 is broken — bad solder joint, broken wire, dead 6GH8A.

## Hum (always present)

Hum doesn't change when music plays. Hum is there even with input unplugged.

### Check

1. **60 Hz hum (lower pitch)**: leakage from a heater winding into the audio path, or a rectifier running half-wave. Common causes:
   - Heater CT not referenced properly (lug 5 or lug 7's 0.02 µF disc cap to grounded lug 6 has a bad solder joint).
   - A heater wire too close to a signal wire (route them perpendicular if possible).
   - Aged 6GH8A with heater-cathode leakage.
   - One leg of the HV winding or one rectifier anode has failed — running half-wave instead of full-wave drops the supply ripple from 120 Hz to 60 Hz.
2. **120 Hz hum (higher pitch, "honkier")**: full-wave rectifier ripple making it through the filter. Causes:
   - A filter cap section is dried out, no longer providing capacitance. Replace the quad filter cap.
   - The choke is shorted internally (rare).
3. **Combined hum**: harder to diagnose. Start with the 60 Hz checks first.

Per the manual (page 15): *"Compare the noise in the two channels. If both are the same, it is not likely to be tubes like the 7199 or EL-34 which affect only the channel in which they operate, but it could be the GZ-34 or the quad capacitor or bias capacitors which are common to both sides of the circuit."*

## Hum (varies with music)

The hum modulates up and down with the volume of the music. Different beast — usually points to a power-supply issue.

### Check

- **Bias caps leaky**: the two 100 µF caps on the seven-lug strip filter the bias supply. If they're dried out, bias voltage sags with current draw → grids become less negative on signal peaks → MORE current draw → "motorboating" or "pumping" hum.
- **Filter cap section dried**: same idea but in the B+ chain. Listen for the hum frequency — if it follows the music's rhythm, suspect a power-supply cap.

Replace the offending cap.

## One channel only

The OTHER channel is silent.

### Check

1. **Swap inputs at the RCA jacks.** Does the problem follow the input? If yes: source/cable. If no: it's in the amp.
2. **Swap the EL-34 pairs.** Move V2/V3 (left channel) to V6/V7 (right channel) and vice versa. Did the dead channel move with the tubes? If yes: bad tube(s). If no: the wiring or driver tube on the dead side is bad.
3. **Probe the OPT primary plate leads with amp on, low signal.** Use an AC voltmeter or scope. Both BLUE and BLUE/WHITE leads (the two halves' plate leads) should show signal. If one doesn't: that tube isn't driving its half of the primary.

## Distortion at normal listening levels

Sound is recognizable but distorted.

### Check

1. **Bias is wrong.** Re-bias. If you can't reach the target, see [bias pot has no usable range](#bias-pot-has-no-usable-range).
2. **One tube in a pair is weak.** With per-tube bias mod, this shows as one tube needing the trimpot much further than the others to hit target. Without the mod, you can't tell which tube it is — swap-test between channels.
3. **Coupling cap leaking DC.** A coupling cap on the PC-3 board can develop a slow DC leak as it ages, causing the next stage's grid to drift positive. This biases the next stage incorrectly → distortion. Measure DC at the EL-34's grid (pin 5) — should be the bias voltage (~−32 V). If it's any less negative (say −20 V), the coupling cap above it is leaky.

## Sizzling, crackling, popping

Random non-musical noise overlaid on the audio.

### Causes

- **Bad tube pin contact** — most common. Tube socket spring loses tension over time. Remove and re-seat all tubes a few times to clean the contacts.
- **Bad solder joint somewhere in the signal path.** Tap each component with a wooden stick (chopsticks work) while listening. Where the noise changes pitch or volume, there's your suspect joint.
- **Corroded socket pins.** Clean with isopropyl alcohol on a swab.
- **A tube with intermittent internal contact**. Tap each tube gently with a pencil while listening. A microphonic tube will ring; an intermittent one will crackle.

The manual notes (page 16): *"In some rare cases, loud pops may be heard through the loudspeakers. These can come from poor conditions inside the pins of the EL-34 tubes. Touching a hot soldering iron to these pins will rectify this."*

## Bias drifts excessively

You set bias, walk away, come back 30 minutes later, and it's moved by more than ~3-5 mV per tube (or ~10-15 mV at the Biaset socket on the stock method).

### Causes

- **Heater-cathode leakage** in an EL-34. As the tube warms fully, the leakage current shifts the bias point. Replace the tube.
- **The bias supply itself is unstable.** A leaky bias filter cap can cause this. Replace the 100 µF bias caps on the 7-lug strip.
- **Tube cathode is aging out.** Drift gets worse as the cathode depletes. Eventually the tube can't sustain its bias and you'll see steady drift over hours. Time to retire that tube.

If only one tube/pair drifts and the others don't, that one is the problem. If all four drift similarly, the bias supply is suspect.

## Bias pot has no usable range

You can't get the cathode voltage to the target (1.56 V stock or 50 mV per-tube), even at maximum negative on the pot.

### Causes

- **Tubes are too "hot" out of the box.** New tubes with very high transconductance can draw more current than the bias network is configured for. Sometimes a 50-100 hour burn-in settles them.
- **Bias supply isn't producing enough negative voltage.** Should be ~−65 V at the diode's (B) lug. If it's −40 V or less, the bias supply has failed (diode partially shorted, filter cap leaky).
- **The fixed series resistor in the bias path is wrong value.** Compare against the schematic.
- **Bias pot is intermittent.** Try wiggling. If the reading jumps around, the pot's wiper is dirty or worn. Spray with DeoxIT or replace.

A common workaround: add a small series resistor in the bias supply path (3.3 kΩ ¼ W typically) to bring the maximum-negative end of the pot's range further negative.

## See also

- [Voltage checks](voltage-checks.md) — concrete reference values to compare against
- [Bias adjustment](bias-adjustment.md) — the procedure many of these symptoms relate to
- [Functional testing](functional-testing.md) — what "working correctly" looks like
- [Grounding and hum](../theory/grounding-and-hum.md) — deep theory on hum diagnosis
- [High-voltage safety](../test-equipment/high-voltage-safety.md) — required reading before any of this
