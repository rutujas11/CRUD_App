from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    with sqlite3.connect("crud_app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            );
        """)
        conn.commit()

# Home Page - List All Items
@app.route("/")
def index():
    with sqlite3.connect("crud_app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()
    return render_template("index.html", items=items)

# Create Item
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        with sqlite3.connect("crud_app.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", (name, description))
            conn.commit()
        return redirect(url_for("index"))
    return render_template("create.html")

# Update Item
@app.route("/update/<int:item_id>", methods=["GET", "POST"])
def update(item_id):
    with sqlite3.connect("crud_app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
        item = cursor.fetchone()
        if request.method == "POST":
            name = request.form["name"]
            description = request.form["description"]
            cursor.execute("UPDATE items SET name = ?, description = ? WHERE id = ?", (name, description, item_id))
            conn.commit()
            return redirect(url_for("index"))
    return render_template("update.html", item=item)

# Delete Item
@app.route("/delete/<int:item_id>")
def delete(item_id):
    with sqlite3.connect("crud_app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
