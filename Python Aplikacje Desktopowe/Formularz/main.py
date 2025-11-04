import tkinter as tk
from tkinter import messagebox

def submit_form():
    imie = entry_imie.get()
    email = entry_email.get()
    wiek = var_wiek.get()
    sport = var_sport.get()
    ksiazki = var_ksiazki.get()
    uwagi = text_uwagi.get("1.0", "end-1c")

    zainteresowania = []
    if sport == 1:
        zainteresowania.append("Sport")
    if ksiazki == 1:
        zainteresowania.append("Książki")
    if not zainteresowania:
        zainteresowania.append("Brak")

    komunikat = (
        f"Imię: {imie}\n"
        f"Email: {email}\n"
        f"Kategoria wiekowa: {wiek}\n"
        f"Zainteresowania: {', '.join(zainteresowania)}\n"
        f"Uwagi: {uwagi}"
    )

    messagebox.showinfo("Dane rejestracyjne", komunikat)

root = tk.Tk()
root.title("Formularz Rejestracyjny")
root.geometry("450x400")

var_wiek = tk.StringVar(value="18-30")
var_sport = tk.IntVar()
var_ksiazki = tk.IntVar()

tk.Label(root, text="Imię:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_imie = tk.Entry(root, width=30)
entry_imie.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Wiek (kategoria):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="18-30", variable=var_wiek, value="18-30").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="31-50", variable=var_wiek, value="31-50").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="50+", variable=var_wiek, value="50+").grid(row=4, column=1, sticky="w")

tk.Label(root, text="Zainteresowania:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Sport", variable=var_sport).grid(row=5, column=1, sticky="w")
tk.Checkbutton(root, text="Książki", variable=var_ksiazki).grid(row=6, column=1, sticky="w")

tk.Label(root, text="Uwagi:").grid(row=7, column=0, padx=10, pady=5, sticky="nw")
text_uwagi = tk.Text(root, width=30, height=5)
text_uwagi.grid(row=7, column=1, padx=10, pady=5)

button_zarejestruj = tk.Button(root, text="Zarejestruj", command=submit_form, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
button_zarejestruj.grid(row=8, column=0, columnspan=2, pady=20)

root.mainloop()