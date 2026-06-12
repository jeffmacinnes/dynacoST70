---
title: High-voltage safety
---

# High-voltage safety

This is the most important page on this site. **Read it before bring-up.**

## What the actual voltages will be

When the ST-70 is powered up and operational:

| Node | Voltage (approx.) | Notes |
|---|---|---|
| Each red lead (relative to center tap) | 360V AC RMS | Swings ±509V peak around 0V |
| Across full red-red winding | 720V AC RMS (~1,018V peak) | Don't measure this; exceeds DMM safety rating |
| 5AR4 anodes (pins 4 and 6) | 360V RMS (≈509V peak) per side | Same as red leads |
| 5AR4 cathode (pin 8) after rectification + filtering | ~450V DC | This is your B+ rail |
| [Filter cap](../components/filter-capacitors.md) positive terminals | ~450V DC | **Holds charge after power-off!** |
| [EL34](../components/el34-output-tube.md) plate pins | ~450V DC | Connected to B+ via output transformer primary |
| EL34 screen pins | ~415V DC | Fed from the OPT's ultralinear taps — slightly *above* the ~410V plate voltage; no dropping resistor |

## The two hazards

### 1. Powered amp

450V DC at 100mA+ available current is more than enough to be lethal. Skin resistance under typical conditions is 1000–10000Ω. At 450V, that's potentially 45–450mA through your body. Currents above about 100mA across the chest can stop the heart. The B+ rail is *capable* of delivering well above that.

### 2. Powered-down amp with charged filter caps

The filter caps are designed to *store* energy — that's their entire job in the power supply. A 30μF cap at 450V holds 3 joules. A 60μF cap holds 6 joules. That's enough energy to seriously injure you, and the discharge happens in milliseconds if you provide a path. The caps don't drain instantly when you flip the power switch; they can hold lethal voltage **for minutes to hours** depending on what bleeder paths exist in the design.

## Discharging filter caps

**Always discharge the filter caps before working inside a powered-down amp.** Methods:

- **Bleeder resistor** built into the design (some kits include one). Drains the caps automatically over ~30 seconds after power-off.
- **Manual discharge tool** — a 10kΩ, 5W resistor with insulated probes. Touch one probe to chassis ground, the other to the cap's positive lug. Hold for several seconds. The voltage discharges through the resistor with no spark or surge.

!!! danger "Don't short the caps directly"
    Don't short the caps directly with a wire or screwdriver. The instantaneous current can melt the conductor, weld the screwdriver to the cap, blow chunks out of the cap's terminal, or cause the cap to rupture and spray electrolyte (which is corrosive and hot). The series resistor turns a violent spark into a controlled drain over several seconds.

### The "every cap is potentially live" mindset

A useful long-term habit: never assume a capacitor is discharged. Always check with a meter before touching, regardless of how long the amp has been off. This applies to the ST-70 and every other piece of vintage gear, and every amp anyone gives you to look at. Filter caps are sneaky.

This is why many amp techs keep a "cap discharge tool" — a 10kΩ resistor with insulated leads on each end — as the first thing they reach for when opening any unfamiliar amp.

## Standard procedure before reaching inside a powered-down amp

1. Power off, unplug from wall
2. Wait at least 60 seconds for any built-in bleeder resistors to drain the caps
3. **Verify with a meter**: probe across each filter cap to confirm it reads <10V or so before touching anything
4. If voltage is still present, **manually discharge** through the 10kΩ 5W resistor as described above
5. Re-verify with meter before proceeding

## One-hand rule

When making a live measurement, keep one hand in your pocket or behind your back. Use the other hand to hold the probe. The reason: if a path forms from probe to your body, you want it to go through the limb that's making the measurement, not across your chest. A current path across your chest can cause cardiac arrhythmia at currents far below what your skin can normally tolerate.

This is also why the **alligator-clip-on-ground / probe-in-hand** setup is so much safer than two free-floating probes. See [probes](probes.md#useful-upgrades).

## Other safety habits

- **Power off and unplug before working inside**, even if you're going to power back up shortly
- **Wait at least 60 seconds** after power-off before reaching in (filter caps need time to drain)
- **Check filter cap voltage with a meter** before assuming they're discharged
- **Wear safety glasses** — blown filter caps can spray electrolyte, and arc flash is bright
- **Keep one hand free** during any live work
- **Don't work tired** — most accidents happen during the third hour of "just one more thing"

## Why voltage alone doesn't tell you whether something is dangerous

See [voltage source vs current path](../theory/voltage-vs-current.md). A van de Graaff generator at 400,000V is a parlor trick because it can't push enough current to hurt you. A 12V car battery can melt a wrench. **It's voltage *across* a low-resistance path that creates dangerous current** — and your body, at 450V, is a low-enough resistance path.

## See also

- [Multimeter](multimeter.md) and [probes](probes.md) — only as safe as the weakest rating in the chain
- [Filter capacitors](../components/filter-capacitors.md) — the specific caps to be careful around
- [Voltage source vs current path](../theory/voltage-vs-current.md) — the mental model behind the safety practices
- [First power-on](../bring-up/first-power-on.md) — the bring-up procedure where these practices first matter
