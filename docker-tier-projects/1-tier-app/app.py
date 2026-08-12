from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)
DB_PATH = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, done INTEGER DEFAULT 0)")
    conn.commit()
    conn.close()

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Task Tracker</title>
    <style>
        body { font-family: Arial; max-width: 500px; margin: 50px auto; }
        .done { text-decoration: line-through; color: gray; }
    </style>
</head>
<body>
    <h1>Task Tracker</h1>
    <form action="/add" method="post">
        <input type="text" name="title" placeholder="New task..." required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for task in tasks %}
            <li class="{{ 'done' if task[2] else '' }}">
                {{ task[1] }}
                {% if not task[2] %}
                    <a href="/complete/{{ task[0] }}">done</a>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template_string(PAGE_TEMPLATE, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
