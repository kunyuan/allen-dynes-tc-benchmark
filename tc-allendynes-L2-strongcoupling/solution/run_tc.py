#!/usr/bin/env python3
"""Oracle (L2): full Allen-Dynes Tc with strong-coupling f1 and shape f2 factors.

    Tc = f1 * f2 * (omega_ln / 1.2) * exp[ -1.04 (1+lambda) / ( lambda - mu*(1+0.62 lambda) ) ]

    f1 = [ 1 + (lambda/Lambda1)^(3/2) ]^(1/3),   Lambda1 = 2.46 (1 + 3.8 mu*)
    f2 = 1 + ( (omega2/omega_ln) - 1 ) * lambda^2 / ( lambda^2 + Lambda2^2 ),
                                         Lambda2 = 1.82 (1 + 6.3 mu*) (omega2/omega_ln)

Reads params.csv (id, material, lambda, omega_ln_K, omega2_K, mu_star),
writes out.csv (id, Tc_K). Generic over any material set.
"""
from __future__ import annotations
import argparse, csv, math
from pathlib import Path


def allen_dynes_full(lam, w_ln, w2, mu):
    denom = lam - mu * (1.0 + 0.62 * lam)
    if denom <= 0.0:
        return 0.0
    r = w2 / w_ln
    Lambda1 = 2.46 * (1.0 + 3.8 * mu)
    Lambda2 = 1.82 * (1.0 + 6.3 * mu) * r
    f1 = (1.0 + (lam / Lambda1) ** 1.5) ** (1.0 / 3.0)
    f2 = 1.0 + ((r - 1.0) * lam * lam) / (lam * lam + Lambda2 * Lambda2)
    return f1 * f2 * (w_ln / 1.2) * math.exp(-1.04 * (1.0 + lam) / denom)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows = []
    with Path(a.params).open(newline="") as f:
        for r in csv.DictReader(f):
            tc = allen_dynes_full(float(r["lambda"]), float(r["omega_ln_K"]),
                                  float(r["omega2_K"]), float(r["mu_star"]))
            rows.append({"id": r["id"], "Tc_K": f"{tc:.6g}"})
    with Path(a.out).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "Tc_K"])
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
