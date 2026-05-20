---
title: Output stage wiring (steps 12-37)
---

# Output stage wiring — manual steps 12-37

After the [power supply wiring (steps 1-11)](../power-supply/index.md) is done, the next 26 manual steps wire up the **output stage**: the EL-34 sockets, the A-470 output transformer primaries with their ultralinear screen taps, the bias network on the seven-lug terminal strip, the per-channel cathode sensing, and the grid stopper resistors.

This is the densest wiring section in the build. Take it in chunks; don't try to do all 26 steps in one sitting.

## What gets built here

The output-stage wiring creates these electrical connections (read all together as a system):

- **Audio signal path output side**: from the EL-34 grids (driven by the PC-3 board, wired later) → through 1 kΩ grid stoppers → into the EL-34s → out their plates and screen grids → into the A-470 primary windings → out the secondaries to the speaker terminals.
- **Cathode sensing**: the four EL-34 cathodes connect to a per-channel 15.6 Ω sense resistor to ground. The voltage across this resistor (target: 1.56 V at full bias) is wired to the Biaset socket on the front panel.
- **Bias network**: the seven-lug terminal strip becomes the home of the bias supply filter caps, dropping resistors, and the wires that distribute negative grid voltage to the EL-34s through the bias potentiometers.
- **B+ chain extension**: the rectifier output (V1 pin 8) lands on filter cap lug 2, completing the rectifier-to-first-filter path. A 6.8 kΩ dropping resistor between filter cap lugs creates the next voltage stage in the B+ chain.

## Step-by-step walkthrough

### Steps 12-14 — Output transformer wiring

#### Step 12: Left OPT secondary to left 4-screw strip

Mirror of [step 11](../power-supply/step-11-right-opt-secondaries.md), but for the left A-470 (the one on the left side of the chassis). The four secondary leads (BLACK, BROWN, ORANGE, YELLOW) go to lugs 4, 3, 2, 1 of the left 4-screw terminal strip respectively.

#### Step 13: Right OPT primary leads to V3 and V2

The right A-470's primary leads (5 total) wire up to V3 and V2 — the right channel EL-34s.

Per the manual: *"Twist the blue and green leads from the left output transformer together and connect the green lead to pin #4 of V3. Connect the blue lead to pin #3 of V3 (S). Twist blue-white and green-white together and connect the blue-white lead to pin #3 of V2 (S). Connect the green-white lead to pin #4 of V2 (S)."*

| Lead | Goes to | Function |
|---|---|---|
| BLUE | V3 pin 3 (S) | Plate of V3 |
| GREEN | V3 pin 4 | UL screen tap of V3 |
| BLUE/WHITE | V2 pin 3 (S) | Plate of V2 |
| GREEN/WHITE | V2 pin 4 (S) | UL screen tap of V2 |

**Twist the blue/green pair together** before routing — minimizes loop area and reduces hum coupling.

**Twist the blue-white/green-white pair together** for the same reason.

Note the polarity: each EL-34's plate (pin 3) and its own screen tap (pin 4) are wired together pairwise — BLUE goes with GREEN (to the same EL-34), and BLUE/WHITE goes with GREEN/WHITE (to the other EL-34). Don't cross-wire (e.g. BLUE plate to GREEN/WHITE screen) — that would put the screens at the wrong potential.

#### Step 14: Left OPT primary to V6 and V7

Mirror of step 13, but on the left channel:

| Lead | Goes to | Function |
|---|---|---|
| BLUE | V6 pin 3 (S) | Plate of V6 |
| GREEN | V6 pin 4 | UL screen tap of V6 |
| BLUE/WHITE | V7 pin 3 (S) | Plate of V7 |
| GREEN/WHITE | V7 pin 4 (S) | UL screen tap of V7 |

After steps 13 and 14, all four EL-34s have their plates and screens connected to the A-470 primaries.

### Step 15 — Two 0.02 µF disc capacitors on 7-lug strip

Two ceramic disc caps go from lug 6 of the seven-lug strip to lugs 5 and 7 respectively. **What they're for:** they bypass any RF or high-frequency junk that might appear on the heater CTs (lugs 5 and 7) to a common ground reference (lug 6, which is wired to chassis ground a few steps later). Ceramic discs are cheap and perfectly adequate for RF bypass duty.

### Steps 16-17 — Heater daisy-chains

EL-34s V2 and V3 share a heater string; V6 and V7 share another. **Step 16** runs a twisted pair (6" total, with 1.5" stripped at each end) between V7 pins 2 & 7 and V6 pins 2 & 7. **Step 17** repeats for V2 and V3.

The 6GH8A heaters get their power from the PC-3A board's daisy-chain off these EL-34 heater strings — that wiring lands later (steps 45-46).

### Steps 18-28 — Bias network on the seven-lug terminal strip

This is where the seven-lug strip becomes the heart of the bias supply. A lot of components land here in sequence.

| Step | Component / wire | From | To |
|---|---|---|---|
| 18 | 5" jumper wire | 7-lug lug 1 | 7-lug lug 6 |
| 19 | 100 µF cap | (−) to lug 4 | (+) to lug 1 |
| 20 | 10 kΩ resistor | lug 4 | lug 3 |
| 21 | 100 µF cap | (−) to lug 3 | (+) to lug 1 |
| 22 | 10 kΩ resistor | lug 2 | lug 1 (S) |
| 23 | 6" wire | lug 6 (S) | ground lug near filter cap |
| 24 | 6" wire | lug 3 (S) | lug 1 of left bias pot |
| 25 | 6" wire | lug 4 (S) | non-banded side of bias diode |
| 26 | 8" wire | lug 2 (S) | lug 3 of left bias control |
| 27 | 3" wire | lug 3 of right bias pot (S) | lug 3 of left bias pot (S) |
| 28 | 3" wire | lug 1 of right bias pot (S) | lug 1 of left bias pot (S) |

**What the bias network does**: the 55 V AC bias winding from the PA-060 (RED/BLK lead, wired to the diode in step 1) becomes pulsing DC after the diode. The two 100 µF caps + two 10 kΩ resistors on the seven-lug strip filter this into smooth −65 V DC, then distribute it to the bias pots via the inter-pot jumpers in steps 27 and 28.

By step 28, you have:

- A clean −65 V DC bias supply.
- Connected to both bias pots in parallel.
- The pots' wipers will eventually drive the EL-34 grids (via the PC-3 board wiring and the 1 kΩ grid stoppers from step 37).

### Steps 29-30 — B+ chain extension

#### Step 29: Rectifier output to first filter cap

A 5¼" wire from V1 pin 8 (GZ-34 cathode = rectifier output) to filter cap lug 2 (S). This completes the high-current path: the GZ-34 rectifies the 720 VAC HV winding into pulsing DC, and that DC lands at the first filter cap section (lug 2 = "lug D" in the voltage table = 435 V DC at idle).

#### Step 30: 6.8 kΩ dropping resistor between cap lugs 1 and 4

Trim the resistor leads to 1". One end at filter cap lug 1, other end at filter cap lug 4. This drops the B+ from lug C (415 V) down to lug B (375 V) — feeding the screen and driver stages.

### Steps 31-36 — Cathode sense network

#### Step 31: 15.6 Ω resistor at V2 socket

Connects from V2's chassis ground lug (the socket's mounting nut bond) to V2 pin 8 (cathode). This is the **stock bias-sense resistor** for the channel B pair (V2 + V3 cathodes will share this resistor after step 32 daisies them together).

#### Step 32: V2-V3 cathode daisy

A 5" wire (½" stripped at each end) through V2 pin 1 to V2 pin 8 (S), continuing through V3 pin 8 to V3 pin 1. After this step, the cathodes of V2 and V3 are tied together — and both share the same 15.6 Ω sense resistor to ground.

#### Step 33: V3 pin 1 to LEFT Biaset socket pin 8

A 4½" wire from V3 pin 1 (S) to pin 8 of the left preamp power take-off socket (V4) (S). This is the wire that brings the bias-measurement voltage out to the front-panel Biaset socket where you can probe it with a meter.

#### Step 34: 15.6 Ω resistor at V7 socket

Mirror of step 31 — connects from V7's ground lug to V7 pin 8. Cathode sense for channel A (V6 + V7).

#### Step 35: V7-V6 cathode daisy

Mirror of step 32 — daisy-chains V6 and V7 cathodes through pins 1 and 8.

#### Step 36: V6 pin 8 to RIGHT Biaset socket pin 8

Mirror of step 33 — wires the channel A bias measurement to V5 (right Biaset socket) pin 8.

After these six steps, **bias measurement is now possible** via the front-panel sockets. See [bias adjustment](../../bring-up/bias-adjustment.md) for the procedure.

### Step 37 — Four 1 kΩ grid stoppers

Each EL-34 gets a 1 kΩ "grid stopper" resistor between its pin 5 (control grid) and pin 6 (which is connected to the cathodyne output from the driver tube via a coupling cap on the PC-3 board, wired in later steps).

Keep the resistor pigtails **short** (about ½") and mount the resistor body close to the tube socket. Long leads here can pick up RF.

**Why grid stoppers**: pentodes and beam tetrodes can oscillate at very high frequencies (10s of MHz) due to internal capacitances. A small series resistor at the grid (= a low-pass filter with the tube's grid capacitance) kills high-frequency feedback paths and prevents oscillation. The resistor doesn't affect audio frequencies (the audio coupling cap above it has much higher impedance at audio than the 1 kΩ has).

## After step 37 — what's left

By the end of step 37, the output stage is **electrically complete** — you could install tubes and run signal into V2/V3/V6/V7 grid stoppers directly to test (though it's not practical because there's no driver tube to amplify a phono-level signal up to grid-drive voltage).

The remaining 28 steps (38-65) build the **driver stage**: mounting the PC-3A board, wiring its eyelets to the tube sockets, and finalising the power cord installation. See [driver stage](../driver-stage/index.md).

## See also

- [Power supply wiring (steps 1-11)](../power-supply/index.md) — what comes before this
- [Driver stage wiring (steps 38-65)](../driver-stage/index.md) — what comes after
- [A-470 output transformer](../../components/a-470-output-transformer.md) — the OPT primary lead colors and roles
- [Seven-lug terminal strip](../../components/seven-lug-terminal-strip.md) — the bias-network home
- [Bias adjustment](../../bring-up/bias-adjustment.md) — what step 33/36 enables
- [EL34 output tube](../../components/el34-output-tube.md) — what the output stage is built around
