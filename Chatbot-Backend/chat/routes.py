from flask import Blueprint, request, jsonify
from ia.rapidapi_service import get_bot_response
from .db_service import create_chat, create_message, get_chats_by_user, get_messages_by_chat
import time

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/start', methods=['POST'])
def start_chat():
    data = request.get_json()
    userUID = data.get('userUID')
    message = data.get('message')
    if not userUID or not message:
        return jsonify({'error': 'userUID y message requeridos'}), 400
    # Crear chat
    chat_id = create_chat(userUID, title="Chat con IA")
    # Guardar mensaje del usuario
    unixTime = int(time.time() * 1000)
    create_message(chat_id, "user", message, unixTime)
    # Obtener respuesta del bot
    bot_response = get_bot_response(message)
    unixTimeBot = int(time.time() * 1000)
    create_message(chat_id, "assistant", bot_response, unixTimeBot)
    return jsonify({
        'chat_id': chat_id,
        'user_message': message,
        'bot_response': bot_response
    }), 200

@chat_bp.route('/user/<userUID>', methods=['GET'])
def get_user_chats(userUID):
    chats = get_chats_by_user(userUID)
    chat_list = [{'id': c[0], 'userUID': c[1], 'title': c[2]} for c in chats]
    return jsonify({'chats': chat_list}), 200

@chat_bp.route('/<int:chat_id>/messages', methods=['GET'])
def get_chat_messages(chat_id):
    messages = get_messages_by_chat(chat_id)
    msg_list = [{'id': m[0], 'chat_id': m[1], 'role': m[2], 'statement': m[3], 'unixTime': m[4]} for m in messages]
    return jsonify({'messages': msg_list}), 200 