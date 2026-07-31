# 🤖 Automatización de RevisTech

Configuración completa para automatizar el pipeline de generación de la revista mensual.

## Arquitectura General

```
┌─────────────────────────────────────────────────┐
│      ROUTINE TRIGGER (Primer día del mes)       │
└────────────────────┬────────────────────────────┘
                     │
         ┌───────────┼───────────┬────────────┐
         │           │           │            │
    ┌────▼────┐  ┌───▼────┐  ┌──▼───┐  ┌────▼─────┐
    │RESEARCH │  │ WRITER │  │DESIGN│  │ REVIEWER │
    │AGENT    │  │ AGENT  │  │AGENT │  │ AGENT    │
    └────┬────┘  └───┬────┘  └──┬───┘  └────┬─────┘
         │           │           │           │
         └───────────┼───────────┼───────────┘
                     │
         ┌───────────▼──────────────────┐
         │    PUBLISHER AGENT           │
         │ - Versionamiento en Git      │
         │ - Commit & Push              │
         │ - Notificación               │
         └──────────────────────────────┘
```

## Routines Configuradas

### Routine 1: Research Agent
**Nombre**: `revisTech-research-monthly`  
**Schedule**: `0 0 1 * *` (1º de cada mes, 00:00 UTC)  
**Descripción**: Investiga tendencias en tech para el mes

```
Ejecuta:
1. Búsqueda de tendencias por sección
2. Recopila fuentes y URLs
3. Genera `content/research/YYYY-MM.md`
4. Commit automático con findings
```

**Prompt Template**:
```
Investiga las tendencias más importantes del mes en [SECCIÓN].
Proporciona:
- 3-5 tendencias clave
- URLs de fuentes confiables
- Contexto breve de cada tendencia
Formato: Markdown

Secciones a cubrir:
1. Tecnología
2. Desarrollo de Software
3. Arquitectura
4. Nube
5. IA
6. Ciberseguridad
```

### Routine 2: Writer Agent
**Nombre**: `revisTech-writer-monthly`  
**Schedule**: Se dispara DESPUÉS de Research (depende de su finalización)  
**Descripción**: Redacta contenido de las 6 secciones

```
Ejecuta:
1. Lee research findings
2. Genera 4 artículos por sección (24 total)
3. Genera `content/articles/YYYY-MM/[section].md`
4. Commit con artículos
```

**Prompt Template**:
```
Eres redactor de tecnología experto. Basándote en estas tendencias:
[RESEARCH FINDINGS]

Genera 4 artículos profesionales para la sección [SECCIÓN]:
- Título técnico y atractivo
- Párrafo introductorio (2-3 líneas)
- Descripción breve (100-150 palabras)
- Lectura estimada (minutos)
- Tags relevantes

Tono: Profesional pero accesible. Evita jerga innecesaria.
Formato: JSON array
```

### Routine 3: Designer Agent
**Nombre**: `revisTech-designer-monthly`  
**Schedule**: Se dispara DESPUÉS de Writer  
**Descripción**: Genera HTML integrado

```
Ejecuta:
1. Lee articles finales
2. Busca/licencia imágenes relevantes
3. Genera HTML completo
4. Produce `issues/YYYY-MM.html`
5. Commit con nueva edición
```

**Tareas específicas**:
- Buscar 6 imágenes (1 por sección) en Adobe Stock
- Integrar artículos en estructura HTML
- Validar responsive design
- Optimizar para impresión

### Routine 4: Reviewer Agent
**Nombre**: `revisTech-reviewer-monthly`  
**Schedule**: Se dispara DESPUÉS de Designer  
**Descripción**: Revisión editorial y fact-checking

```
Ejecuta:
1. Lee HTML generado
2. Fact-check de datos/estadísticas
3. Verifica tono y coherencia
4. Genera `automation/reviews/YYYY-MM.md`
5. Aprueba o solicita correcciones
```

**Checklist de Revisión**:
```
□ Hechos verificables (búsquedas web)
□ Tono coherente entre secciones
□ Imágenes cargan correctamente
□ Títulos son engaging
□ No hay duplicación de contenido
□ Estadísticas tienen fuentes
□ HTML renderiza correctamente
```

### Routine 5: Publisher Agent
**Nombre**: `revisTech-publisher-monthly`  
**Schedule**: Se dispara DESPUÉS de Reviewer (si aprobado)  
**Descripción**: Publica la edición final

```
Ejecuta:
1. Verifica aprobación
2. Crea rama `release/revisTech-YYYY-MM`
3. Commit final con changelog
4. Push a main
5. Crea GitHub Release
6. Notifica (email/Slack)
```

**Changelog automático**:
```
RevisTech - Edición [MES/AÑO]

Secciones:
- Tecnología: [3-4 topics principales]
- Desarrollo: [topics]
- Arquitectura: [topics]
- Nube: [topics]
- IA: [topics]
- Ciberseguridad: [topics]

Total: 24 artículos + 6 imágenes

Investigación: [fuentes clave]
Revisor: Claude IA
```

## Instalación

### Paso 1: Crear Routines
```bash
# Con Claude Code CLI
claude routine create \
  --name "revisTech-research-monthly" \
  --schedule "0 0 1 * *" \
  --prompt "$(cat prompts/research.md)"

# Repetir para cada Routine (writer, designer, reviewer, publisher)
```

### Paso 2: Verificar Dependencias
Asegurar que cada Routine puede:
- Leer archivos previos del repo
- Hacer commits automáticos
- Acceder a APIs (Adobe Stock, Web Search)

### Paso 3: Test Run
```bash
# Ejecutar manualmente una vez para verificar
claude trigger fire revisTech-research-monthly
```

## Mejoras Futuras

- [ ] Agregar webhooks para CI/CD
- [ ] Integrar con Slack para notificaciones
- [ ] Generar múltiples formatos (PDF, EPUB)
- [ ] A/B testing de títulos
- [ ] Análisis de engagement post-publicación
- [ ] Sugerencias automáticas de temas para próxima edición

## Monitoreo

Ver estado de Routines:
```bash
claude routine list
claude routine get revisTech-research-monthly
```

Ver logs de última ejecución:
```bash
# En GitHub Actions o logs de CLI
git log --oneline --grep="revisTech" 
```

## Troubleshooting

| Problema | Solución |
|----------|----------|
| Rutina no dispara | Verificar cron: `0 0 1 * *` = primer día del mes |
| Error en búsqueda | Verificar API keys de Adobe Stock |
| HTML no renderiza | Ejecutar validador: `claude design validate issues/YYYY-MM.html` |
| Commit falla | Verificar permisos de rama en repositorio |
| Imágenes no cargan | Verificar URLs de Stock, licencias activas |

---

**Última actualización**: Julio 2026
