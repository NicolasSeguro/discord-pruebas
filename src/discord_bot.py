"""
Bot de Discord creativo que publica contenido diario automáticamente.
"""

import discord
from discord.ext import commands, tasks
import os
import asyncio
from datetime import datetime, time
from typing import Optional
from dotenv import load_dotenv

from src.external_apis import unsplash_client, apis_client, content_generator

load_dotenv()

class CreativeBot(commands.Bot):
    """Bot de Discord creativo."""
    
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        
        super().__init__(
            command_prefix='!',
            intents=intents,
            description='Bot creativo que publica contenido diario inspirador'
        )
        
        self.channel_id = os.getenv('DISCORD_CHANNEL_ID')
        self.publish_hour = int(os.getenv('PUBLISH_HOUR', 9))
        self.publish_minute = int(os.getenv('PUBLISH_MINUTE', 0))
    
    async def on_ready(self):
        """Evento que se ejecuta cuando el bot está listo."""
        print(f'{self.user} se ha conectado a Discord!')
        print(f'Bot está en {len(self.guilds)} servidores')
        
        # Iniciar tarea de publicación diaria
        if not self.daily_post.is_running():
            self.daily_post.start()
    
    async def on_command_error(self, ctx, error):
        """Manejo de errores de comandos."""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("❌ Comando no encontrado. Usa `!help` para ver comandos disponibles.")
        else:
            print(f"Error en comando: {error}")
            await ctx.send("❌ Ocurrió un error al ejecutar el comando.")
    
    @tasks.loop(time=time(hour=9, minute=0))  # Se ejecuta diariamente a las 9:00 AM
    async def daily_post(self):
        """Tarea que publica contenido diario."""
        if self.channel_id:
            channel = self.get_channel(int(self.channel_id))
            if channel:
                await self.post_daily_content(channel)
    
    async def post_daily_content(self, channel):
        """
        Publica el contenido diario en el canal especificado.
        
        Args:
            channel: Canal de Discord donde publicar
        """
        try:
            # Obtener contenido de las APIs
            photo = unsplash_client.get_random_photo(query="inspiration")
            tool = apis_client.get_random_tool()
            resource = apis_client.get_random_resource()
            creative_idea = content_generator.generate_creative_idea()
            ai_prompt = content_generator.generate_ai_prompt()
            
            # Crear embed con el contenido
            embed = discord.Embed(
                title="🌟 Inspiración Creativa Diaria",
                description="Tu dosis diaria de creatividad y herramientas útiles",
                color=0x7289DA,
                timestamp=datetime.now()
            )
            
            # Agregar imagen destacada
            if photo:
                embed.set_image(url=photo['urls']['regular'])
                photo_credit = f"📸 **Referencia Visual**\\n"
                if photo.get('user'):
                    photo_credit += f"Por: {photo['user']['name']} | "
                photo_credit += f"[Ver imagen]({photo['links']['html']})"
                embed.add_field(name="", value=photo_credit, inline=False)
            
            # Agregar idea creativa
            embed.add_field(
                name="✍️ Idea Creativa",
                value=creative_idea,
                inline=False
            )
            
            # Agregar herramienta del día
            embed.add_field(
                name="🧰 Tool of the Day",
                value=f"**{tool['name']}**\\n{tool['description']}\\n[Explorar]({tool['url']})",
                inline=False
            )
            
            # Agregar recurso útil
            embed.add_field(
                name="🔗 Recurso Útil",
                value=f"**{resource['name']}**\\n{resource['description']}\\n[Visitar]({resource['url']})",
                inline=False
            )
            
            # Agregar prompt para IA
            embed.add_field(
                name="🎲 Prompt Loco para IA",
                value=f"*\"{ai_prompt}\"*\\n\\n💡 Pruébalo en Midjourney, ChatGPT, DALL-E, etc.",
                inline=False
            )
            
            embed.set_footer(text="Bot Creativo • Inspiración diaria para desarrolladores")
            
            await channel.send(embed=embed)
            print(f"Contenido diario publicado en {channel.name}")
            
        except Exception as e:
            print(f"Error publicando contenido diario: {e}")
    
    @commands.command(name='inspiracion', aliases=['inspire', 'daily'])
    async def manual_inspiration(self, ctx):
        """Comando para obtener inspiración manualmente."""
        await ctx.send("🎨 Generando inspiración creativa...")
        await self.post_daily_content(ctx.channel)
    
    @commands.command(name='foto', aliases=['photo', 'imagen'])
    async def get_photo(self, ctx, *, query: Optional[str] = None):
        """Obtiene una foto aleatoria de Unsplash."""
        photo = unsplash_client.get_random_photo(query=query)
        
        if photo:
            embed = discord.Embed(
                title="📸 Foto Inspiradora",
                color=0x7289DA
            )
            embed.set_image(url=photo['urls']['regular'])
            
            if photo.get('user'):
                embed.set_footer(text=f"Por: {photo['user']['name']}")
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("❌ No se pudo obtener una foto en este momento.")
    
    @commands.command(name='herramienta', aliases=['tool'])
    async def get_tool(self, ctx):
        """Obtiene una herramienta útil aleatoria."""
        tool = apis_client.get_random_tool()
        
        embed = discord.Embed(
            title="🧰 Herramienta Útil",
            description=f"**{tool['name']}**",
            color=0x7289DA
        )
        embed.add_field(name="Descripción", value=tool['description'], inline=False)
        embed.add_field(name="Categoría", value=tool['category'], inline=True)
        embed.add_field(name="Enlace", value=f"[Explorar]({tool['url']})", inline=True)
        
        await ctx.send(embed=embed)
    
    @commands.command(name='recurso', aliases=['resource'])
    async def get_resource(self, ctx):
        """Obtiene un recurso útil aleatorio."""
        resource = apis_client.get_random_resource()
        
        embed = discord.Embed(
            title="🔗 Recurso Útil",
            description=f"**{resource['name']}**",
            color=0x7289DA
        )
        embed.add_field(name="Descripción", value=resource['description'], inline=False)
        embed.add_field(name="Tipo", value=resource['type'], inline=True)
        embed.add_field(name="Enlace", value=f"[Visitar]({resource['url']})", inline=True)
        
        await ctx.send(embed=embed)
    
    @commands.command(name='idea', aliases=['creative'])
    async def get_idea(self, ctx):
        """Genera una idea creativa aleatoria."""
        idea = content_generator.generate_creative_idea()
        
        embed = discord.Embed(
            title="✍️ Idea Creativa",
            description=idea,
            color=0x7289DA
        )
        embed.set_footer(text="💡 ¡Dale vida a esta idea!")
        
        await ctx.send(embed=embed)
    
    @commands.command(name='prompt', aliases=['ai'])
    async def get_prompt(self, ctx):
        """Genera un prompt loco para IA."""
        prompt = content_generator.generate_ai_prompt()
        
        embed = discord.Embed(
            title="🎲 Prompt para IA",
            description=f"*\"{prompt}\"*",
            color=0x7289DA
        )
        embed.set_footer(text="Pruébalo en Midjourney, ChatGPT, DALL-E, etc.")
        
        await ctx.send(embed=embed)
    
    @commands.command(name='config')
    @commands.has_permissions(administrator=True)
    async def configure_channel(self, ctx):
        """Configura el canal actual para publicaciones diarias."""
        # Aquí se podría guardar en base de datos
        embed = discord.Embed(
            title="⚙️ Configuración",
            description=f"Canal configurado para publicaciones diarias: {ctx.channel.mention}",
            color=0x00FF00
        )
        embed.add_field(
            name="Horario",
            value=f"Publicaciones diarias a las {self.publish_hour:02d}:{self.publish_minute:02d}",
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @commands.command(name='help_bot', aliases=['ayuda'])
    async def help_command(self, ctx):
        """Muestra ayuda sobre los comandos disponibles."""
        embed = discord.Embed(
            title="🤖 Comandos del Bot Creativo",
            description="Lista de comandos disponibles:",
            color=0x7289DA
        )
        
        commands_list = [
            ("!inspiracion", "Obtiene inspiración creativa completa"),
            ("!foto [búsqueda]", "Obtiene una foto inspiradora"),
            ("!herramienta", "Obtiene una herramienta útil"),
            ("!recurso", "Obtiene un recurso útil"),
            ("!idea", "Genera una idea creativa"),
            ("!prompt", "Genera un prompt para IA"),
            ("!config", "Configura canal (solo admin)"),
            ("!ayuda", "Muestra esta ayuda")
        ]
        
        for command, description in commands_list:
            embed.add_field(name=command, value=description, inline=False)
        
        embed.set_footer(text="Bot Creativo • Inspiración diaria para desarrolladores")
        
        await ctx.send(embed=embed)

def create_bot():
    """Crea y retorna una instancia del bot."""
    return CreativeBot()

def run_bot():
    """Ejecuta el bot de Discord."""
    bot = create_bot()
    token = os.getenv('DISCORD_BOT_TOKEN')
    
    if not token:
        print("❌ Error: DISCORD_BOT_TOKEN no está configurado en las variables de entorno")
        return
    
    try:
        bot.run(token)
    except discord.LoginFailure:
        print("❌ Error: Token de Discord inválido")
    except Exception as e:
        print(f"❌ Error ejecutando el bot: {e}")

if __name__ == "__main__":
    run_bot()

