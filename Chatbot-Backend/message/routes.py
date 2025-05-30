from flask import Blueprint, jsonify
from chat.db_service import get_chats_by_user, get_messages_by_chat

message_bp = Blueprint('message', __name__)

@message_bp.route('/history/<userUID>', methods=['GET'])
def get_history(userUID):
    chats = get_chats_by_user(userUID)
    if not chats:
        return jsonify({'history': []}), 200
    # Tomar el chat más reciente
    last_chat_id = chats[-1][0]
    messages = get_messages_by_chat(last_chat_id)
    msg_list = [{'id': m[0], 'chat_id': m[1], 'role': m[2], 'statement': m[3], 'unixTime': m[4]} for m in messages]
    return jsonify({'history': msg_list}), 200 