---
title: 'Step 41: Eyelet #19 to filter cap lug 3'
---

# Step 41: 3" wire from eyelet #19 (S) to filter cap lug 3

> *Connect a 3" wire from eyelet #19 (S) to filter capacitor lug #3.* — manual page 8

## What you're doing physically

A 3" wire from PC-3 eyelet #19 to filter cap lug 3. The eyelet end is soldered (S); the cap end is NOT soldered yet — more components land at lug 3 in step 42.

## What this wire carries

Lug 3 of the filter cap = "lug A" in the voltage table = **305 V DC** at idle. This is the lowest-voltage section of the B+ chain — the most-dropped, most-filtered point.

This wire delivers that 305 V to PC-3 eyelet #19, which feeds the **6GH8A pentode plate load** (the resistor between the pentode plate and B+ that drops a few hundred volts as the pentode draws plate current). 305 V is the right starting voltage to give the pentode a ~150-200 V plate operating point after the plate load drop.

The PC-3 board does additional per-stage decoupling internally (a small resistor + cap network usually) before this voltage reaches the actual plate load.

## See also

- [Step 42 — 22 kΩ dropping resistor](step-42-22k-dropping-resistor.md) — completes the lug-3-to-lug-4 dropping network
- [Step 43 — Eyelet #20 to lug 4](step-43-eyelet-20-to-cap-4.md) — the higher-voltage feed
- [Filter capacitors](../../components/filter-capacitors.md)
