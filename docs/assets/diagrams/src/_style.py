"""Shared matplotlib style for ST-70 manual diagrams.

Imported by every diagram script so the output stays visually consistent
with the hand-authored SVGs (white background, Inter font, palette).
"""

from pathlib import Path

import matplotlib as mpl

# --- Palette (matches the rest of the diagram set) ---
COLOR_TEXT       = "#1a1a1a"
COLOR_NOTE       = "#444"
COLOR_FAINT      = "#888"
COLOR_AC         = "#1a1a1a"     # raw AC waveform
COLOR_RECTIFIED  = "#1a4e8a"     # rectified output (blue)
COLOR_GHOST      = "#b03020"     # the blocked / dashed-out portion (red)
COLOR_ANODE      = "#2a6b3a"     # "anode 1 / anode 2" labels
COLOR_AXIS       = "#888"
COLOR_ZERO       = "#888"

# --- rcParams ---
def apply_rcparams() -> None:
    mpl.rcParams.update({
        "font.family": ["Inter", "system-ui", "DejaVu Sans", "sans-serif"],
        "font.size": 11,
        "svg.fonttype": "none",     # leave text as text (let the browser handle font)
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": COLOR_AXIS,
        "axes.labelcolor": COLOR_TEXT,
        "xtick.color": COLOR_NOTE,
        "ytick.color": COLOR_NOTE,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.bottom": False,
        "axes.spines.left": True,
        "savefig.facecolor": "white",
        "savefig.transparent": False,
    })


def output_dir() -> Path:
    """The directory the SVGs should land in (one level above `src/`)."""
    return Path(__file__).resolve().parent.parent
