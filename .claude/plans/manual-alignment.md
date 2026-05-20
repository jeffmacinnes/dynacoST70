# Manual alignment report

Reading: **DynakitParts ST-70 Type (B) kit, 2017 copyright**, serial 04267042.
26 pages: cover + intro/spec (1–3), mechanical assembly (4–5), wiring (6–10), initial adjustment + operation + troubleshooting (11–16), parts list (17), warranty (18), voltage test points + schematic A (19–20), schematic B (21), color pictorial (22), PA-060 spec (23), A-470 spec (24), C-354 spec (25), blank (26).

---

## Category A — Discrepancies (current docs say something the manual contradicts)

These need decisions before any rewrites. Each is a flag, not a fait accompli.

### A1. V-numbering is wrong for the 6GH8A drivers

**Current docs:** `build/driver-stage/index.md` says "V4 and V5" are the 6GH8A driver tubes. `build/index.md` parts list calls 6GH8A "Driver tubes".

**Manual:**
- V1 = GZ-34 rectifier (chassis octal socket)
- V2, V3, V6, V7 = EL-34 output tubes (chassis octal sockets)
- V4, V5 = **preamp power take-off sockets** (chassis octals, but they hold no tubes — they're AC/B+ outlets for an external preamp that needs power)
- 6GH8A drivers = **on the PC-3 board itself**, in board-mounted miniature sockets. No chassis V-number.

**Why it matters:** the manual's bias procedure (page 11) measures at "pin #8 of the preamp power take-off sockets" = pin #8 of V4 (left channel) and V5 (right channel). If we have the user looking for 6GH8As in V4/V5, the whole bias procedure breaks.

**Fix:** Rename "V4/V5 = 6GH8A" to "V4/V5 = preamp power take-off sockets". Clarify the 6GH8As live on the PC-3 board without chassis V-numbers. Update `components/6gh8a-driver-tube.md`, `build/driver-stage/index.md`, and `build/index.md` recap.

### A2. Bias methodology — stock vs. modified is inverted

**Current docs:** `bring-up/bias-adjustment.md` documents the per-tube 1Ω cathode sense + per-tube trimpot procedure as the primary. The "stock method" is mentioned only as a fallback.

**Manual (page 11-12):** The stock method uses:
- Two **15.6Ω 1%** precision cathode sense resistors, one per EL-34 *pair* (V2+V3 share one; V6+V7 share one).
- Pin #8 of each preamp power take-off socket (V4 for left, V5 for right) is wired to its channel's 15.6Ω resistor for easy probe access.
- **Target: 1.56VDC** across the 15.6Ω = 100mA per pair = 50mA per tube.
- **One 10K bias pot per channel** (two pots total), shared between the two tubes in that channel.
- "Dyna Biaset" is the kit's marketing name for this arrangement.

The per-tube 1Ω + per-tube trimpot is the [individual-bias-pots](../docs/modifications/individual-bias-pots.md) mod — not stock.

**Fix:** Restructure `bring-up/bias-adjustment.md` so the stock 15.6Ω / 1.56V / per-channel procedure is the primary. The per-tube procedure becomes a "if you've installed the individual-bias-pots mod, do this instead" section. The expected reading changes from "50mV across 1Ω" to "1.56V across 15.6Ω" for the stock path.

### A3. "1N4007 replacement" is documented as a mod, but the current kit ships with it

**Current docs:** `modifications/1n4007-replacement.md` describes replacing a selenium rectifier with a silicon diode as a safety mod.

**Manual:** Step 6 of mechanical assembly says "Connect the diode between each lug with banded end to the left" — a silicon diode is part of the standard kit. The parts list (page 17) shows "1 — Diode 544042" as a stock part.

**Fix:** The "1N4007 replacement" page should be reframed as historical context (what the original 1959 kit had, what the modern kit ships with, why the change happened) rather than as a mod the builder performs. The `build/index.md` modifications list should drop it from the "mods in this build" list since it's stock now.

### A4. PA-060 secondary specifications need verification against the spec sheet

**Manual page 23 spec sheet:**
- Primary: 120VAC 50-60Hz, BLK-BLK
- HV secondary: RED-RED with RED/YEL center tap, **720VAC CT @ 300mA** (i.e., 360-0-360)
- Bias winding: RED/BLK lead, **55VAC**
- Heater #1: GRN-GRN with GRN/YEL CT, **6.3VAC @ 5A**
- Heater #2: BRN-BRN with BRN/YEL CT, **6.3VAC @ 5A**
- Rectifier filament: WHT-WHT, **5VAC @ 4A**
- All leads 12"

**Action:** verify `components/pa-060-power-transformer.md` matches. If we said "300VAC bias" or "5VAC @ 2A rect filament" or anything else, fix. (I have not yet checked the page; need to before rewriting.)

### A5. A-470 specifications

**Manual page 24 spec sheet:**
- Primary leads (5): BLU/WHT, GRN/WHT, RED (CT), GRN, BLU
- Secondary: BLK common, BRN 4Ω, ORG 8Ω, YEL 16Ω
- **35 watts, 4300Ω CT plate-to-plate**
- All leads 12"

**Action:** verify `components/a-470-output-transformer.md` shows 4300Ω plate-to-plate and 35W rating, lead colors match.

### A6. C-354 choke specifications

**Manual page 25 spec sheet:**
- **1.75 H, 200mA DC, 62Ω DCR, 400VDC max, 10% tolerance**
- All leads 6"

**Action:** verify `components/choke.md`. We had "1.75H" already documented; check that 62Ω DCR and 200mA current rating match.

---

## Category B — Gaps (manual content not yet in the docs)

These are sections the manual covers that we haven't written. Listed here for scope, not as discrepancies.

### B1. Mechanical assembly (manual page 4-5, steps 1-15)

Mounting all hardware to the chassis: sockets, transformers, terminal strips, pots, fuse post, switch, choke, filter cap, ground lug(s). 15 steps, all before any wiring.

**Suggested home:** new section `build/mechanical-assembly/` with one page per step or a small set of grouped pages (e.g., "sockets and connectors", "transformers and choke", "filter cap and ground").

**Marginalia:** step 15 has handwritten "Only 1 lug" — the user's kit shipped with one solder lug instead of two at the main ground point. Worth a note in the relevant page.

### B2. Wiring steps 12-37 — power supply + bias network completion (manual page 7-8)

After step 11 (right OPT secondaries), the manual continues with:
- Steps 12, 14: left OPT secondaries (mirror of step 11)
- Steps 13: blue/green and blue-white/green-white from right OPT primary to V3 and V2
- Step 14: same for left OPT primary to V6 and V7
- Step 15: two .02μF disc caps on 7-lug strip lugs 5, 6, 7 (these are heater hum-bypass caps)
- Steps 16-17: heater daisy-chain between V2/V3 and V6/V7
- Step 18: 5" wire from 7-lug strip lug 1 to lug 6
- Steps 19, 21: two 100μF bias caps to 7-lug strip lugs 1, 3, 4
- Steps 20, 22: two 10K resistors on 7-lug strip
- Step 23: 7-lug strip lug 6 to ground lug near filter cap
- Step 24: 7-lug strip lug 3 to lug 1 of left bias pot
- Step 25: 7-lug strip lug 4 to non-banded side of bias diode (the bias HV supply tap)
- Step 26: 7-lug strip lug 2 to lug 3 of left bias control
- Step 27: 3" wire between lug 3 of each bias pot
- Step 28: 3" wire between lug 1 of each bias pot
- Step 29: V1 pin 8 (GZ-34 cathode) to filter cap lug 2 — B+ output from rectifier to first filter
- Step 30: 6800Ω resistor between filter cap lugs 1 and 4 (this is a B+ bleeder/dropping resistor)
- Steps 31, 34: 15.6Ω resistors at V2 and V7 sockets (cathode sense — the stock bias-measurement resistors)
- Steps 32, 35: 5" wires daisy-chaining V2-V3 and V7-V6 pin 1/pin 8 (cathodes paralleled across the pair)
- Steps 33, 36: 4½" wires from V3 pin 1 and V6 pin 8 to V4 and V5 preamp power-take-off pin 8 (this is how bias gets to the meter probe point)
- Step 37: four 1000Ω grid stoppers from EL-34 pin 5 to pin 6 (one per output tube)

**Suggested home:** `build/output-stage/` step pages, since most of these touch the EL-34 sockets and their cathode/grid networks. The bias network on the 7-lug strip is half "power supply" half "output stage" — judgment call where to put it.

### B3. PC-3 driver board mounting and wiring (manual page 8-10, steps 38-65)

The bulk of the remaining build. Step 38 mounts the board; steps 39-58 wire it to the rest of the chassis (B+ feeds, eyelet-to-tube-pin connections, input wiring, RCA jacks, input switch); steps 59-65 install the power cord.

**Suggested home:** `build/driver-stage/` step pages. Manual organises this around eyelet numbers and pin numbers; we should preserve that.

### B4. Initial Adjustment procedure (manual page 11-12)

Pre-power resistance check (capacitor lug 2 to ground > 100KΩ), warm-up sequence, GZ-34 *not* installed for first power-on, then GZ-34 installed and bias dialled in.

Most of this is covered in `bring-up/voltage-checks.md` and `bring-up/bias-adjustment.md` but the *manual's specific procedure* (e.g., "while tubes are warming up, set bias pots to center; this is approximately correct and serves as emergency operating adjustment if no meter available") is worth lifting in.

### B5. Voltage test points table (manual page 19)

This is the table I described in the report intro. It belongs in `bring-up/voltage-checks.md` verbatim as a reference. Currently that page describes the *what* and *why* of voltage checks but doesn't have the canonical expected-value table.

### B6. Parts list with part numbers (manual page 17)

Stock part numbers (e.g., PA-060 = part #464006, A-470 = #454326, C-354 = #423354, PC-3 = #557003). Useful for ordering replacements. **Suggested home:** new appendix `appendices/parts-list.md`, or fold into each component page's "ordering" section.

### B7. Operating-mode wiring (manual page 13)

Stereo / mono / bi-amped operation modes. Most users will use stereo and never touch this, but the manual documents the mono-paralleled and bi-amped wiring options. **Suggested home:** could be a section in `bring-up/functional-testing.md` or a separate `operating-modes.md` page.

### B8. Troubleshooting "In Case of Trouble" (manual page 14-16)

Manual's troubleshooting tree: tubes not lighting, fuse blowing, tubes glowing red, no signal, hum and noise, sizzling, pops. Many of these themes already appear scattered in our `bring-up/` and `theory/grounding-and-hum.md` pages, but the manual's structured decision tree doesn't exist anywhere in our docs.

**Suggested home:** `bring-up/troubleshooting.md` as a new page, or expand the existing `bring-up/functional-testing.md` with a troubleshooting section at the end.

---

## Category C — Useful manual content worth adding (no current equivalent)

### C1. Color wiring pictorial (manual page 22)

The famous full-color routing diagram. We don't have an equivalent. **Suggestion:** either reference the manual page directly (cite "see page 22 of the kit manual") OR — bigger ask — recreate the relevant portions as SVG diagrams alongside the build steps. Recreation is a large undertaking; citing the manual is cheap.

### C2. PC-3 schematic (manual page 21, Version B)

Same situation. Useful reference; we don't have an equivalent SVG; cite the manual is the cheap path; recreate would be a project.

### C3. Component value tables for the PC-3

The schematic shows specific values that aren't currently in `components/pc-3a-driver-board.md`:
- 470KΩ input grid leak
- 330K, 1.5M, 270K resistors in 6GH8A input
- *47K matched 1% (×2) — phase splitter plate loads
- 18K (×2)
- 620Ω cathode resistor
- 82pF (mmf) feedforward cap
- 47Ω
- .05μF input coupling
- .1μF inter-stage coupling (×2)
- *270K matched 1% (×2) — phase splitter cathode/plate balance
- 1K grid stoppers to each EL-34 (×4)
- 15.6Ω cathode sense (per channel pair, ×2)
- 390pF feedback compensation cap
- 1K NFB resistor

**Suggested home:** add a "component values" table to `components/pc-3a-driver-board.md`.

### C4. Eyelet numbering

The manual references PC-3 eyelets by number (1–23). These are screen-printed on the board. We should document the eyelet layout so build-step pages can reference "eyelet #17" with confidence.

**Suggested home:** new section in `components/pc-3a-driver-board.md` with an eyelet-numbering diagram.

---

## Category D — Things in our docs that ARE correct against the manual

Brief positive checklist so we don't change what's already right:

- ✓ All 11 existing power-supply step pages (steps 1–11) match the manual.
- ✓ Lead colors (red-black, white pair, red pair, green pair, brown pair, red-yellow, green-yellow, brown-yellow) match PA-060 spec sheet.
- ✓ Heater pin assignments (pins 2/8 for GZ-34, pins 2/7 for EL-34, pins 2/7 for 6GH8A) are correct.
- ✓ Seven-lug terminal strip: lugs 5 (green-yellow) and 7 (brown-yellow) for heater CTs is correct per manual step 6.
- ✓ Star ground at the filter cap solder lug — correct per manual step 15 (and the "Only 1 lug" marginalia confirms it's the main ground point).
- ✓ Version B / 6GH8A is the right schematic to follow for this kit.

---

## Proposed work order (assuming you sign off on the discrepancies in Category A)

1. **Fix A1** (V-numbering) — touches build/index, driver-stage/index, components/6gh8a-driver-tube, possibly components/pc-3a-driver-board. Small surgical edits, no new content.
2. **Fix A3** (1N4007 framing) — touches modifications/1n4007-replacement and build/index. Reframe as "historical mod, now stock". Small.
3. **Fix A4–A6** (PA-060, A-470, C-354 spec verification) — read each component page, verify against manual spec sheets, correct any wrong numbers. Small per page.
4. **Fix A2** (bias methodology) — bigger. Rewrite `bring-up/bias-adjustment.md` so the stock 15.6Ω procedure is primary, per-tube becomes the mod-conditional path.
5. **Fill B1** (mechanical assembly) — new section with 15-ish step pages. Large but additive, no cross-cutting changes.
6. **Fill B5, B6, B7, B8** (voltage test table, parts list, operating modes, troubleshooting) — smaller additive content drops.
7. **Fill B2** (wiring steps 12-37) — larger additive content drop. Could be done before or after B3.
8. **Fill B3** (PC-3 board wiring 38-65) — largest additive content drop.
9. **Add C3, C4** (PC-3 component values + eyelet diagram) — small additions to existing component page.
10. **C1, C2** (recreate manual pictorial and schematic) — large, deferred indefinitely unless you want to invest there. Citing the manual is the cheap alternative.

Each major chunk is independently committable. Build pages don't depend on each other in a way that requires big-bang rewrites — we can land them incrementally as you build through them.
