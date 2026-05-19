---
title: Tools and workspace
---

# Tools and workspace

For test equipment (DMM, oscilloscope, variac, etc.) see [Test equipment](../test-equipment/index.md). This page is the *other* half: the hand tools, the soldering setup, and the workspace itself.

## Soldering iron

The single most important tool. A bad iron makes every joint a struggle; a good iron makes every joint easy.

**What you want:**

- **Temperature controlled.** Fixed-temperature 25 W "stick" irons aren't enough for the larger ground lugs and chassis bonds you'll encounter. Get something with a dial.
- **~40 W or higher.** ST-70 wiring includes some heavy gauge connections (octal sockets, the seven-lug terminal strip) that suck heat. A 40 W or 60 W iron at ~700 °F handles them comfortably.
- **Chisel or conical tip, 2–3 mm wide.** Big enough to transfer heat fast, small enough to fit between terminal lugs.
- **A stand with a brass-wool tip cleaner.** Sponges work but tend to thermally shock the tip; brass wool doesn't.

**Recommended price points:**

- Budget: **Hakko FX-888D** (~$110). The Toyota Camry of soldering stations. Buy this if you don't already own a temperature-controlled iron. It's available everywhere, parts are cheap, and tips last forever.
- Mid-range: **Weller WE1010NA** (~$140). Slightly nicer ergonomics, faster heat-up.
- Higher: **Hakko FX-951** (~$300) or **JBC CDB-1B** ($500+). Faster recovery, finer tip changes. Overkill for one tube amp, lovely if you'll be soldering forever.

A pencil-style iron from a hardware store will *technically* work, but you'll fight it.

## Solder

**Use 60/40 or 63/37 leaded rosin-core solder.** ~0.7 mm diameter (0.028" or so) is right for hand-soldering chassis wiring. Avoid:

- **Lead-free solder.** Required for new commercial products in many regions, but a real pain for hand soldering — needs higher temps, wets less easily, makes joints that look matte even when good. For a one-off personal build, leaded is much easier.
- **Acid-core solder.** Sold for plumbing. The acid flux destroys electronic connections. Read the label.
- **Solid (no-flux) wire.** Without flux you'll fight oxidation on every joint.

A 1 lb spool of Kester 44 (or equivalent rosin-core) lasts through several amps. ~$30.

## Hand tools

In rough order of importance:

- **Wire strippers.** Get a proper pair of stripping pliers — Klein 11055, Knipex 12 62 180, or similar. Adjustable strippers ("self-adjusting") are nice but the dedicated multi-gauge kind is faster.
- **Needle-nose pliers.** Small ones (4–6"). Used for forming wire bends and holding leads while soldering.
- **Diagonal cutters / flush cutters.** Small flush cutters (Hakko CHP-170 or Xuron equivalents) for trimming leads after soldering — they leave a clean flat cut.
- **Screwdrivers.** A small set with both Phillips and slotted, 3 mm to 6 mm tip sizes. The chassis hardware uses small Phillips heads; the seven-lug strip uses 6-32 screws.
- **Nut driver set.** A small nut driver in 1/4", 5/16", and 11/32" sizes covers most of what's on the chassis.
- **Tweezers.** Pointed, fine-tipped. For positioning components on the PC-3A driver board.
- **A third hand / helping hands tool.** Two alligator clips on a base, used to hold wires or boards while you solder them. PCB vises are nicer but pricier.

## Lighting and magnification

Tube amp wiring is on the larger side — much easier than surface-mount work — but good lighting still matters.

- **Bright overhead lighting**, plus a movable task light pointed at your work.
- **Magnifier visor (Optivisor or similar)**, 2× or 3×. Useful for inspecting solder joints and reading capacitor / resistor markings on dim or oxidized parts.
- A **USB microscope** (~$30) is a nice-to-have for inspecting questionable joints.

If you're 40+ and find yourself moving the work closer and farther to focus — get a visor. Saves your neck.

## Ventilation

Solder fumes are mostly **rosin smoke**, not lead vapor (lead doesn't vaporize at hand-soldering temperatures). But rosin smoke is genuinely irritating and contains compounds you should not inhale repeatedly.

- **Open a window.** Cross-ventilation if you can.
- A small **desk fan blowing AWAY from your face** moves the smoke past you instead of into you.
- A **fume extractor** with a charcoal filter is nice if you'll be soldering a lot. ~$80 for a usable one (Hakko FA-400), more for fancy.

Don't solder in a closed unventilated space. You'll feel it after an hour or two.

## Antistatic precautions

For the tube circuit itself: **mostly irrelevant.** Tube grids and plates don't care about a few thousand volts of static. The PC-3A driver board has only passive components (resistors, caps) and tube sockets — nothing static-sensitive.

If you're handling any modern silicon (e.g., a 1N4007, a solid-state rectifier replacement, anti-click cap), basic care is enough: touch the chassis before picking up parts to discharge yourself. You don't need a wrist strap or an ESD mat for this build.

## Workspace organization

A few things that make the multi-session build less painful:

- **A dedicated table or bench.** The kitchen table works but means clearing it every session.
- **Good lighting** at the work height (not just overhead — direct light onto the workpiece).
- **Parts trays.** Cheap plastic dividers from a hardware store. Sort components by section ("page 6 parts", "page 7 parts", etc.) so each session is set up before you start.
- **A clear binder or photocopy of the manual.** Mark off each step as you complete it. Don't trust memory.
- **A photo log.** Take a picture of the chassis at the end of every session. Future you will thank present you when troubleshooting hum 6 months later.
- **A small notebook.** Note any deviations from the manual ("used 470 Ω instead of 510 Ω because that's what I had"). These deviations always come back to matter.

## What you DON'T need

- A reflow oven (no surface-mount work here).
- A hot air rework station (same).
- A hot air gun (the original Dynaco shrink wraps are all heat-shrink-tubing-with-a-lighter-distance scale).
- Specialty audio test equipment beyond what's listed in [test equipment](../test-equipment/index.md). For an ST-70 build the DMM + a signal source + a dummy load is enough; an oscilloscope is a nice-to-have, not essential.

## Estimated total cost

If you have nothing: budget around **$200** for a complete from-scratch setup (Hakko FX-888D, hand tools, solder, magnifier, lighting). The amp itself is more expensive than the tools to build it.

If you already have a basic electronics workbench: probably $0 — everything on this page is general-purpose.

## See also

- [Test equipment](../test-equipment/index.md) — DMM, scope, variac, etc.
- [Safety basics](safety-basics.md) — before you plug anything in
- [Reading this manual](reading-this-manual.md) — conventions used throughout
