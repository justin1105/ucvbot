from db import get_connection

def create_chat(userUID, title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO chats (userUID, title) VALUES (?, ?)', (userUID, title))
    chat_id = cur.lastrowid
    conn.commit()
    conn.close()
    return chat_id

def get_chats_by_user(userUID):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM chats WHERE userUID = ?', (userUID,))
    rows = cur.fetchall()
    conn.close()
    return rows

def create_message(chat_id, role, statement, unixTime):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO messages (chat_id, role, statement, unixTime) VALUES (?, ?, ?, ?)', (chat_id, role, statement, unixTime))
    message_id = cur.lastrowid
    conn.commit()
    conn.close()
    return message_id

def get_messages_by_chat(chat_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM messages WHERE chat_id = ?', (chat_id,))
    rows = cur.fetchall()
    conn.close()
    return rows 