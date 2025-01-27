import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from docx2pdf import convert
import os
import threading

class DocToPDFConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Word to PDF Converter")
        self.window.geometry("600x400")
        self.window.configure(bg="#f0f0f0")
        
        # Variables
        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.window, bg="#f0f0f0")
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Word to PDF Converter",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0"
        )
        title_label.pack(pady=20)
        
        # Input file section
        input_frame = tk.LabelFrame(
            main_frame,
            text="Input Word File",
            bg="#f0f0f0",
            font=("Arial", 12)
        )
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.input_entry = tk.Entry(
            input_frame,
            textvariable=self.input_file,
            width=50
        )
        self.input_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        input_button = tk.Button(
            input_frame,
            text="Browse",
            command=self.browse_input,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10)
        )
        input_button.pack(side=tk.LEFT, padx=5, pady=10)
        
        # Output file section
        output_frame = tk.LabelFrame(
            main_frame,
            text="Output PDF File",
            bg="#f0f0f0",
            font=("Arial", 12)
        )
        output_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.output_entry = tk.Entry(
            output_frame,
            textvariable=self.output_file,
            width=50
        )
        self.output_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        output_button = tk.Button(
            output_frame,
            text="Browse",
            command=self.browse_output,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10)
        )
        output_button.pack(side=tk.LEFT, padx=5, pady=10)
        
        # Convert button
        self.convert_button = tk.Button(
            main_frame,
            text="Convert to PDF",
            command=self.start_conversion,
            bg="#2196F3",
            fg="white",
            font=("Arial", 12, "bold"),
            width=20,
            height=2
        )
        self.convert_button.pack(pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            main_frame,
            orient=tk.HORIZONTAL,
            length=400,
            mode='indeterminate'
        )
        self.progress.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="",
            bg="#f0f0f0",
            font=("Arial", 10)
        )
        self.status_label.pack(pady=5)
        
    def browse_input(self):
        filename = filedialog.askopenfilename(
            filetypes=[
                ("Word files", "*.docx *.doc"),
                ("All files", "*.*")
            ]
        )
        if filename:
            self.input_file.set(filename)
            # Automatically set output filename
            output_filename = os.path.splitext(filename)[0] + ".pdf"
            self.output_file.set(output_filename)
            
    def browse_output(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if filename:
            self.output_file.set(filename)
            
    def convert_file(self):
        try:
            input_file = self.input_file.get()
            output_file = self.output_file.get()
            
            if not input_file or not output_file:
                raise ValueError("Please select both input and output files")
                
            self.status_label.config(text="Converting... Please wait")
            convert(input_file, output_file)
            
            self.progress.stop()
            self.progress.pack_forget()
            self.status_label.config(text="Conversion completed successfully!")
            self.convert_button.config(state=tk.NORMAL)
            
            messagebox.showinfo("Success", "File converted successfully!")
            
        except Exception as e:
            self.progress.stop()
            self.progress.pack_forget()
            self.status_label.config(text="Conversion failed!")
            self.convert_button.config(state=tk.NORMAL)
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def start_conversion(self):
        self.convert_button.config(state=tk.DISABLED)
        self.progress.pack(pady=10)
        self.progress.start()
        
        # Run conversion in a separate thread
        thread = threading.Thread(target=self.convert_file)
        thread.daemon = True
        thread.start()
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    # First, make sure required package is installed
    try:
        import docx2pdf
    except ImportError:
        print("Installing required package: docx2pdf")
        import subprocess
        subprocess.check_call(["pip", "install", "docx2pdf"])
        
    app = DocToPDFConverter()
    app.run()
