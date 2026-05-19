# ST-70 Build Manual — Website Migration Plan

This document is the kickoff plan for migrating the ST-70 build manual from standalone markdown files (produced in Claude.ai chat) to a deployed website using MkDocs Material on GitHub Pages.

The intended workflow going forward is to use **Claude Code** for all editing, content production, and infrastructure changes against this repo. This document serves as the handoff between the chat-based authoring phase and the repo-based authoring phase.

---

## Current state

### Existing content (produced in chat, ~14,100 words)

Four markdown files have been produced and should be migrated into the new structure:

- `README.md` — table of contents, project overview, current build status, conventions
- `01-power-supply-theory.md` — transformer construction, rectification theory, heater theory, the PA-060 winding chart, complete power supply at a glance, voltage-source-vs-current-path mental model
- `02-power-supply-wiring.md` — page 6 of the Dynaco manual, with full level-2 explainers for steps 1–6. Steps 7–11 are scaffolded as headings with bullet-point notes on what should be covered.
- `09-appendix-test-equipment.md` — DMM (IDEAL 61-327), oscilloscope intro, probe types, high-voltage probe recommendations, variac usage, isolation transformer reconsidered, expanded HV safety section, capacitor diagnosis with a scope

### Build state

- **Physical build:** Page 6, steps 1–6 soldered. Next is step 7 (red-yellow center tap to filter cap solder lug).
- **Documentation state:** Steps 1–6 fully written. Steps 7–11 scaffolded only.

### Build configuration

- **Kit:** DynakitParts ST-70, 6GH8A driver board version
- **Power transformer:** Dynakit PA-060 (Pacific Transformer reproduction)
- **Output transformers:** Dynakit A-470 (Pacific Transformer reproduction)
- **Output tubes:** Electro-Harmonix EL34 Apex Matched Quad
- **Rectifier:** Sovtek 5AR4
- **Driver tubes:** 6GH8A (with adapter set from Amplified Parts)

### Tube layout (this manual's numbering)

This kit's manual uses a non-standard tube numbering. **Always defer to this convention; some online references will differ.**

| Position | Designation | Tube |
|---|---|---|
| Chassis, near power transformer | V1 | 5AR4 rectifier |
| Chassis, octal sockets | V2, V3, V6, V7 | EL34 output tubes |
| PC-3A driver board | V4, V5 | 6GH8A driver/phase-splitters |

### Test equipment on hand

- **DMM:** IDEAL 61-327 (CAT III 600V, manual ranging, AC/DC volts to 600V, no current, no capacitance, no true RMS)
- **Variac:** AC-DC PowerShack SC-5M
- **No oscilloscope yet** — considering Rigol DHO804 (4-channel, 12-bit ADC, ~$370). Plan to add a budget 100× high-voltage probe (P4100-class, ~$30) when scope is purchased.
- **No isolation transformer** — explicitly determined not needed for this build.

### Planned modifications

- 3-prong grounded power cord (safety)
- 1N4007 silicon diode replacing original selenium rectifier (safety, reliability) — already incorporated in step 1
- Anti-click capacitor on power switch
- Individual bias pots per output tube (instead of original shared bias)
- VTA driver board deferred as future upgrade

---

## Target architecture

### Stack

- **Static site generator:** MkDocs Material
- **Hosting:** GitHub Pages (free, auto-deploy via Actions)
- **Source:** Markdown files in this repo
- **Diagrams:** Mix of static SVG (schemdraw, matplotlib) and interactive (Plotly, animated SVG)
- **PDF export:** `mkdocs-with-pdf` or `mkdocs-pdf-export-plugin` for on-demand generation

### Repo structure

```
st70-manual/                          (repo root)
├── docs/                              (MkDocs source)
│   ├── index.md                       (homepage)
│   ├── getting-started/
│   │   ├── overview.md                (what we're building, scope of manual)
│   │   ├── tools-and-workspace.md     (soldering iron, hand tools, ventilation)
│   │   ├── reading-this-manual.md     (conventions, structure, how to navigate)
│   │   └── safety-basics.md           (HV awareness, link to detailed appendix)
│   ├── components/                    (one page per significant component)
│   │   ├── index.md                   (component index page)
│   │   ├── 5ar4-rectifier-tube.md
│   │   ├── el34-output-tube.md
│   │   ├── 6gh8a-driver-tube.md
│   │   ├── pa-060-power-transformer.md
│   │   ├── a-470-output-transformer.md
│   │   ├── filter-capacitors.md
│   │   ├── choke.md
│   │   ├── 1n4007-diode.md
│   │   ├── seven-lug-terminal-strip.md
│   │   ├── pc-3a-driver-board.md
│   │   └── ... (more as we go)
│   ├── theory/                        (conceptual chapters)
│   │   ├── index.md
│   │   ├── how-transformers-work.md
│   │   ├── rectification.md
│   │   ├── heater-circuits.md
│   │   ├── grounding-and-hum.md
│   │   ├── push-pull-topology.md      (later, when we get to output stage)
│   │   ├── phase-splitting.md         (later)
│   │   └── feedback.md                (later)
│   ├── build/                         (step-by-step procedural)
│   │   ├── index.md                   (build progress tracker)
│   │   ├── power-supply/
│   │   │   ├── overview.md
│   │   │   ├── step-01-bias-diode.md
│   │   │   ├── step-02-5ar4-heater.md
│   │   │   ├── step-03-5ar4-anodes.md
│   │   │   ├── step-04-v2-heater.md
│   │   │   ├── step-05-v7-heater.md
│   │   │   ├── step-06-heater-cts.md
│   │   │   ├── step-07-hv-ct.md
│   │   │   ├── ... (etc through step 11)
│   │   │   └── overview-after-page-6.md
│   │   ├── driver-stage/
│   │   ├── output-stage/
│   │   └── final-assembly.md
│   ├── modifications/
│   │   ├── index.md
│   │   ├── 3-prong-cord.md
│   │   ├── 1n4007-replacement.md
│   │   ├── anti-click-cap.md
│   │   └── individual-bias-pots.md
│   ├── bring-up/
│   │   ├── index.md
│   │   ├── pre-power-checklist.md
│   │   ├── continuity-checks.md
│   │   ├── first-power-on.md
│   │   ├── voltage-checks.md
│   │   ├── bias-adjustment.md
│   │   └── functional-testing.md
│   ├── test-equipment/
│   │   ├── index.md
│   │   ├── multimeter.md
│   │   ├── oscilloscope.md
│   │   ├── probes.md
│   │   ├── variac.md
│   │   └── high-voltage-safety.md
│   ├── appendices/
│   │   ├── tube-pinouts.md
│   │   ├── transformer-specs.md
│   │   ├── component-theory.md
│   │   └── references-and-further-reading.md
│   └── assets/
│       ├── diagrams/                  (SVGs and PNGs)
│       │   ├── src/                   (Python source for generated diagrams)
│       │   └── *.svg, *.png
│       ├── photos/                    (build photos, pictorial scans)
│       └── stylesheets/               (custom CSS overrides if any)
├── mkdocs.yml                         (site config)
├── requirements.txt                   (Python deps for build)
├── .github/
│   └── workflows/
│       └── deploy.yml                 (auto-build and deploy on push)
├── .gitignore
├── README.md                          (repo readme, not site content)
└── PLAN.md                            (this file)
```

### Why this structure

- **Components, theory, build, and test equipment are siblings, not nested.** Each can be navigated independently. A reader can drill into the build, look up a component, jump to a theory chapter, all from the top-level nav.
- **One page per step** (rather than one page per manual page) means each step gets its own URL, can be deep-linked from anywhere, and shows up cleanly in search results.
- **Cross-linking is core.** Every step page links to the components it touches and the theory it depends on. Every component page lists where it's referenced in steps.
- **Modifications and bring-up are their own sections** because they're conceptually distinct from "follow the manual" — they have their own logic and benefit from being grouped together.

---

## Migration phase 1: Infrastructure setup

This is the work to do in the first Claude Code session in the new repo.

### Prerequisites

- [ ] GitHub account (if not already set up)
- [ ] New repo created on GitHub (suggested name: `st70-manual`, public for free Pages)
- [ ] Repo cloned locally
- [ ] Python 3.10+ installed (`python --version` to verify)
- [ ] Git configured with GitHub credentials (`git config --global user.name`, `user.email`)
- [ ] Editor of choice (VS Code recommended for markdown editing)
- [ ] Claude Code CLI installed and authenticated

### Tasks

1. **Initialize project structure**
   - Create the `docs/` folder hierarchy as outlined above (just folders + empty `index.md` files in each section to start)
   - Create `mkdocs.yml` with Material theme config
   - Create `requirements.txt` with `mkdocs-material` and any chosen plugins
   - Create `.gitignore` for `site/`, `__pycache__/`, etc.

2. **Configure MkDocs Material**
   - Choose color scheme (suggest dark mode with a warm accent — tube amp vibes)
   - Enable navigation features: instant loading, tabs, sections, expandable sidebar
   - Enable search
   - Enable code highlighting and admonitions
   - Configure the navigation tree in `mkdocs.yml`

3. **Recommended MkDocs Material plugins**
   - `mkdocs-material` (core)
   - `mkdocs-material[imaging]` for image optimization
   - `pymdown-extensions` for admonitions, tabs, task lists
   - `mkdocs-glightbox` for image lightbox
   - `mkdocs-git-revision-date-localized-plugin` for "last updated" timestamps
   - `mkdocs-with-pdf` for PDF export
   - Consider: `mkdocs-redirects` if URLs ever change
   - Consider: `mkdocs-minify-plugin` for production builds

4. **Migrate existing content into new structure**

   Source files → destination paths:

   - `README.md` (current) → split into:
     - `docs/index.md` (project overview, what this manual is)
     - `docs/build/index.md` (current build status, progress tracker)
     - `docs/getting-started/reading-this-manual.md` (conventions)
     - `docs/appendices/transformer-specs.md` (PA-060 winding chart, A-470 specs)

   - `01-power-supply-theory.md` → split into:
     - `docs/theory/how-transformers-work.md` (sections on transformer construction)
     - `docs/theory/rectification.md` (sections on AC→DC, half-wave, full-wave)
     - `docs/theory/heater-circuits.md` (sections on heater AC, twisting, CT-to-ground)
     - `docs/components/pa-060-power-transformer.md` (PA-060 specifics, winding chart)
     - Keep "complete power supply at a glance" diagram in `docs/build/power-supply/overview.md`
     - Keep "voltage-source vs current-path" mental model in `docs/theory/rectification.md` or as its own theory page

   - `02-power-supply-wiring.md` → split into:
     - `docs/build/power-supply/overview.md` (page 6 introduction, conventions)
     - `docs/build/power-supply/step-01-bias-diode.md`
     - `docs/build/power-supply/step-02-5ar4-heater.md`
     - `docs/build/power-supply/step-03-5ar4-anodes.md`
     - `docs/build/power-supply/step-04-v2-heater.md`
     - `docs/build/power-supply/step-05-v7-heater.md`
     - `docs/build/power-supply/step-06-heater-cts.md`
     - Stub files for steps 7–11 (with the scaffolding bullet points preserved as content notes)

   - `09-appendix-test-equipment.md` → split into:
     - `docs/test-equipment/multimeter.md` (IDEAL 61-327 details)
     - `docs/test-equipment/probes.md` (DMM probes, scope probes, HV probes)
     - `docs/test-equipment/oscilloscope.md` (DHO804 considerations, what scopes show)
     - `docs/test-equipment/variac.md` (slow bring-up procedure)
     - `docs/test-equipment/high-voltage-safety.md` (the HV safety section)
     - The "diagnosing capacitors with a scope" section → `docs/test-equipment/oscilloscope.md` as a sub-section, OR a standalone "diagnostic techniques" page

5. **Add cross-reference links**

   During migration, every reference to a component or concept becomes a markdown link. Examples:

   - In step 1's explainer: "Connecting... to the cathode (banded end) of a [1N4007 silicon diode](../../components/1n4007-diode.md)..."
   - In step 2's explainer: "...connecting the [5V @ 4A heater winding](../../components/pa-060-power-transformer.md#heater-windings) to the filament pins of the [5AR4 rectifier](../../components/5ar4-rectifier-tube.md)..."
   - In rectification theory: "See [step 3](../build/power-supply/step-03-5ar4-anodes.md) for the actual wiring of this rectifier topology."

6. **Set up GitHub Pages deployment**

   - Create `.github/workflows/deploy.yml` (standard MkDocs deploy action)
   - In repo settings, enable GitHub Pages from the `gh-pages` branch (Action will publish there)
   - Verify build succeeds and site is accessible at `<username>.github.io/st70-manual/`

7. **Verify locally**

   ```bash
   pip install -r requirements.txt
   mkdocs serve
   ```

   Open `http://localhost:8000`, click through every page, verify navigation works, search returns sensible results, and styling looks right.

### Acceptance criteria for phase 1

- [ ] Site builds locally without errors
- [ ] All 14,100 words of existing content are migrated and findable in the new structure
- [ ] Cross-reference links work
- [ ] Site is deployed to GitHub Pages
- [ ] Mobile view is usable (test on actual phone)
- [ ] Search returns useful results
- [ ] `mkdocs build --strict` passes (catches broken links)

---

## Migration phase 2: Content gaps

After phase 1, the site has all existing content but is missing several sections that we identified as needed. These can be filled in over time, not all at once.

### Pages to author

**Getting started section (estimated 1–2 sessions):**

- `docs/getting-started/overview.md` — what the ST-70 is, why we're building one, what this manual covers and doesn't cover
- `docs/getting-started/tools-and-workspace.md` — soldering iron specs, hand tools, lighting, ventilation, antistatic precautions, workspace organization
- `docs/getting-started/safety-basics.md` — high-level safety overview with links to detailed `test-equipment/high-voltage-safety.md`

**Component pages (1 session per ~3–4 components):**

For each significant component, write a page covering:
- What it is (physically, electrically)
- Spec summary (voltages, currents, ratings)
- How it works (brief, with link to deeper theory chapter)
- Where it's used in the ST-70 (with links to relevant build steps)
- Things that go wrong with it (failure modes)
- Modifications or alternatives (where relevant)

Priority order for component pages:
1. PA-060 power transformer (already partly written, split from theory chapter)
2. 5AR4 rectifier tube
3. EL34 output tube
4. 6GH8A driver tube
5. A-470 output transformer
6. Filter capacitors (quad cap)
7. Choke
8. 1N4007 diode
9. Seven-lug terminal strip
10. PC-3A driver board

**Theory chapter splits (1 session):**

Split the existing power supply theory into the three new theory pages, with proper cross-linking.

**Bring-up section (multiple sessions, when we get there):**

- Pre-power checklist (continuity tests, visual inspection)
- First power-on procedure (variac ramp-up)
- Voltage check procedure (what to measure where)
- Bias adjustment procedure (with individual bias pots mod)
- Functional testing (signal injection, listening tests)

These are produced **after** the build is complete in the chassis. They're informed by what actually happens during bring-up.

---

## Migration phase 3: Diagrams

Diagrams are produced incrementally, not all at once.

### Tier 1: Interactive (highest priority)

Authored as embedded HTML/JS in markdown pages. MkDocs Material supports raw HTML inline.

1. **Rectification waveform interactive** — sliders for capacitor value and load current; reader watches ripple change in real time. Best home: `docs/theory/rectification.md`.

2. **Full-wave rectifier animation** — shows which anode is conducting at each instant, with current path highlighted. Best home: `docs/theory/rectification.md` or `docs/components/5ar4-rectifier-tube.md`.

3. **Heater hum cancellation animation** — magnetic field around two parallel wires vs. twisted wires. Best home: `docs/theory/heater-circuits.md`.

4. **180° phase relationship animation** — two waveforms across a CT, locked in opposite phase. Best home: `docs/theory/rectification.md`.

Tools: Plotly for waveforms, hand-authored animated SVG (SMIL or CSS) for conceptual animations.

### Tier 2: Static SVG with tooltips/hover

Authored as SVG files with `<title>` elements and CSS hover states. Lightweight, no JavaScript.

1. **PA-060 winding diagram** — five secondaries, color-coded leads, hover for voltage/current spec
2. **5AR4 internal structure** — dual anode topology, shared cathode, pinout
3. **EL34 internal structure** — pentode layout, pinout
4. **Star ground topology** — the amp's ground architecture, hover to highlight current paths
5. **Tube pinout charts** — one per tube, with pin functions

### Tier 3: Static SVG (reference)

1. **Transformer cross-section** — laminations, windings, bobbin, end bells (construction reference)
2. **Chassis layout** — top view showing component placement
3. **Schematic snippets** — small extracts of the schematic, called out where relevant

Tools: `schemdraw` (Python) for circuit-style diagrams, `matplotlib` for waveforms, hand-authored SVG for everything else.

### Diagram authoring workflow

1. Diagrams have source files in `docs/assets/diagrams/src/` (Python scripts for generated ones, raw SVG for hand-authored)
2. Generated diagrams output to `docs/assets/diagrams/` as SVG
3. Each diagram has a clear name: `rectification-half-wave.svg`, `pa060-windings.svg`, etc.
4. Reference from markdown: `![Half-wave rectification](../assets/diagrams/rectification-half-wave.svg)`

---

## Migration phase 4: Continuous build content

Once the site is up, all new content goes directly into the appropriate pages. No more "checkpoint" cycle — work happens in the repo, commits trigger deploys, changes appear on the live site within minutes.

### Workflow for each new build step

When Jeff completes a wiring step physically:

1. Update `docs/build/index.md` build progress tracker
2. Open `docs/build/power-supply/step-XX-name.md` (or create it)
3. Claude Code writes the level-2 explainer using established conventions
4. Add cross-references to relevant components and theory pages
5. Update affected component pages' "used in steps" sections
6. Commit and push; auto-deploys to live site

### Workflow for new diagrams

1. Open Claude Code in repo
2. Describe the diagram (or ask Claude to suggest what's needed for the current page)
3. Claude generates source (Python or SVG) in `docs/assets/diagrams/src/`
4. Build the SVG; place in `docs/assets/diagrams/`
5. Reference from markdown
6. Commit and push

---

## Key conventions to maintain

These were established during the chat-based authoring phase. Preserve them across the migration:

### Voice and tone

- Second person ("you connect the lead..."), instructional
- Level-2 conceptual depth: what each step accomplishes, why the circuit is designed that way
- Tangents and "why not" alternatives are valuable, not digressions
- Honest acknowledgment of uncertainty; defer to the manual when in doubt

### Page anatomy for build steps

Each step page should include:

1. The verbatim manual instruction (set in a blockquote with italics)
2. "What you're doing physically" — concrete description of the wire path
3. "What this accomplishes" — the circuit-level role of this connection
4. "Why [some design choice]" sections — the deeper reasoning
5. Cross-references: components touched, theory chapters relevant, related steps
6. Diagrams where they materially help understanding

### Markdown conventions

- Tables for structured data (specs, pinouts, voltages)
- ASCII diagrams as placeholders pending real diagrams
- Admonitions (`!!! note`, `!!! warning`, `!!! danger`) for callouts
- Code blocks for pinout listings, file paths, terminal commands
- Front matter in each page with title, tags, "last updated"

### Component page anatomy

Each component page should include:

1. **What it is** — physical description, where it sits in the amp
2. **Specs** — table format, voltages/currents/dimensions
3. **How it works** — brief, link to deeper theory
4. **In this build** — where this specific component lives, what it does
5. **Failure modes** — what goes wrong, how to diagnose
6. **Alternatives and mods** — relevant substitutions or modifications
7. **References** — links to every step that touches this component, plus external resources

---

## Open decisions

These weren't finalized in the chat phase; resolve in the first Claude Code session:

1. **Color scheme.** MkDocs Material supports both light and dark modes with palette switcher. Suggest: default to auto (follows OS), with warm amber accent on dark mode (tube glow) and matching warm tone on light mode. Final call when we see it.

2. **Custom domain?** Optional. If you own a domain you want to use, configure in `mkdocs.yml` and GitHub Pages settings. Otherwise, lives at `<username>.github.io/st70-manual/`.

3. **Repo visibility.** Public required for free GitHub Pages on personal account (or Pro+ tier for private). Strongly suggest public — this manual has educational value for the broader ST-70 community.

4. **License.** If public, suggest CC BY-SA 4.0 for documentation (encourages sharing and derivatives while requiring attribution). Code (if any) under MIT.

5. **Comments / interactivity.** Not in initial scope. Could add Giscus later if you want reader feedback.

6. **Analytics.** Not in initial scope. Could add privacy-respecting analytics (Plausible, GoatCounter) later.

7. **Versioning.** Not needed initially. If the manual ever stabilizes into "v1" and needs a "v2," look at the `mike` plugin.

---

## What to bring into the first Claude Code session

1. This `PLAN.md` document (you're reading it)
2. The four current markdown files (the latest checkpoint #3 versions)
3. The PA-060 spec sheet image
4. The A-470 spec sheet image
5. The Version B 6GH8A schematic image
6. The page 6 wiring procedure image
7. Photos of the chassis as built so far (optional but useful for chassis layout diagrams later)

---

## What NOT to do in the first session

- Don't try to migrate everything perfectly in one sitting. Get the infrastructure working with the existing content, then iterate.
- Don't generate diagrams yet. Get the structure right first; diagrams come in phase 3.
- Don't write any new content yet (no new component pages, no new theory chapters). Phase 2 is for that.
- Don't try to fill all the navigation stubs with content. Empty index pages are fine for now — they show the planned structure.

The goal of session 1 is: **working site, all current content migrated, all phase-2 page placeholders in place, ready to iterate.**

---

## Open questions to discuss in the first session

- Does the proposed folder structure work, or should we reorganize?
- Any sections missing from the planned structure?
- Diagram tooling preferences? (Plotly vs D3 for interactive, schemdraw vs custom SVG for static)
- PDF export priority — important to have working day 1, or defer?
- Mobile reading priorities — what's the most important thing to get right for bench-side phone reading?

---

## Long-term vision

- Comprehensive, level-2 conceptual manual for the Dynaco ST-70 build
- Searchable, deep-linkable, mobile-friendly website
- Generated PDF available for offline reading or printing
- Cross-linked component, theory, and procedure sections
- Interactive diagrams that build intuition for non-obvious concepts
- Documented modifications, bring-up procedures, and ongoing maintenance
- Eventually: similar treatment for the planned PAS-3 preamp build (separate repo or section)
- Potentially shared with the ST-70 community as an educational resource

---

*End of plan. Time to migrate.*
