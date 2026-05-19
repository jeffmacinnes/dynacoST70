---
title: Choke
---

# Choke

The ST-70's **choke** is a 1.5 H iron-core inductor in the B+ supply, sitting between the first and second filter caps. It's the "L" in the classic LC pi-filter topology — its inductance resists changes in current, smoothing the supply far more effectively than capacitance alone.

The choke and the second filter cap together form a *second-order* low-pass filter that drops B+ ripple by tens of dB, turning the sawtooth output of the first cap into the essentially-flat DC the tube plates want.

<figure class="diagram-fig" markdown="span">
  <object type="image/svg+xml" data="../../assets/diagrams/choke-filter-response.svg" aria-label="LC filter frequency response showing how the choke kills 120 Hz ripple">
    Choke filter response (your browser does not support inline SVG).
  </object>
  <figcaption>Attenuation vs. frequency for the ST-70's L=1.5 H choke + C₂=20 µF second filter cap, with a ~100 mA load. The 120 Hz ripple at the choke input gets cut by ~24 dB (factor of 16) at the choke output. Click to zoom.</figcaption>
</figure>

## What it is, physically

A choke is electrically just a big inductor: a coil of copper wire wound around an iron core, with a gap in the core. Mechanically, it looks like a small power transformer — same kind of laminated iron core, same end bells, same general size — except it has only ONE winding, not two.

The ST-70's choke is about ~1.5 H and rated for ~125 mA (more than the ~100 mA the amp draws at full output). It's mounted on the chassis next to the power transformer.

## What an inductor does in a DC supply

An inductor resists *changes* in current. Specifically, the voltage across it is `V = L · dI/dt` — proportional to the *rate of change* of the current through it.

In a DC supply with ripple riding on the DC:

- The DC component flows freely through the inductor (steady current → no voltage drop except from the resistance of the wire).
- The AC ripple sees the inductor as a high impedance (`Z_L = jωL` — increases linearly with frequency).
- So the inductor passes DC but blocks AC.

That's exactly what we want for a B+ supply: pass the 450 V DC, block the 120 Hz ripple.

## Why a gapped core

The ST-70 choke is mounted just like a transformer, with a laminated iron core. But unlike a transformer, the core has a deliberate **air gap** (a thin non-magnetic spacer between the E and I laminations).

The reason: DC current flowing through a coil on solid iron tries to magnetise the iron. At enough DC current, the iron saturates — the inductance collapses, and the choke stops doing its job. A gapped core has lower inductance per turn but can handle much more DC before saturating.

Tradeoff: gapped core → lower inductance, can handle high DC current; solid core → high inductance, saturates easily. Power supply chokes always have gaps; audio-signal-carrying inductors usually don't.

## How the LC filter works mathematically

The choke + second filter cap form an LC low-pass filter. The corner frequency is:

`f_res = 1 / (2π · √(L · C))`

For the ST-70: `f_res = 1 / (2π · √(1.5 H · 20 µF)) ≈ 29 Hz`

Below 29 Hz: filter passes the signal (DC goes through).
Above 29 Hz: filter rolls off at 40 dB / decade (12 dB / octave).

The 120 Hz ripple is about 4× the corner frequency, deep in the rolloff region. Math gives ~24 dB attenuation — the diagram above shows the curve.

24 dB is a factor of about 16 in voltage. If the first filter cap leaves ~10 V of ripple on the B+, the choke + second cap reduce it to ~600 mV. Then any further filtering (a small decoupling cap on the driver stage, for instance) drops it further into the millivolts range.

## Why an L+C is so much better than just bigger C

You can imagine "what if I just used a 200 µF first cap instead of adding a choke?" The math:

- 200 µF + 100 mA load, 8.33 ms ripple period → droop = 100·8.33e-3/200e-6 = 4.2 V ripple at first cap. Lower than the 30 µF cap's ~28 V, but still meaningful.
- That single cap is acting as a *first-order* low-pass filter — only 20 dB/decade rolloff.
- The LC combo gives 40 dB/decade rolloff — twice the slope. So even with modest L and C values, it crushes ripple much harder than a giant single cap would.

This is why every serious tube amp has a choke in the B+ chain. Solid-state amps usually don't because they can use regulator ICs that achieve the same result with feedback rather than passive filtering.

## DC resistance and voltage drop

A real choke has resistance — typically 100-200 Ω for the ST-70's choke. That resistance drops some voltage:

`V_drop = I · R = 0.100 A · 150 Ω ≈ 15 V`

So if your first filter cap sits at, say, 475 V, the second cap (after the choke) sits at ~460 V. That's the actual ST-70 B+ rail spec.

This DC drop is one of the few downsides of using a choke — you lose a bit of supply voltage to inefficiency. Worth it for the smoothing.

## "Singing" — mechanical hum

Sometimes a choke makes audible noise — a soft 60 or 120 Hz buzz coming from the laminations vibrating against each other. Causes:

- Loose lamination clamping.
- Worn or aged varnish in the iron stack.
- Subharmonic resonance with the supply ripple.

It's annoying but rarely indicates a real problem. Tightening the choke's mounting bolts or wedging shims between the chassis and the choke usually quiets it.

## Failure modes

Chokes are extremely reliable — the simplest "active" component in the amp. They fail in two ways:

### Open winding (rare, terminal)

The single winding breaks somewhere (corrosion, mechanical stress, occasionally a manufacturing defect). Result: no B+ at the second cap, amp doesn't work. Easy to diagnose with a continuity check (DMM beep across the two choke leads).

### Shorted turns (rarer, sneaky)

Insulation between adjacent turns of the winding breaks down, effectively shorting some turns out. Result: lower inductance, ripple gets worse, B+ may sag. Hard to diagnose without an LCR meter.

In ~60+ years of ST-70 history, original chokes failing is uncommon. If you suspect choke problems in a vintage amp, it's usually something else.

## In this build

The choke sits on the chassis next to the power transformer, with two leads exiting the bottom.

- [Step 9](../build/power-supply/step-09-choke.md) — wires both choke leads to the filter cap can (one lead to lug +1, the other to lug +2).

## See also

- [Filter capacitors](filter-capacitors.md) — the caps that pair with the choke
- [Rectification — smoothing](../theory/rectification.md#smoothing-from-pulsating-dc-to-clean-dc) — the smoothing chain in context
- [How transformers work](../theory/how-transformers-work.md) — same iron-core physics, different application
- [Step 9](../build/power-supply/step-09-choke.md) — where the choke is wired up
