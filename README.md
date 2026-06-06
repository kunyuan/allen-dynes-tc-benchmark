# allen-dynes-tc-benchmark — Allen-Dynes Tc Harbor benchmark

[![oracle-selfcheck](https://github.com/kunyuan/allen-dynes-tc-benchmark/actions/workflows/ci.yml/badge.svg)](https://github.com/kunyuan/allen-dynes-tc-benchmark/actions/workflows/ci.yml)

Three [Harbor](https://github.com/harbor-framework/harbor) tasks derived from
**WF-6 (McMillan–Allen-Dynes Tc estimation), sub-family 6a** of the Paper2ARM
superconductivity workflow cluster. The **formula is withheld** in all three —
the agent must recall the theory, not transcribe a given expression — and each
level tests a distinct closed-form **subroutine / variant** of the Tc computation.

| Task | Subroutine / variant tested | Inputs | Cases | Gold |
|---|---|---|---|---|
| **L0** `tc-allendynes-L0-mcmillan` | the **original McMillan (1968)** form (Θ_D/**1.45** prefactor, *not* Allen-Dynes ω_log/1.2) | λ, **Θ_D**, μ\* | weak-moderate | McMillan output |
| **L1** `tc-allendynes-L1-basic` | basic **Allen-Dynes (1975)** exponential (ω_log/**1.2** prefactor) | λ, ω_log, μ\* | weak-moderate, λ ≤ 1.2 | basic Allen-Dynes output |
| **L2** `tc-allendynes-L2-strongcoupling` | strong-coupling **f1** + shape **f2** corrections | λ, ω_log, **ω̄₂**, μ\* | strong, λ > 1.2 | full Allen-Dynes (f1·f2) output |

Ordered by the physics lineage: McMillan (1968) → Allen-Dynes basic (1975) →
Allen-Dynes + strong-coupling corrections.

- **Formula withheld**: no `instruction.md` contains the expression; it names the
  method + regime (L0: the *original McMillan* Debye-temperature form, explicitly
  **not** Allen-Dynes; L2: that f1/f2 are required) and the agent must supply the
  coefficients.
- **Code submission + held-out test** (anti-cheat): each level ships public
  development cases (with gold, in `environment/packet/`) and **concealed**
  held-out cases (`tests/hidden/`, gold root-only). The agent submits a generic
  `run_tc.py`; it is run on cases it never saw.
- **Cross-formula discrimination**: at L0 the McMillan prefactor (Θ_D/1.45) is ~21%
  below Allen-Dynes (Θ_D/1.2), so an agent who reaches for the Allen-Dynes form
  **fails** L0; at L2 the f1·f2 factors raise Tc by ~7–27%, so an L1 basic-only
  implementation **fails** L2. The three variants are genuinely separated.
- **Gold = deterministic formula output** (NOT paper-reported experimental Tc).
  L2's ω̄₂ = ⟨ω²⟩^(1/2) is an assigned representative second moment (papers rarely
  report it); the task grades implementation of the f1/f2 subroutine, not ω̄₂.
- **Pure closed-form** — no DFT/HPC/Julia; sub-second verifiers.

## Data & provenance

All cases derive from **WF-6 (243 papers)** of the Paper2ARM superconductivity
cluster. Classifying each paper by the closed-form Tc variant it actually uses
(best-effort, per-paper method fields):

| Variant | Level | WF-6 papers | Benchmark cases (dev + hidden) |
|---|---|---|---|
| original McMillan (Θ_D/1.45) | **L0** | 11 | 19 (13 + 6) |
| basic Allen-Dynes (ω_log/1.2) | **L1** | 190 | 44 (29 + 15) |
| Allen-Dynes + f1/f2 (strong) | **L2** | 22 | 10 (7 + 3) |
| full Eliashberg (gap equations) | — (not benchmarked) | 20 | — |
| **total** | | **243** | **73 cases** |

The benchmark uses **every** clean, sound case we could extract from WF-6 (73 in
all): all 19 McMillan-frequency cases (L0), all 44 Allen-Dynes ω_log cases with
λ ≤ 1.2 (L1), and all 10 with λ > 1.2 (L2). L1/L2 are split at λ = 1.2 so they are
disjoint. Mis-paired (multi-condition) extractions were dropped via a Tc
self-consistency check.

(±a few at the boundaries. ~150 papers *name* "McMillan", but most use it as the
colloquial name for the Allen-Dynes form — only ~11 use the original Θ_D/1.45
prefactor, confirmed by reproducing their reported Tc.)

Gold is always the **deterministic formula output**, not paper-reported experimental
Tc. Inputs are abstract parameters only (no material identity), so Tc cannot be
recalled from a known compound. L2's ω̄₂ = ⟨ω²⟩^(1/2) is an assigned representative
second moment (papers rarely report it).

### Per-case sources

The source `paper_id` for **every** case — all 73 across L0/L1/L2, with the
dev/hidden split and parameters — is recorded in [`SOURCES.md`](SOURCES.md). Of the
19 L0 cases, only **3** (`k07`, `k15`, `k16`) are papers whose *own* reported Tc is
reproduced by McMillan; the rest report a Debye temperature but used a different
final form — so the tuples are physically realistic while the **task** is defined by
the McMillan gold.

## Layout (standard Harbor, per level)

```
tc-allendynes-L{0,1,2}-*/
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
the L1-basic→L2 and Allen-Dynes-prefactor→L0 discrimination checks) runs in CI via
`scripts/selfcheck.sh` and is also reproduced by the agent solutions in
`experiments/`.

## Harder variants (future)

L4 — withhold even the *method name* (only the physical setup + α²F spectral data),
requiring derivation of the Allen-Dynes form from Eliashberg theory; or require the
agent to compute ω_log / λ / ω̄₂ from a provided α²F(ω) spectrum (adds a
moment-integration subroutine).
