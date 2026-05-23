---
title: Output stage wiring (steps 11-37)
---

# Output stage wiring — manual steps 11-37

After the [power supply wiring (steps 1-10)](../power-supply/index.md) is done, the next 27 manual steps wire up the **output stage**: the A-470 output transformer secondaries (right then left), the OPT primaries with their ultralinear screen taps, the EL-34 sockets, the bias network on the seven-lug terminal strip, the per-channel cathode sensing, and the grid stopper resistors.

Note that **step 11 is physically on manual page 6** alongside the power supply work, but functionally it's an output-stage operation (wiring the right output-transformer secondaries to the rear terminal strip) — so it lives in this section, paired with its left-channel mirror in step 12. The manual's page break between pages 6 and 7 falls between these two channels rather than between subsystems.

This is the densest wiring section in the build. Take it in chunks; don't try to do all 27 steps in one sitting.

## What gets built here

- **Audio signal path output side**: from the EL-34 grids (driven by the PC-3 board, wired later) → through 1 kΩ grid stoppers → into the EL-34s → out their plates and screen grids → into the A-470 primary windings → out the secondaries to the speaker terminals.
- **Cathode sensing**: the four EL-34 cathodes connect to a per-channel 15.6 Ω sense resistor to ground. The voltage across this resistor (target: 1.56 V at full bias) is wired to the Biaset socket on the front panel.
- **Bias network**: the seven-lug terminal strip becomes the home of the bias supply filter caps, dropping resistors, and the wires that distribute negative grid voltage to the EL-34s through the bias potentiometers.
- **B+ chain extension**: the rectifier output (V1 pin 8) lands on filter cap lug 2, completing the rectifier-to-first-filter path. A 6.8 kΩ dropping resistor between filter cap lugs creates the next voltage stage in the B+ chain.

## Step status

| Step | Title | Manual quote covers |
|---|---|---|
| 11 | [Right OPT secondaries](step-11-right-opt-secondaries.md) | Right A-470 secondary → right 4-screw strip *(manual page 6)* |
| 12 | [Left OPT secondaries](step-12-left-opt-secondaries.md) | Left A-470 secondary → left 4-screw strip |
| 13 | [Right OPT primary](step-13-right-opt-primary.md) | A-470 primary to V3 and V2 (plates + UL taps) |
| 14 | [Left OPT primary](step-14-left-opt-primary.md) | A-470 primary to V6 and V7 (mirror) |
| 15 | [Disc caps on 7-lug strip](step-15-disc-caps.md) | RF-bypass on heater CT lugs |
| 16 | [V6 ↔ V7 heater daisy](step-16-v6-v7-heater-daisy.md) | Channel A heater string completion |
| 17 | [V2 ↔ V3 heater daisy](step-17-v2-v3-heater-daisy.md) | Channel B heater string completion |
| 18 | [Bias jumper lug 1↔6](step-18-bias-jumper.md) | Extends ground node on 7-lug strip |
| 19 | [First bias filter cap](step-19-bias-cap-1.md) | 100 µF cap, neg → lug 4, pos → lug 1 |
| 20 | [First bias resistor](step-20-bias-resistor-1.md) | 10 kΩ from lug 4 to lug 3 |
| 21 | [Second bias filter cap](step-21-bias-cap-2.md) | 100 µF cap, neg → lug 3, pos → lug 1 |
| 22 | [Second bias resistor](step-22-bias-resistor-2.md) | 10 kΩ from lug 2 to lug 1 (S) |
| 23 | [Bias ground](step-23-bias-ground.md) | Lug 6 (S) → main ground lug |
| 24 | [Bias to left pot lug 1](step-24-bias-pot-distribution-1.md) | Lug 3 (S) → left pot lug 1 |
| 25 | [Bias from diode](step-25-bias-from-diode.md) | Lug 4 (S) → diode non-banded end (S) |
| 26 | [Bias to left pot lug 3](step-26-bias-pot-distribution-2.md) | Lug 2 (S) → left pot lug 3 |
| 27 | [Inter-pot wire lug 3](step-27-bias-pot-interconnect-1.md) | Right pot lug 3 (S) ↔ left pot lug 3 (S) |
| 28 | [Inter-pot wire lug 1](step-28-bias-pot-interconnect-2.md) | Right pot lug 1 (S) ↔ left pot lug 1 (S) |
| 29 | [Rectifier → filter cap](step-29-rectifier-to-filter-cap.md) | V1 pin 8 (S) → cap lug 2 (S) |
| 30 | [6.8 kΩ B+ dropping](step-30-b-plus-dropping-resistor.md) | Cap lug 1 (S) ↔ lug 4 |
| 31 | [V2 cathode sense](step-31-v2-cathode-sense.md) | 15.6 Ω at V2 socket |
| 32 | [V2 ↔ V3 cathode daisy](step-32-v2-v3-cathode-daisy.md) | Ties V2 and V3 cathodes |
| 33 | [V3 → left Biaset](step-33-v3-to-left-biaset.md) | Routes channel B bias to V4 |
| 34 | [V7 cathode sense](step-34-v7-cathode-sense.md) | 15.6 Ω at V7 socket |
| 35 | [V7 ↔ V6 cathode daisy](step-35-v6-v7-cathode-daisy.md) | Ties V6 and V7 cathodes |
| 36 | [V6 → right Biaset](step-36-v6-to-right-biaset.md) | Routes channel A bias to V5 |
| 37 | [Grid stoppers](step-37-grid-stoppers.md) | Four 1 kΩ from pin 5 to pin 6 |

## After step 37

The output stage is **electrically complete** — the EL-34 plates, screens, cathodes, and grids are all wired. The next 28 steps ([driver stage](../driver-stage/index.md)) build the audio signal path that *feeds* these EL-34 grids: the PC-3A board mounting and wiring, plus the input RCA jacks and power cord.

## See also

- [Power supply wiring (steps 1-10)](../power-supply/index.md) — what comes before
- [Driver stage wiring (steps 38-65)](../driver-stage/index.md) — what comes after
- [A-470 output transformer](../../components/a-470-output-transformer.md) — primary lead colors
- [Seven-lug terminal strip](../../components/seven-lug-terminal-strip.md) — the bias network's home
- [Bias adjustment](../../bring-up/bias-adjustment.md) — what the cathode-sense network enables
- [EL34 output tube](../../components/el34-output-tube.md) — what we're wiring around
