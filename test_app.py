from flask import Flask, render_template

import sqlite3
app=Flask(__name__)
app.secret_key='__privatekey__'

#Default home page
def defaultHome():
    return render_template('test.html')

def __init__(self):
    con=sqlite3.connect('db1.db')
    c=con.cursor
    c.execute("create table user1(name text, password text)")
    con.commit()


if __name__ == "__main__":
    app.run()  