# Protocolo de Investigación: Términos Legitimadores Constitucionales

## Objetivo General

Analizar comparativamente el uso de términos legitimadores ("bien común" vs "bienestar general") en constituciones y jurisprudencia de América Latina para determinar si estos términos predicen resultados judiciales mejor que variables contextuales.

## Hipótesis Central

**H1:** El término legitimador utilizado por tribunales ("bien común" vs "bienestar general") predice el resultado del caso mejor que variables contextuales (área del derecho, composición del tribunal, contexto económico).

**H2:** "Bien común" presenta mayor aptitud memética en casos que favorecen beneficiarios presentes y organizados (sindicatos, corporaciones, iglesias).

**H3:** "Bienestar general" presenta mayor aptitud memética en casos que difunden beneficios hacia poblaciones futuras o desorganizadas.

## Unidades de Análisis

### Nivel 1: Constitucional
- **Unidad:** Artículo constitucional que contiene término legitimador
- **Variables:** País, año de constitución, término utilizado, contexto textual, función normativa, área sustantiva

### Nivel 2: Jurisprudencial
- **Unidad:** Fallo de Corte Suprema que utiliza término legitimador
- **Variables:** País, tribunal, año, término utilizado, resultado (pro-presente vs pro-futuro), área del derecho, composición del tribunal

### Nivel 3: Doctrinal
- **Unidad:** Artículo académico que discute términos legitimadores
- **Variables:** Autor, afiliación institucional, año, citaciones, posición ideológica inferida

## Métodos de Recolección

### Fuente 1: Textos Constitucionales
- **Fuentes:** Sitios oficiales de gobiernos, bases constitucionales (Constitute Project, Political Database of the Americas)
- **Método:** Scraping automatizado + validación manual
- **Cobertura:** 10 países latinoamericanos, todas las constituciones vigentes + reformas desde 1980

### Fuente 2: Jurisprudencia
- **Argentina:** SAIJ (Sistema Argentino de Información Jurídica), CIJ (Centro de Información Judicial)
- **Brasil:** STF (Supremo Tribunal Federal) - base oficial
- **Chile:** Poder Judicial de Chile - base de jurisprudencia
- **México:** SCJN (Suprema Corte de Justicia de la Nación) - Semanario Judicial
- **Colombia:** Corte Constitucional - Relatoría
- **Otros:** Bases oficiales de Poder Judicial de cada país

### Fuente 3: Literatura Académica
- **Google Scholar:** Búsquedas booleanas con términos clave
- **SSRN:** Artículos de derecho constitucional
- **SciELO:** Literatura latinoamericana
- **Criterio:** Artículos publicados 1990-2025, mínimo 10 citas

## Esquema de Codificación

### Variables Dependientes (Nivel Jurisprudencial)

**Resultado del Caso:**
- `1` = Pro-beneficiario presente (organizado, inmediato)
- `0` = Pro-beneficiario futuro (difuso, desorganizado)

**Ejemplos:**
- Pro-presente: Fallo favorece sindicato vs consumidores difusos
- Pro-futuro: Fallo favorece ambiente vs empresa contaminante

### Variables Independientes Principales

**Término Legitimador:**
- `bien_comun` = "bien común" utilizado en fallo
- `bienestar_general` = "bienestar general" utilizado en fallo
- `interes_publico` = "interés público" (control)
- `orden_publico` = "orden público" (control)
- `seguridad_juridica` = "seguridad jurídica" (control)
- `ninguno` = No utiliza término legitimador explícito

### Variables de Control

**Contexto Institucional:**
- `composicion_tribunal` = Composición política del tribunal (1-5, conservador a progresista)
- `año` = Año del fallo
- `area_derecho` = Categoría (laboral, tributario, ambiental, etc.)

**Contexto Económico:**
- `crisis_economica` = Dummy (1 si hay crisis económica en año ±2)
- `pib_per_capita` = PIB per cápita del país en año del fallo

**Contexto Político:**
- `regimen_democratico` = Dummy (1 si régimen democrático)
- `gobierno_ideologia` = Ideología del gobierno (1-5, izquierda a derecha)

## Niveles de Confianza

**Todos los datos deben marcarse con nivel de confianza:**

- `[VERIFICADO]` = Dato verificado en fuente primaria oficial
- `[INFERENCIA]` = Dato inferido mediante razonamiento explícito de fuentes secundarias
- `[ESTIMACIÓN]` = Dato estimado mediante metodología proxy (e.g., web scraping de citas)

## Criterios de Calidad

**PRINCIPIO FUNDAMENTAL: CALIDAD > CANTIDAD**

### Criterio 1: Verificabilidad
- Todos los datos deben ser trazables a fuente primaria
- URLs/DOIs completos para todos los casos jurisprudenciales
- Capturas de pantalla de textos constitucionales (cuando sea necesario)

### Criterio 2: Exhaustividad Declarada
- Declarar explícitamente si búsqueda fue:
  - `EXHAUSTIVA` = Se revisaron todas las fuentes disponibles
  - `MUESTRA_ALEATORIA` = Muestra aleatoria con N casos
  - `MUESTRA_INTENCIONAL` = Casos seleccionados por criterio específico

### Criterio 3: Codificación Consistente
- Manual de codificación para cada variable
- Doble codificación independiente (cuando sea posible)
- Cálculo de confiabilidad inter-evaluadores (Kappa de Cohen)

### Criterio 4: Transparencia de Limitaciones
- Documentar fuentes no accesibles
- Explicitar sesgos de selección
- Reportar datos faltantes (missingness)

## Estándares de Formato

### Datos Tabulares (CSV)
```
País,Constitución_Año,Artículo,Término_Original,Término_Normalizado,Contexto_Textual,Función_Normativa,Área_Sustantiva,Año_Incorporación,Coocurrencias
```

**Requisitos:**
- Codificación UTF-8
- Separador: coma (,)
- Delimitador de texto: comillas dobles (")
- Sin celdas fusionadas
- Headers en primera fila
- Una observación por fila

### Narrativas (Markdown)
```markdown
# Título de Sección

## Subsección

**Concepto clave:** Definición clara.

[Cita académica con DOI/URL]

`[VERIFICADO]` / `[INFERENCIA]` / `[ESTIMACIÓN]`
```

## Cronograma de Ejecución

**FASE 1 (Fundamental):**
1. Prompt 1.1: Inventario constitucional → dataset base
2. Prompt 1.3: Genealogía "bien común" → linaje memético
3. Prompt 1.4: Genealogía "bienestar general" → linaje memético
4. Prompt 2.1: Corpus jurisprudencial LatAm → casos multi-país
5. Prompt 2.2: CSJN Argentina → 50-80 casos anotados

**FASE 2 (Expansión):**
- Prompts 2.3-2.4: Brasil, Chile, México, Colombia
- Prompts 3.1-3.4: Análisis bibliométrico y doctrinal

**FASE 3 (Validación):**
- Prompts 4.1-4.3: Crisis y contexto político
- Prompts 5.1-5.4: Herramientas computacionales
- Prompts 6.1-6.3: Testeo estadístico de hipótesis

## Referencias Metodológicas

- **Extended Phenotype Theory:** Dawkins, R. (1982). The Extended Phenotype.
- **Memética en Derecho:** Lerer, A. (2025). Ultraactivity as Fossilization Meme (en revisión).
- **Inferencia Causal:** Angrist & Pischke (2009). Mostly Harmless Econometrics.
- **Análisis Constitucional Comparativo:** Dixon & Ginsburg (2011). Comparative Constitutional Law.

---

**Fecha de Creación:** 2025-11-14  
**Versión:** 1.0  
**Autor:** Adrián Lerer
