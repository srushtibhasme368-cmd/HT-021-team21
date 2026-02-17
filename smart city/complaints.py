from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database create function
def init_db():
    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            area TEXT,
            problem_type TEXT,
            description TEXT,
            date TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("complaint.html")

@app.route("/submit_complaint", methods=["POST"])
def submit_complaint():
    name = request.form["name"]
    area = request.form["area"]
    problem_type = request.form["problem_type"]
    description = request.form["description"]
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO complaints (name, area, problem_type, description, date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, area, problem_type, description, date, "Pending"))
    
    conn.commit()
    conn.close()

    return "<h3>Complaint Submitted Successfully!</h3><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(debug=True)