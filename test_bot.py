#!/usr/bin/env python3
"""
Script de prueba para verificar todas las funcionalidades del bot de Discord creativo.
"""

import sys
import os
import asyncio
import requests
import time
from dotenv import load_dotenv

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from external_apis import unsplash_client, apis_client, content_generator

def test_unsplash_api():
    """Prueba la API de Unsplash."""
    print("🧪 Probando API de Unsplash...")
    
    try:
        photo = unsplash_client.get_random_photo()
        if photo:
            print(f"✅ Foto obtenida: {photo.get('id', 'N/A')}")
            print(f"   URL: {photo['urls']['regular']}")
            if photo.get('user'):
                print(f"   Autor: {photo['user']['name']}")
            return True
        else:
            print("❌ No se pudo obtener foto")
            return False
    except Exception as e:
        print(f"❌ Error en API de Unsplash: {e}")
        return False

def test_tools_api():
    """Prueba el sistema de herramientas."""
    print("\\n🧪 Probando sistema de herramientas...")
    
    try:
        tool = apis_client.get_random_tool()
        print(f"✅ Herramienta obtenida: {tool['name']}")
        print(f"   Descripción: {tool['description']}")
        print(f"   Categoría: {tool['category']}")
        print(f"   URL: {tool['url']}")
        return True
    except Exception as e:
        print(f"❌ Error en sistema de herramientas: {e}")
        return False

def test_resources_api():
    """Prueba el sistema de recursos."""
    print("\\n🧪 Probando sistema de recursos...")
    
    try:
        resource = apis_client.get_random_resource()
        print(f"✅ Recurso obtenido: {resource['name']}")
        print(f"   Descripción: {resource['description']}")
        print(f"   Tipo: {resource['type']}")
        print(f"   URL: {resource['url']}")
        return True
    except Exception as e:
        print(f"❌ Error en sistema de recursos: {e}")
        return False

def test_content_generator():
    """Prueba el generador de contenido."""
    print("\\n🧪 Probando generador de contenido...")
    
    try:
        # Probar idea creativa
        idea = content_generator.generate_creative_idea()
        print(f"✅ Idea creativa generada: {idea[:100]}...")
        
        # Probar prompt de IA
        prompt = content_generator.generate_ai_prompt()
        print(f"✅ Prompt de IA generado: {prompt[:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Error en generador de contenido: {e}")
        return False

def test_flask_server():
    """Prueba el servidor Flask."""
    print("\\n🧪 Probando servidor Flask...")
    
    # Lista de endpoints para probar
    endpoints = [
        '/api/content/photo',
        '/api/content/tool',
        '/api/content/resource',
        '/api/content/idea',
        '/api/content/prompt',
        '/api/content/daily'
    ]
    
    base_url = 'http://localhost:5000'
    results = []
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=10)
            if response.status_code == 200:
                print(f"✅ {endpoint}: OK")
                results.append(True)
            else:
                print(f"❌ {endpoint}: HTTP {response.status_code}")
                results.append(False)
        except requests.exceptions.RequestException as e:
            print(f"❌ {endpoint}: Error de conexión - {e}")
            results.append(False)
    
    return all(results)

def test_environment_variables():
    """Verifica las variables de entorno."""
    print("🧪 Verificando variables de entorno...")
    
    load_dotenv()
    
    # Variables requeridas
    required_vars = ['OPENAI_API_KEY', 'OPENAI_API_BASE']
    optional_vars = ['DISCORD_BOT_TOKEN', 'UNSPLASH_ACCESS_KEY', 'DISCORD_CHANNEL_ID']
    
    all_good = True
    
    for var in required_vars:
        if os.getenv(var):
            print(f"✅ {var}: Configurado")
        else:
            print(f"❌ {var}: No configurado")
            all_good = False
    
    for var in optional_vars:
        if os.getenv(var):
            print(f"✅ {var}: Configurado")
        else:
            print(f"⚠️ {var}: No configurado (opcional)")
    
    return all_good

def run_comprehensive_test():
    """Ejecuta todas las pruebas."""
    print("🚀 Iniciando pruebas comprehensivas del Bot Creativo de Discord\\n")
    print("=" * 60)
    
    tests = [
        ("Variables de entorno", test_environment_variables),
        ("API de Unsplash", test_unsplash_api),
        ("Sistema de herramientas", test_tools_api),
        ("Sistema de recursos", test_resources_api),
        ("Generador de contenido", test_content_generator),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\\n📋 {test_name}")
        print("-" * 40)
        result = test_func()
        results.append((test_name, result))
        time.sleep(1)  # Pausa entre pruebas
    
    # Resumen de resultados
    print("\\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASÓ" if result else "❌ FALLÓ"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\\n🎯 Resultado final: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron! El bot está listo para usar.")
        return True
    else:
        print("⚠️ Algunas pruebas fallaron. Revisa la configuración.")
        return False

def test_content_generation_variety():
    """Prueba la variedad en la generación de contenido."""
    print("\\n🧪 Probando variedad en generación de contenido...")
    
    ideas = set()
    prompts = set()
    
    # Generar múltiples elementos para verificar variedad
    for i in range(5):
        idea = content_generator.generate_creative_idea()
        prompt = content_generator.generate_ai_prompt()
        ideas.add(idea)
        prompts.add(prompt)
    
    idea_variety = len(ideas) / 5
    prompt_variety = len(prompts) / 5
    
    print(f"✅ Variedad de ideas: {idea_variety:.1%} ({len(ideas)}/5 únicas)")
    print(f"✅ Variedad de prompts: {prompt_variety:.1%} ({len(prompts)}/5 únicos)")
    
    return idea_variety > 0.6 and prompt_variety > 0.6

if __name__ == "__main__":
    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Ejecutar pruebas
    success = run_comprehensive_test()
    
    # Prueba adicional de variedad
    print("\\n" + "=" * 60)
    test_content_generation_variety()
    
    # Código de salida
    sys.exit(0 if success else 1)

