"""Three-panel rectification waveform diagram.

Panel 1: AC input from the transformer secondary (raw sine).
Panel 2: After ONE diode — half-wave rectified. Negative halves shown
         as dashed ghost in red.
Panel 3: After TWO diodes (5AR4 dual anode) — full-wave rectified.

Outputs: docs/assets/diagrams/rectification-waveforms.svg
"""

import numpy as np
import matplotlib.pyplot as plt

from _style import (
    apply_rcparams,
    output_dir,
    COLOR_AC,
    COLOR_RECTIFIED,
    COLOR_GHOST,
    COLOR_ANODE,
    COLOR_NOTE,
    COLOR_FAINT,
    COLOR_TEXT,
    COLOR_ZERO,
)


def build():
    apply_rcparams()

    # --- Waveform math ---
    amplitude = 1.0
    freq = 60.0                       # Hz (mains)
    cycles = 4
    period = 1.0 / freq
    t = np.linspace(0.0, cycles * period, 2000)

    ac = amplitude * np.sin(2.0 * np.pi * freq * t)
    half_wave = np.maximum(ac, 0.0)
    half_wave_blocked = np.minimum(ac, 0.0)       # what got removed
    full_wave = np.abs(ac)

    # --- Figure ---
    # Layout budget (figure-fraction coords):
    #   top 12% : title + subtitle
    #   middle  : 3 stacked panels with hspace
    #   bottom 5%: footer text
    fig, axes = plt.subplots(
        3, 1,
        figsize=(11.0, 8.6),
        sharex=True,
    )
    fig.subplots_adjust(
        top=0.88, bottom=0.08, left=0.07, right=0.96,
        hspace=0.95,
    )

    # ---- Panel 1: AC input ----
    ax = axes[0]
    ax.plot(t, ac, color=COLOR_AC, linewidth=2.6)
    _panel_chrome(
        ax, t, amplitude, cycles, period,
        title="1 · AC input from the transformer secondary",
        note="60 Hz sine wave, swinging ±V relative to the center tap",
    )

    # ---- Panel 2: Half-wave rectified ----
    ax = axes[1]
    ax.plot(
        t, half_wave_blocked,
        color=COLOR_GHOST, linewidth=1.6,
        linestyle=(0, (5, 3)), alpha=0.55,
    )
    ax.plot(t, half_wave, color=COLOR_RECTIFIED, linewidth=2.6)
    _panel_chrome(
        ax, t, amplitude, cycles, period,
        title="2 · After ONE diode (half-wave rectified)",
        note="Negative halves blocked. Unidirectional but bumpy.",
    )
    ax.text(
        2.6 * period, -1.55 * amplitude,
        "negative halves BLOCKED (would have looked like this ↑)",
        fontsize=11, color=COLOR_GHOST,
    )

    # ---- Panel 3: Full-wave rectified ----
    ax = axes[2]
    ax.plot(t, full_wave, color=COLOR_RECTIFIED, linewidth=2.6)
    _panel_chrome(
        ax, t, amplitude, cycles, period,
        title="3 · After TWO diodes — the 5AR4 (full-wave rectified)",
        note="Both halves used. 120 Hz pulse train — twice the input frequency, no flat gaps.",
    )
    # Anode labels under each pulse (2 pulses per AC cycle × 4 cycles = 8 pulses)
    for i in range(2 * cycles):
        anode = "anode 1" if i % 2 == 0 else "anode 2"
        x_center = (i + 0.5) * (period / 2.0)
        ax.text(
            x_center, -1.45 * amplitude, anode,
            ha="center", fontsize=11, color=COLOR_ANODE,
        )

    # ---- Title + subtitle (top) and footer ----
    # Both use fig.text in figure-fraction coords so they sit predictably
    # in the space reserved by subplots_adjust(top=0.88).
    fig.text(
        0.5, 0.955,
        "Rectification — waveforms at each stage",
        ha="center", fontsize=20, fontweight="bold", color=COLOR_TEXT,
    )
    fig.text(
        0.5, 0.918,
        "What the AC looks like before the diodes, after one diode, and after both (5AR4 dual anode)",
        ha="center", fontsize=12, color=COLOR_NOTE,
    )

    fig.text(
        0.5, 0.040,
        "From AC input to pulsating DC. After this, the filter cap and choke smooth panel 3’s pulses "
        "into the ~435 V B+ rail.",
        ha="center", fontsize=11, style="italic", color="#555",
    )
    fig.text(
        0.5, 0.018,
        "In the ST-70, panel 3 is the actual waveform at the 5AR4’s cathode (pin 8) before the filter network downstream.",
        ha="center", fontsize=11, style="italic", color="#555",
    )

    # ---- Save ----
    # Don't use bbox_inches="tight" — we want the explicit layout we set above
    # so figure-fraction coords for the title/subtitle/footer behave predictably.
    out_path = output_dir() / "rectification-waveforms.svg"
    fig.savefig(out_path, format="svg", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out_path}")


def _panel_chrome(ax, t, amplitude, cycles, period, *, title, note):
    """Common per-panel styling: zero line, y-tick labels, x-extent, title/note."""
    ax.axhline(0, color=COLOR_ZERO, linewidth=1.0, linestyle=(0, (4, 3)))

    # Y axis: ±V / 0 ticks
    ax.set_yticks([-amplitude, 0.0, amplitude])
    ax.set_yticklabels(["−V", "0", "+V"], fontsize=11, color=COLOR_NOTE)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.set_xticks([])
    ax.set_ylim(-1.7 * amplitude, 1.7 * amplitude)

    # Some right-side breathing room for the "time →" arrow
    ax.set_xlim(-0.02 * period, cycles * period + 0.18 * period)

    # Time arrow at the right end of the zero line
    ax.annotate(
        "time →",
        xy=(cycles * period + 0.05 * period, 0),
        xytext=(cycles * period + 0.05 * period, 0),
        fontsize=11, color=COLOR_NOTE, va="center",
    )

    # Title + italic note above the axes, left-aligned.
    # `pad` is smaller now because subplots_adjust(top=0.88) gave us room.
    ax.set_title(
        title,
        loc="left", fontsize=14, fontweight="bold", color=COLOR_TEXT,
        pad=10,
    )
    # Italic subtitle sits just under the panel title.
    ax.text(
        0.0, 1.20 * amplitude, note,
        fontsize=11, style="italic", color=COLOR_NOTE,
        transform=ax.transData,
    )


if __name__ == "__main__":
    build()
