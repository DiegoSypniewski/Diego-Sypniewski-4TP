import tkinter as tk

def na_najechaniu(event):
    status_panel.config(bg="yellow")
    status_panel.config(text="UZBROJENIE MOŻLIWE")

def na_kliknieciu(event):
    status_panel.config(bg="red")
    status_panel.config(text="SYSTEM UZBROJONY")

def na_opuszczeniu(event):
    status_panel.config(bg="green")
    status_panel.config(text="SYSTEM ROZBROJONY")

root = tk.Tk()
root.title("Panel Alarmowy")
root.geometry("350x150")

status_panel = tk.Label(
    root,
    text="SYSTEM ROZBROJONY",
    bg="green",
    fg="white",
    font=('Arial', 16, 'bold'),
    width=25,
    height=3
)
status_panel.pack(padx=20, pady=20)

# Powiązanie zdarzeń
status_panel.bind('<Enter>', na_najechaniu)
status_panel.bind('<Leave>', na_opuszczeniu)
status_panel.bind('<Button-1>', na_kliknieciu)

root.mainloop()