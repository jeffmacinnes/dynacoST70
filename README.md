# Dynaco ST-70 Build Manual

An annotated build manual for the Dynaco ST-70 stereo tube amplifier, capturing not just *what* to wire but *why* each connection works the way it does. Written alongside the build of a DynakitParts ST-70 kit (6GH8A driver board version).

Live site: https://jeffmacinnes.github.io/dynacoST70/

## What this is

The original Dynaco manual is procedural — it tells you which wire goes where, but assumes you already understand the underlying theory. This manual fills in the gaps: what each connection is accomplishing electrically, why the circuit is designed that way, and how the components work together to produce music.

## Local development

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000/dynacoST70/>.

To check for broken links and other build problems:

```bash
mkdocs build --strict
```

## Deployment

Every push to `main` triggers the GitHub Actions workflow in [.github/workflows/deploy.yml](.github/workflows/deploy.yml), which builds the site and publishes it to the `gh-pages` branch.

## Repository layout

```
docs/                          MkDocs source (markdown content)
  ├── index.md                 Site home
  ├── getting-started/
  ├── components/
  ├── theory/
  ├── build/                   Step-by-step procedural pages
  ├── modifications/
  ├── bring-up/
  ├── test-equipment/
  ├── appendices/
  └── assets/
mkdocs.yml                     Site config
requirements.txt               Python dependencies
.github/workflows/deploy.yml   CI deploy to GitHub Pages
```

## License

Content is licensed CC BY-SA 4.0. Build configuration code is MIT.
