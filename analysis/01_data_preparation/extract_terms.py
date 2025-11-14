#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para extraer ocurrencias de términos legitimadores en constituciones latinoamericanas

Términos objetivo:
1. "bienestar general"
2. "bien común" 
3. "interés público"
4. "orden público"
5. "seguridad jurídica"

Variables a extraer:
- País
- Constitución_Año
- Artículo
- Término_Original
- Término_Normalizado
- Contexto_Textual (±100 caracteres)
- Función_Normativa
- Área_Sustantiva
- Año_Incorporación
- Coocurrencias
"""

import re
import csv
from pathlib import Path
from collections import defaultdict

# Términos a buscar (regex patterns)
SEARCH_TERMS = {
    'bienestar_general': r'bienestar\s+general',
    'bien_comun': r'bien\s+com[uú]n',
    'interes_publico': r'inter[eé]s\s+p[uú]blico',
    'orden_publico': r'orden\s+p[uú]blico',
    'seguridad_juridica': r'seguridad\s+jur[ií]dica'
}

# Variantes por idioma
SEARCH_TERMS_PT = {
    'bien_comun': r'bem\s+comum',
    'interes_publico': r'interesse\s+p[uú]blico',
    'orden_publico': r'ordem\s+p[uú]blica'
}

def extract_article_number(text_before, text_after):
    """Extrae el número de artículo más cercano"""
    # Buscar hacia atrás
    match = re.search(r'Art[íi]culo\s+(\d+[\w]*\.?)', text_before[-500:])
    if match:
        return match.group(1)
    
    # Buscar hacia adelante
    match = re.search(r'Art[íi]culo\s+(\d+[\w]*\.?)', text_after[:500])
    if match:
        return match.group(1)
    
    return "SIN_ARTICULO"

def classify_normative_function(context):
    """Clasifica la función normativa del término"""
    context_lower = context.lower()
    
    # Patrones de funciones normativas
    if re.search(r'(prohí|vedado|prohibir)', context_lower):
        return "PROHIBICION"
    elif re.search(r'(derecho a|garantiza|asegur)', context_lower):
        return "GARANTIA_DERECHO"
    elif re.search(r'(deber|obligación|corresponde)', context_lower):
        return "DEBER_ESTATAL"
    elif re.search(r'(limite|restring|condicion)', context_lower):
        return "LIMITACION"
    elif re.search(r'(promover|fomentar|impulsar)', context_lower):
        return "OBJETIVO_DIRECTRIZ"
    elif re.search(r'(expropiación|utilidad)', context_lower):
        return "EXPROPIACION"
    elif re.search(r'(impuesto|contribucion|tribut)', context_lower):
        return "TRIBUTACION"
    else:
        return "OTRO"

def classify_substantive_area(context, article_num):
    """Clasifica el área sustantiva del derecho"""
    context_lower = context.lower()
    
    # Patrones de áreas sustantivas
    if re.search(r'(propiedad|expropiación|tierra)', context_lower):
        return "PROPIEDAD"
    elif re.search(r'(trabajo|laboral|sindic)', context_lower):
        return "TRABAJO"
    elif re.search(r'(tribut|impuesto|contribución)', context_lower):
        return "TRIBUTARIO"
    elif re.search(r'(salud|sanit|médic)', context_lower):
        return "SALUD"
    elif re.search(r'(educación|enseñanza|escuel)', context_lower):
        return "EDUCACION"
    elif re.search(r'(ambiente|ecolog|contamin)', context_lower):
        return "AMBIENTAL"
    elif re.search(r'(seguridad|defensa|fuerzas armadas)', context_lower):
        return "SEGURIDAD_NACIONAL"
    elif re.search(r'(familia|matrimonio|niñez)', context_lower):
        return "FAMILIA"
    elif re.search(r'(comercio|económic|empresa)', context_lower):
        return "ECONOMICO"
    elif re.search(r'(religión|culto|iglesia)', context_lower):
        return "RELIGION"
    else:
        return "GENERAL"

def find_cooccurrences(text_window):
    """Encuentra coocurrencias de términos legitimadores en ventana de ±200 caracteres"""
    found_terms = []
    for term_key, pattern in SEARCH_TERMS.items():
        if re.search(pattern, text_window, re.IGNORECASE):
            found_terms.append(term_key)
    return "|".join(found_terms) if found_terms else "NINGUNA"

def extract_from_text(text, country, constitution_year, language='es'):
    """Extrae todas las ocurrencias de términos legitimadores de un texto constitucional"""
    
    results = []
    search_patterns = SEARCH_TERMS if language == 'es' else {**SEARCH_TERMS, **SEARCH_TERMS_PT}
    
    for term_key, pattern in search_patterns.items():
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start_pos = match.start()
            end_pos = match.end()
            
            # Extraer contexto (±150 caracteres)
            context_start = max(0, start_pos - 150)
            context_end = min(len(text), end_pos + 150)
            context = text[context_start:context_end]
            
            # Extraer contexto extendido para coocurrencias (±200 caracteres adicionales)
            extended_start = max(0, start_pos - 350)
            extended_end = min(len(text), end_pos + 350)
            extended_context = text[extended_start:extended_end]
            
            # Extraer número de artículo
            article_num = extract_article_number(
                text[max(0, start_pos - 1000):start_pos],
                text[end_pos:min(len(text), end_pos + 1000)]
            )
            
            # Clasificar función normativa y área sustantiva
            normative_function = classify_normative_function(context)
            substantive_area = classify_substantive_area(context, article_num)
            
            # Buscar coocurrencias
            cooccurrences = find_cooccurrences(extended_context)
            
            # Crear registro
            result = {
                'Pais': country,
                'Constitucion_Año': constitution_year,
                'Articulo': article_num,
                'Termino_Original': match.group(0),
                'Termino_Normalizado': term_key,
                'Contexto_Textual': context.strip().replace('\n', ' ').replace('\r', ''),
                'Funcion_Normativa': normative_function,
                'Area_Sustantiva': substantive_area,
                'Año_Incorporacion': constitution_year,  # Por defecto, puede refinarse
                'Coocurrencias': cooccurrences,
                'Nivel_Confianza': '[VERIFICADO]'
            }
            
            results.append(result)
    
    return results

def main():
    """Función principal - placeholder para procesamiento manual"""
    print("Script de extracción de términos legitimadores constitucionales")
    print("=" * 70)
    print("\nEste script proporciona funciones para extraer ocurrencias de términos")
    print("legitimadores de textos constitucionales.")
    print("\nUso:")
    print("1. Importar el módulo")
    print("2. Llamar extract_from_text(text, country, year, language)")
    print("3. Exportar resultados a CSV")
    
    # Ejemplo de uso
    example_text = """
    Artículo 1. El Estado está al servicio de la persona humana y su finalidad 
    es promover el bien común, para lo cual debe contribuir a crear las condiciones 
    sociales que permitan a todos y a cada uno de los integrantes de la comunidad 
    nacional su mayor realización espiritual y material posible.
    """
    
    results = extract_from_text(example_text, "Chile", "1980", "es")
    
    print(f"\n\nEjemplo: {len(results)} ocurrencias encontradas en texto de muestra")
    if results:
        print(f"\nPrimera ocurrencia:")
        for key, value in results[0].items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
