"""Two sine waves 180° out of phase — the top and bottom RED leads of the
PA-060 HV secondary, measured relative to the RED/YEL center tap.

The pedagogical point: at every instant, one end is exactly the negative of
the other. That's what makes the two 5AR4 anodes take turns conducting —
whichever lead is positive at the moment drives the corresponding anode.

This same 180°-across-a-CT relationship reappears in phase splitters and
push-pull output transformers.

Outputs: docs/assets/diagrams/phase-180-degrees.svg
"""

import numpy as np
import matplotlib.pyplot as plt

from _style import (
    apply_rcparams,
    output_dir,
    COLOR_TEXT,
    COLOR_NOTE,
    COLOR_ZERO,
    COLOR_ANODE,
)

# Two visually distinct colours — both are RED leads physically, but we
# need to tell them apart on the plot.
COLOR_TOP = "#cc3a2a"
COLOR_BOT = "#1a4e8a"
COLOR_BAND_TOP = "#cc3a2a"
COLOR_BAND_BOT = "#1a4e8a"


def build():
    apply_rcparams()

    amplitude = 1.0           # ±A (normalised; in the ST-70 this is ~360 V)
    freq = 60.0
    cycles = 2
    period = 1.0 / freq
    t = np.linspace(0.0, cycles * period, 1500)

    top = amplitude * np.sin(2.0 * np.pi * freq * t)
    bot = -top                # exactly 180° out of phase

    fig = plt.figure(figsize=(11.0, 7.0))
    fig.subplots_adjust(top=0.80, bottom=0.18, left=0.07, right=0.94)
    ax = fig.add_subplot(111)

    # ---- Shaded bands showing which anode conducts at each instant ----
    # Top anode conducts when top > 0 (and bottom < 0); vice versa.
    ax.fill_between(
        t, -1.7 * amplitude, 1.7 * amplitude,
        where=(top > 0), step=None, alpha=0.07, color=COLOR_BAND_TOP,
        linewidth=0,
    )
    ax.fill_between(
        t, -1.7 * amplitude, 1.7 * amplitude,
        where=(bot > 0), step=None, alpha=0.07, color=COLOR_BAND_BOT,
        linewidth=0,
    )

    # ---- Waveforms ----
    ax.plot(t, top, color=COLOR_TOP, linewidth=2.6,
            label="Top RED end (relative to CT)")
    ax.plot(t, bot, color=COLOR_BOT, linewidth=2.6,
            label="Bottom RED end (relative to CT)")

    # ---- Zero line (the CT itself). y-tick label already calls this out
    # as "0 (CT)", so we don't need a redundant right-side label that would
    # sit on top of the waveform. ----
    ax.axhline(0, color=COLOR_ZERO, linewidth=1.2, linestyle=(0, (4, 3)))

    # ---- Annotations for which anode conducts ----
    # Centre of first positive half of "top"
    ax.text(
        period * 0.25, 1.45 * amplitude,
        "Anode 1 conducts",
        ha="center", fontsize=11, color=COLOR_TOP, fontweight="bold",
    )
    ax.text(
        period * 0.75, 1.45 * amplitude,
        "Anode 2 conducts",
        ha="center", fontsize=11, color=COLOR_BOT, fontweight="bold",
    )
    ax.text(
        period * 1.25, 1.45 * amplitude,
        "Anode 1 conducts",
        ha="center", fontsize=11, color=COLOR_TOP, fontweight="bold",
    )
    ax.text(
        period * 1.75, 1.45 * amplitude,
        "Anode 2 conducts",
        ha="center", fontsize=11, color=COLOR_BOT, fontweight="bold",
    )

    # ---- Axes styling ----
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_yticks([-amplitude, 0.0, amplitude])
    ax.set_yticklabels(["−V", "0 (CT)", "+V"], fontsize=11, color=COLOR_NOTE)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.set_xticks([])
    ax.set_ylim(-1.7 * amplitude, 1.7 * amplitude)
    ax.set_xlim(-0.01 * period, cycles * period + 0.02 * period)

    # ---- Legend (above the footer text, below the axes) ----
    leg = ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, -0.20),
        ncol=2, frameon=False, fontsize=11,
    )
    for text in leg.get_texts():
        text.set_color(COLOR_TEXT)

    # ---- Title + subtitle ----
    fig.text(
        0.5, 0.945,
        "180° phase relationship across a center-tapped winding",
        ha="center", fontsize=20, fontweight="bold", color=COLOR_TEXT,
    )
    fig.text(
        0.5, 0.905,
        "Two ends of a CT winding are exact mirror images relative to the CT — when one is +V, the other is −V.",
        ha="center", fontsize=12, color=COLOR_NOTE,
    )

    fig.text(
        0.5, 0.040,
        "Whichever lead is positive drives its 5AR4 anode into conduction.",
        ha="center", fontsize=11, style="italic", color="#555",
    )
    fig.text(
        0.5, 0.020,
        "The same trick reappears in phase splitters and push-pull output transformers.",
        ha="center", fontsize=11, style="italic", color="#555",
    )

    out_path = output_dir() / "phase-180-degrees.svg"
    fig.savefig(out_path, format="svg", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    build()
