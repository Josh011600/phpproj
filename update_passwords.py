import sqlite3
from werkzeug.security import generate_password_hash

def get_db_connection():
    conn = sqlite3.connect('users.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def update_passwords():
    conn = get_db_connection()
    users = conn.execute('SELECT id, password FROM users').fetchall()

    for user in users:
        plain_password = user['password']

        # Check if the password is already hashed
        if not plain_password.startswith('pbkdf2:sha256'):
            hashed_password = generate_password_hash(plain_password, method='sha256')
            conn.execute('UPDATE users SET password = ? WHERE id = ?', (hashed_password, user['id']))

    conn.commit()
    conn.close()
    print("Passwords have been successfully updated.")

if __name__ == '__main__':
    update_passwords()
