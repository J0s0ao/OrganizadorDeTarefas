from database import connect

def register(user, senha):
    conn = connect()
    c = conn.cursor()

    try:
        c.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?)", (user, senha))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login(user, senha):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT id FROM usuarios WHERE username=? AND senha=?", (user, senha))
    res = c.fetchone()

    conn.close()
    return res[0] if res else None