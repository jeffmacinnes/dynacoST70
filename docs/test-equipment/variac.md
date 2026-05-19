---
title: Variac
---

# Variac

A variac is a variable autotransformer that lets you control the AC voltage applied to a device under test. Turn the dial from 0V up to 130V (or so), and the output follows.

## Why it's useful

**Slow bring-up.** When powering up a freshly-built or recently-modified amp for the first time, you don't slam it with full mains voltage. Instead, you ramp slowly from 0V upward, watching for:

- Smoke or unusual smells (immediate stop, find the problem)
- Excessive current draw (check the variac's ammeter or use an inline meter)
- Hum, oscillation, or other audio anomalies
- B+ rail reaching expected levels at expected variac positions

A typical ST-70 bring-up procedure: ramp to 25V, hold, check. 50V, hold, check. 75V, 100V, full voltage. Each step gives the filter caps time to charge and the tubes time to warm up gradually, while you verify each stage of the supply is behaving. See [first power-on](../bring-up/first-power-on.md) for the full procedure.

## The AC-DC PowerShack SC-5M

This build uses the AC-DC PowerShack SC-5M — a manual variac with a fused output. Adequate for ST-70 bring-up. Watch for:

- Output current rating (the SC-5M is 5A, plenty for the ST-70 which draws around 1A from the wall at full operation)
- Whether the variac itself is grounded properly to the wall outlet
- Whether the variac maintains regulation under load (cheap variacs sag noticeably as you draw current)

## Important: variacs do NOT provide isolation

A common misconception. A variac is an **autotransformer** — its primary and secondary share windings, so it does not electrically isolate the output from the mains. The chassis of the device under test is still earth-referenced through the variac.

This is fine for bring-up, but it means:

- You can't safely defeat the earth ground on the device under test by using a variac alone
- A variac alone doesn't protect you against dual-fault scenarios that an isolation transformer would

## A note on isolation transformers (and why we don't use one)

A 1:1 isolation transformer breaks the connection between the device's chassis/circuit ground and mains earth. Useful for specific scenarios — but **not required for the ST-70 build.**

The classic use case is servicing old transformerless ("hot chassis") tube radios and TVs, where the chassis itself can be at line voltage. With an isolation transformer in the path, you can probe such circuits without the scope's earth-grounded shell creating a short to mains.

The ST-70 has a proper [power transformer](../components/pa-060-power-transformer.md) that already isolates the audio circuit from the mains. Once the [3-prong cord modification](../modifications/3-prong-cord.md) is in place, the chassis is bonded to mains earth, and the audio circuit ground is referenced to that. There's no "hot chassis" issue. Scope probes can ground-reference to the same earth as the amp without conflict.

### Why an iso transformer isn't a substitute for safety practices

The real risks during ST-70 work aren't solved by an isolation transformer:

- **Touching the B+ rail (450V DC)** — iso transformer doesn't help, that voltage is still there
- **Touching charged filter caps after power-off** — iso transformer doesn't help, the caps don't care about isolation
- **Probe-rated voltage limits** — iso transformer doesn't change probe ratings

### A subtle argument against routine use

An isolation transformer means your device is no longer earth-referenced. If you accidentally touch a hot point and any earth-grounded surface (a heat register, a metal lamp, a grounded scope chassis), **you become the path between them.** With proper earth grounding, the breaker trips first. Some people argue isolation transformers create false confidence — you feel safer but in some scenarios you've actually removed a protection.

### Bottom line for the ST-70

Skip the isolation transformer for this build. Focus instead on:

- Variac for slow bring-up
- [One-hand rule](high-voltage-safety.md#one-hand-rule) for live measurements
- [Bleeder resistors or discharge tools](high-voltage-safety.md#discharging-filter-caps) for filter caps after power-off
- [Probes rated for the voltages involved](probes.md)

## See also

- [First power-on](../bring-up/first-power-on.md) — the slow ramp-up procedure
- [High-voltage safety](high-voltage-safety.md) — what the variac doesn't protect against
- [PA-060 power transformer](../components/pa-060-power-transformer.md) — the actual isolation barrier in the amp
