#!/usr/bin/env python3
"""Oracle (L0): the ORIGINAL McMillan (1968) Tc formula.

    Tc = (theta_D / 1.45) * exp[ -1.04 (1 + lambda)
                                 / ( lambda - mu* (1 + 0.62 lambda) ) ]

Note the Debye-temperature prefactor theta_D / 1.45 — this is the original
McMillan form, NOT the Allen-Dynes (1975) modification, which replaces it with
omega_log / 1.2 (and would overestimate Tc here by ~21%). Same exponential.

Reads params.csv (id, lambda, theta_D_K, mu_star), writes out.csv (id, Tc_K).
"""
from __future__ import annotations
import argparse, csv, math
from pathlib import Path


def mcmillan_tc(lam: float, theta_D_K: float, mu_star: float) -> float:
    denom = lam - mu_star * (1.0 + 0.62 * lam)
    if denom <= 0.0:
        return 0.0
    return (theta_D_K / 1.45) * math.exp(-1.04 * (1.0 + lam) / denom)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows = []
    with Path(a.params).open(newline="") as f:
        for r in csv.DictReader(f):
            tc = mcmillan_tc(float(r["lambda"]), float(r["theta_D_K"]), float(r["mu_star"]))
            rows.append({"id": r["id"], "Tc_K": f"{tc:.6g}"})
    with Path(a.out).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "Tc_K"])
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
