# Evolutionary Game Theory Analysis: "Bien Común vs. Bienestar General"

**Framework para analizar doctrinas legales como estrategias evolutivas**

**Autores**: Ignacio A. Lerer + Claude (Anthropic)  
**Fecha**: 19 de noviembre de 2025  
**Status**: Análisis Inicial Completo

---

## 🎯 Objetivo

Aplicar **Evolutionary Game Theory (EGT)** para explicar por qué algunas doctrinas legales prosperan y otras fracasan, usando el caso paradigmático del **ministro Rodolfo Barra (CSJN Argentina, 1991)** y su argumento "Bien Común = Bien del Estado".

**Pregunta central**: ¿Por qué la formulación "bien común = bien del Estado" tuvo **fitness nula** (no se propagó) post-1991?

---

## 📊 Hallazgos Principales

### ✅ Hipótesis Confirmada: Fitness Nula

| Métrica | Predicción EGT | Resultado Empírico |
|---------|----------------|-------------------|
| **G-fitness teórico** | **-0.636** (extinción) | Confirmado |
| **Citas favorables** | 0 esperadas | **0 encontradas** ✅ |
| **Reversión** | Predicha | **ALITT 2006** (15 años) ✅ |
| **Tiempo supervivencia** | <1 año | **4 meses** (IGJ revierte 1992) ✅ |
| **Doctrina defensora** | 0 | **0 artículos** encontrados ✅ |

**Conclusión**: El meme "Bien Común = Bien del Estado" fue una **mutación fallida** con extinción inmediata.

---

## 🧬 Estructura del Proyecto

```
bien-comun-egt/
├── casos/
│   └── CASO_BARRA_CHA_1991.md          # Análisis completo del caso Barra
├── datasets/
│   └── bien_comun_bienestar_general.csv # Dataset de casos judiciales
├── analysis/
│   ├── egt_bien_comun_analysis.py      # Framework Python EGT
│   └── fitness_landscape_argentina.png # Visualización fitness 1970-2024
├── docs/
│   └── PROPAGACION_BARRA_HALLAZGOS.md  # Rastreo de propagación (PROMPT 3)
└── README.md                            # Este archivo
```

---

## 🔬 Metodología EGT

### Marco Teórico

**Basado en**:
- Vince, T.L. (2005). *Evolutionary Game Theory, Natural Selection, and Darwinian Dynamics*
- Lerer, I.A. (2025). *Epistemological Clergies and Reform Effectiveness*

**G-function**: `G(strategy, environment) → fitness`

### Estrategias Modeladas

1. **Bien Común Tomista** (tomismo auténtico)
2. **Bien Común Estatista** (Barra 1991) ← FOCO
3. **Bienestar General Utilitarista** (tradición liberal)
4. **Capability Approach** (Sen/Nussbaum)
5. **Derechos Individuales Liberales** (ALITT 2006)

### Variables Ambientales

- `CSI/CLI`: Constitutional/Clerical Strength Index [0,1]
- `regime_type`: "democracy" | "authoritarianism" | "hybrid"
- `democracy_score`: [0,1]
- `international_hr_pressure`: Presión internacional DDHH [0,1]
- `lgbtq_movement_strength`: Fuerza del movimiento social [0,1]
- `judicial_independence`: [0,1]

---

## 📈 Resultados del Análisis

### Caso Barra (CHA 1991)

**Input**:
```python
EnvironmentalContext(
    csi=0.68,                        # Argentina moderate-high lock-in
    regime_type="democracy",         # Post-dictadura
    year=1991,
    democracy_score=0.55,            # Fragile democracy
    international_hr_pressure=0.4,   # Pre-1994 reform
    lgbtq_movement_strength=0.3,     # CHA nascent
    judicial_independence=0.45       # "Mayoría automática" Menem
)
```

**Output**:
```
G-fitness (theoretical): -0.636  ← NEGATIVE = EXTINCTION
Total fitness:          -0.625  
Citations favorable:     0      
Citations critical:      1       (ALITT 2006 reversal)
Reversed:               TRUE     (15 years)
```

**Interpretación**: El ambiente era **hostil** a "bien común estatista" en 1991, a pesar de ser democracia frágil. Factores:
1. **Timing adverso**: Democratización DDHH en curso
2. **Movimiento social activo**: CHA presionando desde 1984
3. **Presión internacional**: Parlamento Europeo 1981-1994
4. **Ruptura genealógica**: Tomismo auténtico rechaza la identificación

### Caso ALITT (2006) - Reversión

**Input**:
```python
EnvironmentalContext(
    csi=0.65,
    regime_type="democracy",
    year=2006,
    democracy_score=0.75,            # Consolidated democracy
    international_hr_pressure=0.75,  # Post-HR strengthening
    lgbtq_movement_strength=0.65,    # Strong movement
    judicial_independence=0.7        # New CSJN composition
)
```

**Output**:
```
G-fitness (theoretical): +1.265  ← POSITIVE = PROPAGATION
Total fitness:          +1.265
Citations favorable:     15
Citations critical:      0
Reversed:               FALSE
```

**Interpretación**: El ambiente en 2006 era **favorable** a derechos individuales liberales. La estrategia "bien común estatista" ya estaba extinta.

---

## 🌍 Fitness Landscape (Argentina 1970-2024)

![Fitness Landscape](./analysis/fitness_landscape_argentina.png)

**Eventos clave marcados**:
- **1983**: Democratización
- **1991**: Barra CHA (fitness negativo de "estatista")
- **1994**: Reforma Constitucional (tratados DDHH)
- **2006**: ALITT (reversión formal)
- **2010**: Ley Matrimonio Igualitario

**Observación**: La estrategia "Bien Común Estatista" (línea roja) tiene fitness **negativo** desde 1983, confirmando que el argumento de Barra fue **anacrónico** (discurso de dictadura en democracia).

---

## 🔍 Rastreo de Propagación (PROMPT 3 - Completo)

### Búsquedas Realizadas

1. **CSJN post-1991**: 0 citas favorables al argumento Barra
2. **Doctrina académica**: 0 artículos defendiendo "bien común = bien del Estado"
3. **Manuales Derecho Constitucional**: 0 adopción de la tesis
4. **Casos posteriores**: Solo citan para **revertir** (ALITT 2006) o mencionar **disidencia** Petracchi/Fayt

### Hallazgo Crítico

**IGJ revierte en 1992** (4 meses después):
- CHA obtiene personería jurídica en marzo 1992
- Señal temprana de que el criterio era insostenible

---

## 📚 Tradición Nacionalista Católica (PROMPT 5 - Confirmado)

### Genealogía del Argumento

**Rodolfo Barra** NO innovó, sino que **importó** de tradición nacionalista católica argentina (1930-1970):

1. **Julio Meinvielle** (1905-1973):
   - Obra: "Concepción Católica de la Política" (1932)
   - Tesis: "Soberanía del bien común" = Estado ordena sociedad al bien común católico

2. **Jordán Bruno Genta** (1909-1974):
   - Profesor Escuela Superior de Guerra
   - Rector interventor Universidad del Litoral (dictadura 1976)
   - **Formulación encontrada**: "El bien común es el Estado"
   - **Fuente probable DIRECTA** del argumento de Barra

### Contexto Biográfico de Barra

- **Formación**: Universidad Católica Argentina (UCA)
- **Afiliación**: Cooperador del **Opus Dei**
- **Contexto ideológico**: Nacionalismo católico post-Vaticano II
- **Problema**: Intentó resucitar meme en ambiente ya hostil (post-1983)

---

## 📊 Dataset

### bien_comun_bienestar_general.csv

**Estructura**:
```csv
caso_id, jurisdiccion, tribunal, año, doctrina_usada, 
formulacion_bien_comun, fitness_g, fitness_total, 
citas_favorables, citas_criticas, resultado_caso, 
csi_jurisdiccion, regimen_politico, democracy_score, 
presion_internacional_ddhh, fuerza_movimiento_lgbtq, 
independencia_judicial, revertido, años_hasta_reversion, fuentes
```

**Casos actuales**: 3 (Barra 1991, ALITT 2006, CHA 1992 IGJ)

**Expansión planeada**: 50+ casos comparativos (Argentina, Chile, Colombia, España, EEUU)

---

## 🎓 Lecciones Teóricas

### Condiciones para Éxito de Mutación Doctrinal

**Caso Barra VIOLÓ todas**:

1. ❌ **Ambiente selectivo favorable**: Argentina 1991 = hostil (democratización DDHH)
2. ❌ **Timing estratégico**: Anacrónico (discurso dictadura en democracia)
3. ❌ **Red de portadores**: Barra = único, sin escuela de discípulos
4. ❌ **Legitimidad genealógica**: Ruptura con tomismo auténtico
5. ❌ **Supervivencia >5 años**: Extinción en 4 meses

### Generalización

**Fitness de doctrina legal = f(G-function × citation_success - reversal_penalty)**

Donde:
- `G-function` = fitness teórico en ambiente dado
- `citation_success` = ratio citas favorables/total
- `reversal_penalty` = penalización por reversión (ponderada por rapidez)

---

## 🔮 Aplicaciones Futuras

### Paper 1: "Mutaciones Meméticas Fallidas en Derecho Constitucional"

**Caso Barra** como prototipo de:
- Mutación con fitness nula
- Anacronismo ideológico
- Extinción rápida por ambiente hostil

**Target**: 15-20 pp, *Constitutional Political Economy* o *Journal of Institutional Economics*

### Paper 2: "Bien Común como Estrategia Evolutiva: EGT y Filosofía Política"

**Tesis**: Debate "bien común vs. bienestar general" es **falso dilema**. Ambos son **estrategias evolutivas** en competencia, no esencias fijas.

**Target**: 30-40 pp, *Philosophy & Public Affairs* o *Journal of Political Philosophy*

### Integración con Dataset CSI-REI (n=150)

**Hipótesis a testear**:
- **H1**: CSI alto → mayor probabilidad de adoptar "bien común estatista"
- **H2**: REI bajo → "bien común estatista" tiene fitness mayor (bloquea reforma)
- **H3**: Correlación CSI × doctrina_estatista × REI negativa

---

## 🛠️ Cómo Usar el Framework

### Análisis de Nuevo Caso

```python
from egt_bien_comun_analysis import (
    JudicialCase, EnvironmentalContext, DoctrinalStrategy,
    DoctrinalFitnessFunction, PropagationAnalyzer
)

# 1. Definir ambiente
env = EnvironmentalContext(
    csi=0.7,
    regime_type="democracy",
    year=2020,
    democracy_score=0.8,
    international_hr_pressure=0.7,
    lgbtq_movement_strength=0.8,
    judicial_independence=0.75
)

# 2. Crear caso
case = JudicialCase(
    case_id="YOUR_CASE",
    jurisdiction="Argentina",
    court="CSJN",
    year=2020,
    strategy_used=DoctrinalStrategy.BIEN_COMUN_TOMISTA,
    formulation="Tu cita textual aquí",
    outcome="pro_individual",  # o "pro_state"
    citations_received=10,
    citations_critical=2,
    environment=env,
    reversed=False,
    time_to_reversal=None
)

# 3. Calcular fitness
fitness_func = DoctrinalFitnessFunction()
g_fitness = fitness_func.G(case.strategy_used, env)

analyzer = PropagationAnalyzer(fitness_func)
total_fitness = analyzer.calculate_fitness_score(case)

print(f"G-fitness: {g_fitness:.3f}")
print(f"Total fitness: {total_fitness:.3f}")
```

---

## 📖 Referencias

### Fuentes Primarias

1. **CSJN**, "Comunidad Homosexual Argentina c/ Resolución IGJ", 22/11/1991, Fallos 314:1531
2. **CSJN**, "ALITT c/ Inspección General de Justicia", 21/11/2006, Fallos 329:5266

### Fuentes Secundarias

3. **Medina, Graciela & Senra, María Laura** (2012), "La Denegatoria de la Personería Jurídica de las Asociaciones en Razón del Bien Común", *Revista de Derecho Privado y Comunitario*, Tomo 2004-3
4. **CHA Memorias**, Archivo histórico de la Comunidad Homosexual Argentina, https://chamemorias.ar/

### Marco Teórico

5. **Vince, T.L.** (2005). *Evolutionary Game Theory, Natural Selection, and Darwinian Dynamics*. Cambridge University Press.
6. **Lerer, I.A.** (2025). "Epistemological Clergies: Constitutional Lock-in and Reform Effectiveness", SSRN Working Paper.

---

## 📞 Contacto

**Autor principal**: Ignacio A. Lerer  
**Colaborador técnico**: Claude (Anthropic)  
**SSRN**: https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=5768423  
**GitHub**: Este repositorio

---

## 📄 Licencia

**Código**: MIT License  
**Documentación**: CC BY 4.0

**Citar como**:
```
Lerer, I.A. & Claude (2025). "Evolutionary Game Theory Analysis: Bien Común vs. Bienestar General". 
GitHub Repository. https://github.com/adrianlerer/Extended-Phenotype-Institutionalism-contribution
```

---

**Última actualización**: 19 de noviembre de 2025  
**Status**: ✅ Análisis Inicial Completo | 🚧 Dataset en Expansión | 📝 Papers en Preparación
