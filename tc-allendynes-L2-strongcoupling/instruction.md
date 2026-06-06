# Working environment

You are in a container with Python 3 (numpy available). Public development data
is in `./packet/`. Write your solution as **`run_tc.py` in the working directory
(`/app`)**. The verifier will invoke it as

```
python run_tc.py --params <params.csv> --out <out.csv>
```

on **concealed held-out cases** (not the ones in `./packet/`). Do not hardcode
per-case answers — the graded cases differ from the development set.

---

# Level 2 — strong-coupling Tc (Allen-Dynes f1, f2 corrections)

Predict the superconducting critical temperature `Tc` for **strong-coupling**
electron-phonon superconductors using the **full Allen-Dynes formula, including
the strong-coupling correction factor f1 and the spectral-shape correction
factor f2**. The formula is intentionally **not** reproduced here — recall the
standard Allen-Dynes (1975) corrections and their coefficients yourself.

You are given, per case (abstract parameters only — no material identity):

- `lambda` — electron-phonon coupling constant (here `lambda > 1.2`, so the f1, f2
  factors are NOT negligible: the basic uncorrected formula is ~7-30% low);
- `omega_ln_K` — logarithmic-average phonon frequency ω_log (K);
- `omega2_K` — the second-moment frequency ω̄₂ = ⟨ω²⟩^(1/2) (K), needed by f2;
- `mu_star` — Coulomb pseudopotential μ*.

Note: the basic (uncorrected) McMillan/Allen-Dynes exponential alone — the Level-1
answer — will **fail** here; you must include f1 and f2.

## Input (`params.csv`)

Columns: `id,lambda,omega_ln_K,omega2_K,mu_star` — one row per case. `id` is an
opaque label; no material identity is provided.

## Output (`out.csv`)

Columns: `id,Tc_K` — exactly one row per input `id`, predicted Tc in Kelvin.

## Development data (`./packet/`)

- `packet/dev_params.csv` — 7 development cases.
- `packet/dev_gold.csv` — their reference `Tc_K` (full Allen-Dynes output), to
  validate your implementation. Reproduce to ~3 significant figures.

## Scoring

Run on concealed materials; each prediction must be within
`max(0.05 K, 1% * |Tc_gold|)` of the gold (the deterministic full Allen-Dynes
output). PASS requires every held-out material to clear its bar, exactly one
prediction each.
