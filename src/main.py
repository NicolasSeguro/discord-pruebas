import os
import sys
import threading
import asyncio
from dotenv import load_dotenv

# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify, request
from src.models.user import db
from src.routes.user import user_bp
from src.discord_bot import create_bot
from src.external_apis import unsplash_client, apis_client, content_generator

load_dotenv()

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

app.register_blueprint(user_bp, url_prefix='/api')

# uncomment if you need to use database
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# Bot de Discord
discord_bot = None

def run_discord_bot():
    """Ejecuta el bot de Discord en un hilo separado."""
    global discord_bot
    discord_bot = create_bot()
    token = os.getenv('DISCORD_BOT_TOKEN')
    
    if token:
        try:
            # Crear un nuevo loop para el bot
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(discord_bot.start(token))
        except Exception as e:
            print(f"Error ejecutando bot de Discord: {e}")
    else:
        print("⚠️ DISCORD_BOT_TOKEN no configurado. Bot de Discord deshabilitado.")

# API endpoints para el bot
@app.route('/api/bot/status')
def bot_status():
    """Obtiene el estado del bot."""
    if discord_bot and discord_bot.is_ready():
        return jsonify({
            'status': 'online',
            'user': str(discord_bot.user),
            'guilds': len(discord_bot.guilds)
        })
    else:
        return jsonify({'status': 'offline'})

@app.route('/api/content/photo')
def get_random_photo():
    """API endpoint para obtener una foto aleatoria."""
    query = request.args.get('query')
    photo = unsplash_client.get_random_photo(query=query)
    return jsonify(photo) if photo else jsonify({'error': 'No se pudo obtener foto'}), 500

@app.route('/api/content/tool')
def get_random_tool():
    """API endpoint para obtener una herramienta aleatoria."""
    tool = apis_client.get_random_tool()
    return jsonify(tool)

@app.route('/api/content/resource')
def get_random_resource():
    """API endpoint para obtener un recurso aleatorio."""
    resource = apis_client.get_random_resource()
    return jsonify(resource)

@app.route('/api/content/idea')
def get_creative_idea():
    """API endpoint para obtener una idea creativa."""
    idea = content_generator.generate_creative_idea()
    return jsonify({'idea': idea})

@app.route('/api/content/prompt')
def get_ai_prompt():
    """API endpoint para obtener un prompt de IA."""
    prompt = content_generator.generate_ai_prompt()
    return jsonify({'prompt': prompt})

@app.route('/api/content/daily')
def get_daily_content():
    """API endpoint para obtener todo el contenido diario."""
    photo = unsplash_client.get_random_photo(query="inspiration")
    tool = apis_client.get_random_tool()
    resource = apis_client.get_random_resource()
    idea = content_generator.generate_creative_idea()
    prompt = content_generator.generate_ai_prompt()
    
    return jsonify({
        'photo': photo,
        'tool': tool,
        'resource': resource,
        'idea': idea,
        'prompt': prompt
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    # Iniciar bot de Discord en un hilo separado si está configurado
    if os.getenv('DISCORD_BOT_TOKEN'):
        bot_thread = threading.Thread(target=run_discord_bot, daemon=True)
        bot_thread.start()
        print("🤖 Bot de Discord iniciado en hilo separado")
    
    print("🌐 Servidor Flask iniciado")
    app.run(host='0.0.0.0', port=5000, debug=True)
