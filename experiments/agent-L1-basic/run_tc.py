#!/usr/bin/env python3
"""Level 1 superconducting Tc predictor.

Uses the basic McMillan / Allen-Dynes formula (weak-to-moderate coupling,
no strong-coupling f1/f2 corrections):

    Tc = (omega_log / 1.2) * exp( -1.04 (1 + lambda)
                                  / (lambda - mu* (1 + 0.62 lambda)) )

with omega_log given in Kelvin (so the 1.2 prefactor carries the k_B / 1.2
convention and Tc comes out directly in Kelvin).
"""

from __future__ import annotations

import argparse
import csv
import math


def mcmillan_tc(lam: float, omega_ln_k: float, mu_star: float) -> float:
    """Return Tc in Kelvin via the basic McMillan/Allen-Dynes expression."""
    denom = lam - mu_star * (1.0 + 0.62 * lam)
    if denom <= 0.0:
        # No superconductivity in this regime; report Tc = 0 K.
        return 0.0
    exponent = -1.04 * (1.0 + lam) / denom
    return (omega_ln_k / 1.2) * math.exp(exponent)


def main() -> None:
    parser = argparse.ArgumentParser(description="Predict Tc (McMillan/Allen-Dynes).")
    parser.add_argument("--params", required=True, help="input params CSV")
    parser.add_argument("--out", required=True, help="output CSV path")
    args = parser.parse_args()

    rows: list[tuple[str, float]] = []
    with open(args.params, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            case_id = row["id"]
            lam = float(row["lambda"])
            omega_ln_k = float(row["omega_ln_K"])
            mu_star = float(row["mu_star"])
            tc = mcmillan_tc(lam, omega_ln_k, mu_star)
            rows.append((case_id, tc))

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["id", "Tc_K"])
        for case_id, tc in rows:
            writer.writerow([case_id, f"{tc:.6g}"])


if __name__ == "__main__":
    main()
