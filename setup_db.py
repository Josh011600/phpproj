import sqlite3

conn = sqlite3.connect('db1.db')
c = conn.cursor()

# Create users table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Sample data
c.execute("INSERT INTO users (username, password) VALUES ('testuser', 'password123')")
conn.commit()
conn.close()

print("Database and table created successfully.")
