import customtkinter as ctk
import json
import os
from tkinter import filedialog
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime

SETTINGS_FILE = "settings.json"

# -----------------------------
# Wczytywanie ustawień
# -----------------------------
def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return {"theme": "Dark"}


def save_settings(theme):
    with open(SETTINGS_FILE, "w") as f:
        json.dump({"theme": theme}, f)


settings = load_settings()

ctk.set_appearance_mode(settings["theme"])
ctk.set_default_color_theme("blue")

# -----------------------------
# Generowanie PDF
# -----------------------------
def generate_pdf():

    produkt = entry_product.get()
    cena = entry_price.get()
    vat = entry_vat.get()

    try:
        cena = float(cena)
        vat = float(vat)
    except:
        textbox.insert("end", "\nBląd danych\n")
        return

    vat_value = (cena * vat) / 100
    brutto = cena + vat_value

    path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF", "*.pdf")]
    )

    if not path:
        return

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("FAKTURA UPROSZCZONA", styles['Title'])
    date = Paragraph(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal'])

    elements.append(title)
    elements.append(Spacer(1,20))
    elements.append(date)
    elements.append(Spacer(1,30))

    data = [
        ["Produkt", "Cena Netto", "VAT %", "VAT", "Brutto"],
        [produkt, f"{cena:.2f} zl", f"{vat}%", f"{vat_value:.2f} zl", f"{brutto:.2f} zl"]
    ]

    table = Table(data, colWidths=[120,100,80,100,100])

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.darkblue),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("ALIGN",(1,1),(-1,-1),"CENTER"),
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")
    ]))

    elements.append(table)
    elements.append(Spacer(1,40))

    summary = Paragraph(f"<b>Do zaplaty: {brutto:.2f} zl</b>", styles['Heading2'])
    elements.append(summary)

    doc = SimpleDocTemplate(path, pagesize=A4)
    doc.build(elements)

    textbox.insert("end", f"\nPDF zapisany: {path}\n")


# -----------------------------
# Zmiana motywu
# -----------------------------
def change_theme(theme):
    ctk.set_appearance_mode(theme)
    save_settings(theme)


# -----------------------------
# GUI
# -----------------------------
app = ctk.CTk()
app.title("Professional Settings Manager + PDF Generator")
app.geometry("900x500")

# Sidebar
sidebar = ctk.CTkFrame(app, width=200)
sidebar.pack(side="left", fill="y")

title = ctk.CTkLabel(sidebar, text="Ustawienia", font=("Arial",18))
title.pack(pady=20)

btn_dark = ctk.CTkButton(
    sidebar,
    text="Dark Mode",
    command=lambda: change_theme("Dark")
)
btn_dark.pack(pady=10)

btn_light = ctk.CTkButton(
    sidebar,
    text="Light Mode",
    command=lambda: change_theme("Light")
)
btn_light.pack(pady=10)

# Main frame
main = ctk.CTkFrame(app)
main.pack(side="right", expand=True, fill="both", padx=20, pady=20)

label = ctk.CTkLabel(main, text="Generator Faktury PDF", font=("Arial",20))
label.pack(pady=10)

entry_product = ctk.CTkEntry(main, placeholder_text="Nazwa produktu")
entry_product.pack(pady=10)

entry_price = ctk.CTkEntry(main, placeholder_text="Cena netto")
entry_price.pack(pady=10)

entry_vat = ctk.CTkEntry(main, placeholder_text="VAT (%)")
entry_vat.pack(pady=10)

checkbox = ctk.CTkCheckBox(main, text="Potwierdzam poprawność danych")
checkbox.pack(pady=10)

btn_pdf = ctk.CTkButton(
    main,
    text="Generuj PDF",
    command=generate_pdf
)
btn_pdf.pack(pady=20)

textbox = ctk.CTkTextbox(main, width=400, height=120)
textbox.pack(pady=10)

app.mainloop()