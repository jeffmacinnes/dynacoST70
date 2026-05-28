---
title: Signal paths
---

# Signal paths

The build manual orders steps by what's *physically reachable next* — the right sequence for soldering, but disconnected from how energy and signals actually flow through the finished amp. This section traces each path end-to-end through the ST-70's specific components and build steps.

These pages are reference material — especially useful during troubleshooting ("where does this voltage come from?", "follow the signal until it stops") and during the initial conceptual learning ("how does the whole thing fit together?").

## The five paths

- **[Audio signal](audio.md)** — from the RCA input jack to the speaker terminals, through the 6GH8A driver tube and the EL34 push-pull pair into the A-470 output transformer.
- **[B+ (high-voltage DC supply)](b-plus.md)** — from the PA-060 HV secondary, through the 5AR4 rectifier and the multi-stage filter network, out to every tube plate and screen in the amp.
- **[Heater (AC to filaments)](heater.md)** — the two separate heater windings on the PA-060: one private 5 V winding for the 5AR4 rectifier, one shared 6.3 V winding daisied through every other tube.
- **[Bias (negative DC supply)](bias.md)** — the small auxiliary supply that holds each EL34's grid at the right negative voltage to set its idle plate current.
- **[Negative feedback](negative-feedback.md)** — the loop that samples the OPT secondary and feeds a small fraction back to the input stage, trading raw gain for lower distortion and lower output impedance.

A sixth path — **ground topology** (star ground, current returns, why the HV CT and heater CT share a chassis tie) — is deliberately out of scope here; it touches every other path and is better explained in [grounding and hum](../theory/grounding-and-hum.md).

## How to read these pages

Every path page follows the same structure:

- **At a glance** — a block diagram of the whole path.
- **Stage by stage** — what happens at each node, with links to the build step where it gets wired and the component page that explains the part.
- **Per-channel notes** — where the left and right channels diverge (or, more often, don't).
- **Where it can break** — common failure modes, with the DMM probe points that diagnose them.
- **See also** — related theory, components, and modifications.

The pages don't re-derive theory; they assume you've read the relevant [theory](../theory/index.md) chapter. What they add is the *specific implementation* in this amp: lead colors, lug numbers, build step references, and concrete voltages.

## See also

- [Theory](../theory/index.md) — the abstract treatments these pages instantiate
- [Build](../build/index.md) — the procedural sequence these paths are constructed from
- [Components](../components/index.md) — the parts each path runs through
