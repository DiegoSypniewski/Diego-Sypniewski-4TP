import tkinter as tk
from tkinter import ttk

def save_settings():
    pbar.start(10)
    print("Zapisywanie ustawień...")
    root.after(3000, finish_saving)

def finish_saving():
    pbar.stop()
    print("Ustawienia zapisane!")

root = tk.Tk()
root.title("Ustawienia Systemu")
root.geometry("350x300")

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, expand=True, fill="both")

tab_apperance = ttk.Frame(notebook, padding=10)
notebook.add(tab_apperance, text="Wygląd")

ttk.Label(tab_apperance, text="Motyw aplikacji:").grid(row=0, column=0, sticky="w")

theme_combo = ttk.Combobox(tab_apperance,
                           values=["Jasny", "Ciemny", "Systemowy"],
                           state="readonly")
theme_combo.current(0)
theme_combo.grid(row=0, column=1, pady=5)

high_contrast = tk.BooleanVar()
ttk.Checkbutton(tab_apperance, text="Włącz wysoki kontrast",
                variable=high_contrast).grid(row=1, column=0, columnspan=2, pady=10, sticky="w")

tab_privacy = ttk.Frame(notebook, padding=10)
notebook.add(tab_privacy, text="Prywatność")

privacy_level = tk.StringVar(value="Anonimowe")

ttk.Label(tab_privacy, text="Udostępnianie danych:").pack(anchor="w")

ttk.Radiobutton(tab_privacy, text="Wszystkie", variable=privacy_level,
                value="Wszystkie").pack(anchor="w")
ttk.Radiobutton(tab_privacy, text="Anonimowe", variable=privacy_level,
                value="Anonimowe").pack(anchor="w")
ttk.Radiobutton(tab_privacy, text="Żadne", variable=privacy_level,
                value="Żadne").pack(anchor="w")

status_frame = ttk.Frame(root, padding=10)
status_frame.pack(fill="x")

pbar = ttk.Progressbar(status_frame, orient="horizontal",
                       length=300, mode="indeterminate")
pbar.pack(pady=5)

ttk.Button(status_frame, text="Zapisz ustawienia",
           command=save_settings).pack(pady=5)

root.mainloop()
