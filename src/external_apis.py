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
        # Lista predefinida de herramientas útiles para artistas y creativos
        tools = [
            {
                'name': 'Adobe Creative Cloud',
                'description': 'Suite completa de herramientas creativas profesionales',
                'url': 'https://www.adobe.com/creativecloud.html',
                'category': 'Design'
            },
            {
                'name': 'Blender',
                'description': 'Software gratuito de modelado 3D y animación',
                'url': 'https://www.blender.org/',
                'category': '3D'
            },
            {
                'name': 'Procreate',
                'description': 'App de dibujo digital para iPad',
                'url': 'https://procreate.art/',
                'category': 'Digital Art'
            },
            {
                'name': 'Figma',
                'description': 'Herramienta de diseño colaborativo en la nube',
                'url': 'https://www.figma.com/',
                'category': 'Design'
            },
            {
                'name': 'Canva',
                'description': 'Plataforma de diseño gráfico online',
                'url': 'https://www.canva.com/',
                'category': 'Design'
            },
            {
                'name': 'Midjourney',
                'description': 'IA para generación de arte y conceptos',
                'url': 'https://www.midjourney.com/',
                'category': 'AI Art'
            },
            {
                'name': 'Stable Diffusion',
                'description': 'Modelo de IA para crear imágenes desde texto',
                'url': 'https://stability.ai/',
                'category': 'AI Art'
            },
            {
                'name': 'DALL-E',
                'description': 'Sistema de OpenAI para generar imágenes',
                'url': 'https://openai.com/dall-e-2',
                'category': 'AI Art'
            },
            {
                'name': 'Cinema 4D',
                'description': 'Software profesional de modelado y animación 3D',
                'url': 'https://www.maxon.net/cinema4d',
                'category': '3D'
            },
            {
                'name': 'Unity',
                'description': 'Motor de juegos para crear experiencias 3D',
                'url': 'https://unity.com/',
                'category': '3D'
            },
            {
                'name': 'Unreal Engine',
                'description': 'Motor de juegos para gráficos de alta calidad',
                'url': 'https://www.unrealengine.com/',
                'category': '3D'
            },
            {
                'name': 'DaVinci Resolve',
                'description': 'Software de edición de video profesional',
                'url': 'https://www.blackmagicdesign.com/davinciresolve/',
                'category': 'Video'
            },
            {
                'name': 'After Effects',
                'description': 'Software de composición y efectos visuales',
                'url': 'https://www.adobe.com/products/aftereffects.html',
                'category': 'Motion Graphics'
            },
            {
                'name': 'Notion',
                'description': 'Plataforma para organizar proyectos creativos',
                'url': 'https://www.notion.so/',
                'category': 'Productivity'
            },
            {
                'name': 'Behance',
                'description': 'Plataforma para mostrar portafolios creativos',
                'url': 'https://www.behance.net/',
                'category': 'Portfolio'
            },
            {
                'name': 'ArtStation',
                'description': 'Comunidad para artistas digitales y 3D',
                'url': 'https://www.artstation.com/',
                'category': 'Community'
            }
        ]
        
        return random.choice(tools)
    
    def get_random_resource(self) -> Dict[str, str]:
        """
        Obtiene un recurso útil aleatorio para artistas y creativos.
        
        Returns:
            Diccionario con información del recurso
        """
        resources = [
            {
                'name': 'Pinterest',
                'description': 'Plataforma de inspiración visual y moodboards',
                'url': 'https://www.pinterest.com/',
                'type': 'Inspiration'
            },
            {
                'name': 'Dribbble',
                'description': 'Comunidad de diseñadores para mostrar trabajos',
                'url': 'https://dribbble.com/',
                'type': 'Community'
            },
            {
                'name': 'Behance',
                'description': 'Plataforma para portafolios creativos profesionales',
                'url': 'https://www.behance.net/',
                'type': 'Portfolio'
            },
            {
                'name': 'ArtStation',
                'description': 'Comunidad para artistas digitales y 3D',
                'url': 'https://www.artstation.com/',
                'type': 'Community'
            },
            {
                'name': 'DeviantArt',
                'description': 'Comunidad de artistas digitales y tradicionales',
                'url': 'https://www.deviantart.com/',
                'type': 'Community'
            },
            {
                'name': 'Unsplash',
                'description': 'Fotografías de alta calidad gratuitas',
                'url': 'https://unsplash.com/',
                'type': 'Photography'
            },
            {
                'name': 'Pexels',
                'description': 'Fotos y videos gratuitos de alta calidad',
                'url': 'https://www.pexels.com/',
                'type': 'Photography'
            },
            {
                'name': 'Freepik',
                'description': 'Recursos gráficos, vectores y fotos',
                'url': 'https://www.freepik.com/',
                'type': 'Graphics'
            },
            {
                'name': 'Creative Market',
                'description': 'Mercado de recursos creativos premium',
                'url': 'https://creativemarket.com/',
                'type': 'Marketplace'
            },
            {
                'name': 'Envato Elements',
                'description': 'Suscripción a recursos creativos ilimitados',
                'url': 'https://elements.envato.com/',
                'type': 'Marketplace'
            },
            {
                'name': 'Skillshare',
                'description': 'Plataforma de cursos creativos online',
                'url': 'https://www.skillshare.com/',
                'type': 'Learning'
            },
            {
                'name': 'Domestika',
                'description': 'Cursos de diseño, ilustración y creatividad',
                'url': 'https://www.domestika.org/',
                'type': 'Learning'
            },
            {
                'name': 'YouTube',
                'description': 'Tutoriales gratuitos de diseño y arte',
                'url': 'https://www.youtube.com/',
                'type': 'Learning'
            },
            {
                'name': 'Instagram',
                'description': 'Red social para mostrar y descubrir arte',
                'url': 'https://www.instagram.com/',
                'type': 'Social'
            },
            {
                'name': 'TikTok',
                'description': 'Plataforma para contenido creativo corto',
                'url': 'https://www.tiktok.com/',
                'type': 'Social'
            }
        ]
        
        return random.choice(resources)

class ContentGenerator:
    """Generador de contenido creativo usando OpenAI."""
    
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.openai_api_base = os.getenv('OPENAI_API_BASE')
        
        # Ideas predefinidas como fallback para artistas y creativos
        self.fallback_ideas = [
            "Crea una serie de ilustraciones que representen emociones como paisajes abstractos",
            "Diseña un personaje que evolucione visualmente según su historia",
            "Desarrolla un concepto de marca que combine minimalismo con tecnología",
            "Construye un mundo visual donde los colores tengan personalidades",
            "Crea una campaña publicitaria que use realidad aumentada",
            "Diseña una app que convierta fotos en pinturas de diferentes estilos",
            "Desarrolla un concepto de packaging que cuente una historia",
            "Construye un universo visual para una banda de música",
            "Crea una serie de NFTs que evolucionen con el tiempo",
            "Diseña una experiencia inmersiva para una exposición de arte",
            "Desarrolla un concepto de moda que combine tradición y futuro",
            "Construye un sistema de iconografía para una ciudad del futuro",
            "Crea una campaña que use el arte como activismo social",
            "Diseña un juego visual que explore la psicología del color",
            "Desarrolla un concepto de arquitectura que sea una obra de arte"
        ]
        
        self.fallback_prompts = [
            "Un dragón de cristal que respira arcoíris en un bosque de neón",
            "Una ciudad flotante construida con nubes y rayos de luz",
            "Un jardín donde las flores son instrumentos musicales vivientes",
            "Un océano de tinta donde nadan criaturas hechas de pinceladas",
            "Una biblioteca donde los libros cobran vida y bailan",
            "Un laboratorio donde los científicos mezclan colores como pociones mágicas",
            "Un robot artista que pinta con emociones en lugar de pintura",
            "Una orquesta de mariposas tocando sinfonías de colores",
            "Un museo donde las obras de arte cobran vida por la noche",
            "Una montaña rusa que viaja a través de diferentes estilos artísticos",
            "Un chef que cocina platos que son obras de arte comestibles",
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

