#!/usr/bin/env python3
"""
Script de debug para verificar la configuración del bot de Discord.
"""

import os
import sys
from dotenv import load_dotenv

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def check_discord_config():
    """Verifica la configuración de Discord."""
    print("🔍 Verificando configuración de Discord...")
    
    # Cargar variables de entorno
    load_dotenv()
    
    # Verificar token
    token = os.getenv('DISCORD_BOT_TOKEN')
    if token:
        if token == 'tu_token_de_discord_aqui':
            print("❌ DISCORD_BOT_TOKEN no está configurado correctamente")
            print("   Debes reemplazar 'tu_token_de_discord_aqui' con tu token real")
            return False
        else:
            print("✅ DISCORD_BOT_TOKEN está configurado")
            print(f"   Token: {token[:10]}...{token[-10:]}")
            return True
    else:
        print("❌ DISCORD_BOT_TOKEN no está configurado")
        return False

def check_other_vars():
    """Verifica otras variables de entorno."""
    print("\n🔍 Verificando otras variables...")
    
    channel_id = os.getenv('DISCORD_CHANNEL_ID')
    if channel_id:
        print(f"✅ DISCORD_CHANNEL_ID: {channel_id}")
    else:
        print("⚠️ DISCORD_CHANNEL_ID no configurado (opcional)")
    
    publish_hour = os.getenv('PUBLISH_HOUR', '09')
    publish_minute = os.getenv('PUBLISH_MINUTE', '00')
    print(f"✅ Horario de publicación: {publish_hour}:{publish_minute}")
    
    unsplash_key = os.getenv('UNSPLASH_ACCESS_KEY')
    if unsplash_key:
        print("✅ UNSPLASH_ACCESS_KEY configurado")
    else:
        print("⚠️ UNSPLASH_ACCESS_KEY no configurado (opcional)")

def test_discord_connection():
    """Prueba la conexión con Discord."""
    print("\n🔍 Probando conexión con Discord...")
    
    try:
        import discord
        from discord.ext import commands
        
        # Crear bot de prueba
        intents = discord.Intents.default()
        intents.message_content = True
        
        bot = commands.Bot(command_prefix='!', intents=intents)
        
        @bot.event
        async def on_ready():
            print(f"✅ Bot conectado como: {bot.user}")
            print(f"✅ Servidores: {len(bot.guilds)}")
            await bot.close()
        
        token = os.getenv('DISCORD_BOT_TOKEN')
        if token and token != 'tu_token_de_discord_aqui':
            import asyncio
            try:
                asyncio.run(bot.start(token))
            except discord.LoginFailure:
                print("❌ Error de autenticación: Token inválido")
                return False
            except Exception as e:
                print(f"❌ Error de conexión: {e}")
                return False
        else:
            print("❌ No se puede probar sin token válido")
            return False
            
    except ImportError:
        print("❌ discord.py no está instalado")
        return False

if __name__ == "__main__":
    print("🚀 Debug del Bot de Discord")
    print("=" * 40)
    
    # Verificar configuración
    token_ok = check_discord_config()
    check_other_vars()
    
    if token_ok:
        test_discord_connection()
    
    print("\n" + "=" * 40)
    print("📋 Resumen:")
    if token_ok:
        print("✅ Token configurado - Revisa los logs en Railway")
    else:
        print("❌ Configura el token en Railway Variables") 