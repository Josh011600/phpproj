from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


# Create a SQL connection to our SQLite database
con = sqlite3.connect("data/db1.db")

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM users;'):
    print(row)

# Be sure to close the connection
con.close()


