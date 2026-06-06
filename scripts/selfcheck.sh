#!/usr/bin/env bash
# Oracle self-check (no Docker needed): mirrors the Harbor verifier on the host.
# Asserts that, for every level, the gold oracle PASSes on both the development
# and the concealed held-out cases, and that a basic-only solver FAILS the
# strong-coupling level (difficulty separation). Exits non-zero if any
# expectation is unmet. Run locally or in CI:  bash scripts/selfcheck.sh
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
tmp="$(mktemp -d)"
rc=0

expect() {  # expect <wanted-exit> <label> <cmd...>
  local want="$1" label="$2"; shift 2
  "$@" >/dev/null 2>&1; local got=$?
  if [ "$got" -eq "$want" ]; then
    echo "  ok    $label"
  else
    echo "  FAIL  $label (got exit $got, want $want)"; rc=1
  fi
}

L1=tc-allendynes-L1-basic
L2=tc-allendynes-L2-strongcoupling
L3=tc-allendynes-L3-mcmillan

for L in "$L1" "$L2" "$L3"; do
  echo "== $L =="
  python3 "$L/solution/run_tc.py" --params "$L/tests/hidden/params.csv" --out "$tmp/h.csv"
  expect 0 "oracle on HIDDEN -> PASS" \
    python3 "$L/tests/score.py" --pred "$tmp/h.csv" --gold "$L/tests/gold/gold.csv" --json "$tmp/r.json"
  python3 "$L/solution/run_tc.py" --params "$L/environment/packet/dev_params.csv" --out "$tmp/d.csv"
  expect 0 "oracle on DEV -> PASS" \
    python3 "$L/tests/score.py" --pred "$tmp/d.csv" --gold "$L/environment/packet/dev_gold.csv" --json "$tmp/r.json"
done

echo "== cross-level (formula separation) =="
# L1 basic (no f1/f2) must fail the strong-coupling level
python3 "$L1/solution/run_tc.py" --params "$L2/tests/hidden/params.csv" --out "$tmp/x.csv"
expect 1 "L1 basic solver on L2 hidden -> FAIL" \
  python3 "$L2/tests/score.py" --pred "$tmp/x.csv" --gold "$L2/tests/gold/gold.csv" --json "$tmp/r.json"
# Using the Allen-Dynes prefactor (theta_D/1.2) on the McMillan level must fail (~21% high)
python3 - "$L3/tests/hidden/params.csv" "$tmp/ad.csv" <<'PY'
import csv, math, sys
src, out = sys.argv[1], sys.argv[2]
rows = []
for r in csv.DictReader(open(src)):
    l, t, m = float(r["lambda"]), float(r["theta_D_K"]), float(r["mu_star"])
    tc = (t / 1.2) * math.exp(-1.04 * (1 + l) / (l - m * (1 + 0.62 * l)))
    rows.append({"id": r["id"], "Tc_K": f"{tc:.6g}"})
w = csv.DictWriter(open(out, "w", newline=""), fieldnames=["id", "Tc_K"]); w.writeheader(); w.writerows(rows)
PY
expect 1 "Allen-Dynes prefactor on L3 McMillan -> FAIL" \
  python3 "$L3/tests/score.py" --pred "$tmp/ad.csv" --gold "$L3/tests/gold/gold.csv" --json "$tmp/r.json"

echo "----------------------------------------"
if [ "$rc" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SELF-CHECK FAILED"; fi
exit "$rc"
