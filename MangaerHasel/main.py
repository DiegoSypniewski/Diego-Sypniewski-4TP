import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import base64
import random
import string


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manager Haseł")
        self.root.geometry("550x450")

        self.file_name = "passwords.json"

        self.create_gui()
        self.load_data()

    def create_gui(self):
        tk.Label(self.root, text="Manager Haseł", font=("Arial", 16)).pack(pady=5)

        tk.Label(self.root, text="Strona / Usługa").pack()
        self.website_entry = tk.Entry(self.root, width=40)
        self.website_entry.pack()

        tk.Label(self.root, text="Login").pack()
        self.login_entry = tk.Entry(self.root, width=40)
        self.login_entry.pack()

        tk.Label(self.root, text="Hasło").pack()
        self.password_entry = tk.Entry(self.root, width=40)
        self.password_entry.pack()

        tk.Button(self.root, text="Zapisz", command=self.save_data).pack(pady=5)
        tk.Button(self.root, text="Generuj hasło", command=self.generate_password).pack(pady=5)

        self.tree = ttk.Treeview(self.root, columns=("site", "login", "password"), show="headings")
        self.tree.heading("site", text="Strona")
        self.tree.heading("login", text="Login")
        self.tree.heading("password", text="Hasło")

        self.tree.pack(fill="both", expand=True, pady=10)

    def encrypt(self, text):
        return base64.b64encode(text.encode()).decode()

    def decrypt(self, text):
        return base64.b64decode(text.encode()).decode()

    def generate_password(self):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(chars) for _ in range(12))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def save_data(self):
        website = self.website_entry.get()
        login = self.login_entry.get()
        password = self.password_entry.get()

        if not website or not login or not password:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione!")
            return

        new_data = {
            "website": website,
            "login": login,
            "password": self.encrypt(password)
        }

        data = []

        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    data = json.load(file)
            except:
                data = []

        data.append(new_data)

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

        self.website_entry.delete(0, tk.END)
        self.login_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        self.load_data()

        messagebox.showinfo("Sukces", "Zapisano dane!")

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not os.path.exists(self.file_name):
            return

        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

            for row in data:
                self.tree.insert("", "end", values=(
                    row["website"],
                    row["login"],
                    self.decrypt(row["password"])
                ))
        except:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()