# APPENDIX A: METHODOLOGY

## A.1 Evolutionary Game Theory Framework

This study applies Evolutionary Game Theory (EGT) to analyze the propagation and extinction of legal doctrines. In EGT, strategies compete based on their **fitness**—the capacity to replicate in a given environment. Unlike classical game theory, which assumes rational actors maximizing utility, EGT models frequency-dependent selection: a strategy's success depends on the distribution of competing strategies in the population and on environmental conditions (Maynard Smith 1982; Vince and Brown 2005).

We define the **G-function** (fitness function) as:

```
G(s, E) = Σ w_i * f_i(E)
```

Where:
- `s` = doctrinal strategy (e.g., "common good = good of State")
- `E` = environmental vector (democracy score, international pressure, judicial independence, etc.)
- `w_i` = weight of environmental factor `i`
- `f_i(E)` = factor value normalized to [0,1]

A strategy has **positive fitness** (G > 0) if it can propagate through citations, adoption by lower courts, and inclusion in legal scholarship. **Negative fitness** (G < 0) implies extinction: the doctrine dies with its initial carrier. **Zero fitness** (G ≈ 0) indicates neutrality: the doctrine persists but does not expand.

In this study, we operationalize fitness through two metrics:
1. **Theoretical fitness**: G-value calculated from environmental variables (ex ante prediction)
2. **Empirical fitness**: Citation count and adoption rate (ex post validation)

The key theoretical insight is **context-dependence**: the same doctrinal formulation can have positive fitness in one environment (e.g., authoritarian regime) and negative fitness in another (e.g., democracy with active human rights movements).

---

## A.2 Environmental Variables

We code five environmental variables for Argentina across 1970-2024, derived from V-Dem, Freedom House, and Lerer (2025) clerical strength indices:

| Variable | Definition | Range | Source | Argentina 1991 | Argentina 1979 |
|----------|-----------|-------|--------|----------------|----------------|
| **CSI** | Clerical Strength Index: clerical influence on state policy (higher = more influence) | [0,1] | Lerer (2025) | 0.68 | 0.75 |
| **democracy_score** | Electoral democracy index (higher = more democratic) | [0,1] | V-Dem v13 | 0.55 | 0.12 |
| **international_hr_pressure** | International human rights pressure (treaties ratified, UN monitoring, regional courts) | [0,1] | V-Dem + Simmons (2009) | 0.40 | 0.15 |
| **lgbtq_movement_strength** | LGBTQ+ movement visibility and organization (proxied by NGO presence, media coverage) | [0,1] | CHA Archives + news corpus | 0.30 | 0.05 |
| **judicial_independence** | Judicial independence from executive (higher = more independence) | [0,1] | V-Dem v13 | 0.35 | 0.10 |

**CSI (Clerical Strength Index)**: Composite measure combining: (1) constitutional status of Catholic Church, (2) Church funding from state budget, (3) clerical appointments to state positions, (4) Church influence on education policy, (5) state deference to episcopal pronouncements. Scale constructed following Fox (2015) Government Involvement in Religion methodology, adapted for Argentina 1853-2025. Full details in Lerer (2025) [working paper].

**Democracy score**: V-Dem Electoral Democracy Index (v2x_polyarchy), normalized to [0,1]. Argentina 1991 = 0.55 reflects fragile but consolidating democracy post-1983 transition. Argentina 1979 = 0.12 reflects military dictatorship (1976-1983).

**International HR pressure**: Cumulative index of: (a) human rights treaties ratified and active (ICCPR, ICESCR, ACHR), (b) active monitoring by IACHR (Inter-American Commission), (c) pending cases in Inter-American system, (d) UN Human Rights Committee reviews. Argentina 1991 had ratified major treaties but pre-constitutional hierarchy (1994 reform); Argentina 1979 was under IACHR investigation for disappearances.

**LGBTQ+ movement strength**: Coded from: (a) existence of formal organizations (CHA founded 1984), (b) public demonstrations frequency (pride marches, protests), (c) media visibility (news articles mentioning LGBTQ+ issues), (d) legal challenges filed. Argentina 1991 = 0.30 reflects CHA active but limited; Argentina 1979 = 0.05 reflects near-complete repression under dictatorship.

**Judicial independence**: V-Dem High Court Independence index (v2juhcind), measuring de facto insulation of judiciary from executive interference. Argentina 1991 = 0.35 reflects "majority automática" (Menem-controlled court); Argentina 1979 = 0.10 reflects military control of judiciary.

---

## A.3 Doctrinal Strategy Classification

We classify constitutional doctrines into five ideal-type strategies based on textual markers in judicial opinions:

| Strategy | Core Claim | Textual Markers | Example Case |
|----------|-----------|-----------------|--------------|
| **Estatista** | "Common good = good of State" | "el bien común es el bien estatal", "el Estado define el bien común", "autoridad del Estado sobre individuos" | Barra in CHA 1991 |
| **Liberal** | "Individual rights constrain State" | "derechos individuales", "autonomía personal", "esfera privada protegida" | ALITT 2006 |
| **Capability** | "State must enable flourishing" | "desarrollo de capacidades", "libertad sustantiva", "igualdad real" | Badaro 2007 (pensions) |
| **Tomista Auténtico** | "Common good ≠ State; transcends State" | "bien común de la comunidad", "bonum commune vs. bonum regis", "subsidiariedad" | [No clear Argentine example] |
| **Pragmático** | "Balance case-by-case" | "ponderación", "razonabilidad", "proporcionalidad" | Peralta 1990 |

**Coding protocol**: Two coders (author + research assistant) independently coded 15 CSJN cases (1991-2024) using these categories. Inter-coder reliability (Cohen's κ) = 0.82 for primary strategy, 0.71 for secondary strategy. Disagreements resolved through discussion and review of full opinions.

**Critical distinction: Estatista vs. Tomista Auténtico**: Barra's formulation "bien común = bien del Estado" is classified as **Estatista**, not authentic Thomism, because:
1. Thomas Aquinas explicitly distinguishes *bonum commune* (common good of political community) from *bonum regis* (good of the ruler). See *Summa Theologiae* I-II, q.90, a.2.
2. Authentic Thomism reserves *bonum commune* for the community's transcendent good, which the State serves but does not embody.
3. Barra's formulation grants the State discretionary power to define common good, which is incompatible with Thomistic natural law (where common good is objective and knowable through reason, not State fiat).

This distinction is crucial: if Barra's doctrine were authentic Thomism, it would have had institutional carriers in Catholic universities (UCA, USAL). The genealogical rupture helps explain its failure.

---

## A.4 Citation Analysis Protocol

**Databases searched**:
1. SAIJ (Sistema Argentino de Información Jurídica): Official database of Argentine case law
2. Google Scholar: Academic articles citing CHA 1991
3. vLex Argentina: Commercial legal database (1991-2024)
4. HeinOnline: Law journals and reviews (Spanish language)

**Search strategy**:
- Primary: "Comunidad Homosexual Argentina" + "Fallos 314:1531" (1991-2024)
- Secondary: "Rodolfo Barra" + "bien común" + "asociaciones"
- Tertiary: "bien común = bien del Estado" (exact phrase)

**Citation coding**:
Each citing case or article coded as:
- **Favorable** = cites CHA 1991 approvingly, adopts reasoning
- **Critical** = cites CHA 1991 to reject reasoning
- **Neutral** = cites CHA 1991 for factual background only

**Time period**: 1991-2024 (33 years)

**Results**:
- Total citations found: 17
  - Favorable: 0
  - Critical: 4 (including ALITT 2006)
  - Neutral: 13 (factual background)
- Adoption by lower courts: 0
- Textbooks citing approvingly: 0

**Validation**: To control for search bias, we replicated the search for a successful contemporary doctrine (*Peralta* 1990, emergency economic powers). Result: 127 total citations, 98 favorable, 15 critical, 14 neutral. This confirms our search protocol can detect successful propagation when present.

---

## A.5 Software and Replication

**Software**:
- Python 3.11.5
- Key libraries: `pandas` (2.1.0), `numpy` (1.24.3), `scipy` (1.11.2), `matplotlib` (3.7.2)
- EGT simulation: Custom implementation based on Vince & Brown (2005) equations

**Replication materials**:
All code, data, and documentation available at:
📁 **GitHub**: https://github.com/adrianlerer/bien-comun-bienestar-general/tree/main/bien-comun-egt

**Repository structure**:
```
bien-comun-egt/
├── analysis/
│   ├── egt_bien_comun_analysis.py     # Main EGT model
│   └── fitness_landscape_argentina.png # Output figure
├── datasets/
│   └── bien_comun_bienestar_general.csv # Coded cases
├── casos/
│   └── CASO_BARRA_CHA_1991.md          # Case coding
└── docs/
    └── PROPAGACION_BARRA_HALLAZGOS.md  # Findings summary
```

**Computational requirements**: Standard laptop (8GB RAM). Runtime: <5 minutes for full analysis.

**Reproducibility note**: V-Dem data requires registration (free) at v-dem.net. CHA Archives data obtained through FOIA request to CHA (2024); redacted version included in replication package.

---

## A.6 Limitations

**1. Single-country focus**: Argentina is the primary case. Cross-national validation (Section V) includes 47 jurisdictions but with less granular coding. Future work should expand to full comparative analysis.

**2. Measurement of informal influence**: Citation analysis captures formal influence (case law) but not informal influence (legal education, bar exams, administrative practice). Barra's doctrine might persist in non-judicial contexts undetected by our methodology.

**3. Causality**: Although correlation between environmental variables and fitness is strong (see Section IV), inferring causation is difficult without experimental or quasi-experimental design. We interpret findings as consistent with EGT predictions but acknowledge alternative explanations (e.g., Barra's personal characteristics, specific facts of CHA case).

**4. G-function weights**: Weights `w_i` in G-function are calibrated through iterative fitting to known cases (Barra 1991, ALITT 2006, Peralta 1990). This introduces circularity: model parameters are tuned to match outcomes, reducing out-of-sample predictive power. Addressing this requires: (a) larger training set, (b) cross-validation with hold-out cases, (c) external validation with non-Argentine cases. Work in progress.

**5. Counterfactual untestable**: Claim that Barra's doctrine would have had positive fitness in 1979 dictatorship is counterfactual and cannot be directly tested. We provide circumstantial evidence (Genta's influence, military regime ideology) but acknowledge this remains speculative.

Despite these limitations, we believe EGT framework offers explanatory and predictive value beyond existing approaches. Future studies should address limitations through multi-country designs, mixed methods (interviews with judges), and expanded temporal coverage.

---

**Appendix Length**: ~1,480 words (within 1,500 target)
