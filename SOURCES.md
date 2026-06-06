# Case provenance (LKM-grounded)

Each case's parameters and method were read from the paper's LKM knowledge-graph
nodes (not regex). A case enters the benchmark only if the formula it actually used,
with the **paper's own μ\***, reproduces the paper's **computed** Tc (within 15%).
Gold = that deterministic formula output. See [`REPRODUCTION.md`](REPRODUCTION.md)
for papers whose computed Tc disagrees with experiment, or that we couldn't reproduce.

## L0 — McMillan (Θ_D/1.45)  (7 cases)

| case | split | source paper_id | λ | Θ_D/freq (K) | μ* | gold Tc (K) | material |
|---|---|---|---|---|---|---|---|
| `L01` | dev | `867764510792876439` | 0.842 | 127.77 | 0.13 | 4.502 | Bi3Ni (bulk) |
| `L02` | hidden | `812737475888807939` | 0.4 | 623 | 0.06 | 4.878 | Silicon high-pressure metallic |
| `L03` | dev | `812322173833183232` | 0.806 | 265 | 0.1 | 10.435 | hcp Li at 247 kbar (high press |
| `L04` | dev | `867747957653373759` | 0.85 | 260 | 0.1 | 11.358 | LaO0.5F0.5BiS2 (layered BiS2 s |
| `L05` | hidden | `811998282417963010` | 0.62 | 626.6 | 0.1 | 13.067 | Layered LiB (MS1 structure) |
| `L06` | dev | `811736896852983809` | 0.75 | 1050 | 0.094 | 37.06 | MgB2 (hexagonal) |
| `L07` | dev | `812276374067740672` | 0.87 | 540 | 0 | 39.829 | MgB2 |

## L1 — basic Allen-Dynes (ω_log/1.2)  (100 cases)

| case | split | source paper_id | λ | ω_log (K) | μ* | gold Tc (K) | material |
|---|---|---|---|---|---|---|---|
| `L01` | dev | `867757942403760362` | 0.29 | 100 | 0.13 | 0.005 | LiFeAs and NaFeAs (iron-based  |
| `L02` | hidden | `811791191132602369` | 0.33 | 240 | 0.1 | 0.272 | BaSi2 (trigonal P-3m1, ambient |
| `L03` | dev | `812383700997111808` | 0.33 | 450 | 0.1 | 0.51 | non-magnetic hcp iron (Fe) at  |
| `L04` | dev | `811870490523074563` | 0.38 | 172.86 | 0.1 | 0.533 | Monatomic iodine under (non)hy |
| `L05` | hidden | `812774568677605378` | 0.38 | 111.4 | 0.07 | 0.698 | YIn3 (cubic AuCu3-type) under  |
| `L06` | dev | `813219863777509378` | 0.42 | 135.9 | 0.1 | 0.745 | YIn3 (AuCu3 structure) |
| `L07` | dev | `867751696124608720` | 0.334 | 494 | 0.09 | 0.873 | Nb(1-x)B2 (NbB2 and vacancy se |
| `L08` | hidden | `867761305644171944` | 0.65 | 60.97 | 0.13 | 1.295 | Doped stanene (Li- and Ca-deco |
| `L09` | dev | `867747545399427399` | 0.41 | 280 | 0.1 | 1.349 | CaSi2 in high-pressure AlB2 ph |
| `L10` | dev | `811685820145598464` | 0.72 | 56.86 | 0.14 | 1.494 | Monolayer Pb on Si(111) (strip |
| `L11` | hidden | `814537145015336960` | 0.47 | 235.81 | 0.12 | 1.534 | SrAuSi3 (I4mm) and SrAu2Si2 (I |
| `L12` | dev | `813254743873814530` | 0.65 | 57.61 | 0.1 | 1.656 | 2D TiB4 monolayer and bilayer  |
| `L13` | dev | `814617345912733702` | 0.51 | 158.3 | 0.11 | 1.79 | Ca3Ir4Ge4 (noncentrosymmetric  |
| `L14` | hidden | `814721288294629376` | 0.78 | 105.5 | 0.2 | 1.908 | SrPtAs (hexagonal pnictide, P6 |
| `L15` | dev | `867772751660712031` | 0.54 | 143 | 0.1 | 2.318 | Mo3Sb7 |
| `L16` | dev | `812325968965271553` | 0.554 | 131.4 | 0.1 | 2.327 | 2H-NbS2 (layered transition-me |
| `L17` | hidden | `811968721915478016` | 0.52 | 169 | 0.1 | 2.389 | rock-salt YS (yttrium sulfide) |
| `L18` | dev | `813152122194362369` | 0.61 | 145.5 | 0.13 | 2.488 | YIr2Si2 and LaIr2Si2 (high-tem |
| `L19` | dev | `811906093474119682` | 0.58 | 162.7 | 0.12 | 2.632 | LaNiPO (layered Ni oxypnictide |
| `L20` | hidden | `812600623223537667` | 0.59 | 140.6 | 0.1 | 3.055 | Noncentrosymmetric superconduc |
| `L21` | dev | `867774180848828479` | 0.52 | 297.8 | 0.12 | 3.123 | Non-centrosymmetric LaNiC2 |
| `L22` | dev | `814601823489884160` | 0.64 | 155 | 0.13 | 3.128 | SnAs (rock-salt / NaCl structu |
| `L23` | hidden | `867772526099431971` | 0.556 | 179.7 | 0.1 | 3.213 | Monolayer Mo2C MXene (2H phase |
| `L24` | dev | `812454340861100036` | 0.74 | 86.3 | 0.1 | 3.42 | BEDT-TTF organic superconducto |
| `L25` | dev | `814639645122887682` | 0.55 | 300.12 | 0.13 | 3.424 | body-centered-tetragonal YC2 a |
| `L26` | hidden | `811893892143120386` | 0.8 | 89.41 | 0.12 | 3.647 | CdCNi3 (cubic antiperovskite,  |
| `L27` | dev | `867754418865439090` | 0.6 | 160 | 0.1 | 3.66 | nH-CaAlSi (1H/5H/6H stacking v |
| `L28` | dev | `813228976360128513` | 0.52 | 376 | 0.12 | 3.944 | boronitride superconductors La |
| `L29` | hidden | `812489993686614016` | 0.55 | 347.32 | 0.13 | 3.963 | YC2 (yttrium dicarbide, CaC2-t |
| `L30` | dev | `813207569110663169` | 0.53 | 306 | 0.11 | 4.039 | Cr3GaN antiperovskite under pr |
| `L31` | dev | `814627375626059776` | 0.96 | 76.1 | 0.13 | 4.226 | hexagonal BaSn5 (P6/mmm) |
| `L32` | hidden | `867752213492007190` | 0.653 | 224.3 | 0.13 | 4.835 | Rock-salt LaO (bulk + strained |
| `L33` | dev | `812601801109929984` | 0.79 | 119.45 | 0.1 | 5.455 | Filled skutterudites MPt4Ge12  |
| `L34` | dev | `813009572703764480` | 1.29 | 69.5 | 0.15 | 5.608 | YSn3 (cubic AuCu3-type, Pm-3m) |
| `L35` | hidden | `811795868670754816` | 1.06 | 85 | 0.12 | 5.885 | elemental lanthanum (fcc and d |
| `L36` | dev | `813094079012274176` | 1.05 | 100.97 | 0.15 | 5.902 | CaIr2 and CaRh2 (cubic C15 Lav |
| `L37` | dev | `884073293311640172` | 0.72 | 209 | 0.13 | 6.034 | Nb4CoSi and Ta4CoSi (ternary s |
| `L38` | hidden | `813231154529304578` | 1.06 | 81.35 | 0.1 | 6.177 | SrPt3P (antiperovskite; series |
| `L39` | dev | `811709692383330305` | 0.66 | 288 | 0.13 | 6.423 | fcc lithium under high pressur |
| `L40` | dev | `867750509996409561` | 1.01 | 206.8 | 0.23 | 6.44 | Honeycomb borophene h-B2 on Al |
| `L41` | hidden | `923643931596423577` | 0.97 | 141.13 | 0.16 | 6.666 | TlTaSe2 (nodal-line semimetal, |
| `L42` | dev | `814547623011680264` | 0.68 | 216.27 | 0.1 | 6.998 | NaAlSi (anti-PbFCl-type ternar |
| `L43` | dev | `811048440174739456` | 0.877 | 150.8 | 0.13 | 7.01 | bcc tantalum (Ta) |
| `L44` | hidden | `812489714396299266` | 0.93 | 120.15 | 0.11 | 7.053 | Mg2Ir3Si (Ir Kagome network, P |
| `L45` | dev | `867756414980849698` | 0.93 | 122 | 0.1 | 7.56 | Zr2Ir (body-centered tetragona |
| `L46` | dev | `812798558582341635` | 0.78 | 216.97 | 0.13 | 7.725 | filled skutterudites YRu4P12,  |
| `L47` | hidden | `812688058997538816` | 1.78 | 72.6 | 0.1 | 9.59 | Monolayer 1T-TiS2 (electron-do |
| `L48` | dev | `812549822006427649` | 0.69 | 288 | 0.1 | 9.667 | Lanthanum at megabar pressures |
| `L49` | dev | `867770734955462927` | 0.77 | 225 | 0.1 | 9.733 | high-pressure tin-sulfide comp |
| `L50` | hidden | `813203421422157825` | 0.795 | 418 | 0.18 | 10.034 | Simple cubic (sc) phosphorus u |
| `L51` | dev | `812552562543689728` | 0.84 | 213.35 | 0.11 | 10.34 | ScRuSi and ZrRhSi (orthorhombi |
| `L52` | dev | `812125933258407937` | 0.83 | 286.6 | 0.14 | 10.978 | bulk C6Ca (CaC6 graphite inter |
| `L53` | hidden | `813198240718520323` | 0.591 | 388.8 | 0.07 | 11.478 | AlH3 cubic Pm-3n phase (73-165 |
| `L54` | dev | `811126087244316673` | 0.73 | 301.23 | 0.1 | 11.572 | La3Ni2B2N3 (quaternary boronit |
| `L55` | dev | `943000233191669804` | 0.79 | 261 | 0.1 | 11.918 | Elemental scandium (high press |
| `L56` | hidden | `867765649085038612` | 2.531 | 80.91 | 0.12 | 12.921 | Zr (alpha hcp, omega, beta bcc |
| `L57` | dev | `870263214510702950` | 0.92 | 249 | 0.1 | 15.149 | Niobium nitrides Nb2N (4 polym |
| `L58` | dev | `811740615149617152` | 0.61 | 789 | 0.12 | 15.218 | AlH3 (Pm-3n, ~109 GPa) |
| `L59` | hidden | `867762315619991562` | 1.92 | 123 | 0.12 | 16.401 | K2Mo3As3 |
| `L60` | dev | `813217096233123840` | 0.76 | 439 | 0.11 | 17.153 | Compressed elemental sulfur (S |
| `L61` | dev | `814582504823455745` | 3 | 102.2 | 0.12 | 17.793 | K2Cr3As3 (noncentrosymmetric q |
| `L62` | hidden | `867757683732643869` | 3 | 102.2 | 0.12 | 17.793 | K2Cr3As3 (noncentrosymmetric q |
| `L63` | dev | `867766648835146368` | 0.98 | 269 | 0.1 | 18.153 | NbN polytypes (delta, epsilon, |
| `L64` | dev | `867760796275311043` | 0.68 | 565.1 | 0.1 | 18.286 | compressed solid benzene molec |
| `L65` | hidden | `811115060788199424` | 1.85 | 203.5 | 0.24 | 18.406 | Nb1-bSnb (A15 Nb3Sn, off-stoic |
| `L66` | dev | `812709013748711424` | 0.69 | 642 | 0.115 | 18.908 | TaH5, monoclinic P2_1/c at 100 |
| `L67` | dev | `867773664412566427` | 0.92 | 314.8 | 0.1 | 19.153 | B2C single-layer (2D monolayer |
| `L68` | hidden | `938859326162862687` | 0.75 | 470.6 | 0.1 | 19.22 | Ca-intercalated AA-stacking bi |
| `L69` | dev | `811176152671453187` | 1.2 | 221.3 | 0.1 | 19.812 | Blue-phosphorus bilayer with L |
| `L70` | dev | `1056817631564136450` | 0.95 | 347 | 0.12 | 20.009 | Transition-metal trioxides XO3 |
| `L71` | hidden | `814602831179808769` | 1.48 | 182 | 0.1 | 20.483 | RM2B2C borocarbides: LaPt2B2C, |
| `L72` | dev | `817359063850418177` | 0.87 | 413.8 | 0.1 | 22.807 | 2D MB6 monolayers (Mg,Ca,Ti,Y, |
| `L73` | dev | `813327028710277120` | 0.84 | 478 | 0.1 | 24.67 | Disilane Si2H6, metallic Cmcm  |
| `L74` | hidden | `811679993317818370` | 0.934 | 396 | 0.1 | 24.716 | Ca-VI (Pnma calcium, high pres |
| `L75` | dev | `867768967756775707` | 0.934 | 396 | 0.1 | 24.716 | Ca-VI (orthorhombic Pnma, high |
| `L76` | dev | `812509483795218435` | 1.31 | 291 | 0.1 | 28.867 | ternary S-P-H alloy hydrides ( |
| `L77` | hidden | `811903513046024196` | 0.73 | 903 | 0.1 | 34.691 | Hole-doped NaBC (NaB1.1C0.9),  |
| `L78` | dev | `867769693774021285` | 0.81 | 971 | 0.135 | 36.448 | Field-effect hole-doped hydrog |
| `L79` | dev | `813214614123708416` | 0.75 | 901 | 0.1 | 36.798 | Hole-doped LiBC via Be substit |
| `L80` | hidden | `867746414900282231` | 1.01 | 652 | 0.13 | 39.651 | MgB2 (multiband, two-gap analy |
| `L81` | dev | `811646046894555139` | 1.01 | 652.1 | 0.13 | 39.657 | MgB2 (multiband, beyond-Eliash |
| `L82` | dev | `812654281252405248` | 0.83 | 1251.7 | 0.15 | 44.377 | doped C60 fullerides A3C60 (al |
| `L83` | hidden | `812998475275829248` | 0.9 | 812.5 | 0.1 | 47.589 | At-H system (AtH2: Cmcm/Pnma;  |
| `L84` | dev | `813087272097284096` | 1.13 | 614 | 0.1 | 50.908 | FeH5 (tetragonal I4/mmm) at 13 |
| `L85` | dev | `867761622720971643` | 1.4 | 506 | 0.1 | 53.885 | Monolayer Mg2B4C2 (2D MgB2-lik |
| `L86` | hidden | `812473244324986880` | 1.4 | 506 | 0.1 | 53.885 | Monolayer Mg2B4C2 (2D MgB2-der |
| `L87` | dev | `867747555490923056` | 1.53 | 530.2 | 0.093 | 62.811 | stoichiometric Li2B3C (MgB2-an |
| `L88` | dev | `814565865667166209` | 1.02 | 1027 | 0.115 | 68.574 | SnH4, C2/m phase (high pressur |
| `L89` | hidden | `814544077151272962` | 1.186 | 898 | 0.13 | 70.121 | H5S2 (sulfur hydride, P1 phase |
| `L90` | dev | `867762423082254784` | 1.139 | 859 | 0.1 | 71.97 | I-4m2 SnH8 (Sn-H hydride) unde |
| `L91` | dev | `812042380692684801` | 0.85 | 1472 | 0.1 | 77.699 | halogen(F)-doped carbon clathr |
| `L92` | hidden | `867765680290660591` | 1.188 | 919 | 0.1 | 81.257 | Tin hydrides SnH8, SnH12, SnH1 |
| `L93` | dev | `814547043904126978` | 1.188 | 919 | 0.1 | 81.257 | Tin hydrides SnH8, SnH12, SnH1 |
| `L94` | dev | `867768106380952491` | 1.46 | 837 | 0.1 | 92.962 | Ternary lanthanum borohydrides |
| `L95` | hidden | `814559975392149507` | 1.46 | 929.1 | 0.1 | 103.191 | Tellurium hydrides (H4Te, H5Te |
| `L96` | dev | `867763770720518898` | 1.214 | 1342.51 | 0.1 | 121.908 | C2/m KYH8 (K-Y-H ternary hydri |
| `L97` | dev | `813179722505650176` | 1.82 | 989 | 0.13 | 123.228 | GeH3 (A15, P4_2/mmc, Cccm) at  |
| `L98` | hidden | `867768886924149296` | 1.38 | 1580 | 0.1 | 165.768 | H3S and H3P, Im-3m bcc, a=3.0  |
| `L99` | dev | `1068413857002684417` | 3.04 | 927.52 | 0.1 | 167.869 | X2MH6 hydrides (X=Mg/Ca/Sr/Ba, |
| `L100` | dev | `811682811466481665` | 2.17 | 1870.04 | 0.1 | 283.731 | Monatomic metallic hydrogen, I |

## L2 — Allen-Dynes + f1/f2  (8 cases)

| case | split | source paper_id | λ | ω_log (K) | μ* | gold Tc (K) | material |
|---|---|---|---|---|---|---|---|
| `L01` | dev | `812507119646408706` | 2.68 | 56.17 | 0.15 | 11.097 | A-15 X3Y compounds (X=V,Cr,Mo; |
| `L02` | hidden | `867770070204416334` | 0.701 | 511.7 | 0.1 | 18.604 | LaPtH6 (ternary hydride, R-3m, |
| `L03` | dev | `1096665832190115840` | 0.701 | 511.7 | 0.1 | 18.604 | LaPtH6 (ternary hydride, R-3m, |
| `L04` | dev | `811680235903778817` | 1.28 | 215.9 | 0.13 | 20.414 | A15 V3Si |
| `L05` | hidden | `867754756150395675` | 0.95 | 482.84 | 0.1 | 33.101 | HPC3 (2D hydrogenated phosphor |
| `L06` | dev | `867760184875811501` | 3 | 327 | 0.1 | 81.854 | (Ce,La)H9 (ordered P-6m2, Ce:L |
| `L07` | dev | `867750354362564780` | 2.01 | 799 | 0.1 | 140.61 | CS2H10 (CH4-intercalated H3S,  |
| `L08` | hidden | `812581407606964224` | 2.53 | 1400 | 0.1 | 303.458 | Mg0.5Ca0.5H6 (Im-3m sodalite c |
