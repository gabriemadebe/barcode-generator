import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk, Image
import barcode
from barcode.writer import ImageWriter
import os

BARCODE_TYPES = ['code128', 'code39', 'ean8', 'ean13', 'isbn13', 'upc']

def generate_barcode():
    number = entry_number.get()
    b_type = combo_barcode.get()

    if not number or not b_type:
        messagebox.showwarning("Warning", "number and barcode type.")
        return

    try:
        BarcodeClass = barcode.get_barcode_class(b_type)
        barcode_obj = BarcodeClass(number, writer=ImageWriter())

        # Chagua mahali pa kuhifadha
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_path:
            return

        barcode_obj.save(file_path.replace(".png", ""))  # Usiongeze .png mara mbili

        # Onyesha barcode preview
        show_preview(file_path)
        messagebox.showinfo("Success", f"Barcode saved:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_preview(path):
    img = Image.open(path)
    img = img.resize((300, 100), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    barcode_label.config(image=img_tk)
    barcode_label.image = img_tk

# GUI Setup
root = tk.Tk()
root.title("📦 Barcode Generator by Gabriel Madebe")
root.geometry("400x300")

tk.Label(root, text="Enter Number:").pack(pady=5)
entry_number = tk.Entry(root, width=30)
entry_number.pack(pady=5)

tk.Label(root, text="Choose Barcode Type:").pack(pady=5)
combo_barcode = ttk.Combobox(root, values=BARCODE_TYPES, state="readonly")
combo_barcode.pack(pady=5)
combo_barcode.set("code128")

tk.Button(root, text="Generate Barcode", command=generate_barcode).pack(pady=10)
barcode_label = tk.Label(root)
barcode_label.pack(pady=10)

root.mainloop()
