# Bien Común vs. Bienestar General: Análisis Memético de Términos Legitimadores Constitucionales

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: In Progress](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)](https://github.com/adrianlerer/bien-comun-bienestar-general)

## Descripción del Proyecto

Este repositorio contiene datos, código y documentación para el proyecto de investigación que analiza términos legitimadores constitucionales ("bien común", "bienestar general", "interés público") desde la perspectiva de Extended Phenotype Theory (EPT) aplicada a sistemas legales.

**Investigador Principal:** Adrian Lerer  
**Afiliación:** Independent Scholar, Buenos Aires, Argentina  
**Período:** 2024-2025  
**Estado:** Work in Progress - Fase 1 (Recolección de Datos)

## Pregunta de Investigación Central

¿Los términos legitimadores constitucionales operan como premisas normativas independientes o como marcadores de identidad memética que predeterminan resultados institucionales?

## Hipótesis Principal

Los términos legitimadores no transmiten contenido normativo sino **identidad memética**. La elección del término (bien común vs. bienestar general) predice el resultado del caso mejor que variables contextuales, porque cada término porta genealogías filosóficas completas que actúan como fenotipos extendidos de memeplexos competidores.

### Mecanismo Propuesto

```
GENEALOGÍA FILOSÓFICA → TÉRMINO LEGITIMADOR → RESULTADO INSTITUCIONAL
      (material genético)      (fenotipo)         (fitness diferencial)
```

**"Bien común":** Aristóteles → Tomás de Aquino → Doctrina Social Católica → Constituciones LatAm  
→ Favorece: beneficiarios presentes, organizados, participación comunitaria

**"Bienestar general":** Locke → Constitución USA → Bentham → Alberdi → Constituciones LatAm  
→ Favorece: beneficiarios futuros, difusos, maximización utilidad agregada

## Estructura del Repositorio

```
├── data/          # Datos primarios y procesados
├── analysis/      # Scripts de análisis estadístico y cualitativo
├── tools/         # Herramientas computacionales (RootFinder, JurisRank, etc.)
├── outputs/       # Figuras, tablas, reportes generados
├── docs/          # Documentación teórica y metodológica
├── notebooks/     # Jupyter notebooks exploratorios
└── prompts/       # Prompts para recolección de datos con IA
```

## Datos

### Corpus Principal
- **Constituciones:** 10 países latinoamericanos (1853-2024)
- **Jurisprudencia:** ~300 casos de Cortes Supremas/Tribunales Constitucionales
  - Argentina (CSJN): n=150 (target)
  - Chile, Colombia, México, Brasil, Perú: n=150 (total)
- **Textos filosóficos:** Corpus genealógico desde Aristóteles (335 BCE) hasta documentos pontificios contemporáneos (2020)
- **Variables contextuales:** Crisis económicas, composición tribunales, reformas constitucionales

### Acceso a Datos
Los datos están organizados en `data/raw/` (fuentes originales) y `data/processed/` (datasets codificados). Ver `data/README.md` para detalles sobre fuentes y licencias.

**Nota sobre datos sensibles:** Algunos textos jurisprudenciales pueden estar sujetos a restricciones de uso. El repositorio incluye metadata y códigos de identificación para replicación, pero usuarios deben obtener textos completos de fuentes oficiales cuando sea necesario.

## Herramientas Computacionales

Este proyecto desarrolla/adapta cuatro herramientas:

### 1. **RootFinder** - Genealogía de Conceptos Legales
Traza linajes filosóficos desde textos fundacionales hasta uso constitucional/jurisprudencial contemporáneo.

**Funcionalidades:**
- Identificación de citaciones directas e influencias conceptuales
- Cálculo de distancia semántica (cosine similarity entre embeddings)
- Visualización de árboles genealógicos
- Detección de mutaciones semánticas

**Implementación:** `tools/rootfinder/`

### 2. **JurisRank** - Fitness Institucional de Precedentes
Análisis de redes de citación con decay temporal para medir "fitness" de conceptos legales.

**Funcionalidades:**
- PageRank con decay temporal exponencial
- Identificación de precedentes "ancestrales" (alta centralidad)
- Medición de aptitud reproductiva (citas en años subsiguientes)
- Detección de conceptos "extintos" (dejaron de citarse)

**Implementación:** `tools/jurisrank/`

### 3. **Legal-Memespace** - Competencia Memética entre Doctrinas
Mapeo espacial de conceptos legales para visualizar competencia territorial.

**Funcionalidades:**
- Embeddings de textos legales (BERT multilingüe)
- Reducción dimensional (UMAP/t-SNE)
- Identificación de "territorios" doctrinales (clustering)
- Análisis de invasiones meméticas (casos donde término "invade" territorio ajeno)

**Implementación:** `tools/legal_memespace/`

### 4. **IusMorfos** - Predicción de Trasplantes Legales
Matriz de compatibilidad para predecir éxito de adopción de conceptos entre jurisdicciones.

**Funcionalidades:**
- Cálculo de compatibilidad genealógica (overlap de linajes filosóficos)
- Predicción de supervivencia de trasplantes
- Identificación de "especies invasoras" (conceptos que prosperan fuera de origen)

**Implementación:** `tools/iusmorfos/`

## Metodología

### Análisis Cuantitativo
- **Regresión logística:** Predicción de resultados según término usado
- **Propensity Score Matching:** Control de sesgo de selección
- **Análisis de redes:** JurisRank para fitness de precedentes
- **Modelos multinivel:** Efectos país en análisis cross-nacional

### Análisis Cualitativo
- **Estudios de caso:** Casos paradigmáticos (Sejean, Mendoza, etc.)
- **Análisis histórico:** Debates constituyentes
- **Reconstrucción argumental:** Mapeo de estructuras argumentativas

### Procesamiento NLP
- **Embeddings semánticos:** BERT multilingüe para análisis semántico
- **Análisis de sentimientos:** (no aplicado - términos no tienen valencia emocional clara)
- **Topic modeling:** LDA para identificar temas asociados a cada término
- **Similarity metrics:** Cosine similarity para distancias genealógicas

Ver `docs/methodology.md` para protocolo completo.

## Resultados Preliminares

**[Actualizado 2025-11-14]**

### Fase 1: Inventario Constitucional
- ✅ **Genealogía "Bien Común" completa:** Aristóteles → Tomás → DSI → Chile/Colombia (2,350 años)
- ✅ **Genealogía "Bienestar General" completa:** Locke → USA → Bentham → Alberdi → Argentina/Perú (336 años)
- ⏳ **Inventario constitucional:** 12/300 ocurrencias verificadas
  - Argentina: 1 ("bienestar general" Preámbulo)
  - Chile: 4 ("bien común" Art. 1, "interés público" Art. 19-24, "orden público" 3x)
  - México: 2 ("interés general", "orden jurídico")
  - Colombia: 2+ ("bien común" Art. 333, "interés general" Art. 1)
  - Perú: 2 ("bienestar general" Art. 44, "orden público" Art. 2)

### Fase 1: Corpus Jurisprudencial
- ⏳ **Estructura de dataset creada:** 13 casos seed (Argentina, Chile, Colombia, Perú, México, Brasil)
- ⏳ **Target:** 300 casos totales (150 Argentina CSJN + 150 otros países)

### Hallazgos Genealógicos Clave
1. **Bifurcación terminológica confirmada:**
   - Norte de LatAm (México, Colombia, Venezuela): predomina "bien común" (herencia hispánica)
   - Sur de LatAm (Argentina, Paraguay, Uruguay): predomina "bienestar general" (influencia USA)
   
2. **Colombia como caso híbrido:** Usa "interés general" (Art. 1) y "bien común" (Art. 333) simultáneamente
   
3. **Incompatibilidades filosóficas documentadas:** 11 dimensiones de divergencia entre linajes (ver `docs/genealogies/`)

Ver `outputs/reports/` para informes actualizados.

## Publicaciones Planeadas

### Working Papers
- **[En preparación]** "Fundamentos sin Fundamento: Análisis Memético de Términos Legitimadores Constitucionales"  
  Target: SSRN (2025-Q1), luego Law & Society Review

### Presentaciones
- **[Target]** IPSA World Congress 2025
- **[Target]** SELA (Seminario en Latinoamérica de Teoría Constitucional y Política) 2025

## Replicación

Para replicar los análisis:

```bash
# 1. Clonar repositorio
git clone https://github.com/adrianlerer/bien-comun-bienestar-general.git
cd bien-comun-bienestar-general

# 2. Crear ambiente
conda env create -f replication/environment.yml
conda activate bien-comun-analysis

# 3. Ejecutar pipeline completo
bash replication/run_all_analyses.sh
```

Ver `replication/README_replication.md` para instrucciones detalladas.

**Nota:** Fase 1 (recolección de datos) aún en progreso. Scripts de replicación serán funcionales tras completar Fase 1.

## Citación

Si usa datos o herramientas de este proyecto, cite como:

```bibtex
@misc{lerer2025biencomun,
  author = {Lerer, Adrian},
  title = {Bien Común vs. Bienestar General: Análisis Memético de Términos Legitimadores Constitucionales},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/adrianlerer/bien-comun-bienestar-general},
  note = {Work in Progress}
}
```

## Licencia

- **Código:** MIT License
- **Datos originales:** CC BY 4.0 (donde aplicable; ver licencias específicas en `data/README.md`)
- **Textos constitucionales y jurisprudenciales:** Dominio público o sujetos a términos de fuentes oficiales
- **Documentos pontificios:** Dominio público (fuente: vatican.va)

## Contacto

**Adrian Lerer**  
Email: adrianlerer@gmail.com  
SSRN: https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=3716273  
GitHub: https://github.com/adrianlerer

## Agradecimientos

Este proyecto se beneficia de:
- Herramientas Genspark para recolección de datos asistida por IA
- Claude (Anthropic) para asistencia en análisis estadístico y genealogía conceptual
- Comunidad SSRN y revisores anónimos por feedback en versiones preliminares

## Estado del Proyecto

**Última actualización:** 2025-11-14  
**Fase actual:** 🟡 Fase 1 - Recolección de Datos (30% completo)

### Completado ✅
- [x] Estructura de repositorio
- [x] Documentación teórica inicial
- [x] Genealogía "Bien Común" completa (Prompt 1.3)
- [x] Genealogía "Bienestar General" completa (Prompt 1.4)
- [x] Inventario constitucional preliminar (12 ocurrencias verificadas)
- [x] Estructura de dataset jurisprudencial

### En Progreso 🟡
- [ ] Prompt 1.1: Inventario constitucional exhaustivo (target 200-300 ocurrencias) - **30% completo**
- [ ] Prompt 2.1: Corpus jurisprudencial LatAm - **10% completo**
- [ ] Prompt 2.2: CSJN Argentina análisis intensivo (target 50-80 casos) - **0% completo**

### Pendiente ⚪
- [ ] Herramientas computacionales (RootFinder, JurisRank, Legal-Memespace, IusMorfos)
- [ ] Análisis estadístico
- [ ] Estudios de caso cualitativos
- [ ] Working paper

### Blockers 🔴
- Ninguno actualmente

---

**Contribuciones:** Este proyecto está en desarrollo activo. Issues y pull requests son bienvenidos para:
- Correcciones de datos constitucionales/jurisprudenciales
- Mejoras en herramientas computacionales
- Sugerencias metodológicas

Ver `CONTRIBUTING.md` para lineamientos (próximamente).
