from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_mysqldb import MySQL
import MySQLdb
import mysql.connector
from werkzeug.security import generate_password_hash
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Default XAMPP MySQL user
app.config['MYSQL_PASSWORD'] = ''  # Default is empty in XAMPP
app.config['MYSQL_DB'] = 'mydb'  # Change this to your actual database name
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Use dictionary cursor for better readability

mysql = MySQL(app)

def get_db_connection():
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",           # Default XAMPP MySQL user
        password="",           # Leave empty unless you set a password
        database="mydb"
    )
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, date FROM users")
    tasks = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return tasks

@app.route('/view')
def view_tasks():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, task_name, scheduled_date, created_at FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    return render_template("view.html", tasks=tasks)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:  # If a matching user is found
            session['loggedin'] = True
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials. Please try again."

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age'] or None
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        status = request.form['status']

        hashed_password = generate_password_hash(password)

        conn = None
        cursor = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if username or email exists
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Username or Email already exists', 'danger')
                return render_template('register.html')

            # Insert new user
            cursor.execute("""
                INSERT INTO users (name, age, email, username, password, role, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (name, age, email, username, hashed_password, role, status))

            conn.commit()
            flash('Account registered successfully!', 'success')
            return redirect(url_for('login'))

        except Exception as e:
            flash(f"Error: {e}", 'danger')
            return render_template('register.html')

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    return render_template('register.html')



#for retrieving data from database
@app.route('/api/data')
def get_data():
    data = {"message": "Hello, JSON!"}
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)
