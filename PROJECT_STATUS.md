# Estado del Proyecto: Bien Común vs. Bienestar General

**Última actualización:** 2025-11-14 18:45 UTC  
**Fase actual:** 🟡 Fase 1 - Recolección de Datos (37% completo)

---

## Progreso General por Fase

```
Fase 1: Recolección de Datos         [███████░░░░░░░░░░░░░] 37%
Fase 2: Análisis Cuantitativo        [░░░░░░░░░░░░░░░░░░░░]  0%
Fase 3: Análisis Cualitativo          [░░░░░░░░░░░░░░░░░░░░]  0%
Fase 4: Herramientas Computacionales  [░░░░░░░░░░░░░░░░░░░░]  0%
Fase 5: Redacción                     [░░░░░░░░░░░░░░░░░░░░]  0%
```

---

## Fase 1: Recolección de Datos

### Completado ✅

#### Estructura de Repositorio
- [x] Estructura de directorios completa (data/, analysis/, tools/, outputs/, docs/)
- [x] README.md principal con descripción del proyecto
- [x] CITATION.cff para citación académica
- [x] LICENSE (MIT para código, CC BY 4.0 para datos)
- [x] .gitignore configurado
- [x] data/README.md con documentación de fuentes
- [x] docs/research_questions.md con hipótesis formalizadas

#### Genealogías Filosóficas
- [x] **Prompt 1.3 COMPLETO:** Genealogía "Bien Común"
  - Linaje completo: Aristóteles (335 BCE) → Tomás (1274) → DSI (1891-2020) → Chile/Colombia (1980-1991)
  - 15 fuentes primarias verificadas
  - 6 fases históricas documentadas
  - Archivo: `docs/genealogies/BIEN_COMUN_GENEALOGIA_COMPLETA.md` (22,380 caracteres)

- [x] **Prompt 1.4 COMPLETO:** Genealogía "Bienestar General"
  - Linaje completo: Locke (1689) → USA (1787) → Bentham (1789) → Alberdi (1852) → Argentina/Perú (1853-1993)
  - 12 fuentes primarias verificadas
  - 7 fases históricas documentadas
  - Archivo: `docs/genealogies/BIENESTAR_GENERAL_GENEALOGIA_COMPLETA.md` (28,880 caracteres)

- [x] Tabla comparativa de incompatibilidades filosóficas (11 dimensiones)
- [x] Hipótesis de aptitud memética diferencial formuladas

#### Inventario Constitucional
- [x] **Prompt 1.1 INICIADO (30%):** Inventario constitucional América Latina
  - Dataset estructurado: `data/processed/inventario_constitucional_FASE1.csv`
  - 12 ocurrencias verificadas en 5 países:
    - Argentina (n=1): "bienestar general" Preámbulo
    - Chile (n=4): "bien común" Art. 1, "interés público" Art. 19-24, "orden público" 3x
    - México (n=2): "interés general", "orden jurídico"
    - Colombia (n=2): "bien común" Art. 333, "interés general" Art. 1
    - Perú (n=2): "bienestar general" Art. 44, "orden público" Art. 2
  - Script de extracción automatizada: `analysis/01_data_preparation/extract_terms.py`
  - Resumen ejecutivo: `docs/PROMPT_1_1_RESUMEN_EJECUTIVO.md`

- [x] Metodología de codificación documentada: `docs/methodology/RESEARCH_PROTOCOL.md`

#### Corpus Jurisprudencial
- [x] Estructura de dataset: `data/processed/corpus_latam_FASE1_estructura.csv`
- [x] 19 casos codificados con 19 VERIFICADOS con fuentes primarias
- [x] Variables codificadas definidas (20 variables)
- [x] **Prompt 2.1 INICIADO (12%):** Corpus jurisprudencial LatAm
  - 19 casos totalmente codificados [VERIFICADO]
  - Casos paradigmáticos Argentina: Sejean (1986), Portal de Belén (2002), FAL (2012), Ekmedjian (1992)
  - Casos paradigmáticos Chile: Aborto 3 causales (Rol 3729-17), Objeción conciencia (Rol 5572-18)
  - Patrones preliminares documentados (bien común 67% difuso, interés público 100% difuso)
  - Resumen ejecutivo: `docs/PROMPT_2_1_RESUMEN_EJECUTIVO.md`

---

### En Progreso 🟡

#### Prompt 1.1: Inventario Constitucional Exhaustivo
**Target:** 200-300 ocurrencias  
**Actual:** 12 verificadas (6%)  
**Pendiente:**
- [ ] Argentina: completar búsqueda exhaustiva (Constitución 1853, 1949, 1994)
- [ ] Brasil: búsqueda completa ("bem comum", "bem-estar social", "interesse público")
- [ ] Chile: completar búsqueda exhaustiva
- [ ] México: completar búsqueda exhaustiva (Art. 25, 27, 28...)
- [ ] Colombia: completar búsqueda exhaustiva
- [ ] Perú: completar búsqueda exhaustiva (Constituciones 1979, 1993)
- [ ] Paraguay: iniciar búsqueda
- [ ] Uruguay: iniciar búsqueda
- [ ] Venezuela: iniciar búsqueda
- [ ] Ecuador: iniciar búsqueda

**Proyección:** 100-153 ocurrencias totales (necesita completarse para llegar a target)

#### Prompt 2.1: Corpus Jurisprudencial LatAm
**Target:** 300 casos totales (150 Argentina + 150 otros)  
**Actual:** 19 casos codificados [VERIFICADO] (6%)  

**Casos VERIFICADOS con fuentes primarias:**
- Argentina (7): Halabi (Fallos 332:111), Mendoza (Fallos 331:1622), Rodríguez (R. 401 XL), Sejean (Fallos 308:2268), Portal de Belén (2002), FAL (Fallos 336:1888), Ekmedjian (Fallos 315:1492)
- Chile (4): Reforma Salud (Rol 1710-10), Ley Pesca (Rol 2299-12), Etiquetado Nutricional (Rol 4317-18), Aborto 3 causales (Rol 3729-17), Objeción conciencia (Rol 5572-18)
- Colombia (3): Expropiación (C-221/92), Consulta Previa (C-313/14), T-760/08 Salud
- Perú (2): Reforma Agraria (Exp. 0048-2004-AI), Anicama (Exp. 1417-2005-AA)
- México (1): Amparo Directo 6/2008 Medio ambiente
- Brasil (1): RE 194.704 Educación

**Casos paradigmáticos recién codificados:**
- ✅ Sejean (1986): Declaró inconstitucional prohibición remarriage, anticipó divorcio vincular
- ✅ Portal de Belén (2002): Prohibió píldora del día después, interpretó vida desde concepción
- ✅ FAL (2012): Amplió aborto no punible a toda víctima violación, sin autorización judicial
- ✅ Ekmedjian (1992): Operatividad directa Art. 14.1 Pacto San José, jerarquía tratados DDHH
- ✅ Chile Aborto 3 causales (2017): Validó despenalización IVE 3 causales
- ✅ Chile Objeción conciencia (2018): Validó objeción institucional clínicas privadas

**Pendiente:**
- [ ] Argentina CSJN: identificar 143 casos adicionales (actual: 7, target: 150)
- [ ] Chile TC: identificar 35-45 casos adicionales
- [ ] Colombia CC: identificar 37-47 casos adicionales
- [ ] México SCJN: identificar 19-29 casos
- [ ] Brasil STF: identificar 19-29 casos
- [ ] Perú TC: identificar 18-28 casos
- [ ] IACHR: identificar 20-30 casos

**Blocker:** Bases de datos oficiales requieren acceso manual o scraping autorizado

---

### Pendiente ⚪

#### Prompt 2.2: CSJN Argentina Análisis Intensivo
**Target:** 50-80 casos con codificación exhaustiva  
**Status:** No iniciado  
**Tareas:**
- [ ] Identificar casos paradigmáticos (Sejean, Mendoza, Halabi, etc.)
- [ ] Codificar variables dependientes (resultado binario)
- [ ] Codificar variables independientes (término usado, frecuencia)
- [ ] Codificar controles (año, crisis, composición tribunal)
- [ ] Análisis de coocurrencias ("bienestar general" + otros términos)
- [ ] Verificación de doble codificación (κ > 0.80)

#### Bloque 3: Corpus Doctrinal
**Status:** No iniciado  
**Tareas:**
- [ ] Identificar artículos académicos que citan términos (n≥50)
- [ ] Análisis bibliométrico de redes de citación
- [ ] Identificación de "escuelas" doctrinales

#### Bloque 4: Crisis y Experimentos Naturales
**Status:** No iniciado  
**Tareas:**
- [ ] Construir timeline de crisis económicas (1980-2024)
- [ ] Codificar tipo y severidad de crisis
- [ ] Identificar casos decididos durante crisis
- [ ] Análisis de interacción término × crisis

---

## Fase 2: Análisis Cuantitativo (0%)

### Análisis Estadístico Descriptivo
- [ ] Frecuencias de términos por país y período
- [ ] Evolución temporal de uso de términos
- [ ] Correlaciones bivariadas término-resultado
- [ ] Visualizaciones (histogramas, time series, heatmaps)

### Modelado Inferencial
- [ ] Regresión logística básica (término → resultado)
- [ ] Regresión con controles (año, país, área legal, crisis)
- [ ] Propensity Score Matching
- [ ] Análisis de sensibilidad

### Análisis de Redes
- [ ] Construir red de citas entre casos
- [ ] Implementar JurisRank (PageRank con decay temporal)
- [ ] Identificar precedentes "ancestrales"
- [ ] Análisis de comunidades (clustering)

### Análisis Multinivel
- [ ] Modelos jerárquicos (casos anidados en países)
- [ ] Efectos aleatorios por país
- [ ] Interacciones término × características país

---

## Fase 3: Análisis Cualitativo (0%)

### Estudios de Caso
- [ ] Caso Sejean (Argentina 1986) - análisis profundo
- [ ] Caso Mendoza (Argentina 2008) - cuenca Matanza-Riachuelo
- [ ] Caso Halabi (Argentina 2009) - acción colectiva
- [ ] Ley de Pesca (Chile 2013) - privatización recursos
- [ ] Tutela salud (Colombia 2008) - estado de cosas inconstitucional

### Análisis Histórico
- [ ] Debates Convención Constituyente Argentina 1853
- [ ] Debates Constitución Chile 1980
- [ ] Debates Constitución Colombia 1991
- [ ] Identificar polisemia deliberada vs. accidental

### Reconstrucción Argumental
- [ ] Mapeo de estructuras argumentativas en casos clave
- [ ] Identificación de patrones retóricos
- [ ] Análisis de votos disidentes

---

## Fase 4: Herramientas Computacionales (0%)

### RootFinder - Genealogía de Conceptos
- [ ] Diseño de arquitectura (Python/NetworkX)
- [ ] Implementación de extracción de citas
- [ ] Cálculo de distancias semánticas (BERT embeddings)
- [ ] Visualización de árboles genealógicos
- [ ] Detección de mutaciones semánticas
- [ ] Testeo con corpus existente

### JurisRank - Fitness Institucional
- [ ] Implementación PageRank con decay temporal
- [ ] Construcción de red de citación jurisprudencial
- [ ] Cálculo de métricas de centralidad
- [ ] Identificación de precedentes extintos
- [ ] Dashboard interactivo (Plotly/Dash)

### Legal-Memespace - Competencia Memética
- [ ] Embeddings de textos legales (BERT multilingüe)
- [ ] Reducción dimensional (UMAP/t-SNE)
- [ ] Clustering de territorios doctrinales
- [ ] Análisis de invasiones meméticas
- [ ] Mapas 2D interactivos

### IusMorfos - Predicción de Trasplantes
- [ ] Matriz de compatibilidad genealógica
- [ ] Modelo predictivo de supervivencia
- [ ] Validación con datos históricos de reformas
- [ ] Identificación de especies invasoras

---

## Fase 5: Redacción (0%)

### Working Paper
- [ ] Introducción y revisión de literatura
- [ ] Marco teórico (EPT aplicada al derecho)
- [ ] Metodología
- [ ] Resultados
- [ ] Discusión
- [ ] Conclusiones
- [ ] Referencias bibliográficas

### Presentaciones
- [ ] Slides para IPSA 2025
- [ ] Slides para SELA 2025

### Documentación Técnica
- [ ] Manuales de usuario para herramientas
- [ ] Vignettes con ejemplos
- [ ] API documentation

---

## Blockers Actuales 🔴

**Ninguno crítico actualmente**

### Blockers Potenciales (en monitoreo)
- **Acceso a bases de datos:** Algunos tribunales (Brasil STF, México SCJN) requieren acceso especial o scraping autorizado
- **Tiempo de codificación manual:** Codificar 300 casos requiere ~150 horas de trabajo (estimado)
- **Inter-rater reliability:** Necesitamos segundo codificador para validación (30% muestra)

---

## Hitos Clave

| Hito | Fecha Target | Status |
|------|--------------|--------|
| Estructura repositorio completa | 2025-11-14 | ✅ Completado |
| Genealogías filosóficas completas | 2025-11-14 | ✅ Completado |
| Inventario constitucional completo | 2025-12-15 | 🟡 En progreso (30%) |
| Corpus jurisprudencial completo | 2026-01-31 | 🟡 En progreso (4%) |
| Análisis estadístico preliminar | 2026-02-28 | ⚪ Pendiente |
| Herramientas computacionales v1.0 | 2026-03-31 | ⚪ Pendiente |
| Working paper draft | 2026-04-30 | ⚪ Pendiente |
| Presentación IPSA/SELA | 2026-06-30 | ⚪ Pendiente |

---

## Próximos Pasos Inmediatos (Semana del 2025-11-14)

1. **Completar Prompt 1.1:** Búsqueda exhaustiva en constituciones Argentina, Brasil, Chile
   - Prioridad: Argentina (expected +5-10 ocurrencias), Brasil (+15-20), Chile (+10-15)
   - Output: Actualizar `inventario_constitucional_FASE1.csv`

2. **Iniciar Prompt 2.1:** Identificar casos CSJN Argentina 2000-2024
   - Búsqueda en sjconsulta.csjn.gov.ar con términos clave
   - Target inmediato: 30 casos adicionales
   - Output: Actualizar `corpus_latam_FASE1_estructura.csv`

3. **Continuar con Prompts FASE 1** según orden de prioridad del usuario
   - No hacer Prompt 2.2 hasta completar 2.1
   - Seguir protocolo "de a uno, sin preguntar"

---

## Notas Metodológicas

### Calidad > Cantidad
Priorizar verificación exhaustiva sobre velocidad. Cada dato debe tener nivel de confianza documentado ([VERIFICADO] / [INFERENCIA] / [ESTIMACION]).

### Principio de Falsabilidad
Para cada hipótesis, condición de falsación definida ex ante. Si p > 0.10 o efecto < 5pp, rechazar hipótesis.

### Replicabilidad
Todo análisis debe ser completamente replicable. Scripts comentados, datos versionados, random seeds fijados.

---

**Contacto para actualizaciones:** Adrian Lerer (adrianlerer@gmail.com)
