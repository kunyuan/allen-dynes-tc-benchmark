#!/usr/bin/env python3
"""Oracle reference solution: basic McMillan/Allen-Dynes Tc from (lambda, omega_ln, mu*).

    Tc = (omega_ln / 1.2) * exp( -1.04 (1+lambda) / ( lambda - mu* (1 + 0.62 lambda) ) )

Reads params.csv (id, material, lambda, omega_ln_K, mu_star), writes out.csv (id, Tc_K).
Generic: works on any material set, including the concealed held-out ones.
"""
from __future__ import annotations
import argparse, csv, math
from pathlib import Path


def allen_dynes_tc(lam: float, omega_ln_K: float, mu_star: float) -> float:
    denom = lam - mu_star * (1.0 + 0.62 * lam)
    if denom <= 0.0:                       # basic form diverges for very strong coupling
        return 0.0
    return (omega_ln_K / 1.2) * math.exp(-1.04 * (1.0 + lam) / denom)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    rows = []
    with Path(a.params).open(newline="") as f:
        for r in csv.DictReader(f):
            tc = allen_dynes_tc(float(r["lambda"]), float(r["omega_ln_K"]), float(r["mu_star"]))
            rows.append({"id": r["id"], "Tc_K": f"{tc:.6g}"})

    with Path(a.out).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "Tc_K"])
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
