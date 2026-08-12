from flask import Flask, request, redirect, render_template_string
import psycopg2
import os
import time

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "tasksdb")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS", "postgres")

def get_conn():
    return psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)

def init_db():
    for attempt in range(10):
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, title TEXT NOT NULL, done BOOLEAN DEFAULT FALSE)")
            conn.commit()
            cur.close()
            conn.close()
            return
        except psycopg2.OperationalError:
            print("waiting for db...")
            time.sleep(3)

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Task Tracker - 2 Tier</title>
    <style>
        body { font-family: Arial; max-width: 500px; margin: 50px auto; }
        .done { text-decoration: line-through; color: gray; }
    </style>
</head>
<body>
    <h1>Task Tracker (2-Tier)</h1>
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
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template_string(PAGE_TEMPLATE, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET done = TRUE WHERE id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
