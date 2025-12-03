import tkinter as tk
from tkinter import ttk

def show_selection(event):
    selected = combo.get()
    selected_label.config(text=f"Wybrano: {selected}")

root = tk.Tk()
root.title("Ćwiczenie: Combobox")

frame = ttk.Frame(root, padding=20)
frame.pack()

ttk.Label(frame, text="Wybierz język:").grid(row=0, column=0, padx=5, pady=5, sticky="w")

programming_languages = ["Python", "Java", "C++", "JavaScript", "C#"]
combo = ttk.Combobox(frame, values=programming_languages, state="readonly")
combo.current(0)
combo.grid(row=0, column=1, padx=5, pady=5)

# Nowa etykieta
selected_label = ttk.Label(frame, text="Wybrano: Python")
selected_label.grid(row=1, column=0, columnspan=2, pady=10)

combo.bind("<<ComboboxSelected>>", show_selection)

root.mainloop()
