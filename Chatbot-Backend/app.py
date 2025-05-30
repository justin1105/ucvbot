from flask import Flask, jsonify
from flask_cors import CORS
from chat.routes import chat_bp
from message.routes import message_bp
from admin.routes import admin_bp
from dashboard.routes import dashboard_bp
from db import init_db

app = Flask(__name__)

# Configuración específica de CORS para tu frontend
CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://localhost:4200",  # Solo permite requests desde este origen
            "methods": ["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
            "allow_headers": ["Content-Type", "Authorization"]
        }
    }
)

# Headers de seguridad adicionales
@app.after_request
def add_security_headers(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

init_db()

@app.route('/')
def index():
    return jsonify({'message': 'Backend de chatbot funcionando'}), 200

# Blueprints
app.register_blueprint(chat_bp, url_prefix='/chat')
app.register_blueprint(message_bp, url_prefix='/messages')
app.register_blueprint(admin_bp, url_prefix='/admins')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

# Ruta temporal para estudiantes (pruebas)
@app.route('/students/<uid>', methods=['GET'])
def get_student(uid):
    uid = uid.strip()  # Limpia espacios
    # Simulación de respuesta (elimínalo cuando implementes el Blueprint real)
    if uid == "Xo7G38YmfbXIGMFFNRSxy41P1903":
        return jsonify({"nombre": "Ejemplo", "uid": uid}), 200
    else:
        return jsonify({"error": "Estudiante no encontrado"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Asegúrate de usar el puerto 5000