import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # open the connection to the database
    conn = sqlite3.connect('AGENTS.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from deployments")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

conn.execute['CREATE TABLE AGENTS(id INTEGER PRIMARY KEY AUTOINCREMENT, Business_Name TEXT, Phone_Number INTEGER, City )  ']