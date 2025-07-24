@echo off
REM Script de inicio para el Bot Creativo de Discord (Windows)
REM Autor: Manus AI

echo 🤖 Iniciando Bot Creativo de Discord...
echo ======================================

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python no está instalado
    echo    Instala Python 3.11 o superior desde https://python.org
    pause
    exit /b 1
)

REM Mostrar versión de Python
echo 🐍 Python detectado:
python --version

REM Verificar si el entorno virtual existe
if not exist "venv" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Error creando entorno virtual
        pause
        exit /b 1
    )
)

REM Activar entorno virtual
echo 🔧 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Verificar si las dependencias están instaladas
if not exist "venv\Lib\site-packages\discord" (
    echo 📚 Instalando dependencias...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Error instalando dependencias
        pause
        exit /b 1
    )
)

REM Verificar archivo de configuración
if not exist ".env" (
    echo ⚠️  Archivo .env no encontrado
    echo    Copiando .env.example a .env...
    copy .env.example .env
    echo    ⚙️  Edita el archivo .env con tus credenciales antes de continuar
    echo    📝 Especialmente configura DISCORD_BOT_TOKEN
    pause
)

REM Verificar token de Discord
findstr /C:"DISCORD_BOT_TOKEN=" .env | findstr /V /C:"DISCORD_BOT_TOKEN=$" >nul
if errorlevel 1 (
    echo ⚠️  DISCORD_BOT_TOKEN no configurado en .env
    echo    El bot funcionará en modo web únicamente
    echo    Para usar Discord, configura tu token en .env
)

REM Ejecutar pruebas rápidas
echo 🧪 Ejecutando pruebas rápidas...
python test_bot.py >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Algunas pruebas fallaron, pero el bot puede funcionar
) else (
    echo ✅ Pruebas pasaron correctamente
)

REM Mostrar información de inicio
echo.
echo 🚀 Iniciando el bot...
echo    📱 Interfaz web: http://localhost:5000
echo    🤖 Bot de Discord: Verificar estado en la interfaz web
echo    🛑 Para detener: Presiona Ctrl+C
echo.

REM Iniciar el bot
python src\main.py

pause

