---
title: References and further reading
---

# References and further reading

The ST-70 is one of the most-documented amps in audio history — 60+ years of manuals, schematics, modifications, forum threads, and books. This page collects the references that actually pay off when you're stuck or curious, organised by what they're good for.

## Primary sources — Dynaco-original

### The Stereo 70 assembly manual (1959 / 1966 revisions)

The original kit manual is the canonical document — step-by-step assembly instructions, wiring diagrams, parts lists, the official schematic. Several revisions exist; the 1966 revision is the most commonly cited.

Multiple scanned PDFs circulate online. Search for "Dynaco Stereo 70 manual" or "Stereo 70 assembly instructions" — the National Valve Museum and Hifi Engine both host clean scans.

What it's good for: original parts values, original wiring sequence, original voltage targets. Use as the baseline reference for "what did Dynaco actually specify?"

What it's NOT good for: modern safety practices (no 3-prong cord, no fused mains), modern components (the recommended PIO caps are long discontinued), or modern troubleshooting (the manual assumes everything is new).

### The original Dynaco schematic

The single-page schematic is the second-most-referenced ST-70 document. Several versions exist:

- **Schematic A** (original 1959) — 7199 driver tubes, paper-in-oil coupling caps.
- **Schematic B** (mid-1960s) — 6GH8A driver tubes (the build documented here).
- **Schematic C** (later) — minor part value changes.

Make sure you reference the schematic that matches your driver board. The build documented here uses the **Version B** schematic — see [PC-3A driver board](../components/pc-3a-driver-board.md).

### Service / repair bulletins

Dynaco published several bulletins over the years addressing common failures. The most useful:

- **Bulletin 1** — early production B+ filter cap issue.
- **Bulletin 4** — bias supply circuit changes.

Less commonly referenced today but occasionally cited in forum troubleshooting threads.

## Current commercial sources

### DynakitParts (dynakitparts.com)

Dynakit, Inc. of Paramus, NJ — not affiliated with Bob Latino. Sells:

- Complete ST-70 kits (faithful reproductions, including the kit this build uses).
- Replacement parts for original ST-70s (transformers, sockets, caps).

DynakitParts' assembly manuals are some of the better current-era references for the platform.

### Tubes4HiFi (tubes4hifi.com) — Roy Mottram and Bob Latino

The separate parts and kit business through which Bob Latino's VTA boards and kits are sold. Source for:

- Upgraded driver boards (the VTA-ST70 variants — Bob Latino's design).
- Bias circuit upgrades.
- Quality coupling capacitors.
- Tubes (matched-quad EL34s, etc.).

Latino's documentation and forum posts, and Mottram's site, are valuable for "what's the best replacement?" questions.

### Triode Electronics (triodeel.com)

Long-running supplier of tube amp parts. Carries period-correct and modern replacement parts for the ST-70 platform.

## Community forums

### Audiokarma — Dynaco ST-70 mega-thread

The single biggest community knowledge base on this amp. Multi-thousand-post thread covering every modification, failure mode, tube preference, and "is this normal?" question that's ever come up.

Search audiokarma.org for "ST-70" or "Stereo 70." The active threads are easy to find; archived ones are deeper.

What it's good for: troubleshooting (someone has hit your exact problem and posted the fix), mod opinions (lots of strong views, but also lots of real-world data), parts sourcing tips.

What it's NOT good for: precise theory (forum posts are mostly empirical; the engineering reasoning is often hand-waved or wrong).

### diyAudio — Tubes forum

Higher signal-to-noise than Audiokarma for theoretical/engineering questions. The Tubes / Valves forum has long-running threads on EL34 amps generally, with ST-70-specific discussion mixed in.

Use diyAudio when you want to understand *why* a mod works, not just whether it works.

### Vintage Asylum / Tube Asylum

Older but still occasionally active. Cohort skews toward "leave it stock and replace parts in-kind" rather than the modify-heavily ethos of the other forums. Useful counterweight.

## Books

### Aspen Pittman, *The Tube Amp Book* (latest edition: 2003)

Encyclopaedic reference on tube amplifiers — primarily guitar-amp focused but broadly applicable. Schematics for hundreds of amps including the ST-70. Heavy on practical info (tube data, layout drawings, troubleshooting), light on theory.

Good first book for tube amps. Cheap used.

### Morgan Jones, *Valve Amplifiers* (4th edition: 2012)

The engineering reference. Covers tube physics, circuit topology, power supplies, transformers, and feedback in serious depth. Mathematically rigorous; assumes some EE background.

The chapter on power supplies (especially LC pi-filters and ripple analysis) is the best single explanation of the topology used in the ST-70. The chapter on output stages similarly covers push-pull topology rigorously.

Not a casual read. But if you want to *understand* rather than just *build*, this is the book.

### Merlin Blencowe, *Designing Tube Preamps for Guitar and Bass*

Strong on small-signal tube circuit design. Useful background for the input stage and phase splitter of the ST-70 even though the book targets guitar applications.

### Norman H. Crowhurst, classic articles (1950s)

Crowhurst was the engineering writer for *Audio Engineering* and *Audio* magazine in the era when amps like the ST-70 were designed. His articles on phase splitters, push-pull stages, and feedback are still the clearest explanations available. Many are scanned and freely available online — search for "Crowhurst" + topic.

### Radiotron Designer's Handbook (4th edition, 1953)

The definitive vacuum-tube engineering reference of the tube era. 1500 pages, free as a PDF (Radio Museum hosts a copy). Crushingly comprehensive — search for what you need; don't try to read cover to cover.

## Datasheets

Original-era datasheets are the most reliable specs. Modern reproductions often differ in subtle ways from originals — always cross-check.

### EL34 / 6CA7

- **Mullard** (UK, original) — the canonical datasheet. Search "Mullard EL34 datasheet PDF."
- **GE / Sylvania** (US, 6CA7) — the 6CA7 is the American equivalent. Datasheet is mostly identical.
- **Frank Philipse's tube database** (frank.pocnet.net) — hosts scanned datasheets for nearly every tube ever made, free.

### 5AR4 / GZ34

- **Mullard** (UK, original) — again the canonical reference.
- **Frank Philipse** for backup.

### 6GH8A

- **RCA datasheet** — the standard reference.
- **GE datasheet** — slightly different spec on some curves; both are valid.

The 6GH8A is no longer manufactured; modern stock is NOS (new-old-stock) from the 1960s-70s.

## Specific online references

A few specific URLs/resources worth bookmarking:

- **Frank Philipse's tube database** — http://frank.pocnet.net/sheets/ — datasheets for everything.
- **Hifi Engine** — hifiengine.com — scanned manuals for vintage HiFi gear, ST-70 manual included.
- **National Valve Museum** — r-type.org — UK-centric but excellent for European tubes (EL34, GZ34).
- **Wallace Audio** — wallaceaudio.com — restorations and parts; site has good photos of original Dynaco wiring as built.

## ST-70 modifications — canonical writeups

The major modifications have been documented multiple times by multiple people. The most influential writeups:

- **Triode-mode operation** — connecting EL34 screens to plates for "triode-strapped" sound. Multiple Audiokarma threads document the procedure and the audio result.
- **Cathode bias mod** — replacing fixed bias with self-bias via a cathode resistor. Simpler, more forgiving, but loses ~30 % output power.
- **Driver board upgrades** — VTA, Curcio, Welborne, Dynaclone — each has its proponents. Tubes4HiFi documents the VTA path in detail.
- **C-core or amorphous output transformer upgrades** — replacing the A-470 with a modern transformer. Audiokarma threads document the various options (Edcor, Hammond, Lundahl).

This documentation site focuses on the relatively-conservative restoration path: stock topology, modern safety upgrades (3-prong cord, fuse), modern components (film caps, metal-film resistors), and the individual-bias-pots mod. The references above cover the more ambitious mods if you want to go further.

## Test equipment guides

- **Eric Wrobbel's "Vintage Tube Test Equipment"** — http://www.ericwrobbel.com/ — reference for the kind of test equipment that was contemporary with the ST-70's design (Heathkit oscilloscopes, Hickok tube testers, etc.). Useful if you're building a period-correct workbench.
- **The Bob Pease columns** in *Electronic Design* magazine — Pease's articles on analog troubleshooting are still relevant. Many are freely available.

## What's deliberately NOT in this list

A few resources are commonly cited online but are not particularly reliable:

- **YouTube "I rebuilt my ST-70" videos** — vary wildly in quality. Some are excellent; others give actively dangerous advice. Cross-check against the books and forums.
- **Reddit r/diytubes** — newer than Audiokarma, smaller community, sometimes good but inconsistent.
- **AI-generated content** — increasingly common in search results; can confidently state things that are flatly wrong. Treat with skepticism.

When in doubt, go back to the original Dynaco documentation, the schematic, and either Morgan Jones or Crowhurst for the engineering reasoning.

## See also

- [Component theory](component-theory.md) — for the theory background that the books above cover in depth.
- [Tube pinouts](tube-pinouts.md) — quick reference for the tubes in this build.
- [Transformer specs](transformer-specs.md) — quick reference for the PA-060 and A-470.
