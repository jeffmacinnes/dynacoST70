---
title: Overview
---

# Overview — what we're building

## The ST-70 in one paragraph

The Dynaco Stereo 70 — universally just called the ST-70 — is a 35-watt-per-channel push-pull EL34 stereo tube amplifier, designed by David Hafler and Ed Laurent and released in 1959 as a kit. Over 300,000 originals were sold in the next two decades, making it the best-selling tube amplifier of all time. Sixty-five years later it's still in production (as kits and finished amps from several vendors), still the reference design that competitors get compared to, and still the amp most likely to be on a hi-fi enthusiast's repair bench.

This is a build of a current-production **DynakitParts ST-70**, which is a faithful reproduction of the 1959 design with optional updates. We're using their 6GH8A driver board version — the same driver topology Dynaco used in the originals — plus four common modifications.

## What makes the ST-70 special

Three things, mostly:

1. **The output transformers.** The A-470 transformers were extraordinary in 1959 and are still excellent today — −1 dB from 6 Hz to 30 kHz at full power. Most modern tube amps don't match this. They're the single biggest reason an ST-70 sounds the way it does. See [A-470](../components/a-470-output-transformer.md).

2. **The ultralinear topology.** Hafler and Keroes had patented "ultralinear" operation a few years earlier — feeding the EL34 screen grids from a fractional tap on the output transformer primary, giving a hybrid of pentode (more power) and triode (lower distortion). The ST-70 was its commercial debut. See the [A-470 page](../components/a-470-output-transformer.md) for the UL screen tap detail.

3. **The kit price point.** It was *affordable*. Hafler optimized aggressively: a minimum-parts driver stage (the [PC-3A board](../components/pc-3a-driver-board.md)), a cheap 5AR4 rectifier instead of solid-state, a simple bias supply. Many of these decisions look "cheap" by modern standards but they're what made the amp ship in volume. The transformers — the parts that actually matter sonically — were premium.

That combination — premium transformers, clever circuit topology, aggressive cost optimization — is why the ST-70 sounds so much better than its price suggests, even today.

## Why build one in 2026

A few reasons:

- **The platform supports endless tweaking.** The original driver board, the VTA driver board (Tubes4HiFi), a CFB driver board (Curcio), triode-strapped operation, ultralinear at different ratios, different output tubes (EL34, KT77, KT88, 6L6GC) — the ST-70 chassis hosts all of them. You're not just buying an amp; you're buying a platform.
- **It teaches you tube electronics.** Building one teaches you how transformers work, how rectifiers work, how the heater hum trick works, how grounding works, how to bias output tubes. None of this knowledge expires.
- **It's repairable forever.** Every part is replaceable from parts you can buy today. Compare to a modern Class-D amp where one failed surface-mount IC means a service-only repair.
- **The build itself is a project.** This is a multi-month endeavor, much of it slow methodical work that's the opposite of staring at a screen. There's something to be said for that.

## The kit landscape

Several current sources:

- **DynakitParts** (this build) — Pacific Transformer reproductions of the original PA-060 / A-470, current-production kits in original configurations. Sold via dynakitparts.com.
- **Bob Latino / Tubes4HiFi** — long-running ST-70 specialist. Sells the VTA driver board upgrade, complete kits, and chassis-up rebuilds. Often considered the "expert's" route.
- **Original Dynaco amps off eBay / used market** — abundant, but every original needs new filter caps, often new bias resistors, sometimes new output transformers. A "rebuild" rather than a "build."
- **Curcio Audio** — known for high-end driver board mods and complete redesigns. More expensive, more involved.

The DynakitParts kit is a good "stock vintage" experience without the gamble of buying a 65-year-old amp sight unseen.

## What this manual covers

- **Theory** — what transformers do, what rectifiers do, what bias is, what push-pull is. The "why" behind every step.
- **Step-by-step wiring** — every step from the original Dynaco manual, paired with a level-2 explainer of what that step accomplishes electrically.
- **Components** — every significant part has its own page explaining what it is, how it works, where it lives in this build, and what goes wrong with it.
- **Modifications** — the four common updates installed in this build (3-prong cord, 1N4007 selenium replacement, anti-click cap, individual bias pots).
- **Bring-up** — the procedure for powering the amp up safely for the first time and setting bias.
- **Test equipment** — what's needed at each stage of the build.

## What this manual doesn't cover

- **Other driver-board variants.** The 7199 / 7591 / VTA boards are all interesting but not covered here. The 6GH8A is what this kit ships with.
- **Other output tubes.** EL34s only. KT77 / KT88 / 6L6GC are direct or near-direct swaps but require different bias and won't be discussed.
- **Speaker matching theory.** The ST-70 has 4 / 8 / 16 Ω taps; pair them with whatever speakers you have.
- **Listening tests / "tube rolling."** Subjective; not in scope.
- **Cosmetic restoration.** This is a new-build, not a refinish job. If you have an original cabinet to refurbish, that's a separate project.

## How long will this take

Honest estimate for someone who's never built a tube amp:

- **Page 6 wiring** (the power supply, where we are): **8-15 hours**, spread across several sessions.
- **Driver board assembly**: 2-3 hours.
- **Output stage wiring + final assembly**: 8-12 hours.
- **Bring-up + bias adjustment**: 2-4 hours (deliberately slow).

Total: **20-35 hours** of focused work. Don't try to do it in two weekends — pace yourself.

## See also

- [Reading this manual](reading-this-manual.md) — conventions and how to navigate
- [Tools and workspace](tools-and-workspace.md) — what you need before you start
- [Safety basics](safety-basics.md) — required reading before bring-up
- [Build progress](../build/index.md) — current status of this specific build
