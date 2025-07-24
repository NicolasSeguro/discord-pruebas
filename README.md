# 🤖 Bot Creativo de Discord

Un bot de Discord inteligente que publica automáticamente contenido diario inspirador para desarrolladores, combinando fuentes externas con generación creativa usando IA.

## ✨ Características

- **📸 Referencia Visual**: Imágenes inspiradoras diarias desde Unsplash
- **✍️ Ideas Creativas**: Generación de ideas innovadoras usando OpenAI
- **🧰 Tool of the Day**: Herramientas útiles para desarrolladores
- **🔗 Recursos Útiles**: Enlaces a recursos valiosos para programadores
- **🎲 Prompts para IA**: Prompts creativos para Midjourney, ChatGPT, DALL-E
- **🌐 Interfaz Web**: Panel web para probar funcionalidades
- **⏰ Publicación Automática**: Scheduler para contenido diario
- **🎨 Comandos Interactivos**: Comandos de Discord para uso manual

## 🚀 Instalación Rápida

### Prerrequisitos

- Python 3.11+
- Cuenta de Discord Developer
- (Opcional) API Key de Unsplash
- (Opcional) API Key de OpenAI

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <repository-url>
   cd discord-creative-bot
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\\Scripts\\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
   ```

5. **Ejecutar el bot**
   ```bash
   python src/main.py
   ```

## ⚙️ Configuración

### Variables de Entorno

Crea un archivo `.env` basado en `.env.example`:

```env
# Discord Bot Token (REQUERIDO)
DISCORD_BOT_TOKEN=tu_token_de_discord_aqui

# Unsplash API (OPCIONAL - usa Lorem Picsum como fallback)
UNSPLASH_ACCESS_KEY=tu_access_key_de_unsplash

# Canal de Discord (OPCIONAL)
DISCORD_CHANNEL_ID=id_del_canal_donde_publicar

# Horario de publicación
PUBLISH_HOUR=09
PUBLISH_MINUTE=00
```

### Crear Bot de Discord

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Crea una nueva aplicación
3. Ve a la sección "Bot"
4. Crea un bot y copia el token
5. Habilita los siguientes permisos:
   - Send Messages
   - Embed Links
   - Attach Files
   - Read Message History

### Invitar Bot al Servidor

Usa este enlace (reemplaza CLIENT_ID con tu ID de aplicación):
```
https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=52224&scope=bot
```

## 🎮 Comandos de Discord

| Comando | Descripción |
|---------|-------------|
| `!inspiracion` | Genera inspiración creativa completa |
| `!foto [búsqueda]` | Obtiene una foto inspiradora |
| `!herramienta` | Muestra una herramienta útil |
| `!recurso` | Muestra un recurso útil |
| `!idea` | Genera una idea creativa |
| `!prompt` | Genera un prompt para IA |
| `!config` | Configura canal (solo admin) |
| `!ayuda` | Muestra lista de comandos |

## 🌐 Interfaz Web

El bot incluye una interfaz web accesible en `http://localhost:5000` que permite:

- Ver el estado del bot
- Generar contenido manualmente
- Probar todas las funcionalidades
- Visualizar el contenido de forma atractiva

### API Endpoints

| Endpoint | Descripción |
|----------|-------------|
| `GET /api/bot/status` | Estado del bot |
| `GET /api/content/photo` | Foto aleatoria |
| `GET /api/content/tool` | Herramienta aleatoria |
| `GET /api/content/resource` | Recurso aleatorio |
| `GET /api/content/idea` | Idea creativa |
| `GET /api/content/prompt` | Prompt para IA |
| `GET /api/content/daily` | Contenido diario completo |

## 🔧 Arquitectura

### Estructura del Proyecto

```
discord-creative-bot/
├── src/
│   ├── main.py              # Punto de entrada principal
│   ├── discord_bot.py       # Lógica del bot de Discord
│   ├── external_apis.py     # Clientes para APIs externas
│   ├── models/              # Modelos de base de datos
│   ├── routes/              # Rutas de Flask
│   └── static/
│       └── index.html       # Interfaz web
├── requirements.txt         # Dependencias
├── .env.example            # Ejemplo de configuración
└── README.md               # Esta documentación
```

### Componentes Principales

#### 1. UnsplashAPI
- Obtiene imágenes inspiradoras
- Fallback a Lorem Picsum si no hay API key
- Soporte para búsquedas temáticas

#### 2. PublicAPIsClient
- Base de datos de herramientas útiles
- Recursos curados para desarrolladores
- Categorización por tipo

#### 3. ContentGenerator
- Integración con OpenAI para ideas creativas
- Generación de prompts para IA
- Sistema de fallback con contenido predefinido

#### 4. CreativeBot
- Bot principal de Discord
- Comandos interactivos
- Scheduler para publicaciones automáticas
- Manejo de errores robusto

## 🎨 Personalización

### Agregar Nuevas Herramientas

Edita `src/external_apis.py` en la clase `PublicAPIsClient`:

```python
tools = [
    {
        'name': 'Tu Herramienta',
        'description': 'Descripción de la herramienta',
        'url': 'https://ejemplo.com',
        'category': 'Categoría'
    },
    # ... más herramientas
]
```

### Personalizar Horario de Publicación

Modifica las variables de entorno:

```env
PUBLISH_HOUR=14  # 2 PM
PUBLISH_MINUTE=30  # 30 minutos
```

### Agregar Nuevos Comandos

En `src/discord_bot.py`:

```python
@commands.command(name='mi_comando')
async def mi_comando(self, ctx):
    """Descripción del comando."""
    # Tu lógica aquí
    await ctx.send("Respuesta del comando")
```

## 🚀 Despliegue

### Opción 1: Servidor Local

```bash
python src/main.py
```

### Opción 2: Docker (Próximamente)

```bash
docker build -t discord-creative-bot .
docker run -d --env-file .env -p 5000:5000 discord-creative-bot
```

### Opción 3: Servicios en la Nube

El bot es compatible con:
- Heroku
- Railway
- DigitalOcean App Platform
- AWS EC2
- Google Cloud Run

## 🔍 Solución de Problemas

### Bot No Se Conecta

1. Verifica que `DISCORD_BOT_TOKEN` esté configurado correctamente
2. Asegúrate de que el bot tenga permisos en el servidor
3. Revisa que el token no haya expirado

### No Se Generan Imágenes

1. Verifica la configuración de `UNSPLASH_ACCESS_KEY`
2. El bot usará Lorem Picsum como fallback automáticamente
3. Revisa los logs para errores de API

### Contenido Repetitivo

1. Configura `OPENAI_API_KEY` para contenido más variado
2. El bot tiene fallbacks predefinidos si OpenAI no está disponible
3. Reinicia el bot para refrescar el contenido

### Problemas de Permisos

1. Verifica que el bot tenga permisos de "Send Messages"
2. Asegúrate de que puede "Embed Links"
3. Revisa que tenga acceso al canal configurado

## 📊 Monitoreo

### Logs del Sistema

El bot registra automáticamente:
- Conexiones y desconexiones
- Errores de API
- Publicaciones exitosas
- Comandos ejecutados

### Métricas Disponibles

- Estado del bot (online/offline)
- Número de servidores conectados
- Frecuencia de comandos
- Errores de API

## 🤝 Contribución

### Reportar Bugs

1. Usa el sistema de issues de GitHub
2. Incluye logs relevantes
3. Describe pasos para reproducir

### Solicitar Características

1. Abre un issue con la etiqueta "enhancement"
2. Describe el caso de uso
3. Proporciona ejemplos si es posible

### Desarrollo

1. Fork el repositorio
2. Crea una rama para tu característica
3. Escribe tests si es aplicable
4. Envía un pull request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🙏 Agradecimientos

- [Discord.py](https://discordpy.readthedocs.io/) - Librería para bots de Discord
- [Unsplash](https://unsplash.com/) - Fotografías de alta calidad
- [OpenAI](https://openai.com/) - Generación de contenido con IA
- [Lorem Picsum](https://picsum.photos/) - Imágenes placeholder
- [Public APIs](https://github.com/public-apis/public-apis) - Lista de APIs públicas

## 📞 Soporte

- **Documentación**: Este README
- **Issues**: GitHub Issues
- **Discusiones**: GitHub Discussions
- **Email**: [Contacto del desarrollador]

---

**Desarrollado con ❤️ por Manus AI**

*¡Inspira a tu comunidad de desarrolladores con contenido creativo diario!*

# discord-pruebas
