---
title: 'Step 50: Right channel grid leak resistor'
---

# Step 50: 470 kΩ resistor at right RCA jack

> *Connect one end of a 470,000 resistor to long lug of right input socket. Connect the other end to the ground (short) lug of the right input socket (S).* — manual page 9

## What you're doing physically

A **470 kΩ resistor** (DynakitParts #111474) lands between the long lug (signal hot) and the short lug (signal ground) of the right RCA jack. The ground end is soldered (S); the hot end is NOT soldered yet — more wires land there in [step 52](step-52-eyelet-17-to-right-rca.md).

## What this resistor does — the grid leak

This is the **grid leak resistor** for the right channel's input. It connects the input signal hot to signal ground through 470 kΩ.

Why does the grid need a leak resistor?

The 6GH8A pentode's control grid receives audio through a coupling cap from the previous stage (in this case, from the RCA input). Coupling caps **block DC**: any DC voltage that builds up on the grid side of the cap (due to grid current, contamination, etc.) gets trapped.

If the grid voltage drifts up (toward positive), the tube draws more plate current, which heats the cathode, which causes more grid current, which drifts the grid voltage further positive. **Runaway → tube destruction.**

The 470 kΩ resistor provides a **DC path to ground** for any drifted grid voltage to leak away. It's high enough resistance (470 kΩ) that the audio signal isn't loaded down — but low enough that DC drift can't accumulate.

## Why 470 kΩ specifically

Tradeoff. Higher value = less signal loading (good for high-impedance sources). Lower value = better DC clamping (good for stability).

470 kΩ is the standard "grid leak" value across most tube amps — high enough that even high-Z sources like a tube preamp aren't loaded; low enough that grid drift is well-controlled.

## See also

- [Step 51 — Left grid leak](step-51-left-grid-leak.md) — channel B's equivalent
- [PC-3A driver board](../../components/pc-3a-driver-board.md) — what's downstream of this
- [6GH8A driver tube](../../components/6gh8a-driver-tube.md) — the grid this resistor protects
