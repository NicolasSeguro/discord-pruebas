# 🚀 Guía de Instalación Rápida - Bot Creativo de Discord

Esta guía te ayudará a configurar y ejecutar el bot de Discord creativo en menos de 10 minutos.

## 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener:

- **Python 3.11 o superior** instalado
- **Git** para clonar el repositorio
- Una **cuenta de Discord** con permisos de administrador en un servidor
- (Opcional) Cuenta de **Unsplash** para imágenes de alta calidad
- (Opcional) Cuenta de **OpenAI** para contenido más variado

## ⚡ Instalación en 5 Pasos

### Paso 1: Descargar el Código

```bash
# Clonar el repositorio
git clone <repository-url>
cd discord-creative-bot

# O descargar y extraer el ZIP
```

### Paso 2: Configurar Entorno Python

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\\Scripts\\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 3: Crear Bot de Discord

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Haz clic en "New Application"
3. Dale un nombre a tu aplicación
4. Ve a la sección "Bot" en el menú lateral
5. Haz clic en "Add Bot"
6. Copia el **Token** (lo necesitarás en el siguiente paso)

### Paso 4: Configurar Variables de Entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar el archivo .env con tu editor favorito
nano .env
```

**Configuración mínima requerida:**
```env
DISCORD_BOT_TOKEN=tu_token_de_discord_aqui
```

**Configuración completa (recomendada):**
```env
DISCORD_BOT_TOKEN=tu_token_de_discord_aqui
UNSPLASH_ACCESS_KEY=tu_access_key_de_unsplash
DISCORD_CHANNEL_ID=id_del_canal_donde_publicar
PUBLISH_HOUR=09
PUBLISH_MINUTE=00
```

### Paso 5: Ejecutar el Bot

```bash
# Ejecutar el bot
python src/main.py
```

¡Listo! Tu bot debería estar funcionando.

## 🔗 Invitar Bot al Servidor

1. En Discord Developer Portal, ve a "OAuth2" > "URL Generator"
2. Selecciona los scopes: `bot`
3. Selecciona los permisos: `Send Messages`, `Embed Links`, `Attach Files`
4. Copia la URL generada y ábrela en tu navegador
5. Selecciona tu servidor y autoriza el bot

## 🧪 Probar el Bot

### Opción 1: Interfaz Web
1. Abre tu navegador en `http://localhost:5000`
2. Haz clic en "Generar Inspiración Completa"
3. Verifica que todo funciona correctamente

### Opción 2: Comandos de Discord
En tu servidor de Discord, escribe:
```
!inspiracion
```

### Opción 3: Script de Pruebas
```bash
python test_bot.py
```

## 🔧 Configuración Avanzada

### Obtener API Key de Unsplash (Opcional)

1. Ve a [Unsplash Developers](https://unsplash.com/developers)
2. Crea una cuenta o inicia sesión
3. Crea una nueva aplicación
4. Copia el "Access Key"
5. Agrégalo a tu archivo `.env`

### Configurar Canal Específico

1. En Discord, haz clic derecho en el canal deseado
2. Selecciona "Copy ID" (necesitas modo desarrollador activado)
3. Agrega el ID a `DISCORD_CHANNEL_ID` en tu `.env`

### Personalizar Horario de Publicación

Modifica estas variables en `.env`:
```env
PUBLISH_HOUR=14    # 2 PM
PUBLISH_MINUTE=30  # 30 minutos
```

## 🚨 Solución de Problemas Comunes

### Error: "discord.LoginFailure"
- Verifica que el token de Discord sea correcto
- Asegúrate de que no haya espacios extra en el token

### Error: "ModuleNotFoundError"
- Verifica que el entorno virtual esté activado
- Ejecuta `pip install -r requirements.txt` nuevamente

### Bot no responde a comandos
- Verifica que el bot tenga permisos en el canal
- Asegúrate de que el bot esté online en Discord

### No se generan imágenes
- El bot usa Lorem Picsum como fallback automáticamente
- Para mejores imágenes, configura `UNSPLASH_ACCESS_KEY`

## 📱 Comandos Disponibles

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `!inspiracion` | Contenido completo | `!inspiracion` |
| `!foto` | Foto aleatoria | `!foto nature` |
| `!herramienta` | Herramienta útil | `!herramienta` |
| `!recurso` | Recurso útil | `!recurso` |
| `!idea` | Idea creativa | `!idea` |
| `!prompt` | Prompt para IA | `!prompt` |
| `!ayuda` | Lista de comandos | `!ayuda` |

## 🎯 Próximos Pasos

1. **Personaliza el contenido** editando `src/external_apis.py`
2. **Agrega más comandos** en `src/discord_bot.py`
3. **Configura publicaciones automáticas** con las variables de entorno
4. **Invita el bot a más servidores** para mayor alcance

## 📞 Soporte

Si tienes problemas:

1. Revisa esta guía nuevamente
2. Ejecuta `python test_bot.py` para diagnosticar
3. Verifica los logs en la consola
4. Consulta el README.md para información detallada

---

**¡Disfruta tu nuevo bot creativo de Discord! 🎉**

