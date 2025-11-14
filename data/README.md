# Datos del Proyecto

## Estructura de Directorios

```
data/
├── raw/                  # Datos sin procesar
│   ├── constitutional_texts/
│   ├── jurisprudence/
│   ├── philosophical_corpus/
│   └── bibliometric/
├── processed/            # Datos codificados y limpios
└── external/             # Datos de fuentes externas
```

## Fuentes de Datos

### Constituciones (`raw/constitutional_texts/`)

| País | Versiones | Fuente | Licencia |
|------|-----------|--------|----------|
| Argentina | 1853, 1949, 1994 | Infoleg / Biblioteca Congreso | Dominio público |
| Brasil | 1988 | Planalto | Dominio público |
| Chile | 1980, 2005 | BCN | Dominio público |
| México | 1917 (reformas) | Diputados | Dominio público |
| Colombia | 1991 | Corte Constitucional | Dominio público |
| Perú | 1979, 1993 | Congreso | Dominio público |
| Paraguay | 1992 | Congreso | Dominio público |
| Uruguay | 1967 | Parlamento | Dominio público |
| Venezuela | 1999 | Asamblea Nacional | Dominio público |
| Ecuador | 2008 | Asamblea Nacional | Dominio público |

**Formato:** Plain text UTF-8, markdown para anotaciones estructurales

**Metadata:** `metadata.json` en cada carpeta de país incluye:
- Fecha de promulgación
- Reformas principales
- Fuente exacta (URL)
- Fecha de descarga

---

### Jurisprudencia (`raw/jurisprudence/`)

#### Argentina - CSJN
- **Período:** 1960-2024
- **n:** 150 casos (target)
- **Fuente:** https://sjconsulta.csjn.gov.ar
- **Criterios de inclusión:** 
  - Menciona "bien común" OR "bienestar general" OR "interés público" en fundamentos (no solo en citas de partes)
  - Áreas: familia, economía, libertad expresión, ambiental, laboral
  - Decisión no unánime (preferible) o caso emblemático
- **Formato:** 
  - `full_texts/`: PDFs originales (no versionados por tamaño, usuarios deben descargar)
  - `metadata/`: CSV con carátula, fecha, ministros, URL
  - `coded/`: CSV con variables codificadas

**Variables codificadas:**
- caso_id
- año
- area_legal (familia/economia/expresion/ambiental/laboral/otro)
- termino_mayoria (bien_comun/bienestar_general/interes_publico/otro)
- termino_disidencia (si aplica)
- resultado (1=individualista, 0=comunitarista, escala -2 a +2 para análisis sensibilidad)
- crisis (1=país en crisis económica, 0=normalidad)
- composicion_conservadora (% de ministros con perfil conservador)
- cita_tratados (1=cita CADH/PIDCP, 0=no)
- citas_posteriores (count de citas en años subsiguientes)

#### Otros Países
Estructura análoga, menor n por país (target 40-50 c/u):
- Brasil (STF)
- Chile (Tribunal Constitucional)
- Colombia (Corte Constitucional)
- México (SCJN)
- Perú (Tribunal Constitucional)

#### Inter-American Court of Human Rights (IACHR)
- **Período:** 1980-2024
- **n:** 20-30 casos
- **Fuente:** https://www.corteidh.or.cr/
- **Criterios:** Casos vs. países latinoamericanos que citan "bien común" en fundamentos

---

### Corpus Filosófico (`raw/philosophical_corpus/`)

#### Textos Clásicos
Selecciones relevantes (no obras completas por derechos de autor en traducciones):

**Dominio público (pre-1928):**
- Aristóteles: Política (trad. Patricio de Azcárate, 1873)
- Tomás de Aquino: Summa Theologiae (trad. varias, dominio público)
- Locke: Two Treatises (ed. 1690, dominio público)
- Bentham: Principles (ed. 1789, dominio público)

**Uso académico fair use:**
- Extractos breves (<500 palabras) de autores contemporáneos para análisis crítico
- Citaciones completas y sin reproducción extensa

**Formato:** Plain text, un archivo por autor/obra, metadata en JSON.

---

### Doctrina Social Católica (`raw/philosophical_corpus/catholic_social_teaching/`)

**Fuente:** Vatican.va (dominio público para documentos pontificios)

**Documentos incluidos:**
- Rerum Novarum (León XIII, 1891)
- Quadragesimo Anno (Pío XI, 1931)
- Mater et Magistra (Juan XXIII, 1961)
- Gaudium et Spes (Concilio Vaticano II, 1965)
- Centesimus Annus (Juan Pablo II, 1991)
- Compendio DSI (Pontificio Consejo Justicia y Paz, 2004)
- Laudato Si' (Francisco, 2015)
- Fratelli Tutti (Francisco, 2020)

**Formato:** HTML original convertido a markdown

---

### Variables Contextuales (`external/`)

#### Indicadores Económicos
- **Fuente:** Banco Mundial, FMI, CEPAL
- **Variables:** PIB trimestral, inflación anual, tipo de cambio, default deuda
- **Período:** 1980-2024
- **Formato:** CSV con columnas [país, año, trimestre, variable, valor, fuente]

#### Variables Políticas
- **Fuente:** V-Dem, Polity IV, Comparative Constitutions Project
- **Variables:** Régimen político, método designación judicial, crisis políticas
- **Formato:** CSV

---

## Datos Procesados (`processed/`)

### constitutional_terms_inventory.csv

Inventario completo de términos en constituciones.

**Columnas:**
- pais
- constitucion_año
- articulo
- termino_original
- termino_normalizado (bien_comun / bienestar_general / interes_publico / orden_publico / seguridad_juridica)
- contexto_textual (±50 palabras)
- funcion_normativa (limite_derechos / objetivo_estado / clausula_interpretacion / expropiacion / tributacion)
- area_sustantiva
- año_incorporacion
- coocurrencias (términos que aparecen en mismo artículo)
- nivel_confianza (VERIFICADO / INFERENCIA / ESTIMACION)

**n esperado:** ~300 filas

**Estado actual:** 12 filas verificadas (Argentina, Chile, México, Colombia, Perú)

---

### jurisprudence_coded.csv

Dataset principal para análisis estadístico.

**Columnas:** (ver variables codificadas arriba)

**n esperado:** 300-400 filas (150 Argentina + 150-250 otros países)

**Control de calidad:**
- Double-coding de 30% muestra aleatoria
- Inter-rater reliability κ > 0.80
- Casos ambiguos discutidos hasta consenso

**Estado actual:** 13 casos seed estructurados

---

### crisis_timeline.csv

Timeline de crisis económicas por país.

**Columnas:**
- pais
- inicio (fecha)
- fin (fecha)
- tipo (recesion / hiperinflacion / default / corralito / devaluacion)
- severidad (1-5)
- fuente

**n esperado:** 20-30 crisis

---

### genealogical_links.csv

Relaciones genealógicas entre textos filosóficos y uso constitucional/jurisprudencial.

**Columnas:**
- texto_origen (ej. "Aquinas_Summa_I-II_q90")
- texto_destino (ej. "Argentina_CSJN_Sejean_1986")
- tipo_relacion (cita_directa / influencia_conceptual / replica_argumento)
- confianza (0-1, basado en evidencia textual)
- anotacion (explicación breve de la relación)

**n esperado:** 100-200 links

**Método de construcción:** RootFinder + validación manual

---

## Políticas de Uso

### Datos Públicos
Textos constitucionales, jurisprudencia, y documentos pontificios son de dominio público. Pueden ser redistribuidos libremente.

### Datos Procesados
Datasets codificados (`processed/`) están bajo CC BY 4.0. Uso libre con atribución.

### Restricciones
- No redistribuir obras con copyright (corpus filosófico moderno). Usuarios deben obtener textos de fuentes legales.
- PDFs de jurisprudencia no versionados por tamaño; scripts provistos para descarga automatizada desde fuentes oficiales.

---

## Actualización de Datos

**Última actualización:** 2025-11-14

**Proceso de actualización:**
1. Nuevas constituciones/reformas: revisar anualmente
2. Jurisprudencia: agregar casos relevantes semestralmente
3. Variables económicas: actualizar trimestralmente

**Log de cambios:** Ver `CHANGELOG.md` en raíz del repositorio.

---

## Control de Calidad

### Verificación de Fuentes
- Todos los textos constitucionales verificados contra fuentes oficiales
- Jurisprudencia verificada contra bases de datos oficiales de cada tribunal
- Documentos filosóficos verificados contra ediciones académicas estándar

### Codificación de Variables
- **Protocolo de doble codificación:** 30% de muestra aleatoria codificada independientemente por dos investigadores
- **Inter-rater reliability:** Kappa de Cohen > 0.80 requerido
- **Resolución de desacuerdos:** Discusión hasta consenso, documentado en notas

### Niveles de Confianza
- **[VERIFICADO]:** Datos extraídos directamente de fuente primaria oficial
- **[INFERENCIA]:** Datos inferidos mediante razonamiento explícito documentado
- **[ESTIMACION]:** Datos estimados mediante método proxy (ej. año de incorporación = año constitución base)

---

## Contribuciones

Si desea contribuir datos o correcciones:

1. Abra un Issue describiendo el problema o contribución
2. Para correcciones menores, envíe Pull Request con:
   - Fuente primaria que respalda la corrección
   - Explicación del cambio
   - Nivel de confianza del dato corregido

3. Para contribuciones mayores (ej. nuevo país), contacte al investigador principal antes de invertir tiempo

Ver `CONTRIBUTING.md` para lineamientos detallados (próximamente).
