from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# -----------------------------
# Database Initialization
# -----------------------------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("register.html")


# -----------------------------
# Register Route
# -----------------------------
@app.route("/register", methods=["POST"])
def register():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    phone = request.form.get("phone")

    # Password Match Check
    if password != confirm_password:
        return "<h3>Password does not match!</h3><a href='/'>Go Back</a>"

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (first_name, last_name, username, email, password, phone)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, username, email, password, phone))

        conn.commit()
        conn.close()

        return "<h3>Registration Successful!</h3><a href='/'>Register Another</a>"

    except sqlite3.IntegrityError:
        return "<h3>Username already exists!</h3><a href='/'>Go Back</a>"


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)