import tkinter as tk
from database import connect

def show_chart(user_id):
    conn = connect()
    c = conn.cursor()

    c.execute("""
        SELECT data, completo
        FROM streak
        WHERE user_id=?
        ORDER BY id DESC
        LIMIT 7
    """, (user_id,))

    data = c.fetchall()
    conn.close()

    if not data:
        return

    data = data[::-1]

    days = [str(d[0]) for d in data]
    values = [int(d[1]) for d in data]

    win = tk.Toplevel()
    win.title("Gráfico de Progresso")
    win.geometry("400x300")
    win.configure(bg="white")

    canvas = tk.Canvas(win, bg="white")
    canvas.pack(fill="both", expand=True)

    # dimensões
    w = 350
    h = 200
    x0 = 30
    y0 = 250

    max_val = max(values) if max(values) > 0 else 1

    step = w / (len(values) - 1 if len(values) > 1 else 1)

    points = []

    # desenha linhas e pontos
    for i in range(len(values)):
        x = x0 + i * step
        y = y0 - (values[i] / max_val) * h

        points.append((x, y))

        # ponto
        canvas.create_oval(x-4, y-4, x+4, y+4, fill="blue")

        # label
        canvas.create_text(x, y+15, text=days[i], font=("Arial", 8))

    # linhas entre pontos
    for i in range(len(points)-1):
        canvas.create_line(points[i][0], points[i][1],
                           points[i+1][0], points[i+1][1],
                           fill="blue", width=2)

    canvas.create_text(200, 20,
                       text="Últimos 7 dias",
                       font=("Arial", 14, "bold"))