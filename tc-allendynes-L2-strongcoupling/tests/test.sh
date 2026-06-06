#!/bin/bash
# Harbor verifier. Defense-in-depth against hidden-answer leaks:
#  - the runner is handed ONLY params.csv (no gold anywhere in its input);
#  - /tests/hidden + /tests/gold are locked root-only and the agent's code runs
#    as the unprivileged `nobody`, so it cannot read the gold even if it tries;
#  - score (shape guard + per-material tolerance) and write a binary reward to
#    /logs/verifier/reward.txt (1 = overall PASS).
set -uo pipefail
mkdir -p /logs/verifier /tmp/preds /tmp/runner_inputs
chmod -R a+rwX /tmp/preds /tmp/runner_inputs
chmod -R go-rwx /tests/hidden /tests/gold
chmod go-rwx /tests/test.sh /tests/score.py
chmod -R a+rX /app

# hand the runner only the params (the gold lives in /tests/gold, root-only)
cp /tests/hidden/params.csv /tmp/runner_inputs/params.csv
chmod -R a+rX /tmp/runner_inputs

run_as_nobody() {
  python3 - "$@" <<'PY'
import os, pwd, subprocess, sys
pw = pwd.getpwnam("nobody")
os.setgid(pw.pw_gid); os.setuid(pw.pw_uid)
raise SystemExit(subprocess.run(sys.argv[1:]).returncode)
PY
}

fail=0
run_as_nobody python3 /app/run_tc.py \
  --params /tmp/runner_inputs/params.csv \
  --out /tmp/preds/out.csv \
  || { echo "[verifier] runner failed"; fail=1; }

python3 /tests/score.py \
  --pred /tmp/preds/out.csv --gold /tests/gold/gold.csv \
  --json /logs/verifier/result.json
pass=$?

if [ "$fail" -eq 0 ] && [ "$pass" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
echo "[verifier] reward=$(cat /logs/verifier/reward.txt)"
exit $((1 - $(cat /logs/verifier/reward.txt)))
