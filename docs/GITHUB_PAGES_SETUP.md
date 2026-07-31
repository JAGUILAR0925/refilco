# 🚀 GitHub Pages Setup - Quantic IA Magazine

Tu landing page profesional está lista. Ahora actívala en GitHub Pages.

---

## ✅ PASO 1: Activar GitHub Pages (2 minutos)

### En GitHub.com:

1. Ve a: **https://github.com/jaguilar0925/refilco**
2. Click en: **Settings** (arriba a la derecha)
3. En el menú izquierdo: Click en **Pages**
4. En "Build and deployment":
   - **Source**: Selecciona `Deploy from a branch`
   - **Branch**: Selecciona `main` (rama principal)
   - **Folder**: Selecciona `/ (root)` o `/docs` según veas
   - Click: **Save**

**Resultado**: GitHub comienza a desplegar tu sitio

---

## ✅ PASO 2: Esperar Activación (3-5 minutos)

GitHub genera tu sitio automáticamente.

Verás un mensaje verde: "Your site is live at: `https://jaguilar0925.github.io/refilco/`"

**Tu sitio está en línea** ✅

---

## ✅ PASO 3: Conectar Dominio Personalizado (Opcional - Semana 2)

Cuando compres el dominio en Namecheap:

### En Namecheap:

1. Ve a tu dominio: **quanticiamagazine.com**
2. Click en: **Manage DNS**
3. Busca: **CNAME Records**
4. Agrega o actualiza:
   ```
   Host: www
   Value: jaguilar0925.github.io
   TTL: 30 min (o default)
   ```
5. Guarda: **Save Changes**

### En GitHub:

1. Ve a **Settings → Pages**
2. En "Custom domain": Escribe `quanticiamagazine.com`
3. Click: **Save**
4. **IMPORTANTE**: Marca la casilla "Enforce HTTPS" (seguridad)

**Espera 24h para propagación DNS**

---

## 📊 URLs Resultantes

### Opción 1: GitHub Gratis (Ahora)
```
https://jaguilar0925.github.io/refilco/
```

### Opción 2: Dominio .COM (Semana 2+)
```
https://quanticiamagazine.com
```

---

## 🔍 Verificar Que Funciona

### Prueba Ahora:
```
https://jaguilar0925.github.io/refilco/
```

Deberías ver:
- ✅ Logo de Quantic IA Magazine
- ✅ Tagline: "Contenido Técnico Profundo"
- ✅ Botón: "Ser Sponsor"
- ✅ 6 secciones de la revista
- ✅ Precios de sponsorship
- ✅ Contacto

Si aparece algo diferente → Espera 5 minutos y recarga

---

## 🛠️ Estructura de Archivos

```
refilco/
├── docs/                    ← Tu sitio web
│   ├── index.html          ← Landing page (lo que ves)
│   └── CNAME               ← Archivo para dominio personalizado
├── revisTech/              ← Tu revista
│   ├── branding/           ← Logo y marca
│   ├── monetization/       ← Estrategia de sponsors
│   └── ...
└── .git/                   ← Control de versión
```

---

## 📝 Próximos Pasos

### Esta Semana
- [x] Crear landing page
- [ ] Activar GitHub Pages (2 min)
- [ ] Verificar en navegador
- [ ] Compartir URL con 20 sponsors potenciales

### Semana 2
- [ ] Si hay respuestas de sponsors
- [ ] Comprar dominio .com en Namecheap ($8.88)
- [ ] Conectar dominio personalizado
- [ ] Publicar primeros artículos

### Mes 2+
- [ ] Expandir contenido
- [ ] Agregar newsletter
- [ ] Integrar Patreon
- [ ] Lanzar productos Gumroad

---

## 🆘 Troubleshooting

### Problema: "No aparece contenido en GitHub Pages"
**Solución**:
1. Espera 5 minutos (GitHub necesita procesar)
2. Limpia caché del navegador: Ctrl+Shift+Del
3. Recarga: Ctrl+R
4. Si sigue sin funcionar: Ve a Settings > Pages y verifica "Build and deployment"

### Problema: "URL incorrecta"
**Solución**: Si ves error 404
1. Verifica la URL: `https://jaguilar0925.github.io/refilco/`
2. Asegúrate de incluir `/refilco/` al final
3. O usa el dominio .com cuando lo conectes

### Problema: "CNAME no funciona"
**Solución**:
1. Espera 24h para propagación DNS
2. Verifica DNS en Namecheap está correcto
3. Intenta `nslookup quanticiamagazine.com` en terminal

---

## 🎯 Resultado Final

Cuando termines:
- ✅ Sitio en línea: `https://jaguilar0925.github.io/refilco/`
- ✅ Landing page profesional
- ✅ Botón para contactar sponsors
- ✅ Información de la revista visible
- ✅ Precios claros
- ✅ Listo para mostrar a inversores

**Costo**: $0 (GitHub Pages es gratis)
**Tiempo**: 5 minutos
**Resultado**: Sitio profesional publicado ✅

---

## 📞 Contacto

¿Necesitas ayuda?
- Email: jaguilar0925@gmail.com
- Chat: [Contáctame en GitHub](https://github.com/jaguilar0925)

---

**¡Tu revista está en línea!** 🚀
