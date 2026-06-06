# Reproduction audit

Two distinct things a Tc paper can fail at — kept separate here (and **not** discarded).

## A. Computed Tc reproducible, but it disagrees with EXPERIMENT

The paper's closed-form/computed Tc **is** reproducible from its parameters, but the
*computed* value differs from the *measured* Tc by >30%. This is a real physics signal —
usually the closed form is inadequate (very strong coupling needs full Eliashberg) or
pair-breaking (magnetism/spin-fluctuations/anharmonicity) suppresses the real Tc.

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

Applying the method the paper reports (with its μ\*) does **not** reproduce the paper's
own computed Tc (>15% off). Likely: the method label is approximate, the paper actually
solved full Eliashberg, a multi-condition value was mis-paired, or a parameter is off.
Flagged for review, not used as benchmark gold.

32 papers:

| paper_id | method | λ | freq (K) | μ* | formula Tc (K) | paper computed Tc (K) | material |
|---|---|---|---|---|---|---|---|
| `867759874547646894` | allen-dynes-f1f2 | 3.39 | 3308 | 0.089 | 943.551 | 764 | Atomic metallic hydrogen (I4_1 |
| `867756901285233340` | mcmillan | 1.5 | 1830 | 0.1 | 172.642 | 210 | high-pressure metallic hydroge |
| `811677132345311232` | mcmillan | 1.5 | 1830 | 0.1 | 172.642 | 210 | high-pressure metallic hydroge |
| `812698038379216897` | allen-dynes-f1f2 | 1.952 | 1188.91 | 0.1 | 203.437 | 168 | Cerium hydrides CeH9 (F-43m) a |
| `812024758601252865` | mcmillan | 1.19 | 1826 | 0.1 | 133.897 | 162 | Molecular metallic hydrogen, C |
| `867763386249642555` | mcmillan | 1.43 | 608 | 0.09 | 56.443 | 68 | Hole-doped Li_xBC (layered B-C |
| `814691620430544896` | allen-dynes-basic | 0.65 | 2170 | 0.13 | 46.083 | 62.4 | BeH2 (Cmcm and P4/nmm metallic |
| `867765509788008942` | mcmillan | 0.835 | 700 | 0.1 | 29.557 | 62 | MgB2 (sp-valent diborides; AlB |
| `812434237373284353` | mcmillan | 0.91 | 861 | 0.15 | 31.354 | 39.4 | MgB2 |
| `867761419615994028` | mcmillan | 0.988 | 662 | 0.13 | 32.056 | 39.3 | beryllium-based alloys (Be-Pb, |
| `811802880196476929` | allen-dynes-basic | 0.89 | 1203 | 0.14 | 53.974 | 37 | AlH3 cubic Pm-3n phase, 70-110 |
| `812346987746689024` | mcmillan | 0.81 | 763.5 | 0.1 | 30.365 | 36.7 | Hole-doped B13C2 (boron icosah |
| `867765895215186065` | mcmillan | 1.12 | 676.2 | 0.2 | 27.724 | 33 | Solid C20 fullerene (NaC22; al |
| `812127705880330240` | mcmillan | 0.94 | 226.3 | 0.13 | 9.998 | 12 | cubic perovskite Sc3InB (vs Mg |
| `867768706984313394` | mcmillan | 0.83 | 287 | 0.14 | 9.098 | 11 | C6Ca (Ca-intercalated graphite |
| `867772889959498403` | mcmillan | 0.57 | 922.3 | 0.14 | 8.709 | 10.95 | Li2B2 (MgB2-type layered borid |
| `1233736905573531652` | allen-dynes-basic | 0.5 | 653.3 | 0.07 | 11.929 | 8 | 25% hole-doped infinite-layer  |
| `812745012499447809` | allen-dynes-basic | 0.22 | 242.6 | 0.1 | 0.001 | 7.3 | Monolayer YS (tetragonal P4/nm |
| `867748099894805062` | mcmillan | 0.57 | 453 | 0.12 | 5.688 | 7 | Li2B2 |
| `811999699547455489` | mcmillan | 0.8 | 146.76 | 0.1 | 5.692 | 6.89 | CaAlSi (ternary silicide, AF-l |
| `811684389233623042` | mcmillan | 0.99 | 93.5 | 0.12 | 4.795 | 5.93 | YSn3 (cubic AuCu3 structure, P |
| `813005060060479488` | allen-dynes-basic | 1.18 | 70.5 | 0.1 | 6.181 | 5.1 | Ultrathin Ga films (1-3 ML) on |
| `1160655936889552901` | allen-dynes-basic | 0.38 | 958.6 | 0.1 | 2.964 | 4.7 | A2PdH2 (A=Li,Na,K,Rb,Cs); supe |
| `812318459089125376` | mcmillan | 0.43 | 1472 | 0.135 | 3.257 | 4 | Boron-doped diamond (substitut |
| `867753789745004576` | allen-dynes-basic | 0.658 | 600 | 0.138 | 12.122 | 4 | bulk 1T-MoS2 (under pressure 0 |
| `812652418742353921` | allen-dynes-basic | 0.43 | 942 | 0.1 | 5.83 | 3.43 | AlB2 and MgB2 (comparative fir |
| `817398434037235713` | allen-dynes-basic | 0.67 | 86.6 | 0.1 | 2.698 | 3.3 | Bi4I4 high-pressure phases (ep |
| `814553717972926464` | mcmillan | 0.54 | 143 | 0.1 | 1.918 | 2.4 | Mo3Sb7 (cubic intermetallic) |
| `867747199868470067` | allen-dynes-basic | 0.37 | 280 | 0.1 | 0.73 | 1 | OsN2 (marcasite-like Pnnm), N- |
| `813060109180600320` | allen-dynes-basic | 0.41 | 193 | 0.08 | 1.412 | 0.76 | LaPtBi (half-Heusler, cubic Mg |
| `811908196133240832` | allen-dynes-basic | 0.41 | 280 | 0.1 | 1.349 | 0.15 | CaSi2 (phase III corrugated tr |
| `814700620282855425` | allen-dynes-basic | 0.17 | 459.25 | 0.14 | 0.0 | 0.01 | HfB2 |
