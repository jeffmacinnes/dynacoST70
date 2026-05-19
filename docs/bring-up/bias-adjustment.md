---
title: Bias adjustment
---

# Bias adjustment

*Page to be written.* Planned coverage:

- What bias is, mechanically: the negative DC voltage on the EL34 control grid that sets idle plate current.
- Target bias point: typically ~50mA per [EL34](../components/el34-output-tube.md) for ST-70 operating conditions. Verify against your tubes' specs.
- The measurement method (using the [individual bias pots mod](../modifications/individual-bias-pots.md) and cathode resistors):
  - Measure DC voltage across each tube's cathode resistor.
  - Apply Ohm's law: I_cathode = V_measured / R_cathode.
  - Adjust the corresponding trimmer until I_cathode hits the target.
- Why we set bias *cold* (just after warm-up) vs. *hot* (after an hour of operation) — the second answer is more accurate to long-term operation.
- The "creeping bias" failure mode: if bias drifts over the course of an hour, the tube is dying.
- Re-checking bias every few months, or after any tube change.
- What the four trimmers' relative positions tell you about your tubes' match.

## See also

- [Individual bias pots](../modifications/individual-bias-pots.md) — the mod that enables this procedure
- [EL34 output tube](../components/el34-output-tube.md)
- [Multimeter — bias measurement](../test-equipment/multimeter.md#working-around-the-missing-functions)
