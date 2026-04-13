from database import connect

def add_task(user_id, desc):
    conn = connect()
    c = conn.cursor()

    c.execute("INSERT INTO tarefas (user_id, descricao, concluida) VALUES (?, ?, 0)",
              (user_id, desc))

    conn.commit()
    conn.close()

def get_tasks(user_id):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT id, descricao, concluida FROM tarefas WHERE user_id=?", (user_id,))
    data = c.fetchall()

    conn.close()
    return data

def complete_task(task_id):
    conn = connect()
    c = conn.cursor()

    c.execute("UPDATE tarefas SET concluida=1 WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect()
    c = conn.cursor()

    c.execute("DELETE FROM tarefas WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def all_done(user_id):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM tarefas WHERE user_id=? AND concluida=0", (user_id,))
    res = c.fetchone()[0]

    conn.close()
    return res == 0