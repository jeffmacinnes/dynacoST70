---
title: Driver stage wiring (steps 38-65)
---

# Driver stage wiring — manual steps 38-65

The final 28 manual steps mount the PC-3A driver board, wire the audio input chain, complete the global feedback paths, and install the power cord. After this section the amp is electrically complete and ready for [bring-up](../../bring-up/index.md).

## What gets built here

- **PC-3A board mount** and the wiring fabric that connects 23 board eyelets to the rest of the chassis.
- **Audio signal path** — RCA jacks → input switch → grid leak resistors → board input → 6GH8A pentode (input stage) → 6GH8A triode (cathodyne phase splitter) → coupling caps → EL-34 grids via grid stoppers.
- **B+ feeds to the board** — filter cap lugs A and B (305 V and 375 V) deliver power to the pentode plate, screen, and triode plate loads via the 22 kΩ + 6.8 kΩ dropping resistors.
- **Driver heaters** — daisy-chained off the EL-34 heater strings (V6 for channel A driver, V3 for channel B driver).
- **Global negative feedback** — two paths per channel: from the OPT primary UL screen taps (steps 48, 58) and from the OPT secondary 16 Ω taps (steps 60, 62).
- **Star ground completion** (step 64) — the moment all chassis-ground rays converge at one lug.
- **Power cord** (step 65) — final step in the build.

## Step status

| Step | Title | Manual quote covers |
|---|---|---|
| 38 | [Mount PC-3 board](step-38-mount-pc-3.md) | PC-3 mounting, eyelet conventions, soldering technique |
| 39 | [Eyelet #23 to V6 pin 6](step-39-eyelet-23-to-v6.md) | Phase splitter output → channel A push tube |
| 40 | [Eyelet #22 to V7 pin 6](step-40-eyelet-22-to-v7.md) | Phase splitter output → channel A pull tube |
| 41 | [Eyelet #19 to cap lug 3](step-41-eyelet-19-to-cap-3.md) | B+ feed (305 V) to board |
| 42 | [22 kΩ B+ dropping resistor](step-42-22k-dropping-resistor.md) | Cap lug 3 (S) ↔ lug 4 |
| 43 | [Eyelet #20 to cap lug 4](step-43-eyelet-20-to-cap-4.md) | B+ feed (375 V) to board |
| 44 | [Input grounds to board](step-44-input-grounds-to-board.md) | RCA shields to PC-3 input pads |
| 45 | [V6 heater to board](step-45-v6-heater-to-board.md) | Driver heater for channel A |
| 46 | [V3 heater to board](step-46-v3-heater-to-board.md) | Driver heater for channel B |
| 47 | [Eyelet #21 to right pot](step-47-eyelet-21-to-right-pot.md) | Bias distribution to channel A driver |
| 48 | [Eyelet #14 to V6 pin 4](step-48-eyelet-14-to-v6-feedback.md) | Channel A feedback from UL tap |
| 49 | [Input switch lug 3 to right RCA](step-49-input-switch-to-right-rca.md) | Right input signal path |
| 50 | [Right grid leak](step-50-right-grid-leak.md) | 470 kΩ DC clamp at right input |
| 51 | [Left grid leak](step-51-left-grid-leak.md) | 470 kΩ DC clamp at input switch lug 1 |
| 52 | [Eyelet #17 to right RCA](step-52-eyelet-17-to-right-rca.md) | Right input signal → board |
| 53 | [Eyelet #7 to left RCA](step-53-eyelet-7-to-left-rca.md) | Left input signal → board |
| 54 | [Left RCA to input switch](step-54-left-rca-to-input-switch.md) | Left input → switch lug 2 |
| 55 | [Eyelet #2 to V3 pin 6](step-55-eyelet-2-to-v3.md) | Phase splitter output → channel B push tube |
| 56 | [Eyelet #1 to V2 pin 6](step-56-eyelet-1-to-v2.md) | Phase splitter output → channel B pull tube |
| 57 | [Eyelet #6 to left pot](step-57-eyelet-6-to-left-pot.md) | Bias distribution to channel B driver |
| 58 | [V3 pin 4 to eyelet #11](step-58-v3-to-eyelet-11-feedback.md) | Channel B feedback from UL tap |
| 59 | [Eyelet #9 to ground](step-59-eyelet-9-to-ground.md) | Board signal ground → main ground lug |
| 60 | [Left strip lug 1 to eyelet #12](step-60-left-strip-1-to-eyelet-12.md) | Channel B feedback from 16 Ω secondary |
| 61 | [Left strip lug 4 to ground](step-61-left-strip-4-to-ground.md) | Left speaker common → chassis |
| 62 | [Right strip lug 1 to eyelet #13](step-62-right-strip-1-to-eyelet-13.md) | Channel A feedback from 16 Ω secondary |
| 63 | [Right strip lug 4 to ground](step-63-right-strip-4-to-ground.md) | Right speaker common → chassis |
| 64 | [Star ground completion](step-64-star-ground-completion.md) | Solder six wires at the main ground lug |
| 65 | [Power cord](step-65-power-cord.md) | Mains cord installation; build complete |

## After step 65

The amp is **electrically complete**. Continue with:

1. [Pre-power checklist](../../bring-up/pre-power-checklist.md) — final visual inspection
2. [Continuity checks](../../bring-up/continuity-checks.md) — verify wiring with a DMM
3. [First power-on](../../bring-up/first-power-on.md) — gradual variac-controlled bring-up
4. [Voltage checks](../../bring-up/voltage-checks.md) — confirm B+ and heater rails
5. [Bias adjustment](../../bring-up/bias-adjustment.md) — set EL-34 idle currents
6. [Functional testing](../../bring-up/functional-testing.md) — first audio through the amp

## See also

- [Output stage wiring (steps 12-37)](../output-stage/index.md) — what comes before
- [PC-3A driver board](../../components/pc-3a-driver-board.md) — the board this section is built around
- [6GH8A driver tube](../../components/6gh8a-driver-tube.md) — what sits on the board
- [Phase splitting](../../theory/phase-splitting.md)
- [Feedback](../../theory/feedback.md)
- [Bring-up](../../bring-up/index.md) — the next phase
