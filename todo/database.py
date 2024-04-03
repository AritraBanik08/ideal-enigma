import sqlite3


def conn():
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    return cur


def create_table(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, status TEXT)")
    cur.connection.commit()


def add_task(cur, task):
    cur.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, "Not Done"))
    cur.connection.commit()


def view_tasks(cur):
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    return tasks


def update_task(cur, task_id):
    cur.execute("UPDATE tasks SET status = 'Done' WHERE id = ?", (task_id,))
    cur.connection.commit()