# tc-allendynes-6a — Harbor task

A [Harbor](https://github.com/harbor-framework/harbor) task derived from
**WF-6 (McMillan–Allen-Dynes Tc estimation), sub-family 6a** of the Paper2ARM
superconductivity workflow cluster.

**Task (one coding problem):** implement the basic McMillan/Allen-Dynes closed
form `Tc = (ω_ln/1.2)·exp[ -1.04(1+λ) / (λ − μ*(1+0.62λ)) ]` as a generic
`run_tc.py`, and reproduce the held-out gold on **concealed** materials.

- **Pure closed-form** — no DFT/HPC/Julia; sub-second verifier.
- **Code submission + held-out test** (anti-cheat): 8 public development
  materials (`environment/packet/`, with gold) vs **4 concealed** materials
  (`tests/hidden/`, gold root-only). The agent develops a *generic* solver; it is
  run on materials it never saw, so per-item answers cannot be hardcoded.
- **Gold = deterministic formula output**, NOT paper-reported experimental Tc
  (papers may use the f1/f2 strong-coupling variant). Materials restricted to
  λ ≤ 1.5 where the basic form is valid; coverage is a curated subset, not
  exhaustive.

## Layout (standard Harbor)

```
tc-allendynes-6a/
├── task.toml                  # metadata + verifier/agent/build timeouts
├── instruction.md             # agent-facing task (formula, I/O contract, scoring)
├── environment/
│   ├── Dockerfile             # python:3.12-slim + numpy
│   └── packet/                # PUBLIC dev data (agent-facing)
│       ├── dev_params.csv     #   8 materials: id,material,lambda,omega_ln_K,mu_star
│       └── dev_gold.csv       #   their gold Tc_K (to self-validate)
├── solution/                  # ORACLE (not shown to agent)
│   ├── solve.sh               #   installs the reference run_tc.py at /app
│   └── run_tc.py              #   reference implementation
└── tests/                     # VERIFIER (not shown to agent)
    ├── test.sh                #   run /app/run_tc.py as `nobody` on hidden params; reward.txt
    ├── score.py               #   shape guard + per-material tolerance; result.json; exit 0 iff PASS
    ├── hidden/params.csv      #   4 concealed materials (NO gold)
    └── gold/gold.csv          #   their gold Tc_K (root-only)
```

## Submission & scoring

Agent submits `/app/run_tc.py`, invoked as
`python run_tc.py --params <params.csv> --out <out.csv>`. PASS iff **every**
concealed material is within `max(0.05 K, 1%·|Tc_gold|)` and exactly one
prediction per material (missing/duplicate/unknown ids rejected).

```bash
harbor run --agent oracle --path tc-allendynes-6a       # confirm solvable (reward 1.0)
harbor run --agent claude-code --path tc-allendynes-6a  # run a real agent
```

Host-side validation (done): oracle → PASS; a wrong formula (missing the 1.2
prefactor) → FAIL; a short submission → INVALID_SHAPE/FAIL.

## Harder variants (future)

Withhold the formula in `instruction.md` (test whether the agent knows/derives
Allen-Dynes), or require the f1/f2 strong-coupling factors (needs the α²F
spectral moments, not just λ/ω_ln).
