# Reproduction audit

Two independent axes, both catalogued (not discarded).

## A. Computed Tc reproducible, but disagrees with EXPERIMENT

The computed Tc is reproducible from the paper's parameters, but the *computed* value
differs from the *measured* Tc by >30% — the closed form is inadequate (strong coupling
needs full Eliashberg) or pair-breaking suppresses the real Tc.

25 papers:

| paper_id | method | computed Tc (K) | experimental Tc (K) | computed/exp | material |
|---|---|---|---|---|---|
| `867761419615994028` | mcmillan | 39.3 | 0.026 | 1511.54× | beryllium-based alloys (Be-Pb, Be- |
| `867769693774021285` | allen-dynes-basic | 32.27 | 4 | 8.07× | Field-effect hole-doped hydrogenat |
| `812549822006427649` | allen-dynes-basic | 10.1 | 2.8 | 3.61× | Lanthanum at megabar pressures (R- |
| `867757683732643869` | allen-dynes-basic | 17.8 | 6 | 2.97× | K2Cr3As3 (noncentrosymmetric quasi |
| `814582504823455745` | allen-dynes-basic | 17 | 6 | 2.83× | K2Cr3As3 (noncentrosymmetric quasi |
| `812127705880330240` | mcmillan | 12 | 4.45 | 2.7× | cubic perovskite Sc3InB (vs MgCNi3 |
| `811188275547996162` | allen-dynes-basic | 2.3 | 1.2 | 1.92× | Titanium-oxypnictides BaTi2Pn2O (P |
| `811607029712945153` | mcmillan | 20.4 | 11.2 | 1.82× | NbC1-xNx / NbN^x (rock-salt carbon |
| `867756062256660659` | allen-dynes-basic | 4.23 | 2.55 | 1.66× | ThCoC2 (noncentrosymmetric, strong |
| `814639645122887682` | allen-dynes-basic | 3.81 | 2.4 | 1.59× | body-centered-tetragonal YC2 and L |
| `812322173833183232` | mcmillan | 11.03 | 7 | 1.58× | hcp Li at 247 kbar (high pressure) |
| `867762315619991562` | allen-dynes-basic | 16.4 | 10.4 | 1.58× | K2Mo3As3 |
| `867765509788008942` | mcmillan | 62 | 39.5 | 1.57× | MgB2 (sp-valent diborides; AlB2, N |
| `811048440174739456` | allen-dynes-basic | 7.01 | 4.5 | 1.56× | bcc tantalum (Ta) |
| `814655275444207618` | allen-dynes-basic | 2.92 | 2.15 | 1.36× | NaBi (topological metal, body-cent |
| `814519204332961793` | allen-dynes-basic | 6.15 | 8 | 0.77× | Sb2Se3 (orthorhombic Pnma) under h |
| `813282992469311488` | allen-dynes-basic | 5.4 | 8 | 0.68× | APt3P (A=Ca,Sr,La); Tc focus on Sr |
| `867754418865439090` | allen-dynes-basic | 3.66 | 6.5 | 0.56× | nH-CaAlSi (1H/5H/6H stacking varia |
| `812325968965271553` | allen-dynes-basic | 2.3 | 6 | 0.38× | 2H-NbS2 (layered transition-metal  |
| `813030422085632000` | mcmillan | 2 | 8.5 | 0.24× | LaFeSiHx (Fe-based, single-stripe  |
| `813272662255075331` | allen-dynes-basic | 1.1 | 8 | 0.14× | FeSe and KFe2Se2 (checkerboard AFM |
| `813170535063093254` | allen-dynes-basic | 3.2 | 30 | 0.11× | Ba0.5K0.5BiO3 (Ba1-xKxBiO3) |
| `811908196133240832` | allen-dynes-basic | 0.15 | 3 | 0.05× | CaSi2 (phase III corrugated trigon |
| `811791191132602369` | allen-dynes-basic | 0.3 | 6.8 | 0.04× | BaSi2 (trigonal P-3m1, ambient pre |
| `867749749405515980` | mcmillan | 0.08 | 8.8 | 0.01× | FeSe single crystal (ultrafast pum |

## B. Could not reproduce the paper's own COMPUTED Tc

For these per-condition data points, the method the paper reports (with its μ\*) does not
reproduce the computed Tc (>15%). Causes: non-standard prefactor / custom-fit coefficients,
the paper actually solving full Eliashberg, a Debye-vs-log frequency mismatch, or a residual
mis-pairing. Flagged, not used as gold.

65 per-condition points:

| paper_id | condition | method | λ | freq (K) | μ* | formula Tc (K) | paper computed Tc (K) |
|---|---|---|---|---|---|---|---|
| `867747407591375067` | YH9 P6_3/mmc-1 clathra | eliashberg | 2.9 | 790 | 0.1 | 140.013 | 250 |
| `867747407591375067` | YH9 P6_3/mmc-1 clathra | eliashberg | 2.06 | 1255 | 0.1 | 184.144 | 234 |
| `867747407591375067` | YH9 Pnma 210 GPa | eliashberg | 2.19 | 1153 | 0.1 | 175.94 | 233 |
| `811677132345311232` | (single) | mcmillan | 1.5 | 1830 | 0.1 | 172.642 | 210 |
| `867756901285233340` | (single) | mcmillan | 1.5 | 1830 | 0.1 | 172.642 | 210 |
| `867747407591375067` | YH9 Pnma 160 GPa | eliashberg | 2.26 | 890 | 0.1 | 138.433 | 191 |
| `812698038379216897` | CeH10 (Fm-3m) 94 GPa,  | allen-dynes-f1f2 | 1.952 | 1188.912 | 0.1 | 203.437 | 168 |
| `811940808310652928` | Cmca H2 428 GPa | mcmillan | 1.19 | 1826 | 0.1 | 133.897 | 162 |
| `812024758601252865` | (single) | mcmillan | 1.19 | 1826 | 0.1 | 133.897 | 162 |
| `812698038379216897` | CeH9 (F-43m) 94 GPa, m | allen-dynes-f1f2 | 1.596 | 1181.379 | 0.1 | 164.5 | 142 |
| `811940808310652928` | Cmca H2 388 GPa | mcmillan | 1.02 | 1818 | 0.1 | 107.975 | 130 |
| `1102596319534383170` | Li2AgH6 harmonic DFPT, | eliashberg | 3.783 | 338 | 0.1 | 66.569 | 110.6 |
| `811940808310652928` | Cmca H2 347 GPa | mcmillan | 0.91 | 1784 | 0.1 | 88.155 | 107 |
| `811671572849885185` | C6 fictitious charge - | allen-dynes-basic | 1.94 | 471 | 0.1 | 66.325 | 80 |
| `867763386249642555` | Li_xBC, x=0.125 (max h | mcmillan | 1.43 | 608 | 0.09 | 56.443 | 68 |
| `867765895215186065` | NaC22, mu*=0.1 | mcmillan | 1.12 | 676.2 | 0.1 | 45.853 | 55 |
| `867765509788008942` | MgB2 equilibrium volum | mcmillan | 0.835 | 700 | 0.1 | 29.557 | 39.5 |
| `812434237373284353` | (single) | mcmillan | 0.91 | 861 | 0.15 | 31.354 | 39.4 |
| `867767689039315155` | FCC CuN | allen-dynes-basic | 3.099 | 124.2 | 0.1 | 22.665 | 39.29 |
| `812276374067740672` | MgB2, HGH relativistic | mcmillan | 0.87 | 540 | 0.05 | 32.061 | 39.2 |
| `812346987746689024` | B13C2, mu*=0.10 | mcmillan | 0.81 | 763.5 | 0.1 | 30.365 | 36.7 |
| `814553717972926464` | NaB1.1C0.9 (10% B-for- | mcmillan | 0.73 | 903 | 0.1 | 28.71 | 35 |
| `813327028710277120` | Cmcm 100 GPa | allen-dynes-basic | 0.84 | 687.7 | 0.1 | 35.492 | 24.6 |
| `811607029712945153` | NbN^0.5 charged model  | mcmillan | 1.943 | 145 | 0.1 | 16.917 | 20.4 |
| `867746645356315608` | t-BC3 5 GPa | allen-dynes-basic | 0.67 | 1240.2 | 0.13 | 28.992 | 20 |
| `813327028710277120` | Cmcm 140 GPa | allen-dynes-basic | 0.68 | 795.6 | 0.1 | 25.745 | 17.9 |
| `867746645356315608` | t-BC3 10 GPa | allen-dynes-basic | 0.66 | 1097.8 | 0.13 | 24.483 | 17.5 |
| `813327028710277120` | Cmcm 160 GPa | allen-dynes-basic | 0.66 | 800 | 0.1 | 23.96 | 16.7 |
| `813327028710277120` | Cmcm 200 GPa | allen-dynes-basic | 0.68 | 720.8 | 0.1 | 23.324 | 16.2 |
| `813327028710277120` | Cmcm 220 GPa | allen-dynes-basic | 0.76 | 552.5 | 0.1 | 23.233 | 16.1 |
| `812030861221298177` | CaC6, 100 kbar (10 GPa | mcmillan | 1.03 | 230 | 0.145 | 11.048 | 13.5 |
| `812030861221298177` | CaC6, 50 kbar (5 GPa) | mcmillan | 0.86 | 300 | 0.145 | 9.962 | 12 |
| `812127705880330240` | Sc3InB stoichiometric  | mcmillan | 0.94 | 226.3 | 0.13 | 9.998 | 12 |
| `812030861221298177` | CaC6, 0 kbar (ambient) | mcmillan | 0.84 | 305 | 0.145 | 9.58 | 11.4 |
| `811607029712945153` | NbC (x=0, N_F=0.361) | mcmillan | 0.682 | 345 | 0.1 | 9.308 | 11.2 |
| `867768706984313394` | (single) | mcmillan | 0.83 | 287 | 0.14 | 9.098 | 11 |
| `867772889959498403` | Li2B2 0 GPa | mcmillan | 0.57 | 942.9 | 0.14 | 8.904 | 10.95 |
| `812830786389540865` | amorphous Ga | allen-dynes-basic | 1.62 | 55 | 0.1 | 6.723 | 8.03 |
| `1233736905573531652` | (single) | allen-dynes-basic | 0.5 | 653.3 | 0.07 | 11.929 | 8 |
| `812830786389540865` | amorphous SnCu | allen-dynes-basic | 1.82 | 39.6 | 0.04 | 6.086 | 7.8 |
| `811978101436186627` | bcc Ta (Allen-Dynes, m | mcmillan | 0.877 | 150.8 | 0.13 | 5.801 | 7.01 |
| `867748099894805062` | (single) | mcmillan | 0.57 | 453 | 0.12 | 5.688 | 7 |
| `812830786389540865` | amorphous PbCu | allen-dynes-basic | 2.01 | 29.1 | 0.04 | 4.75 | 6.33 |
| `812830786389540865` | amorphous Bi | allen-dynes-basic | 2.46 | 28.3 | 0.1 | 4.62 | 6.06 |
| `811684389233623042` | (single) | mcmillan | 0.99 | 93.5 | 0.12 | 4.795 | 5.93 |
| `812830786389540865` | amorphous InSb | allen-dynes-basic | 1.69 | 38.6 | 0.1 | 4.891 | 5.84 |
| `813005060060479488` | Ga 2 ML / GaN(0001), N | allen-dynes-basic | 1.18 | 70.5 | 0.1 | 6.181 | 5.1 |
| `812127705880330240` | Sc3InB0.93 (7% B defic | mcmillan | 0.62 | 226.3 | 0.13 | 3.392 | 4 |
| `812318459089125376` | (single) | mcmillan | 0.43 | 1472 | 0.135 | 3.257 | 4 |
| `814655275444207618` | NaBi with SOC | allen-dynes-basic | 0.84 | 55.7 | 0.1 | 2.875 | 3.75 |
| `814655275444207618` | NaBi without SOC | allen-dynes-basic | 0.72 | 58.8 | 0.1 | 2.188 | 2.59 |
| `812595503937093633` | bcc Li | mcmillan | 0.51 | 180 | 0.12 | 1.434 | 1.73 |
| `812507119646408706` | Mo3Ir (A-15) | allen-dynes-f1f2 | 0.54 | 242.7 | 0.15 | 1.854 | 1.6 |
| `1056817631564136450` | IrO3, R-3c, 30 GPa, no | allen-dynes-basic | 0.401 | 478 | 0.1 | 2.036 | 1.4 |
| `812745012499447809` | unstrained monolayer t | allen-dynes-basic | 0.22 | 242.6 | 0.1 | 0.001 | 1 |
| `867747199868470067` | OsN2 pristine | allen-dynes-basic | 0.37 | 280 | 0.1 | 0.73 | 1 |
| `813060109180600320` | (single) | allen-dynes-basic | 0.41 | 193 | 0.08 | 1.412 | 0.76 |
| `812595503937093633` | 9R Li | mcmillan | 0.41 | 200 | 0.12 | 0.485 | 0.58 |
| `811908196133240832` | corrugated trigonal ph | allen-dynes-basic | 0.27 | 300 | 0.1 | 0.045 | 0.15 |
| `813282992469311488` | corrugated trigonal ph | allen-dynes-basic | 0.27 | 300 | 0.1 | 0.045 | 0.15 |
| `867772889959498403` | Li2B2 10 GPa | mcmillan | 0.32 | 1090.2 | 0.14 | 0.091 | 0.11 |
| `1068413857002684417` | Ba2IrH6 at 20 GPa | allen-dynes-basic | 0.27 | 1077.48 | 0.1 | 0.162 | 0.1 |
| `867772889959498403` | Li2B2 20 GPa | mcmillan | 0.22 | 1213.5 | 0.14 | 0.0 | 0.07 |
| `814700620282855425` | (single) | allen-dynes-basic | 0.17 | 459.25 | 0.14 | 0.0 | 0.01 |
| `867772526099431971` | Ti2CH2 monolayer | allen-dynes-basic | 0.12895 | 530.139 | 0.1 |  | 0 |
