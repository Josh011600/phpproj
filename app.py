from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# Database connection



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(f"Received Username: {username}, Password: {password}")  # Debugging step

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user:
            print(f"User found in database: {user['username']}")  # Debugging step
        else:
            print("User not found in database.")  # Debugging step

        if user and check_password_hash(user['password'], password):
            print("Login successful!")  # Debugging step
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            print("Login failed: Invalid username or password.")  # Debugging step
            flash('Invalid username or password.', 'error')

    return render_template('login.html')


def get_db_connection():
    try:
        conn = sqlite3.connect('users.db', check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password, method='sha256')

        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')



# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('index1.html') 


if __name__ == '__main__':
    app.run(debug=True)
