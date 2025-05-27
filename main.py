import tkinter as tk
from tkinter import filedialog
from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf_paths, output_path):
    writer = PdfWriter()
    for path in pdf_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if files:
        output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output:
            merge_pdfs(files, output)
            label.config(text="Merging completed!")

root = tk.Tk()
root.title("PDF Merger Tool")

label = tk.Label(root, text="Click to merge PDFs", padx=20, pady=10)
label.pack()

button = tk.Button(root, text="Select and Merge PDFs", command=select_files, padx=10, pady=5)
button.pack()

root.mainloop()
