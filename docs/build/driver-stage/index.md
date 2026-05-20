---
title: Driver stage wiring (steps 38-65)
---

# Driver stage wiring — manual steps 38-65

The final 28 manual steps mount and wire the **PC-3A driver board**, connect input audio, and install the power cord. After this section is done, the amp is electrically complete and ready for [bring-up](../../bring-up/index.md).

## What gets built here

- **The PC-3A driver board** is mounted on the chassis underside. Its two 6GH8A driver tubes (one per channel) provide audio voltage amplification + phase splitting.
- **Audio input path**: RCA jacks → input switch → grid leak resistors → board input pads → 6GH8A pentode grids → pentode plates → coupling caps → 6GH8A triode grids (cathodyne phase splitter) → out as two 180°-apart signals per channel → coupling caps → EL-34 grids.
- **Board B+ feeds**: filter cap lugs deliver multiple voltages to the board through eyelets — the dropping resistors on the board itself produce the final operating voltages for the 6GH8A pentode plates and screens.
- **6GH8A heaters**: daisy-chained from the EL-34 heater strings (V3 for the right channel driver, V6 for the left channel driver — note the apparent reversal is because the wiring topology routes the heater through the closest EL-34's pins 2/7).
- **Power cord installation**: cord through the chassis grommet → fuse holder → on-off switch → power transformer primary.

## Step-by-step walkthrough

### Step 38 — Mount the PC-3 board

> *Mount the printed circuit board PC-3 from the bottom of the chassis. Note the numbers of the eyelets are upright when looking from the front of the chassis. Use a 4/40 screw and nut at each mounting hole.* — manual page 8

The PC-3A board mounts to the bottom of the chassis with two #4-40 screws. The board hangs in the chassis interior with its eyelets pointing up (component side faces down toward the chassis bottom). Orient so the **eyelet numbers read upright** when you view from the front of the chassis.

The board has 23 numbered eyelets (small punched holes for solder connections). They're labeled by number on the board itself.

The manual provides the soldering convention for the board: *"all connections are made to the square solder pads. The lead wires are stripped back about ¼" and inserted into the appropriate solder pad hole. With soldering iron, heat both the exposed lead and solder pad while introducing the solder at this junction. Allow solder to flow into the solder pad hole and remove solder iron tip allowing connection to set. Insure that top board side components are clear of exposed lead and all connections are made from bottom side of the PC board."*

### Steps 39-43 — B+ feeds to the board

These five steps deliver the B+ supply rails from the filter cap to the PC-3 board.

| Step | Wire | From | To |
|---|---|---|---|
| 39 | 2¾" wire | PC-3 eyelet #23 (S) | V6 pin 6 (S) |
| 40 | 3" wire | PC-3 eyelet #22 (S) | V7 pin 6 (S) |
| 41 | 3" wire | PC-3 eyelet #19 (S) | Filter cap lug #3 |
| 42 | 22 kΩ resistor (1" leads) | Filter cap lug #3 (S) | Filter cap lug #4 |
| 43 | 3½" wire | PC-3 eyelet #20 (S) | Filter cap lug #4 (S) |

**What this builds**:

- **Steps 39, 40**: connect the cathodyne phase-splitter outputs from the PC-3 (eyelets #22 and #23) to pin 6 of the right-channel EL-34s. Pin 6 is the EL-34's "internal connection" pin which serves as the convenient through-pin for the grid signal (it's wired internally between pins, and the actual control grid is pin 5 with the grid stopper from step 37). Wait — let me check the schematic... Actually pin 6 connects via the 1 kΩ grid stopper (step 37) to pin 5 (the grid). So pin 6 is the *coupling-cap input* side of the grid stopper.

- **Steps 41-43**: build the rest of the B+ chain — the 22 kΩ dropping resistor between filter cap lug 4 (375 V "lug B") and... wait, this seems off. Let me read it again.

Re-reading: step 30 already installed a 6.8 kΩ between cap lugs 1 and 4. Now step 42 installs a 22 kΩ between lugs 3 and 4. So the chain is:

- Lug 2 (D, 435 V) ← from rectifier
- Lug 1 (C, 415 V) ← from choke output
- Lug 4 (B, 375 V) ← via 6.8 kΩ from lug 1, also connected to PC-3 eyelet #20
- Lug 3 (A, 305 V) ← via 22 kΩ from lug 4, also connected to PC-3 eyelet #19

So eyelet #19 receives 305 V (lug A) and eyelet #20 receives 375 V (lug B). On the board, eyelet #20's 375 V feeds the 6GH8A pentode plate load resistors, and eyelet #19's 305 V feeds the 6GH8A pentode screens and the triode plate.

### Step 44 — Input wiring to the board

A short wire from the PC-3 board's "input [L]" pad to the **grounded (short) lug** of the left RCA socket, and another from the board's "input [R]" pad to the grounded lug of the right RCA socket. These are the audio-ground returns from the input jacks to the board.

Note: the LEFT input grounded lug, not the LEFT input long lug. The long lugs carry signal hot; the short lugs are signal ground.

### Steps 45-46 — Driver tube heaters

The 6GH8A drivers don't have their own heater connection from the PA-060 — they tap off the EL-34 heater strings.

**Step 45**: a twisted pair of wires (length to suit) connects PC-3 eyelets #15 (S) and #16 (S) to socket V6 pin 7 (S) and pin 2 (S). This brings 6.3 V AC from the V6 heater pins (channel A heater string) up to the PC-3 board for the channel A 6GH8A driver.

**Step 46**: same idea, but PC-3 eyelets #4 (S) and #5 (S) to socket V3 pin 7 (S) and pin 2 (S). Channel B driver's heater taps off V3's heater pins.

### Step 47 — Bias to right bias pot

A 2½" wire from PC-3 eyelet #21 (S) to lug 2 of the right potentiometer (S). This is part of the bias distribution — connects the per-channel bias point through the board (where there's an internal resistor network) and out to the right bias pot's wiper.

### Step 48 — Feedback path

A 5½" wire from PC-3 eyelet #14 (S) to V6 pin 4 (S). Pin 4 of V6 is the **UL screen tap** connected to the green lead of the left A-470 primary — which means eyelet #14 connects back to the screen-grid side of the EL-34's UL operating point. This is the **global negative feedback path** for the channel A driver: a portion of the OPT primary signal returns to the driver stage to apply feedback. See [feedback](../../theory/feedback.md).

### Steps 49-54 — Input switch and RCA jack wiring

| Step | Wire / component | From | To |
|---|---|---|---|
| 49 | 2" wire | Input switch lug #3 (S) | Long lug of right input socket |
| 50 | 470 kΩ resistor | Long lug of right input socket | Short (ground) lug of right input socket (S) |
| 51 | 470 kΩ resistor | Input switch lug #1 (S) | Short (ground) lug of left input socket (S) |
| 52 | 1¾" wire | PC-3 eyelet #17 (S) | (long) lug of right input socket (S) |
| 53 | 3½" wire | PC-3 eyelet #7 (S) | (long) lug of left input socket |
| 54 | Short link | Left input socket (long) lug (S) | Input switch lug #2 |

These steps build the input signal path. The **470 kΩ resistors** at the input jacks are **grid leak resistors** — they provide a DC return path for the 6GH8A pentode grid, holding it at ground potential when no signal is present (the coupling cap to the grid blocks DC).

The **input switch** is the mono/stereo selector: lug 2 is the common, lug 1 connects to the left channel, lug 3 connects to the right channel. In MONO position the switch ties left and right inputs together.

### Steps 55-58 — Coupling cap connections

| Step | Wire | From | To |
|---|---|---|---|
| 55 | 2½" wire | PC-3 eyelet #2 (S) | V3 pin 6 (S) |
| 56 | 3½" wire | PC-3 eyelet #1 (S) | V2 pin 6 (S) |
| 57 | 2½" wire | PC-3 eyelet #6 (S) | Lug 2 of left potentiometer (S) |
| 58 | 8" wire | V3 pin 4 (S) | PC-3 eyelet #11 (S) |

**What these wire**:

- Steps 55-56 connect the board's outputs to the channel B output tubes (V2 and V3). These pair with steps 39-40 (V6, V7) to give all four EL-34 grids a signal connection.
- Step 57 mirrors step 47 — left channel bias point through the board to the left bias pot.
- Step 58 is the **channel B feedback path** (mirror of step 48): wires V3's UL screen tap (pin 4, GREEN lead from OPT primary) back to PC-3 eyelet #11 for feedback to the channel B driver.

Per the manual: *"It is important to keep this wire close to the chassis and carried around the printed circuit board as shown in the pictorial."* The feedback wire is sensitive to inductive pickup; routing it close to the chassis minimizes loop area.

### Steps 59-65 — Power cord installation

The last 7 steps finish the build by installing the AC mains cord through the chassis grommet (from [M7](../mechanical-assembly/step-m07-grommet.md)) and wiring it to the fuse holder, on-off switch, and power transformer primary.

| Step | Wire / component | From | To |
|---|---|---|---|
| 59 | 5" wire | PC-3 eyelet #9 (S) | Solder lug near filter cap (chassis ground) |
| 60 | 12" wire | Lug 1 of left screw terminal strip (S) | PC-3 eyelet #12 (S) |
| 61 | 10½" wire | Lug 4 of left screw terminal strip (S) | Solder lug near filter cap |
| 62 | 9½" wire | Lug 1 of right screw terminal strip (S) | PC-3 eyelet #13 (S) |
| 63 | 9" wire | Lug 4 of right screw terminal strip (S) | Solder lug near filter cap |
| 64 | Short link | Capacitor ground lug (S) | Solder lug near capacitor. **Solder all six wires** which converge at this pair of solder lugs. |
| 65 | (See below) | Power cord installation | Multiple destinations |

**Step 64** is critical: it's the moment the **star ground** is completed. Six wires converge at the main solder lug (or pair of solder lugs) near the filter capacitor:

- PC-3 board ground (eyelet #9, step 59)
- Left speaker common (step 61)
- Right speaker common (step 63)
- The HV center tap (RED/YEL from PA-060, step 7)
- Possibly more depending on revision

Solder all of them in one session — once everything is on the lug, melt the solder so it flows around all six wires at once. Hot work, requires a higher-wattage iron temporarily, but it gives a single clean joint instead of six separately-tinned wires.

**Step 65** installs the power cord:

> *Strip back and remove outer jacket of power cord exposing approx. 5" of all (3) insulated wires. Insert power cord from outside through the chassis grommet with the outer cord jacket protruding ½" inside of the chassis. Now, install the cord stop bushing on the cord and position on the ½" extended cord jacket and tighten securely with the provided cable tie. (See pictorial). Now, cut the white lead 3", strip end and connect to (B) lug of fuse holder (S). Cut black wire 4 ½", strip end and connect to lug (2) of on-off switch (S). Mount solder lug to L/H 8/32 extended threaded stud at power transformer. Cut green lead 2 ¾" and connect to solder lug (S). This completes wiring of your amplifier.* — manual page 10

This is the AC mains wiring:

| Cord wire | Goes to | Role |
|---|---|---|
| WHITE (neutral) | Fuse holder (B) lug (S) | Mains return |
| BLACK (hot) | On-off switch lug 2 (S) | Switched mains |
| GREEN (earth) | Solder lug at PA-060's 8/32 mounting stud (S) | Chassis ground via the [3-prong cord modification](../../modifications/3-prong-cord.md) |

The **green (earth) lead** is the modern 3-prong cord's safety ground — see the [3-prong cord modification page](../../modifications/3-prong-cord.md). Earlier 2-prong kits omitted this lead.

The **strain relief bushing** (cord stop) clamps the cord jacket inside the chassis so any tug on the cord doesn't pull the internal connections off.

## After step 65

The amp is **electrically complete**. Before powering on:

1. Re-check all soldering for cold joints (dull or grainy solder).
2. Run [continuity checks](../../bring-up/continuity-checks.md).
3. Re-read [HV safety](../../test-equipment/high-voltage-safety.md).
4. Then follow [first power-on](../../bring-up/first-power-on.md).

## See also

- [Output stage wiring (steps 12-37)](../output-stage/index.md) — what comes before this
- [Bring-up](../../bring-up/index.md) — what happens next
- [PC-3A driver board](../../components/pc-3a-driver-board.md) — the board this section is built around
- [6GH8A driver tube](../../components/6gh8a-driver-tube.md) — the tubes on the board
- [Phase splitting](../../theory/phase-splitting.md) — what the triode section of the 6GH8A does
- [Feedback](../../theory/feedback.md) — the loops wired in steps 48 and 58
