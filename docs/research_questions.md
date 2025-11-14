# Research Questions

## Central Research Question

**RQ:** ¿Los términos legitimadores constitucionales ("bien común", "bienestar general") operan como premisas normativas independientes o como marcadores de identidad memética que predeterminan resultados institucionales?

## Sub-Research Questions

### RQ1: Correlación Término-Resultado

**RQ1.1:** ¿Existe correlación estadísticamente significativa entre el término usado en sentencias judiciales y el resultado del caso?

**RQ1.2:** ¿Esta correlación persiste después de controlar por área legal, composición del tribunal, contexto de crisis, y año?

**Hipótesis asociadas:**
- **H1.1:** "Bien común" predice resultado comunitarista (OR > 2, p < 0.05)
- **H1.2:** "Bienestar general" predice resultado individualista (OR > 2, p < 0.05)
- **H1.3:** El efecto es más fuerte en contextos de crisis (interacción término × crisis)

**Operacionalización:**
- **Variable dependiente:** Resultado codificado binariamente (1=individualista, 0=comunitarista)
- **Variable independiente:** Término usado (bien común / bienestar general / otro)
- **Controles:** año, país, área legal, crisis, composición tribunal, cita tratados internacionales

**Método:** Regresión logística + Propensity Score Matching

**Condición de falsación:** Si p > 0.10 o efecto marginal < 5 puntos porcentuales en probabilidad predicha.

---

### RQ2: Polisemia Funcional

**RQ2.1:** ¿La polisemia de "bien común" y "bienestar general" es accidental o funcionalmente adaptativa?

**RQ2.2:** ¿Existe evidencia histórica de que actores constitucionales eligieron deliberadamente términos ambiguos para facilitar coaliciones?

**Hipótesis asociadas:**
- **H2.1:** Términos con mayor polisemia tienen mayor persistencia temporal (survival analysis)
- **H2.2:** Debates constituyentes muestran discusión explícita sobre ventajas de ambigüedad
- **H2.3:** Intentos de precisar términos vía reforma fracasan más que otras reformas (análisis comparativo)

**Operacionalización:**
- **Medida de polisemia:** número de definiciones incompatibles en jurisprudencia (basado en análisis semántico)
- **Persistencia:** años desde incorporación constitucional hasta presente sin eliminación
- **Datos cualitativos:** análisis de actas de debates constituyentes

**Método:** Análisis histórico + survival analysis + estudios de caso

**Condición de falsación:** Si reformas constitucionales que clarifican términos tienen igual tasa de éxito que reformas que mantienen ambigüedad.

---

### RQ3: Genealogía Memética

**RQ3.1:** ¿Los términos "bien común" y "bienestar general" portan genealogías filosóficas distinguibles estadísticamente?

**RQ3.2:** ¿El uso contemporáneo mantiene conexión semántica con textos fundacionales o ha ocurrido deriva semántica?

**Hipótesis asociadas:**
- **H3.1:** Análisis de embeddings semánticos separa cluster "bien común" (tomista) de cluster "bienestar general" (utilitarista)
- **H3.2:** Distancia semántica entre uso contemporáneo y textos clásicos es < 0.40 (escala 0-1), indicando persistencia genealógica
- **H3.3:** Jueces que citan autores tomistas usan "bien común" 3× más que jueces que citan autores liberales

**Operacionalización:**
- **RootFinder:** construir árbol genealógico desde Aristóteles/Locke hasta jurisprudencia actual
- **Distancia semántica:** cosine similarity entre embeddings de uso clásico vs. contemporáneo
- **Red de co-citación:** correlación entre autores citados y términos usados

**Método:** NLP (BERT embeddings multilingües) + análisis de redes + genealogía conceptual

**Condición de falsación:** Si análisis de clustering no separa términos (silhouette score < 0.3) o si distancia con textos originales es > 0.60.

---

### RQ4: Efecto Causal del Término

**RQ4.1:** ¿El término tiene efecto causal sobre el resultado o es simplemente proxy de ideología judicial previa?

**RQ4.2:** ¿Jueces que varían el término entre casos también varían el resultado sistemáticamente?

**Hipótesis asociadas:**
- **H4.1:** PSM muestra que casos similares (covariables balanceadas) tienen resultados diferentes según término (ATE significativo)
- **H4.2:** Análisis within-judge muestra que mismo juez usando diferentes términos produce resultados sistemáticamente diferentes
- **H4.3:** Experimentos de framing (si posible con muestras de jueces) muestran que presentar mismos hechos con diferentes términos altera decisión

**Operacionalización:**
- **PSM:** construir contrafactuales emparejando casos según propensity score
- **Within-judge variation:** fixed effects por juez, analizar casos donde mismo juez usa términos diferentes
- **ATE:** diferencia promedio en probabilidad de resultado individualista entre casos tratados (bien común) vs. control (bienestar general)

**Método:** Propensity Score Matching + Fixed Effects Logit + (idealmente) Survey Experiment

**Condición de falsación:** Si ATE no es significativo (p > 0.10) o si within-judge variation no muestra patrón sistemático.

---

### RQ5: Variación Cross-Nacional

**RQ5.1:** ¿Los patrones argentinos se replican en otras jurisdicciones latinoamericanas?

**RQ5.2:** ¿Qué factores institucionales predicen mayor o menor efecto del término?

**Hipótesis asociadas:**
- **H5.1:** Países con constituciones explícitamente católicas (Chile, Colombia) muestran efecto más fuerte de "bien común"
- **H5.2:** Países con sistemas de designación judicial más politizados muestran mayor efecto del término
- **H5.3:** Países con mayor inestabilidad económica muestran mayor uso de "bien común" en crisis

**Operacionalización:**
- **Variables país-nivel:** índice de secularización, método de designación judicial, frecuencia de crisis
- **Análisis multinivel:** casos anidados en países, efectos aleatorios por país
- **Interacciones:** término × características país

**Método:** Hierarchical/Multilevel Logistic Regression

**Condición de falsación:** Si coeficiente del término no varía significativamente entre países (test de heterogeneidad no significativo).

---

## Matriz de RQs, Hipótesis, Métodos y Datos

| RQ | Hipótesis | Método Principal | Datos Requeridos | Condición Falsación |
|---|---|---|---|---|
| RQ1 | H1.1, H1.2, H1.3 | Logit + PSM | Corpus jurisprudencial (n≥300) | p > 0.10 o efecto < 5pp |
| RQ2 | H2.1, H2.2, H2.3 | Survival analysis + cualitativo | Debates constituyentes + reformas | No diferencia en tasas éxito |
| RQ3 | H3.1, H3.2, H3.3 | NLP + redes | Corpus filosófico + jurisprudencia | Silhouette < 0.3 o dist > 0.60 |
| RQ4 | H4.1, H4.2, H4.3 | PSM + Fixed Effects | Corpus jurisprudencial detallado | ATE no sig. o no within-variation |
| RQ5 | H5.1, H5.2, H5.3 | Multilevel models | Multi-país (≥5 países, n≥50 c/u) | No heterogeneidad entre países |

---

## Timeline de Testeo

**Fase 1 (Meses 1-3):** Recolección de datos + RQ3 (genealogía descriptiva)  
**Fase 2 (Meses 4-6):** RQ1 análisis preliminar (Argentina only)  
**Fase 3 (Meses 7-9):** RQ4 (causalidad) + RQ2 (polisemia histórica)  
**Fase 4 (Meses 10-12):** RQ5 (cross-nacional) + RQ1 refinado  

---

## Notas Metodológicas

**Sobre validez externa:** Hallazgos en LatAm pueden no generalizarse a sistemas common law o a democracias consolidadas sin historia de crisis. Proyecto enfoca explícitamente en jurisdicciones no-WEIRD donde memética constitucional enfrenta mayores presiones selectivas.

**Sobre validez interna:** Principal amenaza es sesgo de selección (jueces eligen términos según ideología previa). PSM y within-judge variation buscan mitigar esto, pero experimento sería ideal (éticamente complejo).

**Sobre confiabilidad:** Inter-rater reliability en codificación de resultados es crítico. Protocolo: double-coding de 30% muestra aleatoria, κ > 0.80 requerido. Ver `prompts/data_collection_protocols/jurisprudence_annotation_manual.md`.
