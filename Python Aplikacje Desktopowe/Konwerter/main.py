import tkinter as tk
from tkinter import messagebox

def konwertuj():
    try:
        metry = float(entry_wartosc.get())
        stopy = metry * 3.28084
        label_wynik.config(text=f"Wynik: {stopy:.2f} stóp")
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawną wartość liczbową!")

root = tk.Tk()
root.title("Konwerter Jednostek")
root.geometry("300x200")

label_info = tk.Label(root, text="Wprowadź wartość (metry):")
label_info.pack(pady=10)

entry_wartosc = tk.Entry(root, width=20)
entry_wartosc.pack(pady=5)

button_konwertuj = tk.Button(root, text="Konwertuj na stopy", command=konwertuj)
button_konwertuj.pack(pady=10)

label_wynik = tk.Label(root, text="Wynik: 0.0 stóp")
label_wynik.pack(pady=10)

root.mainloop()