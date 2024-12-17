import tkinter as tk
from tkinter import messagebox

# Funkcia spracovania formulára
def submit():
    meno = meno_entry.get()
    email = email_entry.get()
    if meno and email:
        messagebox.showinfo("Úspech", f"Údaje prijaté:\nMeno: {meno}\nEmail: {email}")
    else:
        messagebox.showwarning("Chyba", "Vyplňte všetky polia!")

# Vytvorenie hlavného okna
root = tk.Tk()
root.title("Jednoduchý formulár")

# Pridanie prvkov formulára
tk.Label(root, text="Meno:").grid(row=0, column=0)
meno_entry = tk.Entry(root)
meno_entry.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

submit_button = tk.Button(root, text="Odoslať", command=submit)
submit_button.grid(row=2, column=0, columnspan=2)

# Spustenie aplikácie
root.mainloop()
