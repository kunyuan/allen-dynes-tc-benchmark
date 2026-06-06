#!/usr/bin/env python3
"""Verifier scorer for the Allen-Dynes Tc task.

Reads the runner's out.csv and the hidden gold, applies a shape guard (exactly
one prediction per gold material) + a per-material tolerance, writes result.json,
and exits 0 iff overall verdict is PASS.

  score.py --pred <out.csv> --gold <gold.csv> --json <out.json>

Tolerance: |Tc_pred - Tc_gold| <= max(ABS_FLOOR_K, REL_TOL * |Tc_gold|).
Gold is the deterministic basic Allen-Dynes formula output (NOT paper-reported
experimental Tc), so a faithful implementation reproduces it to ~1e-4 K.
"""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path

REL_TOL = 0.01
ABS_FLOOR_K = 0.05


def read_csv_map(path: Path, value_col: str):
    out = {}
    if not path.exists():
        return out
    with path.open(newline="") as f:
        rows = csv.DictReader(f)
        if rows.fieldnames is None or "id" not in rows.fieldnames or value_col not in rows.fieldnames:
            return out
        for r in rows:
            v = (r.get(value_col) or "").strip()
            if v == "":
                continue
            out.setdefault(r["id"], []).append(float(v))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pred", required=True)
    ap.add_argument("--gold", required=True)
    ap.add_argument("--json", required=True)
    a = ap.parse_args()

    gold = {k: v[0] for k, v in read_csv_map(Path(a.gold), "Tc_K").items()}
    pred = read_csv_map(Path(a.pred), "Tc_K")

    per_item, all_pass = {}, True
    for mid, g in sorted(gold.items()):
        vals = pred.get(mid, [])
        if len(vals) != 1:                       # missing / duplicate -> reject
            per_item[mid] = {"verdict": "INVALID_SHAPE", "n_predictions": len(vals),
                             "gold_K": g, "pred_K": None}
            all_pass = False
            continue
        p = vals[0]
        tol = max(ABS_FLOOR_K, REL_TOL * abs(g))
        ok = abs(p - g) <= tol
        per_item[mid] = {"verdict": "PASS" if ok else "FAIL", "gold_K": g,
                         "pred_K": p, "abs_err_K": abs(p - g), "tol_K": tol}
        all_pass = all_pass and ok

    extra = sorted(set(pred) - set(gold))
    if extra:                                    # predictions for unknown ids -> reject
        all_pass = False

    result = {"verdict": "PASS" if all_pass else "FAIL",
              "n_materials": len(gold), "n_pass": sum(1 for v in per_item.values() if v["verdict"] == "PASS"),
              "rel_tol": REL_TOL, "abs_floor_K": ABS_FLOOR_K,
              "extra_unknown_ids": extra, "per_material": per_item}
    Path(a.json).write_text(json.dumps(result, indent=2))
    print(json.dumps({"verdict": result["verdict"], "n_pass": result["n_pass"],
                      "n_materials": result["n_materials"]}))
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
