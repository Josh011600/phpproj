from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.secret_key = 'your_secret_key'

class Public:
    def __init__(self):
        self.name = "John"  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
print(obj.name)  # Accessible




