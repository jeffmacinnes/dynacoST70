---
title: Pre-power checklist
---

# Pre-power checklist

Before the amp ever sees mains voltage, work through this checklist. The goal is to catch obvious mistakes while they're cheap — a wire touching the chassis is free to fix now, expensive once it sets fire to the power transformer.

This is the FIRST bring-up page in the sequence:

1. **Pre-power checklist** ← you are here
2. [Continuity checks](continuity-checks.md) — DMM verification of every node
3. [First power-on](first-power-on.md) — variac slow ramp
4. [Voltage checks](voltage-checks.md) — measure expected voltages everywhere
5. [Bias adjustment](bias-adjustment.md) — set EL34 idle current
6. [Functional testing](functional-testing.md) — signal injection and listening

## Visual inspection

Spend 30 minutes with a bright light and a magnifier visor, looking at every connection on the chassis.

### Solder joints

A good joint is:

- **Shiny.** A matte or grainy joint is a "cold" joint — wire wasn't hot enough when the solder set, mechanical bond only, will fail.
- **Concave fillet.** Solder flows up the wire and the lug, forming a smooth slope. A ball-shape (convex blob) means the solder didn't wet the metal.
- **Wire visible through the solder.** You can see the wire's profile inside the joint. If the wire is completely buried in a solder blob, you've used way too much.

Re-flow any suspicious joint: heat the joint until the solder visibly melts, hold for a second, remove heat. The joint will re-solidify into a proper shape.

### Whisker bridges

Stray bits of solder, tinned wire ends sticking out, or strands of stranded wire can short adjacent points. Look between:

- Adjacent pins on every tube socket.
- Adjacent lugs on terminal strips.
- The filter cap lugs (especially the high-voltage +1 lug to nearby chassis points).
- Any small-pitch resistor leads.

A magnifier and a bright light catch ~95 % of these. Investigate anywhere that looks like solder reached past where it should be.

### Component orientation

Check that polarized components are oriented correctly:

- **Filter caps** — positive lugs to the high-voltage side, negative (the can itself) to chassis.
- **Diodes** — banded end (cathode) is where the current flows OUT. The 1N4007 in step 1 has its banded end connected to the transformer lead.
- **Electrolytic coupling caps** (if any) — match the schematic's polarity marks.

Get any polarity wrong and you get a quick, dramatic failure on power-up.

## Lead-dress audit

Look at how wires are routed across the chassis.

### Things that should be apart

- **Heater wires and signal wires** should cross at right angles, not run parallel. Parallel = 60 Hz capacitive coupling into the audio signal = hum.
- **Heater wires and grid wires** specifically — the EL34 grid wire is the most sensitive node in the amp. Keep heater AC far away.
- **B+ wires and signal wires** should not be bundled together. B+ has the ripple frequency on it; you don't want it inductively coupling into signal wires.

### Things that should be close

- **Heater pair twisted together** — the two leads of a 6.3 V winding (GRN-GRN or BRN-BRN) should be tightly twisted along their entire length. Twist suppresses the magnetic field. Loose pairs radiate.
- **Speaker output and feedback wire** can be close — the feedback wire IS sampling the speaker output, so they're effectively the same signal.

### General tidiness

Wires should be:

- **At rest** in their position. Not under tension, not pulling on solder joints.
- **Pressed against the chassis** where possible — the chassis is grounded and provides electrostatic shielding.
- **Out of the way of mounting bolts** that you might need to remove for maintenance.

## Mechanical inspection

Check the chassis for anything loose:

- **Transformer mounting bolts** — both the power transformer and the two A-470s. Loose mounting causes mechanical hum.
- **Filter cap mounting** — the can's chassis bond IS the negative connection. A loose mount = a loose ground = hum + danger.
- **Tube socket retention** — sockets should be firmly mounted, no wiggle.
- **Terminal strip mounting** — both the seven-lug strip and any other terminal strips.
- **Chassis grounding bolt** (3-prong cord) — must be tight. Use a star washer for bite.
- **Switch and fuse holder** — both should be firmly mounted with their nuts tight against the chassis from inside.

A loose bolt found now is a five-second fix. A loose bolt found while debugging a hum mystery six months from now is a multi-hour adventure.

## Tube socket inspection

For each tube socket (8 octal sockets for the EL34s and 5AR4, plus the smaller sockets for the 6GH8As):

- **No debris inside.** Look down into the socket with a flashlight. Any flake of solder, wire snippet, or piece of dust will arc when high voltage hits it.
- **All pins clean and shiny.** Tarnished pins make poor connections. A pencil eraser cleans them effectively.
- **Sockets sit square on the chassis.** A tilted socket means tubes will sit at an angle — stresses solder joints over time.
- **Solder joints on the socket pins look clean.** This is where chassis-side wires meet tube-side connections — usually multiple wires per pin.

## Tube installation strategy

**Don't install all the tubes for first power-on.** The recommended sequence:

1. **First power-on: NO TUBES.** Verifies the transformer and filter caps without risking anything sensitive. You should see no heater glow (no tubes!), no B+ load, just the transformer humming and the filter caps charging.

2. **Second power-on: RECTIFIER ONLY (5AR4).** Verifies the HV rectification works. B+ should come up to a higher-than-normal value (no load) — maybe 500-520 V at the first filter cap.

3. **Third power-on: ADD DRIVER TUBES (6GH8As).** Driver-stage voltages should reach their nominal values. B+ will sag slightly as the drivers draw current.

4. **Fourth power-on: ADD OUTPUT TUBES (EL34s) with bias maximum negative.** Set the bias pots to their most-negative setting (the output tubes barely conduct). Power up, gradually reduce bias toward target. See [bias adjustment](bias-adjustment.md).

This sequence catches problems where they happen: transformer issues stay transformer issues, not "transformer destroyed the driver tubes" issues.

## Smell test

After each power-on session, sniff the amp. Burnt smells are unambiguous:

- **Burnt resistor** — sharp acrid smell, like ozone but worse. Probably an overheating dropping resistor.
- **Burnt insulation** — sweet burnt-plastic smell. A wire is running too hot somewhere.
- **Burnt transformer** — terminal smell. Distinctive, you'll know. If you smell this, the transformer is probably already dead. Stop, don't reapply power.
- **Capacitor leakage** — pungent electrolyte smell, sometimes visible weeping. Cap is failing.

If you smell anything weird during bring-up, power off, walk away, and come back when the smell is gone. Diagnose before re-powering.

## Resistance check (manual page 11)

Before applying any power, the manual recommends a single resistance check:

- DMM on resistance / ohms range.
- One probe to **capacitor lug #2** (the first filter cap, where the rectifier output lands).
- Other probe to **chassis ground**.

**Expected: in excess of 100 kΩ.** Anything significantly lower indicates a short, a leaky cap, or a mis-wiring that needs fixing before powering up.

This check verifies that nothing on the B+ rail is shorted to ground — which would cause a catastrophic fuse-blow (or worse) on first power-on.

## Final pre-power check

The "is everything else right?" final pass:

- [ ] All [step 1-11 connections](../build/power-supply/index.md) are made.
- [ ] Resistance check above passed (>100 kΩ from cap lug 2 to ground).
- [ ] Power switch is OFF.
- [ ] Variac (if used) is at 0 V.
- [ ] No tubes installed (for first power-on).
- [ ] No speakers connected (for first power-on — protects the speakers if something is wrong).
- [ ] DMM ready, set to AC volts, 600 V range.
- [ ] You're rested. Don't do bring-up tired.
- [ ] [High-voltage safety procedures](../test-equipment/high-voltage-safety.md) have been re-read.

When all of these are checked, proceed to [continuity checks](continuity-checks.md).

## See also

- [Continuity checks](continuity-checks.md) — next page in the bring-up sequence
- [High-voltage safety](../test-equipment/high-voltage-safety.md) — required reading
- [Tools and workspace](../getting-started/tools-and-workspace.md) — gear you'll need
