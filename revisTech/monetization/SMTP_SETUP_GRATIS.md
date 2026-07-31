# 📧 Setup SMTP (GRATIS - Sin Google Cloud)

Script Python que envía emails usando Gmail SMTP. **Completamente gratis. Sin costos.**

---

## 🚀 Setup (2 minutos)

### Paso 1: Activar 2FA en Gmail (1 min)

1. Abre: https://myaccount.google.com/
2. Click en **"Seguridad"** (lado izquierdo)
3. Busca: **"Verificación en dos pasos"**
4. Si no está activada: Click en **"Activar"** y sigue pasos

---

### Paso 2: Generar Contraseña de App (1 min)

1. En https://myaccount.google.com/
2. Click en **"Seguridad"**
3. Desplázate hasta **"Contraseñas de app"** (aparece si 2FA está activado)
4. Selecciona:
   - Device: **"Windows Computer"** (o tu sistema)
   - App: **"Mail"**
5. Click **"Generate"**
6. **Copia la contraseña** que aparece (16 caracteres)

**Ejemplo:**
```
abcd efgh ijkl mnop
```

---

### Paso 3: Instalar Python (si no lo tienes)

```bash
python3 --version
```

Si no aparece, descargar de: https://www.python.org/

---

### Paso 4: Ejecutar Script

```bash
cd /home/user/refilco/revisTech/monetization
python3 send_emails_smtp.py
```

**Cuando pida:**
```
Ingresa tu contraseña de app de Gmail: [PEGA LA CONTRASEÑA AQUI]
```

Pega la contraseña de 16 caracteres (sin espacios).

---

## ✅ Qué pasa después

1. Se conecta a Gmail SMTP
2. Envía los 20 emails (uno por uno)
3. Guarda tracking en `tracking_week1.txt`
4. Muestra progreso:

```
🚀 RevisTech Week 1 Email Campaign (SMTP - FREE)

✅ Gmail SMTP authenticated (FREE)

✅ Parsed 20 emails from EMAILS_TO_SEND_WEEK1.md

📧 Enviando 20 emails...

[1/20] AWS...
   ✓ Sent | AWS → devrel@aws.amazon.com
[2/20] Google Cloud...
   ✓ Sent | Google Cloud → partnerships@google.com
[... continúa ...]

✅ ¡Campaña completada!
```

---

## 💰 Costo

**$0**

- No requiere Google Cloud
- No requiere tarjeta de crédito
- Gmail SMTP es gratis
- Contraseña de app es gratis

---

## 🔒 Seguridad

- Contraseña de app es segura (específica solo para apps)
- NO es tu contraseña de Gmail real
- Puedes revocar en cualquier momento

---

## ⚠️ Troubleshooting

### Error: "Authentication failed"
```
Soluciones:
1. Verifica que 2FA está activado en Gmail
2. Verifica que generaste contraseña de app
3. Verifica que copiaste bien (16 caracteres)
4. Espera 1-2 min después de generar
```

### Error: "Module not found"
```
Instala Python:
pip install --upgrade pip
```

### Los emails no se envían
```
1. Verifica dirección email correcta en EMAILS_TO_SEND_WEEK1.md
2. Verifica conexión a internet
3. Verifica que no pusiste contraseña incorrecta
```

---

## 🎯 El Lunes 4 de Agosto

```bash
cd /home/user/refilco/revisTech/monetization
python3 send_emails_smtp.py
```

Ingresar contraseña de app → Los 20 emails se envían en 2 minutos → ✅

---

## 📊 Plan de Gastos (Tu presupuesto $50)

Ver: BUDGET_PLAN.md

---

**¡Listo! Economizamos mucho dinero. 🚀**

_Última actualización: Julio 2026_
