import sqlite3
from contextlib import closing

DB_NAME = 'database.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with closing(get_connection()) as conn:
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    userUID TEXT PRIMARY KEY,
                    userName TEXT,
                    email TEXT,
                    photoURL TEXT,
                    level_id INTEGER,
                    correctExercises INTEGER,
                    incorrectExercises INTEGER,
                    score INTEGER
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS chats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    userUID TEXT,
                    title TEXT,
                    FOREIGN KEY(userUID) REFERENCES students(userUID)
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chat_id INTEGER,
                    role TEXT,
                    statement TEXT,
                    unixTime INTEGER,
                    FOREIGN KEY(chat_id) REFERENCES chats(id)
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS admins (
                    email TEXT PRIMARY KEY,
                    password TEXT,
                    name TEXT
                )
            ''') 