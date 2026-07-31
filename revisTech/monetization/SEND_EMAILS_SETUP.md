# 📧 Setup: Enviar Emails Automáticamente

Script Python que envía los 20 emails de sponsor automáticamente usando Gmail API.

---

## 🚀 Quick Start (5 minutos)

### 1. Instalar dependencias

```bash
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 2. Obtener credenciales de Google

**Paso A: Crear proyecto en Google Cloud Console**

1. Ir a https://console.cloud.google.com/
2. Crear nuevo proyecto: "RevisTech"
3. Esperar creación (1-2 min)

**Paso B: Activar Gmail API**

1. En Google Cloud Console, buscar "Gmail API"
2. Click en "Gmail API"
3. Click en "ENABLE"
4. Esperar unos segundos

**Paso C: Crear OAuth2 Credentials**

1. Click en "Create Credentials" (azul)
2. Seleccionar:
   - Application type: "Desktop application"
   - User data (no service account)
3. Click "Create"
4. Descargar JSON
5. Renombrar a `credentials.json`
6. Copiar a: `/revisTech/monetization/credentials.json`

### 3. Ejecutar script

```bash
cd revisTech/monetization
python3 send_emails.py
```

**Primera vez:**
- Se abrirá navegador
- Click "Allow" para darle permisos a RevisTech
- Se guardará `token.pickle` (no compartir)

---

## 📋 Verificación Pre-Envío

Antes de ejecutar, verifica:

- [ ] `credentials.json` en `revisTech/monetization/`
- [ ] `EMAILS_TO_SEND_WEEK1.md` actualizado con tu info
- [ ] Internet conexión activa
- [ ] Gmail account con espacio

---

## 🎯 Qué hace el script

1. ✅ Lee 20 emails de EMAILS_TO_SEND_WEEK1.md
2. ✅ Envía cada email automáticamente
3. ✅ Registra en `tracking_week1.txt`
4. ✅ Muestra progreso en pantalla

---

## 📊 Output esperado

```
🚀 RevisTech Week 1 Email Campaign

✅ Gmail API authenticated

✅ Parsed 20 emails from EMAILS_TO_SEND_WEEK1.md

📧 Sending 20 emails...

[1/20] AWS...
✓ Sent | AWS → devrel@aws.amazon.com (2026-08-04 09:05:23)

[2/20] Google Cloud...
✓ Sent | Google Cloud → partnerships@google.com (2026-08-04 09:06:15)

[... continúa para los 20 ...]

✅ Campaign complete! Check tracking_week1.txt
```

---

## ⚠️ Troubleshooting

### Error: "credentials.json not found"
```
Solución: Descarga credentials.json de Google Cloud Console
y cópialo a revisTech/monetization/
```

### Error: "Gmail API not enabled"
```
Solución: Ve a Google Cloud Console
1. Busca "Gmail API"
2. Click "Enable"
3. Espera 1-2 minutos
```

### Error: "Permission denied"
```
Solución: En Google Cloud, asegúrate que:
1. Project seleccionado: "RevisTech"
2. Gmail API está ENABLED
3. Credentials son OAuth2 (no Service Account)
```

### Script envió pero no recibes respuestas
```
Normal - Los emails pueden tardar en llegar a la bandeja de entrada
Verifica:
1. Folder "Enviados" en tu Gmail
2. Spam folder en tu cuenta
3. Datos de contacto correctos en tracking_week1.txt
```

---

## 🔒 Seguridad

- `credentials.json` = publica (se regenera cada vez)
- `token.pickle` = PRIVADA (nunca compartir)
- NO compartir estos archivos en GitHub

---

## 🎯 Próximos Pasos

### Lunes 4 de Agosto

```bash
cd revisTech/monetization
python3 send_emails.py
```

Espera: Enviará los 20 emails en ~2 minutos

---

## 📞 Soporte

Si algo no funciona:
1. Verifica Python 3.8+ instalado: `python3 --version`
2. Verifica conexión a internet
3. Verifica credenciales.json en lugar correcto
4. Reinicia terminal y prueba de nuevo

---

**¡Listo para campaña!** 🚀

_Última actualización: Julio 2026_
