# Guía de Configuración: Gumroad para Quantic IA Magazine

## Introducción

Gumroad es una plataforma para vender productos digitales sin comisiones altas. Perfecto para:
- Ebooks ($9.99-19.99)
- Cursos online ($99+)
- Masterclasses ($49.99+)
- Datasets y recursos ($19.99+)

---

## Paso 1: Crear Cuenta de Gumroad

1. Ve a **https://gumroad.com**
2. Haz clic en "Sign up" (Registrarse)
3. Usa tu email: **jaguilar0925@gmail.com**
4. Elige contraseña segura
5. Completa tu perfil:
   - Nombre: "Quantic IA Magazine"
   - URL de tu tienda: `gumroad.com/quanticiamagazine` (o similar)
   - Foto de perfil: Logo de Quantic IA
   - Biografía: "Revista digital de tecnología. Ebooks, cursos y datasets exclusivos."
   - Link a sitio web: https://quanticiamagazine.com (o tu GitHub Pages)

---

## Paso 2: Configurar Método de Pago

**Importante:** Necesitas una cuenta bancaria para recibir pagos.

1. Ve a **Settings > Payouts**
2. Elige tu método:
   - **Stripe** (recomendado): Depósitos automáticos cada 7 días
   - **PayPal**: Más lento pero acepta más países
   - **Direct Bank Transfer**: Transferencias directas
3. Proporciona:
   - Información bancaria completa
   - Tax ID (si aplica en tu país)
   - Dirección

**Nota sobre comisiones:**
- Gumroad toma 10% de cada venta
- Tú recibes 90% del precio que fijas
- Ejemplo: Si vendes un ebook a $9.99, recibes $8.99

---

## Paso 3: Crear 4 Productos Iniciales

### PRODUCTO 1: Ebook - IA Transparente en Periodismo

**Tipo:** Ebook (PDF)

**Configuración básica:**
- Nombre: "IA Transparente en Periodismo Tech"
- Precio: $9.99
- Descripción:
  ```
  Cómo usamos Inteligencia Artificial manteniendo 
  integridad editorial y transparencia completa.
  
  En este ebook descubrirás:
  ✓ Metodología de investigación hybrid AI-Human
  ✓ Herramientas y prompts que utilizamos
  ✓ Checklist editorial para verificar calidad
  ✓ Casos de uso reales de nuestra revista
  ✓ Mejores prácticas para periodismo con IA
  
  30 páginas. PDF descargable inmediatamente.
  ```

**Creación del archivo:**
1. Convierte `revisTech/AI_TRANSPARENCY.md` a PDF
   - Usa Google Docs o Markdown to PDF tool
   - Formatea con logo de Quantic IA
   - Añade tabla de contenido

**Carga en Gumroad:**
1. Ve a **Create New Product > Digital Product**
2. Sube el PDF
3. Precio: $9.99
4. Haz público

---

### PRODUCTO 2: Masterclass - Construyendo Agentes IA

**Tipo:** Guía + Video (opcional)

**Configuración:**
- Nombre: "Construyendo Agentes de IA en Producción"
- Precio: $49.99
- Descripción:
  ```
  Aprende a crear agentes de IA que realmente funcionan 
  en aplicaciones de producción.
  
  Contenido:
  ✓ Arquitectura de agentes: patterns probados
  ✓ Prompt engineering para instrucciones claras
  ✓ Orquestación de herramientas/tools
  ✓ Manejo de errores y edge cases
  ✓ Evaluación y testing de agentes
  ✓ 3 proyectos paso-a-paso
  ✓ Códigos de ejemplo en Python
  
  Bonus: Acceso a Discord privado + email support
  Duración: ~5 horas de contenido
  ```

**Creación:**
1. Usa contenido de `revisTech/AGENT_ARCHITECTURE.md`
2. Expande con ejemplos de código
3. Crea guía en formato PDF (~50 páginas)
4. (Opcional) Graba videos de demostración (10-15 minutos)
5. Sube todo a Gumroad

---

### PRODUCTO 3: Curso - Arquitectura en la Nube

**Tipo:** Guía completa + plantillas

**Configuración:**
- Nombre: "Cloud Architecture Deep Dive"
- Precio: $99.99
- Descripción:
  ```
  Domina patrones de arquitectura moderna en la nube.
  Diseñado para developers y architects.
  
  Módulos:
  ✓ Fundamentos: Monolith vs Microservicios
  ✓ Patrones: Event-driven, CQRS, Saga
  ✓ Caso de uso 1: E-commerce escalable
  ✓ Caso de uso 2: Real-time analytics
  ✓ Caso de uso 3: Global distribution
  ✓ DevOps + Infrastructure as Code
  ✓ Seguridad y compliance
  ✓ Cost optimization
  
  Incluye: 100+ diagramas, checklist de diseño, 
  templates de Terraform, 20+ referencias.
  ```

**Creación:**
1. Redacta guía de arquitectura (~80 páginas)
2. Incluye diagramas (usa draw.io o Excalidraw)
3. Proporciona templates de código/infraestructura
4. Sube como PDF + archivos ZIP

---

### PRODUCTO 4: Dataset - Tendencias Tecnológicas Mensual

**Tipo:** Dataset (CSV/JSON)

**Configuración:**
- Nombre: "Tech Trends Dataset - Actualizado Mensualmente"
- Precio: $19.99 (o $19.99/mes si haces suscripción)
- Descripción:
  ```
  Dataset mensual de tendencias tecnológicas reales.
  Datos estructurados listos para análisis.
  
  Incluye:
  ✓ 50-100 tendencias por mes
  ✓ Categorías: AI, Cloud, Security, DevOps, Frontend
  ✓ Formato: CSV + JSON
  ✓ Campos: nombre, descripción, links, fecha, impacto
  ✓ Análisis de velocidad: crecimiento de tendencia
  ✓ Fuentes verificadas
  
  Perfecto para:
  - Investigadores de tech trends
  - Data journalists
  - Tech recruiters
  - Product managers
  
  Nuevos datos cada mes.
  ```

**Creación:**
1. Extrae datos de ediciones mensuales
2. Normaliza en CSV (nombre, descripción, enlaces, fecha, categoría)
3. Proporciona ambos formatos: CSV + JSON
4. Sube como archivo ZIP mensual

---

## Paso 4: Configurar Información de Productos en Gumroad

Para cada producto que crees, Gumroad te asigna una URL:

```
https://gumroad.com/l/[PRODUCTO_ID]
```

**Dónde encontrar la URL:**
1. Ve a Dashboard > Products
2. Selecciona cada producto
3. Copia el "share link" (URL corta)

**Ejemplo de URLs que obtendrás:**
```
Ebook: https://gumroad.com/l/ai-journalism
Masterclass: https://gumroad.com/l/ai-agents
Curso: https://gumroad.com/l/cloud-arch
Dataset: https://gumroad.com/l/tech-trends
```

**Actualiza estas en:**
- `docs/subscribe.html` - en los botones de productos
- Emails de promoción
- Social media

---

## Paso 5: Configurar Descuentos y Promociones

Gumroad permite crear cupones de descuento:

1. Ve a **Product > Pricing**
2. Haz clic en "Licensing" o "Discounts"
3. Crea cupones:
   - Para Patreon Supporters: 10% de descuento
   - Para Patreon Professional: 20% de descuento
   - Para Enterprise: 50% de descuento
4. Distribuye códigos a tus patrocinadores

**Ejemplo:**
```
Coupon: SUPPORTER10 → 10% off
Coupon: PROFESSIONAL20 → 20% off
Coupon: ENTERPRISE50 → 50% off
```

---

## Paso 6: Habilitar Membresías/Suscripción (Opcional)

Si quieres que el dataset se actualice mensualmente:

1. Ve a **Product Settings**
2. Habilita "Membership" o "Recurring"
3. Precio: $19.99/mes (renovación automática)
4. Los clientes reciben actualizaciones automáticas

**Alternativa:** Vender cada mes como producto separado:
```
Tech Trends Dataset - Julio 2026: $19.99
Tech Trends Dataset - Agosto 2026: $19.99
...
```

---

## Paso 7: Email y Autorespuesta

Gumroad puede enviarte emails cuando alguien compra:

1. Ve a **Settings > Notifications**
2. Elige recibir notificaciones por compra
3. (Opcional) Configura mensaje automático de agradecimiento
   - Email que se envía automáticamente al comprador
   - Ejemplo: "Gracias por comprar. Aquí están tus archivos..."

---

## Paso 8: Integración con tu Sitio Web

**Opción A: Solo Links (Lo que usa subscribe.html)**

En `docs/subscribe.html` tenemos botones que enlazan a Gumroad.
Actualiza con las URLs reales de tus productos:

```html
<!-- Actualiza estos href con tus URLs reales -->
<a href="https://gumroad.com/l/[TU_PRODUCTO_ID]">Comprar</a>
```

**Opción B: Embed Products en tu Sitio**

Si quieres mostrar productos directamente en tu sitio:

1. Ve a cada producto en Gumroad
2. Haz clic en "Embed"
3. Copia el código HTML
4. Pégalo en `docs/subscribe.html`

(No es necesario para MVP)

---

## Paso 9: Analytics y Crecimiento

**Dashboard importante:** Gumroad Home page

Monitorea:
- Ventas totales por producto
- Ingresos acumulados
- Tasa de conversión
- Clientes nuevos/repeat

**Meta sugerida:**
- Mes 1: 1-2 ventas
- Mes 2: 5-10 ventas
- Mes 3: 20-30 ventas
- Mes 6: 50+ ventas/mes = $1,000+/mes

---

## Paso 10: Promover en Redes Sociales

Después de crear tus productos, promociónelos:

**Twitter/X:**
```
Nuevo: Mi ebook "IA Transparente en Periodismo Tech"
Aprende cómo usamos IA manteniendo integridad editorial.
30 páginas de metodología, herramientas y mejores prácticas.
Ahora en Gumroad: [link]
```

**LinkedIn:**
```
Acabo de publicar un masterclass sobre construir 
agentes de IA en producción.

5 horas de contenido + proyectos paso-a-paso + soporte.
Ideal para developers y architects.

Disponible: [link]
```

**Email Newsletter:**
```
Nuevo producto:
📚 Ebook: IA Transparente en Periodismo Tech - $9.99
💻 Masterclass: Agentes IA - $49.99
🏢 Curso: Cloud Architecture - $99.99
📊 Dataset: Tech Trends - $19.99/mes

Todos en Gumroad →
```

---

## Troubleshooting

### Problema: Gumroad toma mucha comisión

**Solución:**
- Gumroad toma 10% + payment processor (3.5%)
- Total típico: ~13-14% de comisión
- Alternativas si quieres menos comisión: Podia (8%), SendOwl (10%)
- Para MVP, 10% es razonable

### Problema: No sé qué precio poner

**Sugerencia:**
- Ebooks: $9.99-19.99 (accesibles)
- Masterclass: $39.99-$99.99 (contenido valioso)
- Cursos: $99.99-$299.99 (certificado educativo)
- Datos: $19.99+ (depende de uniqueness)

### Problema: Necesito cambiar precio

**Solución:**
- Gumroad permite cambiar precios en cualquier momento
- Los clientes anteriores mantienen su acceso
- Anúncialo en emails para que sepan cambios

### Problema: Quiero hacer producto gratis

**Solución:**
- Establece precio a $0
- Útil para: lead magnets, samples gratis
- Ejemplo: "Primeros 2 capítulos de curso" gratis

---

## Checklist de Configuración

- [ ] Cuenta creada en Gumroad
- [ ] Perfil completado
- [ ] Método de pago configurado
- [ ] Información bancaria verificada

**Productos:**
- [ ] Ebook: IA Transparente ($9.99)
- [ ] Masterclass: Agentes IA ($49.99)
- [ ] Curso: Cloud Architecture ($99.99)
- [ ] Dataset: Tech Trends ($19.99)

**Integración:**
- [ ] URLs copiadas de cada producto
- [ ] `docs/subscribe.html` actualizado con URLs reales
- [ ] Descuentos configurados (opcional)
- [ ] Notificaciones por email activadas

**Promoción:**
- [ ] Twitter/X posts programados
- [ ] LinkedIn actualizado
- [ ] Email newsletter listos
- [ ] Links compartidos en redes

---

## Próximos Pasos

1. **Semana 1:** Configura Gumroad según esta guía
2. **Semana 2:** Crea/sube los 4 productos iniciales
3. **Semana 3:** Promociona en redes (Twitter, LinkedIn, email)
4. **Mes 2+:** Agrega nuevos productos basado en feedback

---

**¿Preguntas?** Escribe a jaguilar0925@gmail.com

Soporte Gumroad: https://gumroad.com/help
Documentación: https://gumroad.com/blog
