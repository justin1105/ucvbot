from db import get_connection

def get_admin(email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM admins WHERE email = ?', (email,))
    row = cur.fetchone()
    conn.close()
    return row

def create_admin(admin):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO admins (email, password, name)
        VALUES (?, ?, ?)
    ''', (
        admin['email'],
        admin['password'],
        admin.get('name', '')
    ))
    conn.commit()
    conn.close()

def update_password(email, new_password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('UPDATE admins SET password=? WHERE email=?', (new_password, email))
    conn.commit()
    conn.close() 