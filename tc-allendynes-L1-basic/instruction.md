# Working environment

You are in a container with Python 3 (numpy available). Public development data
is in `./packet/`. Write your solution as **`run_tc.py` in the working directory
(`/app`)**. The verifier will invoke it as

```
python run_tc.py --params <params.csv> --out <out.csv>
```

on **concealed held-out cases** (not the ones in `./packet/`). Your code must
read `params.csv` and write `out.csv`; do not hardcode per-case answers — the
graded cases are different from the development set.

---

# Level 1 — basic Allen-Dynes / McMillan Tc

Predict the superconducting critical temperature `Tc` from the electron-phonon
parameters using the **basic McMillan / Allen-Dynes formula** (the
weak-to-moderate-coupling form, with **no** strong-coupling f-factors). The
formula — its functional form and every coefficient — is intentionally **not**
given; recall the standard Allen-Dynes expression yourself.

You are given, per case (abstract parameters only — no material identity):

- `lambda` — electron-phonon coupling constant (these cases are papers that
  applied the basic form; λ spans weak to strong, but none used f1/f2 corrections);
- `omega_ln_K` — logarithmic-average phonon frequency ω_log (K);
- `mu_star` — Coulomb pseudopotential μ*.

Output `Tc` in Kelvin. (Strong-coupling f1/f2 corrections are out of scope here —
that is Level 2.)

## Input (`params.csv`)

Columns: `id,lambda,omega_ln_K,mu_star` — one row per case. `id` is an opaque
label; no material identity is provided, so `Tc` must be computed from the three
physical numbers, not recalled from a known compound.

## Output (`out.csv`)

Columns: `id,Tc_K` — exactly one row per input `id`, in any order, with the
predicted Tc in Kelvin.

## Development data (`./packet/`)

- `packet/dev_params.csv` — 157 development cases (same column format).
- `packet/dev_gold.csv` — their reference `Tc_K`, so you can validate your
  implementation before submitting. Reproduce these to ~3 significant figures.

## Scoring

Your `run_tc.py` is run on concealed materials. For each, the prediction must be
within `max(0.05 K, 1% * |Tc_gold|)` of the gold (the deterministic formula
output). **PASS requires every held-out material to clear its bar**, and exactly
one prediction per material (missing or duplicate rows are rejected).
