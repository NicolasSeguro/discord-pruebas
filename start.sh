#!/bin/bash

# Script de inicio para el Bot Creativo de Discord
# Autor: Manus AI

echo "🤖 Iniciando Bot Creativo de Discord..."
echo "======================================"

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    echo "   Instala Python 3.11 o superior desde https://python.org"
    exit 1
fi

# Verificar versión de Python
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "🐍 Python detectado: $PYTHON_VERSION"

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Error creando entorno virtual"
        exit 1
    fi
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Verificar si las dependencias están instaladas
if [ ! -f "venv/lib/python*/site-packages/discord/__init__.py" ]; then
    echo "📚 Instalando dependencias..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Error instalando dependencias"
        exit 1
    fi
fi

# Verificar archivo de configuración
if [ ! -f ".env" ]; then
    echo "⚠️  Archivo .env no encontrado"
    echo "   Copiando .env.example a .env..."
    cp .env.example .env
    echo "   ⚙️  Edita el archivo .env con tus credenciales antes de continuar"
    echo "   📝 Especialmente configura DISCORD_BOT_TOKEN"
    read -p "   Presiona Enter cuando hayas configurado .env..."
fi

# Verificar token de Discord
if ! grep -q "DISCORD_BOT_TOKEN=.*[a-zA-Z0-9]" .env; then
    echo "⚠️  DISCORD_BOT_TOKEN no configurado en .env"
    echo "   El bot funcionará en modo web únicamente"
    echo "   Para usar Discord, configura tu token en .env"
fi

# Ejecutar pruebas rápidas
echo "🧪 Ejecutando pruebas rápidas..."
python test_bot.py --quick 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ Pruebas pasaron correctamente"
else
    echo "⚠️  Algunas pruebas fallaron, pero el bot puede funcionar"
fi

# Mostrar información de inicio
echo ""
echo "🚀 Iniciando el bot..."
echo "   📱 Interfaz web: http://localhost:5000"
echo "   🤖 Bot de Discord: Verificar estado en la interfaz web"
echo "   🛑 Para detener: Presiona Ctrl+C"
echo ""

# Iniciar el bot
python src/main.py

