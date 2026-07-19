"""Heater center-tap-to-ground comparison.

Panel A — floating heater winding:
   • The two heater leads carry ±3.15 V at 60 Hz.
   • Their midpoint is NOT tied to ground, so the whole pair drifts
     (slow noise / mains pickup / capacitive coupling).
   • Capacitive coupling into nearby signal wiring sees a wandering
     reference → audible 60 Hz hum.

Panel B — CT grounded:
   • CT tied to chassis / signal ground → midpoint locked at 0 V.
   • The two leads swing symmetrically ±3.15 V around 0 V.
   • Any voltage induced into nearby signal wiring is balanced
     (+ and − halves cancel) → no hum coupling.

Outputs: docs/assets/diagrams/heater-ct-comparison.svg
"""

import numpy as np
import matplotlib.pyplot as plt

from _style import (
    apply_rcparams,
    output_dir,
    COLOR_TEXT,
    COLOR_NOTE,
    COLOR_ZERO,
)

# Two heater leads — physically both green (or both brown), but we
# need them distinguishable on the plot.
COLOR_LEAD_A = "#2a8c3a"     # darker (lead 1)
COLOR_LEAD_B = "#5fb04f"     # lighter (lead 2)
COLOR_MIDPT  = "#b8851a"     # the implicit / explicit center-tap voltage
COLOR_GROUND = "#444"


def build():
    apply_rcparams()

    # --- Heater waveform parameters ---
    amplitude = 3.15            # heater half-amplitude (V), labelled but unitless on plot
    freq = 60.0
    cycles = 3
    period = 1.0 / freq
    t = np.linspace(0.0, cycles * period, 2000)
    heater_signal = amplitude * np.sin(2.0 * np.pi * freq * t)

    # --- Floating midpoint: a slow wandering noise component ---
    rng = np.random.default_rng(42)   # deterministic for reproducible builds
    # Sum a few low-frequency sinusoids + a tiny bit of noise to look like
    # "stray pickup" — visibly drifting on the timescale of a few cycles.
    # Amplitudes capped at < 1.0 V combined so the drifted heater waveform
    # stays inside the visible plot area below the panel's italic note.
    drift = (
        0.45 * np.sin(2.0 * np.pi * 7.0 * t + 0.6)
        + 0.25 * np.sin(2.0 * np.pi * 13.0 * t + 1.4)
        + 0.15 * np.sin(2.0 * np.pi * 23.0 * t + 2.1)
    )
    drift += 0.08 * rng.standard_normal(t.size)

    # ---- Figure: two stacked panels ----
    fig, (ax_a, ax_b) = plt.subplots(
        2, 1, figsize=(11.0, 8.6), sharex=True,
    )
    fig.subplots_adjust(
        top=0.80, bottom=0.10, left=0.07, right=0.96,
        hspace=1.05,
    )

    # ============ PANEL A: FLOATING ============
    lead_a1 = drift + heater_signal
    lead_a2 = drift - heater_signal

    # Heater leads (the two ends of the winding)
    ax_a.plot(t, lead_a1, color=COLOR_LEAD_A, linewidth=2.4, label="Heater lead 1")
    ax_a.plot(t, lead_a2, color=COLOR_LEAD_B, linewidth=2.4, label="Heater lead 2")
    # The wandering midpoint
    ax_a.plot(t, drift, color=COLOR_MIDPT, linewidth=2.0,
              linestyle=(0, (5, 3)), label="Midpoint (wandering — picks up stray noise)")

    _panel_chrome(
        ax_a, t, cycles, period, amplitude,
        title="A · Floating winding — no CT-to-ground connection",
        note="The two leads swing ±3.15 V around an undefined midpoint that drifts. Capacitive coupling into the signal path → 60 Hz hum.",
        with_ground=False,
    )

    # ============ PANEL B: CT GROUNDED ============
    lead_b1 =  heater_signal
    lead_b2 = -heater_signal

    ax_b.plot(t, lead_b1, color=COLOR_LEAD_A, linewidth=2.4, label="Heater lead 1")
    ax_b.plot(t, lead_b2, color=COLOR_LEAD_B, linewidth=2.4, label="Heater lead 2")
    # The (now grounded) midpoint = 0 V
    ax_b.plot(t, np.zeros_like(t), color=COLOR_MIDPT, linewidth=2.0,
              linestyle=(0, (5, 3)),
              label="Midpoint = CT (tied to 0 V ground)")

    _panel_chrome(
        ax_b, t, cycles, period, amplitude,
        title="B · CT-to-ground connection in place",
        note="Midpoint is anchored at 0 V. Lead 1 = +3.15 V when lead 2 = −3.15 V (and vice versa). Induced voltages into nearby signal wiring cancel.",
        with_ground=True,
    )

    # ---- Single shared legend below the figure ----
    handles_a, labels_a = ax_a.get_legend_handles_labels()
    fig.legend(
        handles_a, labels_a,
        loc="lower center", bbox_to_anchor=(0.5, 0.005),
        ncol=3, frameon=False, fontsize=11,
    )

    # ---- Title + subtitle ----
    fig.text(
        0.5, 0.955,
        "Heater winding — floating midpoint vs. CT grounded",
        ha="center", fontsize=20, fontweight="bold", color=COLOR_TEXT,
    )
    fig.text(
        0.5, 0.920,
        "Why grounding the heater center tap reduces 60 Hz hum in the audio signal.",
        ha="center", fontsize=12, color=COLOR_NOTE,
    )

    out_path = output_dir() / "heater-ct-comparison.svg"
    fig.savefig(out_path, format="svg", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out_path}")


def _panel_chrome(ax, t, cycles, period, amplitude, *, title, note, with_ground):
    ax.axhline(0, color=COLOR_ZERO, linewidth=1.0, linestyle=(0, (4, 3)))
    if with_ground:
        # Mark the ground bus more prominently
        ax.text(
            cycles * period * 1.01, 0,
            "GND",
            fontsize=10, fontweight="bold", color=COLOR_GROUND, va="center",
        )

    ax.set_yticks([-amplitude, 0.0, amplitude])
    ax.set_yticklabels(["−3.15 V", "0 V", "+3.15 V"], fontsize=11, color=COLOR_NOTE)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.set_xticks([])
    ax.set_ylim(-1.4 * amplitude, 1.4 * amplitude)
    ax.set_xlim(-0.01 * period, cycles * period + 0.10 * period)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    # Title and italic note both positioned in AXES coords above the axes top
    # (y > 1.0), so they never depend on the data range or overlap the waveform.
    ax.text(
        0.0, 1.22, title,
        fontsize=14, fontweight="bold", color=COLOR_TEXT,
        transform=ax.transAxes,
    )
    ax.text(
        0.0, 1.07, note,
        fontsize=11, style="italic", color=COLOR_NOTE,
        transform=ax.transAxes,
    )


if __name__ == "__main__":
    build()
