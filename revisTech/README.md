# RevisTech - Revista Digital de Tecnología

Revista digital mensual especializada en tendencias y análisis profundo de tecnología, desarrollo de software, arquitectura de software, nube, inteligencia artificial y ciberseguridad.

## 📋 Estructura

```
revisTech/
├── template/               # Templates base
│   └── base.html          # Template HTML principal (10 páginas)
├── content/
│   ├── articles/          # Artículos generados (por edición)
│   └── research/          # Investigación y fuentes
├── issues/                # Ediciones publicadas
│   ├── 2026-07.html       # Edición julio 2026
│   └── [ediciones...]
├── scripts/               # Herramientas y utilidades
├── automation/            # Configuración de automatización
│   ├── prompts/           # Prompts para agentes
│   └── routines.md        # Configuración de Routines
└── config.json            # Configuración del proyecto
```

## 🎨 Especificaciones de Diseño

### Paleta de Colores
- **Fondo Primario**: `#0F172A` (Azul marino profundo)
- **Accent Primario**: `#00D9FF` (Cyan tech)
- **Accent Secundario**: `#8B5CF6` (Púrpura - IA)
- **Accent Peligro**: `#FF6B6B` (Rojo - Ciberseguridad)
- **Texto**: `#F0F7FF` (Blanco azulado)
- **Texto Secundario**: `#94A3B8` (Gris azulado)

### Tipografía
- **Display**: Space Grotesk (títulos y headers)
- **Body**: Inter (texto principal)
- **Mono**: IBM Plex Mono (datos y código)

### Dimensiones
- **Ancho**: 900px (máximo)
- **Alto por página**: 100vh (viewport completo)
- **Páginas**: 10 (Portada, TOC, 6 secciones, 2 finales)

## 📄 Secciones

1. **Portada**: Presentación de la revista
2. **Tabla de Contenido**: Índice visual (6 secciones)
3. **Tecnología**: Computación cuántica, semiconductores, 5G/6G, edge computing
4. **Desarrollo de Software**: Frameworks, testing, CI/CD, Rust
5. **Arquitectura de Software**: Microservicios, escalabilidad, observabilidad
6. **Nube**: Multi-cloud, Kubernetes, FinOps, edge cloud
7. **Inteligencia Artificial**: LLMs, agentes, prompt engineering, gobernanza
8. **Ciberseguridad**: IA adversaria, criptografía post-cuántica, Zero Trust
9. **Cierre**: Reflexión y llamado a acción
10. **Contraportada**: Información y contacto

## 🤖 Automatización

La revista es completamente automatizable usando un sistema de agentes Claude:

### Pipeline de Agentes
1. **Research Agent**: Investiga tendencias y fuentes
2. **Writer Agent**: Redacta contenido de las 6 secciones
3. **Designer Agent**: Genera HTML integrado e imágenes
4. **Review Agent**: QA de contenido y hechos
5. **Publish Agent**: Versionea y publica

Ver `automation/routines.md` para configuración completa.

## 📅 Cadencia

- **Mensual**: Edición nueva cada mes
- **Trigger**: Primer día del mes (configurable)
- **Versioning**: `issues/YYYY-MM.html`

## 🛠️ Herramientas

- **Investigación**: Web search, APIs de news
- **Redacción**: Claude API (LLM)
- **Diseño**: HTML/CSS, Adobe Stock (imágenes)
- **Revisión**: Claude API (fact-check)
- **Publicación**: Git + GitHub Pages

## 📖 Próximas Ediciones

- [ ] 2026-08: Focus en WebAssembly y Edge Computing
- [ ] 2026-09: Focus en Quantum Computing Advances
- [ ] 2026-10: Focus en AI Security & Alignment

## 📝 Guía de Contribución

Para ediciones manuales:
1. Crear rama `feature/revisTech-YYYY-MM`
2. Editar archivos en `content/`
3. Actualizar `template/base.html` si aplica
4. PR con descripción de cambios
5. Merge a main y publicar

## 📞 Contacto & Info

- **Editor**: IA (Claude)
- **Frecuencia**: Mensual
- **Suscripción**: [Próximamente]
- **Archivo**: `/issues/`

---

**Última actualización**: Julio 2026  
**Próxima edición**: Agosto 2026
