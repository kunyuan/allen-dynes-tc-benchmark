#!/usr/bin/env python3
"""Strong-coupling Tc via the full Allen-Dynes (1975) formula.

Implements the McMillan/Allen-Dynes exponential together with the
strong-coupling correction factor f1 and the spectral-shape correction
factor f2, as defined in Allen & Dynes, Phys. Rev. B 12, 905 (1975).

    Tc = (f1 * f2) * (omega_log / 1.2)
         * exp[ -1.04 (1 + lambda)
                / ( lambda - mu* (1 + 0.62 lambda) ) ]

with

    f1 = [ 1 + (lambda / Lambda1)^(3/2) ]^(1/3)
    Lambda1 = 2.46 (1 + 3.8 mu*)

    f2 = 1 + ( (omega2/omega_log - 1) * lambda^2 )
                / ( lambda^2 + Lambda2^2 )
    Lambda2 = 1.82 (1 + 6.3 mu*) (omega2 / omega_log)

Usage:
    python run_tc.py --params <params.csv> --out <out.csv>
"""

from __future__ import annotations

import argparse
import csv
import math


def allen_dynes_tc(
    lam: float,
    omega_ln_k: float,
    omega2_k: float,
    mu_star: float,
) -> float:
    """Return Tc (K) from the full Allen-Dynes formula with f1, f2.

    Args:
        lam: Electron-phonon coupling constant lambda.
        omega_ln_k: Logarithmic-average phonon frequency omega_log (K).
        omega2_k: Second-moment frequency <omega^2>^(1/2) (K).
        mu_star: Coulomb pseudopotential mu*.

    Returns:
        Critical temperature Tc in Kelvin.
    """
    # Base McMillan/Allen-Dynes exponential (the Level-1 answer).
    denom = lam - mu_star * (1.0 + 0.62 * lam)
    exponent = -1.04 * (1.0 + lam) / denom
    base = (omega_ln_k / 1.2) * math.exp(exponent)

    # f1: strong-coupling correction.
    lambda1 = 2.46 * (1.0 + 3.8 * mu_star)
    f1 = (1.0 + (lam / lambda1) ** 1.5) ** (1.0 / 3.0)

    # f2: spectral-shape correction.
    ratio = omega2_k / omega_ln_k
    lambda2 = 1.82 * (1.0 + 6.3 * mu_star) * ratio
    f2 = 1.0 + ((ratio - 1.0) * lam**2) / (lam**2 + lambda2**2)

    return f1 * f2 * base


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--params", required=True, help="input params CSV")
    parser.add_argument("--out", required=True, help="output CSV")
    args = parser.parse_args()

    rows: list[tuple[str, float]] = []
    with open(args.params, newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            tc = allen_dynes_tc(
                lam=float(row["lambda"]),
                omega_ln_k=float(row["omega_ln_K"]),
                omega2_k=float(row["omega2_K"]),
                mu_star=float(row["mu_star"]),
            )
            rows.append((row["id"], tc))

    with open(args.out, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["id", "Tc_K"])
        for cid, tc in rows:
            writer.writerow([cid, f"{tc:.6g}"])


if __name__ == "__main__":
    main()
