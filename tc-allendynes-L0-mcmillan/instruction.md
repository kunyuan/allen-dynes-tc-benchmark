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

# Level 0 — the original McMillan Tc formula

Predict the superconducting critical temperature `Tc` using the **original
McMillan (1968) formula**, which uses the **Debye temperature** with the
prefactor `theta_D / 1.45`.

This is **NOT** the Allen-Dynes (1975) modification (which replaces the prefactor
with `omega_log / 1.2`). The two share the same exponential but differ in the
prefactor; using the Allen-Dynes form here **overestimates Tc by ~21% and FAILs**.
Use the McMillan Debye-temperature form. The formula — its functional form and
every coefficient — is intentionally **not** given; recall it yourself.

You are given, per case (abstract parameters only — no material identity):

- `lambda` — electron-phonon coupling constant;
- `theta_D_K` — Debye temperature Θ_D (K);
- `mu_star` — Coulomb pseudopotential μ*.

Output `Tc` in Kelvin.

## Input (`params.csv`)

Columns: `id,lambda,theta_D_K,mu_star` — one row per case. `id` is an opaque
label; no material identity is provided.

## Output (`out.csv`)

Columns: `id,Tc_K` — exactly one row per input `id`, predicted Tc in Kelvin.

## Development data (`./packet/`)

- `packet/dev_params.csv` — 9 development cases.
- `packet/dev_gold.csv` — their reference `Tc_K` (McMillan output), to validate
  your implementation. Reproduce to ~3 significant figures.

## Scoring

Run on concealed cases; each prediction must be within
`max(0.05 K, 1% * |Tc_gold|)` of the gold (the deterministic McMillan output).
PASS requires every held-out case to clear its bar, exactly one prediction each.
