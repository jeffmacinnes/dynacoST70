"""Choke filter response: LC pi-filter attenuation vs frequency.

Shows why putting a choke (~1.5 H) between the first and second filter
caps dramatically reduces 120 Hz ripple. Plot is in dB attenuation
vs frequency, with the 60/120 Hz ripple frequencies marked.

Outputs: docs/assets/diagrams/choke-filter-response.svg
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


def build():
    apply_rcparams()

    # ST-70 filter section values (per Dynaco C-354 spec sheet)
    L = 1.75       # H, choke
    C1 = 30e-6     # F, first filter cap (input side of choke)
    C2 = 20e-6     # F, second filter cap (output side of choke — feeds tubes)
    R_load = 4500  # Ω, ~100 mA from 450 V B+

    # The LC pi-filter has a natural resonant frequency:
    #   f_res = 1 / (2π · √(LC))
    # Above this, attenuation rises at ~40 dB/decade (12 dB/octave).
    # We compute the |H(jω)| transfer function from cap_1 to cap_2 through
    # the choke loaded by R_load // C2.
    f = np.logspace(0, 4, 2000)   # 1 Hz to 10 kHz
    w = 2 * np.pi * f
    Z_L = 1j * w * L
    Z_C2 = 1 / (1j * w * C2)
    Z_R = R_load
    Z_load = (Z_C2 * Z_R) / (Z_C2 + Z_R)
    # Voltage divider: input → series choke → parallel(load, C2)
    H = Z_load / (Z_L + Z_load)
    H_db = 20 * np.log10(np.abs(H))

    f_res = 1.0 / (2 * np.pi * np.sqrt(L * C2))

    # --- Figure ---
    fig = plt.figure(figsize=(11.0, 6.4))
    fig.subplots_adjust(top=0.85, bottom=0.13, left=0.09, right=0.94)
    ax = fig.add_subplot(111)

    # Response curve
    ax.semilogx(f, H_db, color=COLOR_RECTIFIED, linewidth=2.6)

    # Mark 60 Hz (mains), 120 Hz (full-wave ripple fundamental), 240 Hz (2nd harmonic)
    for freq, label, color in [
        (60.0,  "60 Hz\n(mains)",            "#888"),
        (120.0, "120 Hz\n(full-wave ripple)", "#cc3a2a"),
        (240.0, "240 Hz\n(2nd harmonic)",    "#888"),
    ]:
        # Find the actual response value at this frequency
        idx = np.argmin(np.abs(f - freq))
        atten = H_db[idx]
        ax.axvline(freq, color=color, linewidth=1.0, linestyle=(0, (4, 3)), alpha=0.6)
        ax.scatter([freq], [atten], s=60, color=color, zorder=5)
        # Annotate the attenuation at this frequency
        ax.annotate(
            f"{label}\n{atten:.0f} dB",
            xy=(freq, atten),
            xytext=(freq * 1.4, atten - 8),
            fontsize=10, color=color,
            arrowprops=dict(arrowstyle="-", color=color, alpha=0.4),
        )

    # Mark resonance
    ax.axvline(f_res, color="#1a4e8a", linewidth=1.0, linestyle=(0, (2, 3)), alpha=0.6)
    ax.text(
        f_res * 1.1, 5,
        f"LC resonance\n≈ {f_res:.0f} Hz",
        fontsize=10, color="#1a4e8a",
    )

    # Axes labels
    ax.set_xlabel("Frequency (Hz)", fontsize=12, color=COLOR_TEXT)
    ax.set_ylabel("Attenuation (dB)", fontsize=12, color=COLOR_TEXT)
    ax.set_xlim(1, 10_000)
    ax.set_ylim(-100, 10)
    ax.grid(True, which="both", linestyle=":", alpha=0.4)
    ax.axhline(0, color=COLOR_ZERO, linewidth=0.8)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Title + subtitle
    fig.text(
        0.5, 0.945,
        "LC filter response — how the choke kills 120 Hz ripple",
        ha="center", fontsize=20, fontweight="bold", color=COLOR_TEXT,
    )
    fig.text(
        0.5, 0.900,
        "ST-70 values: L = 1.75 H choke (C-354), C₂ = 20 µF second filter cap, ~100 mA load. Plot shows attenuation from C₁ to C₂.",
        ha="center", fontsize=12, color=COLOR_NOTE,
    )

    fig.text(
        0.5, 0.020,
        "Above the LC resonance, attenuation rises at ~40 dB/decade. 120 Hz ripple gets cut by ~26 dB — a factor of ~20.",
        ha="center", fontsize=11, style="italic", color="#555",
    )

    out_path = output_dir() / "choke-filter-response.svg"
    fig.savefig(out_path, format="svg", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    build()
