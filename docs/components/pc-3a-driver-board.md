---
title: PC-3A driver board
---

# PC-3A driver board

The PC-3A is the ST-70's small printed circuit board that holds the [6GH8A driver tubes](6gh8a-driver-tube.md) (V4 and V5) and the associated voltage amplification and phase-splitting circuitry that drives the [EL34 output stage](el34-output-tube.md).

*Page to be written.* Planned coverage:

- What's on the board: tube sockets, resistors, coupling caps, screen feed network.
- How the two 6GH8A halves work together to amplify the input and produce push-pull drive.
- Why Dynaco moved to a PCB here (cost, consistency, ease of assembly) when the rest of the amp is point-to-point.
- Version A vs. Version B PCBs (the 6GH8A version is "Version B" in some references).
- The schematic — to be embedded as an image and explained section by section.
- Failure modes:
  - Cracked solder joints from decades of thermal cycling
  - Drifted resistors
  - Aged coupling caps (the #1 failure point on old PC-3As)
- The "rebuild" workflow: every original PC-3A benefits from a parts replacement pass.
- The VTA upgrade alternative: replaces the whole board with a long-tail-pair design.

## See also

- [6GH8A driver tube](6gh8a-driver-tube.md)
- [Phase splitting](../theory/phase-splitting.md)
- [Feedback](../theory/feedback.md) — the global feedback loop terminates near this board
