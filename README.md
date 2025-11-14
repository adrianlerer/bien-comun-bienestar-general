# Análisis Comparativo: "Bien Común" vs "Bienestar General" en Constituciones Latinoamericanas

## Resumen del Proyecto

Este repositorio contiene la investigación comparativa sobre el uso de términos legitimadores en constituciones y jurisprudencia de América Latina, con foco en:

- **"bien común"** (common good) - linaje aristotélico-tomista-Doctrina Social de la Iglesia
- **"bienestar general"** (general welfare) - linaje lockeano-utilitarista-constitucionalismo anglosajón

**Hipótesis central:** El término legitimador utilizado por tribunales predice resultados judiciales mejor que variables contextuales, revelando patrones de aptitud memética.

## Marco Teórico

**Extended Phenotype Theory (Dawkins 1982) aplicada al derecho:**
- Normas jurídicas como constructos que modifican el ambiente (como represas de castores)
- Términos constitucionales llevan "material genético" filosófico que afecta resultados
- Aptitud memética = éxito reproductivo en doctrina judicial

**Aptitud Memética Asimétrica:**
- "Bien común" favorece **beneficiarios presentes** (actores organizados con intereses inmediatos)
- "Bienestar general" difunde beneficios hacia **poblaciones futuras/desorganizadas**

## Ámbito Geográfico

**10 jurisdicciones latinoamericanas:**
Argentina, Brasil, Chile, México, Colombia, Perú, Uruguay, Venezuela, Ecuador, Bolivia

## Estructura del Proyecto

```
bien-comun-bienestar-general/
├── data/
│   ├── constitutional/          # Inventarios constitucionales (CSV)
│   ├── jurisprudential/         # Corpus de fallos de Cortes Supremas
│   ├── bibliometric/            # Datos de análisis bibliométrico
│   └── raw/                     # Datos sin procesar
├── docs/
│   ├── genealogies/             # Genealogías filosóficas de términos
│   ├── analysis/                # Documentos de análisis
│   └── methodology/             # Metodología y protocolos
├── analysis/
│   ├── statistical/             # Scripts de análisis estadístico
│   ├── computational/           # Herramientas computacionales (RootFinder, IusMorfos, etc.)
│   └── visualization/           # Código de visualización
├── figures/                     # Gráficos y visualizaciones
└── references/                  # Bibliografía y materiales de referencia
```

## Bloques de Investigación

### BLOQUE 1: Fundamentos Constitucional-Doctrinales
- Inventario constitucional (10 países)
- Análisis diacrónico (reformas constitucionales)
- Genealogía "bien común" (Aristóteles → Tomás → CSI)
- Genealogía "bienestar general" (Locke → Bentham → USA)
- Análisis de explotación de polisemia

### BLOQUE 2: Corpus Jurisprudencial
- Cortes Supremas de América Latina (corpus multi-país)
- CSJN Argentina (análisis intensivo: 50-80 fallos anotados)
- STF Brasil (análisis comparativo: 30-50 fallos)
- Chile/México/Colombia (20-30 fallos cada uno)

### BLOQUE 3: Análisis Doctrinal/Académico
- Mapeo bibliométrico (redes de citación)
- Doctrina Social de la Iglesia (León XIII → Francisco)
- Comunitarismo anglosajón (Sandel, MacIntyre, Walzer)
- Clusters académicos (escuelas iberoamericanas vs anglosajonas)

### BLOQUE 4: Crisis y Contexto Político
- Correlación con crisis económicas (2001 Argentina, 2008 global)
- Análisis de regímenes autoritarios (patrones de adopción de términos)
- Transiciones democráticas (momentos de rediseño constitucional)

### BLOQUE 5: Preparación para Herramientas Computacionales
- RootFinder (grafos genealógicos)
- IusMorfos (puntajes de viabilidad de trasplantes)
- JurisRank (métricas de centralidad de citación)
- Legal-Memespace (coordenadas ideológicas)

### BLOQUE 6: Validación de Hipótesis
- Testeo estadístico (regresión logística, PSM)
- Análisis de casos desviantes (resultados anómalos)
- Métricas de aptitud memética (cuantificación de éxito reproductivo)

## Términos Clave Analizados

1. **"bien común"** - Common good
2. **"bienestar general"** - General welfare
3. **"interés público"** - Public interest
4. **"orden público"** - Public order
5. **"seguridad jurídica"** - Legal certainty

## Metodología

**Recolección de Datos:**
- Scraping de textos constitucionales (fuentes gubernamentales oficiales)
- Consultas a bases jurisprudenciales (SAIJ, Lex Paulista, SCJN, etc.)
- Minería bibliométrica (Google Scholar, SSRN, SciELO)
- Codificación manual con chequeos de confiabilidad inter-evaluadores

**Técnicas Estadísticas:**
- Regresión logística (resultado ~ término_legitimador + controles)
- Propensity Score Matching (inferencia causal)
- Análisis de redes (patrones de citación)
- Procesamiento de lenguaje natural (embeddings contextuales)

**Control de Calidad:**
- Etiquetado de confianza: `[VERIFICADO]` / `[INFERENCIA]` / `[ESTIMACIÓN]`
- Declaraciones de muestra (exhaustiva vs. representativa)
- Triangulación entre fuentes
- **Principio: CALIDAD > CANTIDAD**

## Formatos de Entregables

**Datos Tabulares:**
- Formato CSV, codificación UTF-8
- Encabezados claros, sin celdas fusionadas
- Archivos separados por unidad analítica

**Análisis Narrativos:**
- Documentos estructurados en Markdown
- Citas completas con URLs/DOIs
- Encabezados de sección para navegación

**Advertencias/Limitaciones:**
- Declaración explícita del alcance de búsqueda
- Niveles de confianza marcados
- Decisiones de exclusión/muestreo documentadas

## Autor

**Adrián Lerer**
- GitHub: [@adrianlerer](https://github.com/adrianlerer)
- Repositorio: https://github.com/adrianlerer/bien-comun-bienestar-general

## Licencia

[Pendiente de especificación]

## Estado del Proyecto

**Fase actual:** FASE 1 - Fundamentos (en progreso)

**Última actualización:** 2025-11-14
