# APIs Investigadas para Bot de Discord Creativo

## Resumen del Proyecto
Bot de Discord que publica diariamente:
- 📸 Referencia visual (imagen destacada + link)
- ✍️ Idea creativa random generada con IA
- 🧰 Tool of the Day
- 🔗 Link a recurso útil
- 🎲 Prompt loco para probar en Midjourney, ChatGPT, etc

## APIs para Imágenes/Fotografía

### Unsplash API
- **URL**: https://unsplash.com/developers
- **Descripción**: Photography API con OAuth
- **Uso**: Obtener imágenes destacadas diarias
- **Autenticación**: OAuth
- **HTTPS**: Sí
- **CORS**: Unknown

### Pexels API
- **URL**: https://www.pexels.com/api/
- **Descripción**: Free Stock Photos and Videos
- **Uso**: Alternativa para imágenes gratuitas
- **Autenticación**: apiKey
- **HTTPS**: Sí
- **CORS**: Sí

### Pixabay API
- **Descripción**: Photography
- **Uso**: Otra alternativa para imágenes
- **Autenticación**: apiKey
- **HTTPS**: Sí
- **CORS**: Unknown

### Lorem Picsum
- **Descripción**: Images from Unsplash
- **Uso**: Imágenes placeholder de Unsplash
- **Autenticación**: No
- **HTTPS**: Sí
- **CORS**: Unknown

## APIs para Contenido Creativo

### OpenAI API
- **Descripción**: Para generar ideas creativas y prompts
- **Uso**: Generar contenido creativo diario
- **Variables de entorno**: OPENAI_API_KEY, OPENAI_API_BASE ya configuradas

## APIs para Herramientas y Recursos

### GitHub Public APIs Repository
- **URL**: https://github.com/public-apis/public-apis
- **Descripción**: Lista curada de APIs públicas
- **Uso**: Fuente para "Tool of the Day" y recursos útiles
- **Categorías relevantes**:
  - Development
  - Programming
  - Art & Design
  - Photography

## Librerías de Discord

### discord.py
- **URL**: https://discordpy.readthedocs.io/
- **Descripción**: Modern, easy to use, feature-rich, and async ready API wrapper for Discord
- **Características**:
  - Modern Pythonic API using async/await syntax
  - Sane rate limit handling that prevents 429s
  - Command extension to aid with bot creation
  - Easy to use with an object oriented design
  - Optimised for both speed and memory

### Instalación
```bash
pip install discord.py
```

### Ejemplo básico
```python
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('your token here')
```

## Próximos Pasos

1. Configurar discord.py en el proyecto Flask
2. Implementar sistema de obtención de imágenes desde Unsplash/Pexels
3. Crear generador de contenido creativo con OpenAI
4. Desarrollar sistema de selección de herramientas del día
5. Implementar scheduler para publicaciones automáticas
6. Crear sistema de formateo de mensajes con emojis

