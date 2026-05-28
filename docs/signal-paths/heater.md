---
title: Heater path
---

# Heater path

The heater (filament) path supplies low-voltage AC to every tube's heater filament, which warms the cathode so it can emit electrons. Heaters don't carry the audio or B+ signal — they're a separate power network — but they're a major source of audible hum if they're not wired and grounded correctly. Twist, daisy, center-tap, ground. Get any of those wrong and the amp hums.

The PA-060 [power transformer](../components/pa-060-power-transformer.md) supplies **two completely separate heater networks**:

| Winding | Voltage | Current draw | Feeds |
|---|---|---|---|
| White pair | 5 V AC | 1.9 A | 5AR4 rectifier (V1 only) |
| Green pair + green/yellow CT | 6.3 V AC | ~3.5 A | Left channel: V2, V3 (EL34s) + left 6GH8A |
| Brown pair + brown/yellow CT | 6.3 V AC | ~3.5 A | Right channel: V7, V6 (EL34s) + right 6GH8A |

The 5 V is its own thing — only the 5AR4 uses 5 V heaters, and it has its own dedicated winding. The two 6.3 V windings each feed one *channel's worth* of tubes via a series chain (technically still a parallel circuit at the tube terminals, but the wires daisy-chain from socket to socket). Keeping the two channels on separate windings is a deliberate hum-rejection choice — heater current ripple on one channel doesn't couple into the other.

## At a glance

```
PA-060 secondaries
  │
  ├── WHITE pair (5 V, 1.9 A) ────────→ V1 pins 2 & 8           [5AR4 heater + cathode]
  │
  ├── GREEN pair (6.3 V) ──→ V2 pins 2 & 7   ─→ V3 pins 2 & 7  ─→ PC-3A left 6GH8A heater
  │         (one half is V2 pin 2, daisied to V3 pin 2,
  │          which then runs to the board)
  │  GRN/YEL CT → 7-lug strip → ground (via star-ground point)
  │
  └── BROWN pair (6.3 V) ─→ V7 pins 2 & 7    ─→ V6 pins 2 & 7  ─→ PC-3A right 6GH8A heater
              BRN/YEL CT → 7-lug strip → ground
```

The center taps don't carry signal current — they're a **DC reference clamp** that holds the heater AC symmetric about ground, which suppresses hum coupling.

## Stage by stage

### Stage 1 — White pair → V1 (5AR4 heater)

The 5AR4 uses a 5 V AC heater that draws 1.9 A. The WHITE pair of leads from the PA-060 goes to V1 **pins 2 and 8** in [step 2](../build/power-supply/step-02-5ar4-heater.md), with pin 8 deliberately *not soldered yet* because the cathode wire also lands on pin 8 in a later step ([step 29](../build/output-stage/step-29-rectifier-to-filter-cap.md)).

Note pin 8 is **both** the cathode and one end of the heater — this is normal for indirectly heated rectifiers. The cathode and one heater pin share an internal connection inside the tube, which is fine because the 5 V heater winding floats relative to ground (no CT).

The white pair is twisted close together to minimize radiated hum — see [heater circuits](../theory/heater-circuits.md#how-twisting-the-leads-helps).

### Stage 2 — Green pair → V2 → V3 → left 6GH8A (left channel heater chain)

The GREEN pair carries the 6.3 V AC for the left channel's three tubes. Wiring sequence:

1. [Step 4](../build/power-supply/step-04-v2-heater.md): green pair from PA-060 → **V2 pins 2 and 7** (left EL34 heater).
2. [Step 17](../build/output-stage/step-17-v2-v3-heater-daisy.md): a short jumper from V2 to V3 — **V2 pin 2 ↔ V3 pin 2**, and **V2 pin 7 ↔ V3 pin 7** — putting V3's heater in parallel with V2's.
3. [Step 46](../build/driver-stage/step-46-v3-heater-to-board.md): from V3 to the PC-3A board, feeding the left 6GH8A's heater pins.

Total left-channel heater load: 2 × EL34 (1.5 A each) + 1 × 6GH8A (0.45 A) ≈ **3.45 A** at 6.3 V.

The green pair is twisted from the PA-060 to V2; the V2↔V3 daisy is also twisted; and the V3-to-board wire is twisted. The twist is essential for hum control — see [why we twist heater leads](../theory/heater-circuits.md#how-twisting-the-leads-helps).

### Stage 3 — Brown pair → V7 → V6 → right 6GH8A (right channel heater chain)

Mirror of stage 2, on the other channel:

1. [Step 5](../build/power-supply/step-05-v7-heater.md): brown pair → V7 pins 2 and 7.
2. [Step 16](../build/output-stage/step-16-v6-v7-heater-daisy.md): V7 ↔ V6 daisy.
3. [Step 45](../build/driver-stage/step-45-v6-heater-to-board.md): V6 to PC-3A board, feeding the right 6GH8A.

Total right-channel heater load: same ~3.45 A.

### Stage 4 — Center taps to ground (both windings)

Each 6.3 V winding has its own center tap — the **green/yellow** lead for the left winding, the **brown/yellow** lead for the right. Both CTs land on the [seven-lug terminal strip](../components/seven-lug-terminal-strip.md) in [step 6](../build/power-supply/step-06-heater-cts.md), which is then grounded as part of the [star ground](../build/driver-stage/step-64-star-ground-completion.md).

Why ground the CT instead of one end? Because the heater AC is then **symmetric around ground** — at any instant, one end of the heater is at +4.5 V and the other end is at −4.5 V (relative to ground). Any heater-to-cathode capacitance couples equal amounts of positive-going and negative-going AC into the cathode, which cancels at the audio output rather than appearing as hum.

If you grounded one end of the heater instead, the heater would swing from 0 V to +9 V — all positive-going AC coupling into the cathode, audible as hum. The CT-ground arrangement is a free hum-reduction trick that costs only a wire.

### Stage 5 — RF bypass caps on the heater CTs (step 15)

[Step 15](../build/output-stage/step-15-disc-caps.md) adds two **disc ceramic capacitors** (typically 0.01 µF) across each heater CT to ground. These don't do anything at 60 Hz — they're a short circuit only to RF — but they suppress high-frequency noise that can capacitively couple into the heater wires from outside the chassis (computer monitors, switching power supplies, radio signals).

In modern environments with more RF pollution than 1959 had, these caps earn their place.

## Per-channel notes

| | Left channel | Right channel |
|---|---|---|
| 6.3 V winding | Green pair, green/yellow CT | Brown pair, brown/yellow CT |
| Tubes fed | V2, V3, left 6GH8A | V7, V6, right 6GH8A |
| Daisy step | [Step 17 (V2↔V3)](../build/output-stage/step-17-v2-v3-heater-daisy.md) | [Step 16 (V6↔V7)](../build/output-stage/step-16-v6-v7-heater-daisy.md) |
| Board feed | [Step 46 (V3 → board)](../build/driver-stage/step-46-v3-heater-to-board.md) | [Step 45 (V6 → board)](../build/driver-stage/step-45-v6-heater-to-board.md) |

The two windings are **electrically isolated** all the way up to the chassis ground (where their CTs meet). This means heater current draw on one channel doesn't ripple onto the other channel's heater rail — preventing channel-to-channel crosstalk via the heater path.

## Where it can break

| Symptom | Likely cause | DMM probe |
|---|---|---|
| One tube has no glow, others fine | Bad solder joint on that tube's heater pin | Probe AC voltage at the dark tube's pins 2 and 7 — should be 6.3 V (or 5 V for V1) |
| All tubes on one channel are dark | Open in that channel's heater daisy chain | Trace continuity from PA-060 secondary through V2/V3 (or V7/V6) — look for the break |
| All tubes dark | PA-060 primary fuse blown, or amp not plugged in | Check fuse first |
| Audible 60 Hz hum, channel-specific | Heater CT not grounded, or one heater wire shorted to cathode (heater-cathode leakage in tube) | Probe each CT to ground — should be < 1 Ω. Swap tubes between channels; if hum follows the tube, replace it |
| Audible 120 Hz hum | Not a heater issue — that's B+ ripple. See [B+ path](b-plus.md) |
| RF noise (buzz when nearby device runs) | Disc bypass caps on heater CTs missing or open | Visual inspection at 7-lug strip |
| One channel dim, other normal | Heater voltage low on the dim channel (resistive joint, low PA-060 winding) | Measure AC at any heater pin on the dim channel — should be ~6.3 V; if 5–5.5 V, suspect a resistive joint |

## Why heater hum matters more than you'd think

The heater is the **lowest-voltage** network in the amp (5 V or 6.3 V vs. 450 V B+), but it has by far the **largest current** (~10 A total). Big current + AC = big radiated magnetic field. That field induces voltage into anything close to it — including signal wires running nearby.

The mitigations stack up:

1. **Twist** the heater pair — opposing magnetic fields cancel at any distance.
2. **Route** heater wires close to the chassis (which acts as a shield) and perpendicular to signal wires (so any field that does radiate doesn't pick up by coupling).
3. **CT-ground** to keep the heater symmetric around ground.
4. **RF-bypass** to short high-frequency components to ground.

The original ST-70 manual was specific about all of these for a reason — get any one wrong and you have an amp with audible heater hum. See [heater circuits](../theory/heater-circuits.md) for the theory and [grounding and hum](../theory/grounding-and-hum.md) for how heater grounding interacts with the rest of the amp's grounding.

## See also

- [Heater circuits](../theory/heater-circuits.md) — the underlying theory
- [PA-060 power transformer](../components/pa-060-power-transformer.md) — the two heater windings
- [Seven-lug terminal strip](../components/seven-lug-terminal-strip.md) — where both CTs land
- [Grounding and hum](../theory/grounding-and-hum.md) — how the CT-ground fits into the star scheme
- [Audio signal path](audio.md) — what the heater enables but doesn't carry
