from flask import Blueprint, jsonify
from db import get_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/stats', methods=['GET'])
def stats():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM students')
    students = cur.fetchone()[0]
    cur.execute('SELECT COUNT(*) FROM chats')
    chats = cur.fetchone()[0]
    cur.execute('SELECT COUNT(*) FROM messages')
    messages = cur.fetchone()[0]
    conn.close()
    return jsonify({
        'students': students,
        'chats': chats,
        'messages': messages
    })

@dashboard_bp.route('/top-users', methods=['GET'])
def top_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT students.userUID, students.userName, COUNT(chats.id) as chat_count
        FROM students LEFT JOIN chats ON students.userUID = chats.userUID
        GROUP BY students.userUID
        ORDER BY chat_count DESC
        LIMIT 5
    ''')
    users = [{'userUID': row[0], 'userName': row[1], 'chat_count': row[2]} for row in cur.fetchall()]
    conn.close()
    return jsonify({'top_users': users}) 