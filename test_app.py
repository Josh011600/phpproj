from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Default XAMPP MySQL user
app.config['MYSQL_PASSWORD'] = ''  # Default is empty in XAMPP
app.config['MYSQL_DB'] = 'mydb'  # Change this to your actual database name
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Use dictionary cursor for better readability

mysql = MySQL(app)

def get_all_tasks_from_db():
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
    return render_template('test.html')

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

if __name__ == '__main__':
    app.run(debug=True)
