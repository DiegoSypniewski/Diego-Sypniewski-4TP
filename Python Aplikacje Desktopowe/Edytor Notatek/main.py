import tkinter as tk

bufor_notatki = ""

def zmien_tryb():
    if tryb_var.get() == "normalny":
        pole_tekstowe.config(state=tk.NORMAL)
    else:
        pole_tekstowe.config(state=tk.DISABLED)

def obsluz_bufor():
    global bufor_notatki
    if bufor_var.get() == 1:
        bufor_notatki = pole_tekstowe.get("1.0", tk.END)
        pole_tekstowe.config(state=tk.NORMAL)
        pole_tekstowe.delete("1.0", tk.END)
        pole_tekstowe.insert("1.0", "Treść została bezpiecznie zbuforowana i ukryta.")
        pole_tekstowe.config(state=tk.DISABLED)
    else:
        pole_tekstowe.config(state=tk.NORMAL)
        pole_tekstowe.delete("1.0", tk.END)
        pole_tekstowe.insert("1.0", bufor_notatki)
        zmien_tryb()

root = tk.Tk()
root.title("Edytor Notatek - Tkinter")

pole_tekstowe = tk.Text(root, height=10, width=50)
pole_tekstowe.insert("1.0", "Witaj w Edytorze Notatek!")
pole_tekstowe.pack(padx=10, pady=10)

tk.Label(root, text="Tryb edycji:").pack(anchor="w", padx=10)

tryb_var = tk.StringVar(value="normalny")
tk.Radiobutton(root, text="Normalny", variable=tryb_var, value="normalny",
               command=zmien_tryb).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Tylko do odczytu", variable=tryb_var, value="readonly",
               command=zmien_tryb).pack(anchor="w", padx=20)

bufor_var = tk.IntVar(value=0)
tk.Checkbutton(root, text="Buforuj i ukryj notatkę", variable=bufor_var,
               onvalue=1, offvalue=0, command=obsluz_bufor).pack(anchor="w", padx=10, pady=10)

root.mainloop()
