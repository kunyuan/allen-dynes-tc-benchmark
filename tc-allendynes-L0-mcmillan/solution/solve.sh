#!/bin/bash
# Oracle: install the reference solution as the agent's /app/run_tc.py.
# Used by Harbor (`--agent oracle`) to confirm the task is solvable.
set -e
cp /solution/run_tc.py /app/run_tc.py
echo "oracle reference solution installed at /app/run_tc.py"
