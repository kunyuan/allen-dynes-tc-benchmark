# experiments — independent solver solutions (solvability evidence)

These are `run_tc.py` submissions produced by **fresh Claude subagents** during
benchmark validation. Each agent saw **only** the level's `instruction.md` and
its public `environment/packet/` development data — **not** the formula, the
`solution/` oracle, or the `tests/` (hidden cases + gold). It had to recall the
Allen-Dynes theory from its own knowledge, write a generic `run_tc.py`, and
self-validate against the dev gold. The submissions were then scored by the
verifier on the concealed held-out cases.

| Submission | Recalled | Dev | Hidden |
|---|---|---|---|
| `agent-L1-basic/run_tc.py` | basic McMillan/Allen-Dynes exponential | PASS 8/8 | PASS 4/4 |
| `agent-L2-strongcoupling/run_tc.py` | full Allen-Dynes incl. f1, f2 (with the correct Λ1, Λ2 coefficients) | PASS 5/5 | PASS 3/3 |

Cross-check: the L1 basic submission, run on the L2 hidden cases, **FAILs**
(13–21% low) — confirming the f1·f2 strong-coupling subroutine is genuinely
required at L2 and the two levels are not interchangeable.

These files are **audit / reproduction evidence**, kept like `solution/`: under
Harbor they are not part of any task's `environment/`, so a benchmarked agent
never sees them. They show the tasks are solvable by an independent agent (not
just the maintainer oracle). Re-check any submission with the verifier, e.g.:

```bash
python3 experiments/agent-L2-strongcoupling/run_tc.py \
  --params tc-allendynes-L2-strongcoupling/tests/hidden/params.csv --out /tmp/out.csv
python3 tc-allendynes-L2-strongcoupling/tests/score.py \
  --pred /tmp/out.csv --gold tc-allendynes-L2-strongcoupling/tests/gold/gold.csv --json /tmp/r.json
```

(The full host-side self-check — both oracles on dev+hidden plus the L1→L2
cross-check — runs in CI via `scripts/selfcheck.sh`.)
