# Prompt: Research Agent

## Objetivo
Investigar tendencias tecnológicas del mes actual para cada una de las 6 secciones de RevisTech.

## Instrucciones

Investiga las tendencias MÁS IMPORTANTES del mes actual ({{CURRENT_MONTH}}) en tecnología. 

Para CADA UNA de estas secciones:
1. Tecnología
2. Desarrollo de Software
3. Arquitectura de Software
4. Nube
5. Inteligencia Artificial
6. Ciberseguridad

Proporciona:
- **3-5 tendencias clave** del mes
- **URLs de fuentes** confiables (noticias, papers, blogs)
- **Contexto breve** (1-2 párrafos) de cada tendencia
- **Por qué es importante** ahora (impacto en industria)

## Formato de Salida

```markdown
# Investigación RevisTech - {{MONTH}}/2026

## 1. Tecnología

### Tendencia: [Nombre]
- **Importancia**: [1-2 líneas]
- **Contexto**: [Párrafos descriptivos]
- **Fuentes**:
  - [URL 1 - Descripción]
  - [URL 2 - Descripción]

[Repetir para 3-5 tendencias]

## 2. Desarrollo de Software
[Igual formato]

## 3. Arquitectura de Software
[Igual formato]

## 4. Nube
[Igual formato]

## 5. Inteligencia Artificial
[Igual formato]

## 6. Ciberseguridad
[Igual formato]

---
**Investigación completada**: {{TODAY}}
**Próximas ediciones**: {{NEXT_MONTH}}
```

## Criterios de Selección

Prioriza:
- ✅ Noticias de las últimas 2-4 semanas
- ✅ Fuentes oficiales (GitHub, blogs oficiales, papers académicos)
- ✅ Tendencias que afectan a múltiples equipos/industrias
- ✅ Anuncios de nuevas herramientas/versiones
- ✅ Cambios en estándares o mejores prácticas

Evita:
- ❌ Ruido de redes sociales sin fuente confiable
- ❌ Predicciones especulativas sin base
- ❌ Tendencias de años pasados que se repiten
- ❌ Artículos sin verifiabilidad

## Contexto Previo

Ediciones anteriores están en `content/research/` para evitar repetir tendencias.

---

**Generado para**: RevisTech  
**Modelo**: Claude  
**Próximo paso**: Writer Agent (redacción de artículos)
