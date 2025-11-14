# Estado del Proyecto: Bien Común vs. Bienestar General

**Última actualización:** 2025-11-14 21:55 UTC  
**Fase actual:** 🟡 Fase 1 - Recolección de Datos (43% completo)

---

## Progreso General por Fase

```
Fase 1: Recolección de Datos         [████████░░░░░░░░░░░░] 43%
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
- [x] 46 casos codificados con 46 VERIFICADOS con fuentes primarias
- [x] Variables codificadas definidas (20 variables)
- [x] **Prompt 2.1 AVANZANDO (26%):** Corpus jurisprudencial LatAm
  - 46 casos totalmente codificados [VERIFICADO]
  - **Casos fundacionales:** Siri (1957 - creación pretoriana amparo), Kot (1958 - amparo horizontal)
  - **Casos paradigmáticos Argentina CSJN:** Sejean, Portal de Belén, FAL, Ekmedjian, Verbitsky, Badaro, Aquino, Arriola, Vizzoti, Simón, Campodónico, Benghalensis, Hooft, Fernández Arias, Madorrán, Álvarez, Pellejero, Defensor del Pueblo, Rodríguez Pereyra, Partido Nuevo Triunfo, Carranza Latrubesse, Castillo, Bussi, Casal, Kloosterman, Arancibia Clavel, ALITT, Mazzeo, Salas
  - **Casos paradigmáticos Chile:** Aborto 3 causales (Rol 3729-17), Objeción conciencia (Rol 5572-18)
  - Patrones preliminares documentados (bien común, interés público, bienestar general)
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
**Actual:** 46 casos codificados [VERIFICADO] (15.3%)  

**Casos VERIFICADOS con fuentes primarias:**
- **Argentina (34):** Siri (1957), Kot (1958), Fernández Arias (1960), Sejean (1986), Salas (1989), Ekmedjian (1992), Castillo ATE (1998), Campodónico (2000), Benghalensis (2000), Portal de Belén (2002), Aquino (2004), Vizzoti (2004), Hooft (2004), Arancibia Clavel (2004), Kloosterman (2004), Verbitsky (2005), Simón (2005), Casal (2005), ALITT (2006), Badaro (2007), Bussi (2007), Madorrán (2007), Mazzeo (2007), Mendoza (2008), Defensor del Pueblo (2008), Arriola (2009), Halabi (2009), Rodríguez Pereyra (2009), Rodríguez VIH (2009), Partido Nuevo Triunfo (2009), Álvarez (2010), Pellejero (2010), FAL (2012), Carranza Latrubesse (2013)
- **Chile (5):** Reforma Salud (Rol 1710-10), Ley Pesca (Rol 2299-12), Aborto 3 causales (Rol 3729-17), Etiquetado Nutricional (Rol 4317-18), Objeción conciencia (Rol 5572-18)
- **Colombia (3):** Expropiación (C-221/92), Consulta Previa (C-313/14), T-760/08 Salud
- **Perú (2):** Reforma Agraria (Exp. 0048-2004-AI), Anicama (Exp. 1417-2005-AA)
- **México (1):** Amparo Directo 6/2008 Medio ambiente
- **Brasil (1):** RE 194.704 Educación

**Casos fundacionales históricos:**
- ✅ Siri (1957): Creación pretoriana del amparo en Argentina
- ✅ Kot (1958): Extensión amparo a actos de particulares (Drittwirkung horizontal)

**Casos CSJN recién codificados (sesión actual +16):**
- ✅ Fernández Arias (1960): Doctrina arbitrariedad de sentencias
- ✅ Madorrán (2007): Estabilidad laboral empleados públicos
- ✅ Álvarez (2010): Discriminación sindical
- ✅ Pellejero (2010): Discriminación por embarazo
- ✅ Defensor del Pueblo (2008): Legitimación causas ambientales
- ✅ Rodríguez Pereyra (2009): Control constitucionalidad de oficio
- ✅ Partido Nuevo Triunfo (2009): Límites asociación política
- ✅ Carranza Latrubesse (2013): Vinculatoriedad recomendaciones CIDH
- ✅ Castillo ATE (1998): Huelga en servicios esenciales
- ✅ Bussi (2007): Control ético representación política
- ✅ Casal (2005): Doble instancia, recurso casación
- ✅ Kloosterman (2004): Protección zona ribereña
- ✅ Arancibia Clavel (2004): Imprescriptibilidad lesa humanidad
- ✅ ALITT (2006): Identidad travesti-transexual
- ✅ Mazzeo (2007): Obligatoriedad fallos Corte IDH
- ✅ Salas (1989): Libertad expresión post-dictadura

**Pendiente:**
- [ ] Argentina CSJN: identificar 116 casos adicionales (actual: 34, target: 150)
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
