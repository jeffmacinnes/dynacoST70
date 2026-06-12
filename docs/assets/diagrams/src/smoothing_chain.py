"""Smoothing chain: what each stage of the B+ filter does to the waveform.

Stage 1 — rectified output from 5AR4 (full-wave pulses, 120 Hz)
Stage 2 — after first filter cap (large sawtooth ripple riding on DC)
Stage 3 — after the choke (ripple smaller, more sinusoidal)
Stage 4 — after second filter cap (ripple essentially gone — clean B+)

Voltages are the actual ST-70 values: rectified pulses peak at ~480 V (the
720 V CT secondary gives ±360 V per half-winding RMS, ~509 V peak, minus
the 5AR4's drop). The raw rail settles at ~435 V (cap lug 2); the choke
drops ~20 V, so the rail after the choke (cap lug 1) is ~415 V.

Stage 2 uses a charge/discharge cap model (cap follows rising input, droops
linearly between pulses under load) — that's how a real filter cap works,
NOT what a linear low-pass gives you. Stages 3 and 4 use IIR low-pass to
approximate the further smoothing.

Outputs: docs/assets/diagrams/smoothing-chain.svg
"""

import numpy as np
import matplotlib.pyplot as plt

from _style import (
    apply_rcparams,
    output_dir,
    COLOR_TEXT,
    COLOR_NOTE,
    COLOR_RECTIFIED,
    COLOR_ZERO,
)


# --- ST-70 voltages (approximate) ---
V_PEAK = 480.0       # peak rectified voltage at 5AR4 cathode
V_RAW = 435.0        # raw rail at the first filter cap (lug 2)
CHOKE_DROP = 20.0    # DC drop across the choke's winding resistance
V_BPLUS = V_RAW - CHOKE_DROP   # ~415 V — B+ rail after the choke (lug 1)
V_YMAX = 520.0       # y-axis top (V_peak + headroom)


def lowpass(x: np.ndarray, alpha: float, y0: float | None = None) -> np.ndarray:
    """First-order IIR low-pass: y[n] = y[n-1] + alpha · (x[n] - y[n-1]).

    If `y0` is provided, the filter is pre-initialised to that value so
    its output starts at steady-state instead of settling from zero.
    """
    y = np.empty_like(x)
    y[0] = x[0] if y0 is None else y0
    for n in range(1, len(x)):
        y[n] = y[n - 1] + alpha * (x[n] - y[n - 1])
    return y


def cap_filter(signal: np.ndarray, droop_per_sample: float, y0: float) -> np.ndarray:
    """Reservoir-cap behaviour: cap follows the input when input is rising
    above the cap voltage (diode forward-biased, cap charges to input);
    cap discharges linearly at `droop_per_sample` volts when input is
    below cap voltage (diode reverse-biased, cap discharges through load).
    """
    y = np.empty_like(signal)
    y[0] = y0
    for n in range(1, len(signal)):
        if signal[n] >= y[n - 1]:
            y[n] = signal[n]
        else:
            y[n] = y[n - 1] - droop_per_sample
    return y


def build():
    apply_rcparams()

    # --- Source waveform: full-wave rectified at 60 Hz mains ---
    freq = 60.0
    cycles = 4
    period = 1.0 / freq
    n_samples = 4000
    t = np.linspace(0.0, cycles * period, n_samples)

    # Stage 1: rectified pulses 0 → V_PEAK
    stage1 = V_PEAK * np.abs(np.sin(2.0 * np.pi * freq * t))

    # Stage 2: first filter cap. Real ST-70 droop is small (~5 V per half-
    # cycle); we exaggerate to ~100 V so the sawtooth ripple is clearly
    # visible AND there's enough ripple left for stages 3-4 to smooth.
    samples_per_half_cycle = n_samples / (cycles * 2)
    droop_v = 100.0
    stage2 = cap_filter(stage1, droop_v / samples_per_half_cycle, y0=V_PEAK - droop_v / 2)

    # Stages 3 + 4: progressive low-pass filtering (choke + second cap).
    # Pre-init at the average of stage 2 so we see steady-state output.
    # The choke's winding resistance also drops ~20 V of DC, so stages
    # 3 and 4 sit at ~415 V instead of the ~435 V raw rail.
    settled = stage2[n_samples // 2:].mean()
    stage3 = lowpass(stage2, alpha=0.010,  y0=settled) - CHOKE_DROP
    stage4 = lowpass(stage3, alpha=0.0015, y0=settled - CHOKE_DROP)

    panels = [
        ("1 · Rectified output (cathode of 5AR4)",
         "120 Hz pulse train. Voltage swings between 0 V and V_peak (~480 V) on every half-cycle.",
         stage1, V_RAW, "435 V (raw)"),
        ("2 · After the first filter cap",
         "Cap charges to V_peak on each pulse, then droops linearly through the load between pulses. Sawtooth ripple on a near-DC level (~435 V).",
         stage2, V_RAW, "435 V (raw)"),
        ("3 · After the choke",
         "Inductor resists current changes. Ripple is much smaller and more sinusoidal; the choke's resistance also drops ~20 V of DC.",
         stage3, V_BPLUS, "415 V (B+)"),
        ("4 · After the second filter cap (final B+)",
         "Essentially flat B+ at ~415 V. Any remaining ripple is well below the noise floor of any decent amp.",
         stage4, V_BPLUS, "415 V (B+)"),
    ]

    # --- Figure ---
    fig, axes = plt.subplots(
        4, 1,
        figsize=(11.0, 12.0),
        sharex=True,
    )
    fig.subplots_adjust(
        top=0.88, bottom=0.07, left=0.09, right=0.96,
        hspace=1.15,
    )

    for ax, (title, note, signal, level, level_label) in zip(axes, panels):
        ax.plot(t, signal, color=COLOR_RECTIFIED, linewidth=2.4)
        _panel_chrome(ax, t, cycles, period, title=title, note=note,
                      level=level, level_label=level_label)

    # --- Title + subtitle (top) ---
    fig.text(
        0.5, 0.972,
        "Smoothing chain — what each filter stage removes",
        ha="center", fontsize=20, fontweight="bold", color=COLOR_TEXT,
    )
    fig.text(
        0.5, 0.950,
        "Approximate ST-70 voltages. Ripple amplitudes are exaggerated so the shape of each stage is clearly visible.",
        ha="center", fontsize=12, color=COLOR_NOTE,
    )

    fig.text(
        0.5, 0.035,
        "ST-70 chain: 5AR4 cathode → first filter cap → choke → second filter cap → tube plates.",
        ha="center", fontsize=11, style="italic", color="#555",
    )
    fig.text(
        0.5, 0.015,
        "Real ST-70 first-cap droop is ~5–10 V (not 100 V as shown); B+ ripple at the tube plates is under 1 V.",
        ha="center", fontsize=10, style="italic", color="#777",
    )

    out_path = output_dir() / "smoothing-chain.svg"
    fig.savefig(out_path, format="svg", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out_path}")


def _panel_chrome(ax, t, cycles, period, *, title, note, level, level_label):
    # 0 V reference line — always shown, since panel 1 reaches it.
    ax.axhline(0.0, color="#aaaaaa", linewidth=1.0)

    # Y axis: just two ticks — 0 V and the rail level for this panel
    # (435 V raw before the choke, 415 V B+ after it). V_peak is
    # implicit from the panel-1 pulse tops.
    ax.set_yticks([0.0, level])
    ax.set_yticklabels(["0 V", level_label], fontsize=11, color=COLOR_NOTE)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.set_xticks([])
    ax.set_ylim(-30.0, V_YMAX)
    ax.set_xlim(-0.01 * period, cycles * period + 0.16 * period)

    # Faint reference line at the rail level so the eye can see where the
    # filtered output settles vs. where the pulses peak.
    ax.axhline(level, color="#cccccc", linewidth=0.8, linestyle=(0, (4, 3)))

    ax.annotate(
        "time →",
        xy=(cycles * period + 0.04 * period, level),
        fontsize=11, color=COLOR_NOTE, va="center",
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    ax.set_title(
        title,
        loc="left", fontsize=14, fontweight="bold", color=COLOR_TEXT,
        pad=28,
    )
    ax.text(
        0.0, V_PEAK + 30, note,
        fontsize=11, style="italic", color=COLOR_NOTE,
        transform=ax.transData,
    )


if __name__ == "__main__":
    build()
