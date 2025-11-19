# PROMPTS PARA EXPANSIÓN DEL DATASET (+20 casos)

**Objetivo**: Expandir dataset de 3 casos actuales a 23 casos totales para validación preliminar del paper.

**Estrategia**: Versión "light" enfocada en confirmar que:
1. El argumento de Barra es **único** (no se replicó en Argentina)
2. NO hay formulaciones similares en Chile/Colombia contemporáneamente
3. Validar hipótesis de fitness nula comparativamente

---

## PROMPT 1: EXPANSIÓN ARGENTINA (+10 casos)

### Contexto

Necesitamos identificar casos argentinos (1990-2010) sobre denegación/otorgamiento de personería jurídica por "bien común" o "moral pública" para validar que el argumento de Barra "bien común = bien del Estado" NO se propagó.

### Búsqueda Específica

**Fuente primaria**: Artículo de Graciela Medina (2012) menciona varios casos:

Medina, Graciela & Senra, María Laura (2012). "La Denegatoria de la Personería Jurídica de las Asociaciones en Razón del Bien Común", *Revista de Derecho Privado y Comunitario*, Tomo 2004-3.
URL: https://gracielamedina.com/wp-content/uploads/2024/11/LA-DENEGATORIA-DE-LA-PERSONERIA-JURIDICA-DE-LAS-ASOCIACIONES-EN-RAZON-DEL-BIEN-COMUN.pdf

**Instrucciones**:

1. Leer artículo completo de Medina (2012) y extraer **todos los casos mencionados** sobre personería jurídica y "bien común"

2. Para cada caso, crear entrada en CSV con estructura:

```csv
caso_id, jurisdiccion, tribunal, año, 
peticionario, tipo_asociacion,
doctrina_bien_comun_usada, 
argumento_textual,
resultado_caso (otorga/deniega),
juez_redactor,
citas_a_barra_1991 (si/no),
citas_posteriores_count,
fuente_primaria
```

3. **Casos específicamente mencionados para buscar**:
   - Club swinger (denegación personería)
   - Iglesia Maradoniana / Iglesia del Dios Bostero
   - Vaca Profana (asociación)
   - Cualquier otro caso 1990-2010 sobre "moral pública" + personería

4. **Pregunta clave para cada caso**: ¿Algún juez usa argumento "bien común = bien del Estado" o cita a Barra CHA 1991?

### Output Esperado

**Tabla CSV** con 10 casos argentinos adicionales:

| caso_id | año | peticionario | doctrina_usada | cita_barra | resultado |
|---------|-----|--------------|----------------|------------|-----------|
| SWINGER_IGJ_[año] | [TBD] | Club swinger | [TBD] | NO | Deniega |
| MARADONA_IGJ_[año] | [TBD] | Iglesia Maradoniana | [TBD] | NO | Deniega |
| ... | ... | ... | ... | ... | ... |

**Hipótesis a confirmar**: 0 de los 10 casos citan argumento de Barra → confirma fitness nula

---

## PROMPT 2: EXPANSIÓN CHILE (+5 casos)

### Contexto

Necesitamos casos del Tribunal Constitucional de Chile (1990-2024) donde se mencione "bien común" para:
1. Comparación cross-nacional
2. Verificar si formulación "bien común = bien del Estado" aparece fuera de Argentina
3. Identificar estrategias doctrinales alternativas en Chile

### Búsqueda Específica

**Base de datos**: Tribunal Constitucional de Chile - Jurisprudencia
URL: https://www.tribunalconstitucional.cl/

**Query de búsqueda**: "bien común" en texto de sentencias

**Filtros**:
- Período: 1990-2024
- Tipo: Sentencias (no autos de admisibilidad)
- Materia: Diversa (familia, economía, libertad expresión, derechos sociales)

**Instrucciones**:

1. Seleccionar **5 casos representativos**:
   - Distribución temporal: 1 caso por década (1990s, 2000s, 2010s) + 2 adicionales 2020s
   - Áreas diversas: 1 familia, 1 economía, 1 libertad expresión, 1 derecho social, 1 otro

2. Para cada caso, extraer:
   - **Definición de "bien común"** utilizada por el TC
   - ¿Se identifica con "bien del Estado"? (SÍ/NO)
   - ¿Se cita tradición tomista? ¿DSI católica? ¿Liberal-utilitarista?
   - Resultado del caso (pro-individuo / pro-Estado)

3. Crear entrada CSV:

```csv
caso_id, jurisdiccion, tribunal, año,
materia, doctrina_bien_comun,
definicion_textual,
identifica_con_estado (si/no),
tradicion_citada (tomista/liberal/DSI/otra),
resultado_caso,
fuente_url
```

### Output Esperado

**Tabla CSV** con 5 casos chilenos:

| caso_id | año | materia | definicion_bien_comun | identifica_con_estado |
|---------|-----|---------|----------------------|----------------------|
| TC_CHILE_[ROL]-[AÑO] | 1995 | Familia | [cita textual] | NO |
| TC_CHILE_[ROL]-[AÑO] | 2005 | Economía | [cita textual] | NO |
| ... | ... | ... | ... | ... |

**Hipótesis a confirmar**: 0 de los 5 casos usan formulación estatista → confirma que Barra es idiosincrasia argentina

---

## PROMPT 3: EXPANSIÓN COLOMBIA (+5 casos)

### Contexto

Necesitamos casos de la Corte Constitucional de Colombia (1992-2024) donde se mencione "bien común" para:
1. Comparación con Argentina y Chile
2. Identificar si Colombia usa tradición tomista/DSI de manera distinta
3. Evaluar fitness de estrategias doctrinales alternativas

### Búsqueda Específica

**Base de datos**: Corte Constitucional de Colombia - Relatoría
URL: https://www.corteconstitucional.gov.co/relatoria/

**Query de búsqueda**: "bien común" en texto de sentencias

**Filtros**:
- Período: 1992-2024
- Tipo: Sentencias de constitucionalidad (C-) o tutela (T-)
- Materia: Diversa

**Instrucciones**:

1. Seleccionar **5 casos representativos**:
   - Incluir al menos 1 caso sobre derechos LGBTQ+ si existe (comparación directa con Barra)
   - Incluir casos sobre libertad de asociación
   - Diversificar áreas temáticas

2. Para cada caso, extraer:
   - **Definición de "bien común"** utilizada por la CC
   - ¿Cita Constitución 1991 (derechos fundamentales)?
   - ¿Usa doctrina tomista? ¿Doctrina Social de la Iglesia? ¿Utilitarismo liberal?
   - Resultado (expansivo de derechos / restrictivo)

3. Crear entrada CSV con misma estructura que Chile

### Output Esperado

**Tabla CSV** con 5 casos colombianos:

| caso_id | año | materia | doctrina_usada | resultado |
|---------|-----|---------|----------------|-----------|
| CC_COL_C-[NUM]-[AÑO] | [TBD] | LGBTQ+ | [TBD] | Pro-derechos |
| CC_COL_T-[NUM]-[AÑO] | [TBD] | Asociación | [TBD] | Pro-derechos |
| ... | ... | ... | ... | ... |

**Hipótesis a evaluar**: Colombia post-1991 usa "bien común" compatible con derechos humanos (NO estatista)

---

## CONSOLIDACIÓN: DATASET FINAL

### Estructura Completa

Integrar los 3 prompts en un solo archivo CSV:

**bien_comun_bienestar_general_expanded.csv**

Columnas:
```csv
caso_id,
jurisdiccion (Argentina/Chile/Colombia),
tribunal,
año,
materia,
peticionario,
doctrina_bien_comun_usada (Estatista/Tomista/Liberal/DSI/Capability),
formulacion_textual,
identifica_bien_comun_con_estado (si/no),
cita_a_barra_1991 (si/no/NA),
resultado_caso (pro_individuo/pro_estado),
fitness_g (calculado con modelo),
fitness_empirico (citas_favorables / (citas_favorables + citas_criticas)),
csi_jurisdiccion,
regimen_politico (democracy/hybrid/authoritarianism),
democracy_score,
año_regimen,
revertido (si/no),
años_hasta_reversion,
fuente_primaria (URL),
notas
```

### Análisis a Realizar

Una vez completado el dataset (23 casos totales):

1. **Frecuencia de estrategias**:
   - ¿Cuántos usan "Estatista"? (Hipótesis: solo Barra = 1)
   - ¿Cuántos usan "Liberal"? (Hipótesis: mayoría post-1990s)
   - ¿Cuántos usan "Tomista auténtico"? (Hipótesis: pocos, más en Chile)

2. **Fitness comparado**:
   - Calcular G-fitness para todos los casos usando modelo Python
   - Comparar fitness teórico vs. empírico (citas)
   - Identificar outliers (casos con fitness teórico bajo pero citas altas o viceversa)

3. **Correlación régimen-doctrina**:
   - ¿Democracias usan más "Liberal"?
   - ¿Regímenes híbridos usan más "Estatista"?

4. **Tabla comparativa para Paper (Sección IV)**:

| Jurisdicción | N casos | % Estatista | % Liberal | Fitness promedio |
|--------------|---------|-------------|-----------|------------------|
| Argentina    | 13      | 7.7%        | 69.2%     | 0.45             |
| Chile        | 5       | 0%          | 80%       | 0.62             |
| Colombia     | 5       | 0%          | 100%      | 0.71             |

**Conclusión esperada**: Barra es caso único (7.7% Argentina = 1/13 casos), confirma mutación no-viable

---

## TIMELINE EJECUCIÓN

### Semana 1 (Paralelo a redacción paper)

**Día 1-2**: PROMPT 1 (Argentina +10 casos)
- Leer Medina (2012) completo
- Extraer casos mencionados
- Buscar fallos en SAIJ/CIJ
- Codificar en CSV

**Día 3-4**: PROMPT 2 (Chile +5 casos)
- Buscar en TC Chile
- Seleccionar casos representativos
- Extraer definiciones "bien común"
- Codificar en CSV

**Día 5-6**: PROMPT 3 (Colombia +5 casos)
- Buscar en CC Colombia
- Seleccionar casos representativos
- Extraer doctrinas
- Codificar en CSV

**Día 7**: Consolidación y análisis preliminar
- Unificar CSV
- Calcular fitness con modelo Python
- Generar tabla comparativa para paper
- Actualizar Sección IV con resultados

---

## HERRAMIENTAS Y RECURSOS

### Bases de Datos

1. **Argentina**:
   - SAIJ: http://www.saij.gob.ar/
   - CIJ: http://www.cij.gov.ar/
   - Planeta Ius: http://www.planetaius.com.ar/

2. **Chile**:
   - TC Chile: https://www.tribunalconstitucional.cl/
   - Biblioteca Congreso: https://www.bcn.cl/

3. **Colombia**:
   - CC Colombia: https://www.corteconstitucional.gov.co/
   - Ámbito Jurídico: https://www.ambitojuridico.com/

### Scripts Python

**Calcular fitness automático para nuevos casos**:

```python
from bien_comun_egt.analysis.egt_bien_comun_analysis import (
    JudicialCase, EnvironmentalContext, DoctrinalStrategy,
    DoctrinalFitnessFunction
)

# Leer CSV
import pandas as pd
df = pd.read_csv('bien_comun_bienestar_general_expanded.csv')

# Para cada caso, calcular fitness_g
fitness_func = DoctrinalFitnessFunction()

for idx, row in df.iterrows():
    env = EnvironmentalContext(
        csi=row['csi_jurisdiccion'],
        regime_type=row['regimen_politico'],
        year=row['año'],
        democracy_score=row['democracy_score'],
        # ... otros campos
    )
    strategy = DoctrinalStrategy[row['doctrina_bien_comun_usada'].upper()]
    g = fitness_func.G(strategy, env)
    df.at[idx, 'fitness_g'] = g

# Guardar con fitness calculado
df.to_csv('bien_comun_bienestar_general_with_fitness.csv', index=False)
```

---

## VALIDACIÓN

### Criterios de Calidad

Para cada caso incluido:
- [ ] Tiene cita textual de definición "bien común"
- [ ] Metadata completa (tribunal, año, carátula)
- [ ] Codificación clara de doctrina usada
- [ ] Resultado del caso explícito
- [ ] Fuente verificable (URL a fallo)

### Intercoder Reliability

Si tiempo permite:
- Segundo codificador revisa 30% de los casos (7/23)
- Cálculo de kappa de Cohen para variables clave:
  - `doctrina_bien_comun_usada`
  - `identifica_bien_comun_con_estado`
  - `resultado_caso`
- Target: κ > 0.75 (substantial agreement)

---

## CONTINGENCIAS

### Si no se encuentran 10 casos argentinos en Medina (2012)

**Plan B**:
- Búsqueda directa en SAIJ: "personería jurídica" + "bien común" (1990-2010)
- Seleccionar casos manualmente hasta completar n=10
- Priorizar casos sobre asociaciones controvertidas (moral pública)

### Si bases de datos Chile/Colombia no son accesibles

**Plan B**:
- Usar Google Scholar: "site:tribunalconstitucional.cl bien común"
- Usar Repositorios académicos: Dialnet, SciELO
- Limitar a casos muy citados (> 10 citas académicas)

### Si timing es muy ajustado

**Plan C** (mínimo viable):
- Argentina: +5 casos (en vez de +10)
- Chile: +3 casos (en vez de +5)
- Colombia: +2 casos (en vez de +5)
- **Total**: 13 casos (suficiente para mencionar en paper como "validación preliminar")

---

**RESPONSABLE EJECUCIÓN**: [Asignar a Genspark o ejecutar manualmente]

**FECHA INICIO**: [Hoy - iniciar con PROMPT 1]

**FECHA LÍMITE**: 1 semana (para inclusion en Paper Sección IV)

**STATUS ACTUAL**: ⏳ PENDIENTE EJECUCIÓN
