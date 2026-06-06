# Reproduction audit — papers whose reported Tc is NOT reproducible by any closed form

These WF-6 papers report (λ, ω/Θ_D, μ*) **and** a Tc, but no standard closed form
(McMillan Θ_D/1.45, Allen-Dynes ω_log/1.2, or Allen-Dynes + f1/f2) reproduces the
reported Tc from the reported parameters (within 20%). They are **not dropped** —
they are listed here because *failing to reproduce a reported result is itself a
finding*. Causes differ:

- **needs full Eliashberg (strong coupling)** — high λ; the closed form genuinely
  underestimates and the paper used the full Eliashberg gap equations.
- **params incoherent: λ too low for reported Tc** — most likely a multi-condition
  paper (λ at one pressure/doping, Tc at another); needs per-condition splitting.
- **formula overshoots paper Tc** — μ* or an extracted number is suspect.
- **no closed form reproduces reported Tc** — uncategorised; review needed.

Total flagged: **28**.

| paper_id | λ | ω_log (K) | Θ_D (K) | μ* | paper Tc (K) | closed-form max (K) | reason | title |
|---|---|---|---|---|---|---|---|---|
| `867791146489741774` | 2.0 | 500.0 |  | 0.1 | 255.0 | 87.57 | needs full Eliashberg (strong coupling) | Superconducting phase above room temperature i |
| `813107915761123328` | 1.5 | 500.0 |  | 0.12 | 30.6 | 53.65 | needs full Eliashberg (strong coupling) | Investigation of superconductivity in compress |
| `813214157951205376` | 1.7 | 160.0 |  | 0.13 | 27.0 | 21.56 | needs full Eliashberg (strong coupling) | Phonon-mediated superconductivity in electron- |
| `867765649085038612` | 1.7822 | 200.0 |  | 0.12 | 8.6 | 25.14 | needs full Eliashberg (strong coupling) | First-principles calculations of phase transit |
| `811740615149617152` | 0.61 | 789.1 |  | 0.14 | 19.0 | 12.2 | params incoherent: lambda too low for reported Tc (multi-condition mis-pair?) | Giant anharmonicity suppresses superconductivi |
| `812481926441992193` | 0.41 | 200.0 |  | 0.12 | 1.16 | 0.59 | params incoherent: lambda too low for reported Tc (multi-condition mis-pair?) |  |
| `867757942403760362` | 0.29 | 100.0 |  | 0.13 | 0.1 | 0.01 | params incoherent: lambda too low for reported Tc (multi-condition mis-pair?) | Electronic and lattice dynamical properties of |
| `812123095799169025` | 1.0 | 200.0 |  | 0.1 | 8.7 | 13.93 | formula overshoots paper Tc (mu*/extraction suspect) | Ab-initio Calculations of Lattice Dynamics and |
| `867771980533727398` | 1.0 | 200.0 |  | 0.1 | 7.5 | 13.93 | formula overshoots paper Tc (mu*/extraction suspect) | Manipulating superconductivity of $1T$-TiTe$_2 |
| `812127705880330240` | 0.94 | 226.3 |  | 0.13 | 4.5 | 12.08 | formula overshoots paper Tc (mu*/extraction suspect) | Competition of ferromagnetism and superconduct |
| `814692371164823552` | 0.678 | 165.53 |  | 0.1 | 3.34 | 5.32 | formula overshoots paper Tc (mu*/extraction suspect) |  |
| `811192921058443264` | 0.7 |  | 213.0 | 0.13 | 3.1 | 4.7 | formula overshoots paper Tc (mu*/extraction suspect) |  |
| `814721288294629376` | 0.78 | 105.5 |  | 0.1 | 2.4 | 4.69 | formula overshoots paper Tc (mu*/extraction suspect) | Theoretical examination of electron–phonon int |
| `811940808310652928` | 1.151 |  | 177.2 | 0.135 | 0.1 | 10.73 | formula overshoots paper Tc (mu*/extraction suspect) | Screening dependence superconducting state par |
| `812042380692684801` | 0.85 | 1023.0 |  | 0.1 | 77.0 | 57.07 | no closed form reproduces reported Tc | Electron-phonon coupling in halogen-doped carb |
| `813087272097284096` | 1.13 | 426.0 |  | 0.1 | 51.0 | 38.48 | no closed form reproduces reported Tc | Superconductivity in FeH 5 |
| `813184744584904705` | 0.84 | 395.0 |  | 0.12 | 28.2 | 18.83 | no closed form reproduces reported Tc | Superconductivity at 28 K in CaB 3 C 3 predict |
| `817359063850418177` | 0.87 | 300.0 |  | 0.12 | 22.6 | 15.42 | no closed form reproduces reported Tc | Electron-phonon coupling superconductivity in  |
| `813327028710277120` | 0.84 | 478.0 |  | 0.1 | 20.1 | 24.67 | no closed form reproduces reported Tc | High-Pressure Structures of Disilane and Their |
| `867746645356315608` | 0.67 | 862.0 |  | 0.1 | 20.0 | 26.85 | no closed form reproduces reported Tc | Superconductivity in Diamond-like BC3 Phase: A |
| `867765895215186065` | 1.12 | 470.0 |  | 0.3 | 15.0 | 11.09 | no closed form reproduces reported Tc | Electron-phonon interaction in the solid form  |
| `812688058997538816` | 1.0 | 200.0 |  | 0.1 | 9.6 | 13.93 | no closed form reproduces reported Tc | Doping induced charge density wave in monolaye |
| `867749749405515980` | 0.16 | 230.9 |  | 0.1 | 8.8 |  | no closed form reproduces reported Tc | Quasiparticle dynamics and phonon softening in |
| `811709692383330305` | 0.83 | 200.0 |  | 0.13 | 6.8 | 8.25 | no closed form reproduces reported Tc | Superconductivity and electron-phonon coupling |
| `811684389233623042` | 0.99 | 65.0 |  | 0.12 | 5.93 | 4.29 | no closed form reproduces reported Tc | First-principles study of electron-phonon supe |
| `812318459089125376` | 0.43 | 1023.0 |  | 0.13 | 4.0 | 3.19 | no closed form reproduces reported Tc | Role of the Dopant in the Superconductivity of |
| `811906093474119682` | 0.58 | 113.0 |  | 0.12 | 2.6 | 1.88 | no closed form reproduces reported Tc | Electron-phonon superconductivity in LaNiPO |
| `813219863777509378` | 0.42 | 94.5 |  | 0.1 | 0.77 | 0.53 | no closed form reproduces reported Tc | Electron–phonon superconductivity in YIn 3 |
