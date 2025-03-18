import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Update passwords to hashed values
users = c.execute('SELECT * FROM users').fetchall()
for user in users:
    hashed_password = generate_password_hash(user[1], method='pbkdf2:sha256')
    c.execute('UPDATE users SET password = ? WHERE username = ?', (hashed_password, user[0]))

conn.commit()
conn.close()

print("Passwords updated successfully.")