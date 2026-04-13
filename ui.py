import tkinter as tk
from tkinter import messagebox, ttk

import auth
import tasks
import streak
import charts
from database import init_db

user_id = None
root = tk.Tk()

# ---------------- THEME CONTROL ----------------
dark_mode = True

def apply_theme():
    if dark_mode:
        bg = "#1e1e1e"
        fg = "#ffffff"
        entry_bg = "#2a2a2a"
    else:
        bg = "#f2f2f2"
        fg = "#000000"
        entry_bg = "#ffffff"

    root.configure(bg=bg)

    style.configure("TLabel", background=bg, foreground=fg)
    style.configure("TFrame", background=bg)
    style.configure("TButton", padding=6)
    style.configure("TCheckbutton", background=bg, foreground=fg)

    return bg, fg, entry_bg


def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

    if user_id:
        main_screen()
    else:
        login_screen()

# ---------------- STYLE ----------------
style = ttk.Style()
style.theme_use("clam")

# ---------------- LOGIN ----------------
def login_screen():
    global entry_user, entry_pass

    for w in root.winfo_children():
        w.destroy()

    bg, fg, entry_bg = apply_theme()

    frame = ttk.Frame(root, padding=25)
    frame.pack(expand=True)

    ttk.Label(frame, text="Organizador de Tarefas", font=("Segoe UI", 16, "bold")).pack(pady=10)

    ttk.Label(frame, text="Usuário").pack(anchor="w")
    entry_user = tk.Entry(frame, bg=entry_bg, fg=fg, insertbackground=fg)
    entry_user.pack(fill="x", pady=5)

    ttk.Label(frame, text="Senha").pack(anchor="w")
    entry_pass = tk.Entry(frame, show="*", bg=entry_bg, fg=fg, insertbackground=fg)
    entry_pass.pack(fill="x", pady=5)

    ttk.Button(frame, text="Login", command=do_login).pack(fill="x", pady=5)
    ttk.Button(frame, text="Cadastrar", command=do_register).pack(fill="x")

    ttk.Button(frame, text="Alternar tema", command=toggle_theme).pack(pady=10)

def do_login():
    global user_id

    user_id = auth.login(entry_user.get(), entry_pass.get())

    if user_id:
        main_screen()
    else:
        messagebox.showerror("Erro", "Login inválido")


def do_register():
    ok = auth.register(entry_user.get(), entry_pass.get())

    if ok:
        messagebox.showinfo("Sucesso", "Usuário criado com sucesso")
    else:
        messagebox.showerror("Erro", "Não foi possível cadastrar")

# ---------------- MAIN ----------------
def main_screen():
    for w in root.winfo_children():
        w.destroy()

    bg, fg, entry_bg = apply_theme()

    global listbox, entry_task, bar, label_streak, label_prog

    frame = ttk.Frame(root, padding=15)
    frame.pack(fill="both", expand=True)

    header = ttk.Frame(frame)
    header.pack(fill="x")

    ttk.Label(header, text="Minhas Tarefas", font=("Segoe UI", 16, "bold")).pack(side="left")
    ttk.Button(header, text="Tema", command=toggle_theme).pack(side="right")

    # input
    input_frame = ttk.Frame(frame)
    input_frame.pack(fill="x", pady=10)

    entry_task = tk.Entry(input_frame, bg=entry_bg, fg=fg, insertbackground=fg)
    entry_task.pack(side="left", fill="x", expand=True, padx=5)

    ttk.Button(input_frame, text="Adicionar", command=add).pack(side="left")

    # list
    listbox = tk.Listbox(
        frame,
        height=12,
        bg=entry_bg,
        fg=fg,
        selectbackground="#444"
    )
    listbox.pack(fill="both", expand=True, pady=10)

    # actions
    btns = ttk.Frame(frame)
    btns.pack(fill="x")

    ttk.Button(btns, text="Concluir", command=complete).pack(side="left", expand=True, padx=5)
    ttk.Button(btns, text="Remover", command=delete).pack(side="left", expand=True, padx=5)
    ttk.Button(btns, text="Gráfico", command=lambda: charts.show_chart(user_id)).pack(side="left", expand=True, padx=5)

    # stats
    stats = ttk.Frame(frame)
    stats.pack(fill="x", pady=10)

    label_streak = ttk.Label(stats, text="")
    label_streak.pack(side="left")

    label_prog = ttk.Label(stats, text="")
    label_prog.pack(side="right")

    bar = ttk.Progressbar(frame, length=300)
    bar.pack(fill="x")

    refresh()

# ---------------- ACTIONS ----------------
def refresh():
    listbox.delete(0, tk.END)

    for t in tasks.get_tasks(user_id):
        status = "✔" if t[2] else " "
        listbox.insert(tk.END, f"{t[0]} - [{status}] {t[1]}")

    label_streak.config(text=f"Streak: {streak.streak(user_id)} dias")
    label_prog.config(text=f"{streak.progress(user_id)}% concluído")
    bar["value"] = streak.progress(user_id)

def add():
    if entry_task.get().strip():
        tasks.add_task(user_id, entry_task.get())
        entry_task.delete(0, tk.END)
        refresh()

def complete():
    try:
        idx = listbox.curselection()[0]
        task_id = tasks.get_tasks(user_id)[idx][0]
        tasks.complete_task(task_id)
        refresh()
    except:
        pass

def delete():
    try:
        idx = listbox.curselection()[0]
        task_id = tasks.get_tasks(user_id)[idx][0]
        tasks.delete_task(task_id)
        refresh()
    except:
        pass

# ---------------- START ----------------
def start():
    init_db()
    login_screen()
    root.title("Organizador Profissional")
    root.geometry("520x520")
    root.minsize(500, 500)
    root.mainloop()