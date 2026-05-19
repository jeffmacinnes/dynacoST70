---
title: Step 7 — HV center tap
---

# Step 7: Connect the red-yellow lead to the filter capacitor solder lug

> *Connect the red-yellow lead to the solder lug near the filter capacitor.*

!!! info "Explainer pending"
    Step 7 is the next physical step in the build. Explainer to be written when this step gets soldered.

*Topics to cover when written:*

- Center tap of the 720V high-voltage winding on the [PA-060](../../components/pa-060-power-transformer.md).
- This is the **ground reference** for the full-wave rectification circuit started in [step 3](step-03-5ar4-anodes.md).
- Why the CT goes to the filter cap area (which is the main B+ ground reference point).
- How CT + two anodes + 5AR4 = full-wave rectifier topology, completing what we set up in step 3.
- The first ground reference for any of the [PA-060](../../components/pa-060-power-transformer.md)'s windings — until this step, every connection has been a "live" lead with no return path. With this step, the rectifier circuit becomes electrically complete.

## See also

- [Step 3 — 5AR4 anodes](step-03-5ar4-anodes.md) — the upstream wiring that this step completes
- [Filter capacitors](../../components/filter-capacitors.md) — where the CT lands
- [Rectification](../../theory/rectification.md) — the full-wave topology
- [Previous: Step 6](step-06-heater-cts.md) · [Next: Step 8 — OPT B+ feeds](step-08-opt-b-plus.md)
