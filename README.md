# tc-allendynes-bench — Allen-Dynes Tc Harbor benchmark

Two [Harbor](https://github.com/harbor-framework/harbor) tasks derived from
**WF-6 (McMillan–Allen-Dynes Tc estimation), sub-family 6a** of the Paper2ARM
superconductivity workflow cluster. The **formula is withheld** in both — the
agent must recall the Allen-Dynes theory, not transcribe a given expression — and
the two levels test two distinct **subroutines** of the Tc computation.

| Task | Subroutine tested | Inputs | Materials | Gold |
|---|---|---|---|---|
| **L1** `tc-allendynes-L1-basic` | basic McMillan/Allen-Dynes exponential (ω_log/1.2 prefactor) | λ, ω_log, μ\* | weak-moderate, λ ≤ 1.5 | basic-formula output |
| **L2** `tc-allendynes-L2-strongcoupling` | strong-coupling **f1** + shape **f2** corrections | λ, ω_log, **ω̄₂**, μ\* | strong, λ ≥ 1 | full Allen-Dynes (f1·f2) output |

- **Formula withheld**: neither `instruction.md` contains the expression; it names
  the method + regime (and, for L2, that f1/f2 are required) and the agent must
  supply the coefficients.
- **Code submission + held-out test** (anti-cheat): each level ships public
  development materials (with gold, in `environment/packet/`) and **concealed**
  held-out materials (`tests/hidden/`, gold root-only). The agent submits a
  generic `run_tc.py`; it is run on materials it never saw.
- **Cross-level discrimination**: at L2 the f1·f2 factors raise Tc by ~7–27%, so
  an L1-style basic-only implementation **fails** L2 — the two subroutines are
  genuinely separated.
- **Gold = deterministic formula output** (NOT paper-reported experimental Tc).
  L2's ω̄₂ = ⟨ω²⟩^(1/2) is an assigned representative second moment (papers rarely
  report it); the task grades implementation of the f1/f2 subroutine, not ω̄₂.
- **Pure closed-form** — no DFT/HPC/Julia; sub-second verifiers.

## Layout (standard Harbor, per level)

```
tc-allendynes-L{1,2}-*/
├── task.toml          # metadata + verifier/agent/build timeouts
├── instruction.md     # agent-facing task (formula WITHHELD; I/O contract; scoring)
├── environment/
│   ├── Dockerfile     # python:3.12-slim + numpy
│   └── packet/        # public dev data (params + gold)
├── solution/          # oracle (run_tc.py + solve.sh) — not shown to agent
└── tests/             # verifier — not shown to agent
    ├── test.sh        #   run /app/run_tc.py as `nobody` on hidden params; reward.txt
    ├── score.py       #   shape guard + per-material tolerance; result.json; exit 0 iff PASS
    ├── hidden/params.csv
    └── gold/gold.csv  #   root-only
```

## Run

```bash
harbor run --agent oracle --path tc-allendynes-L1-basic            # confirm solvable
harbor run --agent claude-code --path tc-allendynes-L2-strongcoupling
```

PASS iff every concealed material is within `max(0.05 K, 1%·|Tc_gold|)`, exactly
one prediction each. Host-side validated: each level's oracle → PASS; a basic-only
solver → FAIL on L2; wrong/short submissions → FAIL.

## Harder variants (future)

L3 — withhold even the *method name* (only the physical setup + α²F spectral data),
requiring derivation of the Allen-Dynes form from Eliashberg theory; or require the
agent to compute ω_log / λ / ω̄₂ from a provided α²F(ω) spectrum (adds a
moment-integration subroutine).
