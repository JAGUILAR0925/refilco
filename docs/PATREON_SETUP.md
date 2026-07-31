# Guía de Configuración: Patreon para Quantic IA Magazine

## Paso 1: Crear Cuenta de Patreon

1. Ve a **https://patreon.com**
2. Haz clic en "Sign Up" (Registrarse)
3. Elige "I'm a creator" (Soy un creador)
4. Usa tu email: **jaguilar0925@gmail.com**
5. Elige un nombre de usuario (recomendación: `revisTech` o `quanticiamagazine`)
6. Completa el perfil con:
   - Foto de perfil (usa el logo de Quantic IA)
   - Descripción: "Revista digital de tecnología independiente. Impulsada por IA, supervisada por humanos."
   - Sitio web: https://quanticiamagazine.com (o tu URL de GitHub Pages)

---

## Paso 2: Configurar los 3 Planes de Suscripción

Patreon te permite crear múltiples "membership tiers". Crea estos tres:

### Tier 1: Supporter ($5/mes)

**Configuración:**
- Nombre: "Supporter"
- Precio: $5 USD/mes
- Descripción: "Acceso a todas las ediciones y archivos completos"

**Beneficios a incluir:**
- Ediciones PDF descargables
- Archivo completo de ediciones pasadas
- Newsletter mensual
- Acceso a la comunidad privada
- Mención en la página de patrocinadores

**Nota:** En Patreon, puedes crear "posts" exclusivos (solo para patrocinadores) donde subes los PDFs de las ediciones.

---

### Tier 2: Professional ($15/mes) ⭐ RECOMENDADO

**Configuración:**
- Nombre: "Professional"
- Precio: $15 USD/mes
- Descripción: "Acceso premium con contenido exclusivo y apoyo directo"

**Beneficios a incluir:**
- Todos los beneficios de Supporter
- Acceso anticipado a ediciones (5 días antes)
- Newsletter semanal exclusivo
- Acceso a borradores sin publicar
- Descuentos 20% en productos Gumroad
- Soporte prioritario por email

---

### Tier 3: Enterprise ($50/mes)

**Configuración:**
- Nombre: "Enterprise"
- Precio: $50 USD/mes
- Descripción: "Acceso VIP con consultoría personalizada"

**Beneficios a incluir:**
- Todos los beneficios de Professional
- Llamada de 30 minutos mensual con el editor
- Reportes personalizados sobre tendencias
- Mención especial en edición mensual
- Descuento 50% en consultorías
- Acceso a grupo privado de Discord

---

## Paso 3: Configurar la URL de Patreon

Después de crear tu perfil, Patreon te asigna una URL automáticamente:

```
https://patreon.com/[TU_NOMBRE_DE_USUARIO]
```

Guarda esta URL. La necesitarás para:
1. Actualizar botones en `docs/subscribe.html`
2. Compartir en emails
3. Poner en biografía de redes sociales

**Dónde actualizar la URL:**
- En `docs/subscribe.html`, los botones de "Unirme a Patreon" tienen placeholders que apuntan a `https://patreon.com/revisTech`
- Cambia esto por tu URL real

---

## Paso 4: Activar Patreon Widget (Opcional)

Patreon te ofrece un "embed code" para mostrar información de patrones en tu sitio.

### Opción A: Widget Mínimo (Recomendado para MVP)
Solo mantén los botones/links a Patreon en `subscribe.html`. Sin necesidad de código adicional.

### Opción B: Embed Completo
Si quieres mostrar información de patrones en tu sitio:

1. Ve a tu panel de Patreon > Settings > Integrations
2. Encuentra "Embed & Website Tools"
3. Copia el código HTML que te proporciona
4. Pégalo en `docs/subscribe.html` si lo deseas

---

## Paso 5: Configurar Impuestos y Pagos

**Importante para recibir dinero:**

1. Ve a **Settings > Payout Method**
2. Elige tu método de pago:
   - **Stripe** (recomendado): depósitos directos a tu cuenta bancaria
   - **Payoneer**: transferencias internacionales
   - **PayPal**: alternativa fácil
3. Completa la información bancaria
4. Configura tu impuesto (tax ID si es requerido en tu país)

---

## Paso 6: Primeras Publicaciones (Posts)

Para que tus patrocinadores accedan al contenido:

1. Ve a **Creator Studio > Posts**
2. Crea un post nuevo
3. Añade título: "Edición Julio 2026"
4. Carga el PDF de la edición
5. Establece la visibilidad: "Patrons only" (solo patrocinadores)
6. Elige nivel mínimo: Para Tier 1 Supporter
7. Publica

**Sugerencia:** Crea una publicación por edición mensual.

---

## Paso 7: Promoción y Compartir

Después de configurar, comparte tu Patreon:

**En emails:**
```
Apoya Quantic IA Magazine en Patreon:
https://patreon.com/[TU_URL]

Elige el plan que mejor se adapte a ti:
- Supporter ($5/mes): Acceso a todas las ediciones
- Professional ($15/mes): Contenido exclusivo + newsletter semanal
- Enterprise ($50/mes): Consultoría personalizada + llamadas mensuales
```

**En redes sociales:**
- Bio de Twitter: Incluye link a Patreon
- Bio de LinkedIn: Menciona "Patrons welcome at..."
- Publicaciones: "Apoya nuestra investigación independiente"

**En encabezado de emails:**
```
¿Te gusta el contenido? Apoya la revista en Patreon →
```

---

## Paso 8: Comisión de Patreon

Patreon toma un porcentaje de cada suscripción:

- **Por defecto**: 5% de comisión
- **Rango**: 5% a 12% (tú controlas)
- **Ejemplo**: Si alguien se suscribe a $15/mes con comisión 5%, recibes $14.25

En tu panel de control puedes ver:
- Ingresos totales
- Comisión de Patreon
- Monto que recibirás

---

## Paso 9: Estadísticas y Crecimiento

**Dashboard importante:** Creator Studio > Insights

Monitorea:
- Nuevos patrocinadores por mes
- Tasa de cancelación
- Ingresos proyectados
- Engagement en posts

**Meta sugerida:**
- Mes 1: 5-10 supporters
- Mes 2: 15-20 supporters
- Mes 3: 30-50 supporters
- Mes 6: 300+ supporters = $1,500+/mes

---

## Troubleshooting

### Problema: Los pagos se tardan

**Solución:**
- Patreon procesa pagos mensualmente (típicamente día 1-5 del mes siguiente)
- Los depósitos tardan 2-5 días más en tu banco
- Verifica que tu información bancaria sea correcta en Settings

### Problema: Necesito cambiar el precio

**Solución:**
- Ve a Settings > Membership Tiers
- Puedes cambiar precios futuros (patrones actuales mantienen precio antiguo)
- Anúncialo en un post para que nuevos patrocinadores sepan el cambio

### Problema: Un patrón se queja del pago

**Solución:**
- Ve a Creator Studio > Messages
- Comunícate directamente con el patrón
- Patreon tiene política de devolución (30 días)

---

## Checklist de Configuración

- [ ] Cuenta creada en Patreon
- [ ] Perfil completado (foto, descripción, sitio web)
- [ ] 3 membership tiers configurados
- [ ] Precios correctos ($5, $15, $50)
- [ ] Beneficios descritos por tier
- [ ] Método de pago configurado (Stripe/Payoneer/PayPal)
- [ ] Información bancaria verificada
- [ ] Primer post/edición publicado
- [ ] URL de Patreon actualizada en `docs/subscribe.html`
- [ ] Link compartido en email de sponsors

---

## Próximos Pasos

1. **Semana 1-2:** Configura Patreon según esta guía
2. **Semana 3:** Comparte URL con tus primeros 20 sponsors
3. **Mes 2+:** Incrementa promoción a medida que crece tu audiencia
4. **Mes 6:** Evalúa si necesitas agregar nuevos tiers basado en feedback

---

**¿Preguntas?** Escribe a jaguilar0925@gmail.com

Soporte Patreon oficial: https://support.patreon.com
