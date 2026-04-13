from datetime import datetime
from database import connect

def today():
    return datetime.now().strftime("%Y-%m-%d")

# REGISTRA O DIA NO STREAK
def register_day(user_id, completo):
    conn = connect()
    c = conn.cursor()

    data = today()

    # evita duplicar o mesmo dia
    c.execute("""
        SELECT id FROM streak
        WHERE user_id=? AND data=?
    """, (user_id, data))

    exists = c.fetchone()

    if exists:
        c.execute("""
            UPDATE streak
            SET completo=?
            WHERE user_id=? AND data=?
        """, (completo, user_id, data))
    else:
        c.execute("""
            INSERT INTO streak (user_id, data, completo)
            VALUES (?, ?, ?)
        """, (user_id, data, completo))

    conn.commit()
    conn.close()


# CALCULA STREAK CONSECUTIVO
def streak(user_id):
    conn = connect()
    c = conn.cursor()

    c.execute("""
        SELECT completo
        FROM streak
        WHERE user_id=?
        ORDER BY data DESC
    """, (user_id,))

    rows = c.fetchall()
    conn.close()

    s = 0

    for (v,) in rows:
        if v == 1:
            s += 1
        else:
            break

    return s


# PROGRESSO DAS TAREFAS
def progress(user_id):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM tarefas WHERE user_id=?", (user_id,))
    total = c.fetchone()[0]

    c.execute("""
        SELECT COUNT(*)
        FROM tarefas
        WHERE user_id=? AND concluida=1
    """, (user_id,))

    done = c.fetchone()[0]

    conn.close()

    return int((done / total) * 100) if total > 0 else 0