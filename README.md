# allen-dynes-tc-benchmark — Allen-Dynes Tc Harbor benchmark

[![oracle-selfcheck](https://github.com/kunyuan/allen-dynes-tc-benchmark/actions/workflows/ci.yml/badge.svg)](https://github.com/kunyuan/allen-dynes-tc-benchmark/actions/workflows/ci.yml)

Three [Harbor](https://github.com/harbor-framework/harbor) tasks derived from
**WF-6 (McMillan–Allen-Dynes Tc estimation), sub-family 6a** of the Paper2ARM
superconductivity workflow cluster. The **formula is withheld** in all three —
the agent must recall the theory, not transcribe a given expression — and each
level tests a distinct closed-form **subroutine / variant** of the Tc computation.

| Task | Subroutine tested | Inputs | Cases | Gold |
|---|---|---|---|---|
| **L1** `tc-allendynes-L1-basic` | basic McMillan/Allen-Dynes exponential (ω_log/1.2 prefactor) | λ, ω_log, μ\* | weak-moderate, λ ≤ 1.5 | basic Allen-Dynes output |
| **L2** `tc-allendynes-L2-strongcoupling` | strong-coupling **f1** + shape **f2** corrections | λ, ω_log, **ω̄₂**, μ\* | strong, λ ≥ 1 | full Allen-Dynes (f1·f2) output |
| **L3** `tc-allendynes-L3-mcmillan` | the **original McMillan (1968)** form (Θ_D/**1.45** prefactor, *not* Allen-Dynes ω_log/1.2) | λ, **Θ_D**, μ\* | weak-moderate | McMillan output |

- **Formula withheld**: no `instruction.md` contains the expression; it names the
  method + regime (L2: that f1/f2 are required; L3: the *original McMillan*
  Debye-temperature form, explicitly **not** Allen-Dynes) and the agent must
  supply the coefficients.
- **Code submission + held-out test** (anti-cheat): each level ships public
  development cases (with gold, in `environment/packet/`) and **concealed**
  held-out cases (`tests/hidden/`, gold root-only). The agent submits a generic
  `run_tc.py`; it is run on cases it never saw.
- **Cross-level / cross-formula discrimination**: at L2 the f1·f2 factors raise Tc
  by ~7–27%, so an L1 basic-only implementation **fails** L2; at L3 the McMillan
  prefactor (Θ_D/1.45) is ~21% below Allen-Dynes (Θ_D/1.2), so an agent who reaches
  for the Allen-Dynes form **fails** L3. The three variants are genuinely
  separated.
- **Gold = deterministic formula output** (NOT paper-reported experimental Tc).
  L2's ω̄₂ = ⟨ω²⟩^(1/2) is an assigned representative second moment (papers rarely
  report it); the task grades implementation of the f1/f2 subroutine, not ω̄₂.
- **Pure closed-form** — no DFT/HPC/Julia; sub-second verifiers.

## Layout (standard Harbor, per level)

```
tc-allendynes-L{1,2,3}-*/
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

PASS iff every concealed case is within `max(0.05 K, 1%·|Tc_gold|)`, exactly one
prediction each. The full host-side self-check (every oracle on dev+hidden, plus
the L1→L2 and Allen-Dynes→L3 discrimination checks) runs in CI via
`scripts/selfcheck.sh` and is also reproduced by the agent solutions in
`experiments/`.

## Harder variants (future)

L4 — withhold even the *method name* (only the physical setup + α²F spectral data),
requiring derivation of the Allen-Dynes form from Eliashberg theory; or require the
agent to compute ω_log / λ / ω̄₂ from a provided α²F(ω) spectrum (adds a
moment-integration subroutine).
