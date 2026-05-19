"""Smoothing chain: what each stage of the B+ filter does to the waveform.

Stage 1 — rectified output from 5AR4 (full-wave pulses, 120 Hz)
Stage 2 — after first filter cap (large sawtooth ripple riding on DC)
Stage 3 — after the choke (ripple smaller, more sinusoidal)
Stage 4 — after second filter cap (ripple essentially gone — clean B+)

The filtering is modelled by a first-order IIR low-pass (one for each
energy-storage element). The alphas are hand-tuned so each successive
stage looks visibly cleaner — exact ST-70 numbers aren't the point;
the *shape change* across stages is.

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


def lowpass(x: np.ndarray, alpha: float) -> np.ndarray:
    """First-order IIR low-pass: y[n] = y[n-1] + alpha · (x[n] - y[n-1])."""
    y = np.empty_like(x)
    y[0] = x[0]
    for n in range(1, len(x)):
        y[n] = y[n - 1] + alpha * (x[n] - y[n - 1])
    return y


def build():
    apply_rcparams()

    # --- Source waveform: full-wave rectified at 60 Hz mains ---
    amplitude = 1.0
    freq = 60.0
    cycles = 4
    period = 1.0 / freq
    n_samples = 4000
    t = np.linspace(0.0, cycles * period, n_samples)
    full_wave = amplitude * np.abs(np.sin(2.0 * np.pi * freq * t))

    # --- Filtering stages ---
    # alphas tuned so the visible ripple shrinks roughly as
    #   stage 2: ~25 % p-p ripple
    #   stage 3: ~6 %  p-p ripple
    #   stage 4: ~1 %  p-p ripple
    stage2 = lowpass(full_wave, alpha=0.040)
    stage3 = lowpass(stage2,    alpha=0.014)
    stage4 = lowpass(stage3,    alpha=0.006)

    # Each stage settles to a DC mean — we'll plot each panel relative
    # to its own mean (after a settling time) so the ripple is centred
    # and easy to read. The ABSOLUTE DC level is the same idea everywhere;
    # the visible *ripple* is the pedagogical point.
    settled = n_samples // 2  # ignore initial transient
    means = [
        full_wave[settled:].mean(),
        stage2[settled:].mean(),
        stage3[settled:].mean(),
        stage4[settled:].mean(),
    ]

    panels = [
        ("1 · Rectified output (cathode of 5AR4)",
         "120 Hz pulse train. Peak-to-peak swing is the full rectified amplitude.",
         full_wave, means[0]),
        ("2 · After the first filter cap",
         "Cap charges on each pulse, discharges through the load between pulses. ~20–30 % p-p ripple.",
         stage2, means[1]),
        ("3 · After the choke",
         "The choke (inductor) resists current changes. Ripple is much smaller and more sinusoidal.",
         stage3, means[2]),
        ("4 · After the second filter cap (final B+)",
         "Essentially flat DC. Audible hum at this point is well below the noise floor of any decent amp.",
         stage4, means[3]),
    ]

    # --- Figure ---
    # Taller figure so 4 panels each have room for: panel title (14 px) +
    # italic note (11 px) + ~12 px gap + plot area. hspace=1.3 means the
    # vertical gap between adjacent axes is 130 % of one axes' height,
    # which is what it takes to fit the title+note in that gap.
    fig, axes = plt.subplots(
        4, 1,
        figsize=(11.0, 12.0),
        sharex=True,
    )
    fig.subplots_adjust(
        top=0.88, bottom=0.07, left=0.07, right=0.96,
        hspace=1.15,
    )

    # We normalise every panel to the same y-range relative to its own
    # mean, so the *shape* of the ripple is comparable. The y-axis label
    # makes the framing clear: "deviation from the DC level".
    yrange = 1.2 * amplitude   # roomy enough for stage 1's full swing

    for ax, (title, note, signal, mean) in zip(axes, panels):
        deviation = signal - mean
        ax.plot(t, deviation, color=COLOR_RECTIFIED, linewidth=2.4)
        _panel_chrome(ax, t, cycles, period, yrange, title=title, note=note)

    # --- Title + subtitle (top) ---
    fig.text(
        0.5, 0.972,
        "Smoothing chain — what each filter stage removes",
        ha="center", fontsize=20, fontweight="bold", color=COLOR_TEXT,
    )
    fig.text(
        0.5, 0.950,
        "Y axis: voltage deviation from each panel's DC mean. Compare panel 1 to panel 4.",
        ha="center", fontsize=12, color=COLOR_NOTE,
    )

    fig.text(
        0.5, 0.020,
        "ST-70 chain: 5AR4 cathode → first filter cap → choke → second filter cap → tube plates.",
        ha="center", fontsize=11, style="italic", color="#555",
    )

    out_path = output_dir() / "smoothing-chain.svg"
    fig.savefig(out_path, format="svg", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out_path}")


def _panel_chrome(ax, t, cycles, period, yrange, *, title, note):
    ax.axhline(0, color=COLOR_ZERO, linewidth=1.0, linestyle=(0, (4, 3)))
    ax.set_yticks([-yrange / 2, 0.0, yrange / 2])
    ax.set_yticklabels(["−Δ", "DC level", "+Δ"], fontsize=11, color=COLOR_NOTE)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.set_xticks([])
    ax.set_ylim(-yrange, yrange)
    ax.set_xlim(-0.01 * period, cycles * period + 0.16 * period)

    ax.annotate(
        "time →",
        xy=(cycles * period + 0.04 * period, 0),
        fontsize=11, color=COLOR_NOTE, va="center",
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    # Panel title sits 26 pt above the axes spine; italic note sits between
    # the title and the axes top, in data coords above the +Δ line.
    ax.set_title(
        title,
        loc="left", fontsize=14, fontweight="bold", color=COLOR_TEXT,
        pad=28,
    )
    ax.text(
        0.0, 1.20 * yrange, note,
        fontsize=11, style="italic", color=COLOR_NOTE,
        transform=ax.transData,
    )


if __name__ == "__main__":
    build()
