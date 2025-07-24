"""
Módulo para manejar APIs externas para el bot de Discord creativo.
Incluye funciones para obtener imágenes, herramientas y recursos.
"""

import requests
import random
import os
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv

load_dotenv()

class UnsplashAPI:
    """Cliente para la API de Unsplash."""
    
    def __init__(self):
        self.access_key = os.getenv('UNSPLASH_ACCESS_KEY')
        self.base_url = 'https://api.unsplash.com'
        self.headers = {
            'Authorization': f'Client-ID {self.access_key}' if self.access_key else None
        }
    
    def get_random_photo(self, query: Optional[str] = None, orientation: str = 'landscape') -> Optional[Dict[str, Any]]:
        """
        Obtiene una foto aleatoria de Unsplash.
        
        Args:
            query: Término de búsqueda opcional
            orientation: Orientación de la foto (landscape, portrait, squarish)
            
        Returns:
            Diccionario con información de la foto o None si hay error
        """
        if not self.access_key:
            # Fallback a Lorem Picsum si no hay API key
            return self._get_lorem_picsum_photo()
        
        endpoint = f'{self.base_url}/photos/random'
        params = {
            'orientation': orientation
        }
        
        if query:
            params['query'] = query
            
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error obteniendo foto de Unsplash: {e}")
            return self._get_lorem_picsum_photo()
    
    def _get_lorem_picsum_photo(self) -> Dict[str, Any]:
        """
        Fallback usando Lorem Picsum (que usa imágenes de Unsplash).
        """
        width = random.randint(800, 1200)
        height = random.randint(600, 800)
        photo_id = random.randint(1, 1000)
        
        return {
            'id': f'picsum_{photo_id}',
            'urls': {
                'regular': f'https://picsum.photos/{width}/{height}?random={photo_id}',
                'small': f'https://picsum.photos/400/300?random={photo_id}',
                'thumb': f'https://picsum.photos/200/150?random={photo_id}'
            },
            'links': {
                'html': f'https://picsum.photos/{width}/{height}?random={photo_id}'
            },
            'user': {
                'name': 'Lorem Picsum',
                'username': 'picsum'
            },
            'description': 'Imagen aleatoria de Lorem Picsum'
        }

class PublicAPIsClient:
    """Cliente para obtener herramientas y recursos del repositorio public-apis."""
    
    def __init__(self):
        self.github_api_url = 'https://api.github.com/repos/public-apis/public-apis/contents/README.md'
        self.categories = [
            'Development', 'Programming', 'Art & Design', 'Photography',
            'Machine Learning', 'Data Validation', 'Text Analysis',
            'Entertainment', 'Games & Comics', 'Music', 'Video'
        ]
    
    def get_random_tool(self) -> Dict[str, str]:
        """
        Obtiene una herramienta aleatoria de las categorías relevantes.
        
        Returns:
            Diccionario con información de la herramienta
        """
        # Lista predefinida de herramientas útiles para desarrolladores
        tools = [
            {
                'name': 'Unsplash API',
                'description': 'API gratuita para obtener fotografías de alta calidad',
                'url': 'https://unsplash.com/developers',
                'category': 'Photography'
            },
            {
                'name': 'Discord.py',
                'description': 'Librería de Python para crear bots de Discord',
                'url': 'https://discordpy.readthedocs.io/',
                'category': 'Development'
            },
            {
                'name': 'OpenAI API',
                'description': 'API para generar texto e imágenes con IA',
                'url': 'https://openai.com/api/',
                'category': 'Machine Learning'
            },
            {
                'name': 'GitHub API',
                'description': 'API para interactuar con repositorios de GitHub',
                'url': 'https://docs.github.com/en/rest',
                'category': 'Development'
            },
            {
                'name': 'Pexels API',
                'description': 'API gratuita para fotos y videos de stock',
                'url': 'https://www.pexels.com/api/',
                'category': 'Photography'
            },
            {
                'name': 'JSONPlaceholder',
                'description': 'API falsa para testing y prototipado',
                'url': 'https://jsonplaceholder.typicode.com/',
                'category': 'Development'
            },
            {
                'name': 'Cat Facts API',
                'description': 'API para obtener datos curiosos sobre gatos',
                'url': 'https://catfact.ninja/',
                'category': 'Entertainment'
            },
            {
                'name': 'Lorem Picsum',
                'description': 'Servicio para obtener imágenes placeholder',
                'url': 'https://picsum.photos/',
                'category': 'Photography'
            }
        ]
        
        return random.choice(tools)
    
    def get_random_resource(self) -> Dict[str, str]:
        """
        Obtiene un recurso útil aleatorio para desarrolladores.
        
        Returns:
            Diccionario con información del recurso
        """
        resources = [
            {
                'name': 'MDN Web Docs',
                'description': 'Documentación completa para tecnologías web',
                'url': 'https://developer.mozilla.org/',
                'type': 'Documentation'
            },
            {
                'name': 'Stack Overflow',
                'description': 'Comunidad de preguntas y respuestas para programadores',
                'url': 'https://stackoverflow.com/',
                'type': 'Community'
            },
            {
                'name': 'GitHub',
                'description': 'Plataforma de desarrollo colaborativo',
                'url': 'https://github.com/',
                'type': 'Platform'
            },
            {
                'name': 'Codecademy',
                'description': 'Plataforma interactiva para aprender programación',
                'url': 'https://www.codecademy.com/',
                'type': 'Learning'
            },
            {
                'name': 'FreeCodeCamp',
                'description': 'Cursos gratuitos de programación y desarrollo web',
                'url': 'https://www.freecodecamp.org/',
                'type': 'Learning'
            },
            {
                'name': 'Can I Use',
                'description': 'Compatibilidad de características web en navegadores',
                'url': 'https://caniuse.com/',
                'type': 'Tool'
            },
            {
                'name': 'Regex101',
                'description': 'Herramienta online para probar expresiones regulares',
                'url': 'https://regex101.com/',
                'type': 'Tool'
            },
            {
                'name': 'Postman',
                'description': 'Plataforma para desarrollo y testing de APIs',
                'url': 'https://www.postman.com/',
                'type': 'Tool'
            }
        ]
        
        return random.choice(resources)

class ContentGenerator:
    """Generador de contenido creativo usando OpenAI."""
    
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.openai_api_base = os.getenv('OPENAI_API_BASE')
        
        # Ideas predefinidas como fallback
        self.fallback_ideas = [
            "Crea una aplicación que convierta código en poesía visual",
            "Diseña un bot que genere paletas de colores basadas en emociones",
            "Desarrolla una herramienta que transforme música en patrones geométricos",
            "Construye un generador de historias interactivas usando APIs públicas",
            "Crea un visualizador de datos que convierta estadísticas en arte",
            "Diseña una app que genere fondos de pantalla basados en el clima",
            "Desarrolla un bot que cree memes usando inteligencia artificial",
            "Construye una herramienta que transforme texto en paisajes sonoros",
            "Crea un juego donde los jugadores programen robots virtuales",
            "Diseña una red social para compartir algoritmos como arte",
            "Desarrolla una app que genere música basada en patrones de código",
            "Construye un asistente IA que escriba documentación automáticamente",
            "Crea una plataforma para colaborar en proyectos usando realidad virtual",
            "Diseña un sistema que convierta emociones en interfaces de usuario",
            "Desarrolla una herramienta que genere APIs basadas en lenguaje natural"
        ]
        
        self.fallback_prompts = [
            "Un gato programador escribiendo código en un café flotante en el espacio",
            "Una ciudad futurista donde los edificios están hechos de código binario",
            "Un dragón que respira algoritmos en lugar de fuego",
            "Una biblioteca infinita donde cada libro contiene un lenguaje de programación diferente",
            "Un océano de datos donde nadan peces hechos de píxeles",
            "Un jardín donde crecen árboles de sintaxis y flores de variables",
            "Una montaña rusa que viaja a través de diferentes frameworks de desarrollo",
            "Un laboratorio donde los científicos mezclan APIs como pociones mágicas",
            "Un robot chef que cocina aplicaciones web en una cocina cibernética",
            "Una orquesta de inteligencias artificiales tocando sinfonías de código",
            "Un museo donde las obras de arte son algoritmos vivientes",
            "Una escuela mágica donde se enseñan hechizos de programación",
            "Un parque de diversiones construido dentro de una base de datos",
            "Una nave espacial pilotada por un sistema operativo consciente",
            "Un bosque encantado donde los árboles son estructuras de datos"
        ]
    
    def generate_creative_idea(self) -> str:
        """
        Genera una idea creativa usando OpenAI o fallback.
        
        Returns:
            String con la idea creativa
        """
        if self.openai_api_key:
            try:
                import openai
                
                # Configurar cliente OpenAI
                client = openai.OpenAI(
                    api_key=self.openai_api_key,
                    base_url=self.openai_api_base
                )
                
                prompts = [
                    "Genera una idea creativa e innovadora para un proyecto de programación que combine tecnología con arte o entretenimiento. La idea debe ser específica, factible y original. Responde en una sola oración clara y directa.",
                    "Crea una idea única para una aplicación o herramienta que resuelva un problema cotidiano de manera creativa usando tecnología. Debe ser algo que no existe actualmente. Una sola oración.",
                    "Propón una idea innovadora que combine inteligencia artificial con creatividad para crear algo útil y divertido. Sé específico y conciso en una oración.",
                    "Imagina una herramienta o aplicación que transforme datos aburridos en algo visualmente atractivo e interactivo. Describe la idea en una oración clara.",
                    "Genera una idea para un proyecto que use APIs públicas de manera creativa para crear algo completamente nuevo e inesperado. Una oración específica."
                ]
                
                selected_prompt = random.choice(prompts)
                
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": "Eres un generador de ideas creativas para desarrolladores. Tus respuestas deben ser concisas, específicas y factibles."},
                        {"role": "user", "content": selected_prompt}
                    ],
                    max_tokens=100,
                    temperature=0.9
                )
                
                idea = response.choices[0].message.content.strip()
                
                # Validar que la respuesta no esté vacía
                if idea and len(idea) > 10:
                    return idea
                else:
                    return random.choice(self.fallback_ideas)
                    
            except Exception as e:
                print(f"Error generando idea con OpenAI: {e}")
                return random.choice(self.fallback_ideas)
        
        return random.choice(self.fallback_ideas)
    
    def generate_ai_prompt(self) -> str:
        """
        Genera un prompt creativo para usar en herramientas de IA.
        
        Returns:
            String con el prompt
        """
        if self.openai_api_key:
            try:
                import openai
                
                client = openai.OpenAI(
                    api_key=self.openai_api_key,
                    base_url=self.openai_api_base
                )
                
                prompt_generators = [
                    "Crea un prompt visual surrealista que combine tecnología con elementos fantásticos. Debe ser descriptivo y específico para generar imágenes interesantes en DALL-E o Midjourney.",
                    "Genera un prompt que describa una escena imposible donde la programación y la magia coexisten. Sé muy descriptivo y visual.",
                    "Crea un prompt para generar una imagen que muestre el futuro de la tecnología de manera artística y creativa. Incluye detalles visuales específicos.",
                    "Genera un prompt que combine animales con elementos de programación de manera divertida y surrealista. Debe ser muy visual y detallado.",
                    "Crea un prompt que describa un mundo donde los conceptos abstractos de programación tienen forma física. Sé específico en los detalles visuales."
                ]
                
                selected_generator = random.choice(prompt_generators)
                
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": "Eres un experto en crear prompts visuales creativos para herramientas de IA como DALL-E, Midjourney y Stable Diffusion. Tus prompts deben ser descriptivos, específicos y generar imágenes interesantes."},
                        {"role": "user", "content": selected_generator}
                    ],
                    max_tokens=150,
                    temperature=1.0
                )
                
                prompt = response.choices[0].message.content.strip()
                
                # Limpiar el prompt si viene con comillas
                prompt = prompt.strip('"').strip("'")
                
                if prompt and len(prompt) > 20:
                    return prompt
                else:
                    return random.choice(self.fallback_prompts)
                    
            except Exception as e:
                print(f"Error generando prompt con OpenAI: {e}")
                return random.choice(self.fallback_prompts)
        
        return random.choice(self.fallback_prompts)
    
    def generate_themed_content(self, theme: str) -> Dict[str, str]:
        """
        Genera contenido temático usando OpenAI.
        
        Args:
            theme: Tema para el contenido (ej: "machine learning", "web development")
            
        Returns:
            Diccionario con idea y prompt temáticos
        """
        if self.openai_api_key:
            try:
                import openai
                
                client = openai.OpenAI(
                    api_key=self.openai_api_key,
                    base_url=self.openai_api_base
                )
                
                # Generar idea temática
                idea_response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": f"Eres un experto en {theme}. Genera ideas creativas e innovadoras relacionadas con este tema."},
                        {"role": "user", "content": f"Crea una idea específica y factible para un proyecto relacionado con {theme}. Debe ser innovadora y útil. Una sola oración clara."}
                    ],
                    max_tokens=100,
                    temperature=0.8
                )
                
                # Generar prompt temático
                prompt_response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": "Creas prompts visuales creativos para herramientas de IA."},
                        {"role": "user", "content": f"Crea un prompt visual que represente {theme} de manera artística y surrealista. Debe ser muy descriptivo y específico."}
                    ],
                    max_tokens=150,
                    temperature=1.0
                )
                
                idea = idea_response.choices[0].message.content.strip()
                prompt = prompt_response.choices[0].message.content.strip().strip('"').strip("'")
                
                return {
                    'idea': idea if idea and len(idea) > 10 else random.choice(self.fallback_ideas),
                    'prompt': prompt if prompt and len(prompt) > 20 else random.choice(self.fallback_prompts)
                }
                
            except Exception as e:
                print(f"Error generando contenido temático con OpenAI: {e}")
        
        # Fallback
        return {
            'idea': random.choice(self.fallback_ideas),
            'prompt': random.choice(self.fallback_prompts)
        }

# Instancias globales
unsplash_client = UnsplashAPI()
apis_client = PublicAPIsClient()
content_generator = ContentGenerator()

