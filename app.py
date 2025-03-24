from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import hashlib
import os
from werkzeug.security import generate_password_hash, check_password_hash
currentdirectory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

app.secret_key = 'your_secret_key'  # For flash messages

# Database connection
def get_db_connection():
    conn = sqlite3.connect('db1.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password, method='sha256')

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            flash('Username already exists.', 'error')
        finally:
            conn.close()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)
