# Extracts all pages in a PDF and convert them to JPEG.
# You might need to run "pip install pymupdf pillow" if they're not already installed.


import fitz  # PyMuPDF
from PIL import Image
import io
import tkinter as tk
from tkinter import filedialog, messagebox

def pdf_to_jpeg(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    
    # Loop through each page
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)

        pix = page.get_pixmap()

        img_data = pix.tobytes("jpeg")

        img = Image.open(io.BytesIO(img_data))
        img.save(f"{output_folder}/page_{page_num + 1}.jpeg", "JPEG")
    
    messagebox.showinfo("Success", "PDF pages have been converted to JPEG images.")

def select_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        pdf_path_var.set(pdf_path)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_folder_var.set(output_folder)

def convert_pdf():
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()
    
    if not pdf_path or not output_folder:
        messagebox.showwarning("Warning", "Please select both PDF file and output folder.")
        return
    
    pdf_to_jpeg(pdf_path, output_folder)

# GUI
root = tk.Tk()
root.title("PDF to JPEG Converter")

pdf_path_var = tk.StringVar()
output_folder_var = tk.StringVar()

tk.Label(root, text="Select PDF File:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=pdf_path_var, width=40).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_pdf).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Select Output Folder:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=output_folder_var, width=40).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=5)

tk.Button(root, text="Convert PDF to JPEG", command=convert_pdf).grid(row=2, column=0, columnspan=3, pady=20)

root.mainloop()
