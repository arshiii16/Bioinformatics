from tkinter import Tk, Frame, Button, Label, filedialog
from tkinter.ttk import Progressbar
from core.fasta_parser import read_fasta
from gui.components.results_display import ResultsDisplay
import threading

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("FASTA Analyzer")

        self.frame = Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.label = Label(self.frame, text="Select a FASTA file to analyze:")
        self.label.pack()

        self.select_button = Button(self.frame, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)

        # Progress bar
        self.progress_frame = Frame(self.frame)
        self.progress_frame.pack(pady=5, fill='x')
        
        self.progress_bar = Progressbar(self.progress_frame, mode='indeterminate', length=300)
        self.progress_label = Label(self.progress_frame, text="")
        
        self.results_display = ResultsDisplay(self.frame)
        self.results_display.pack(pady=10)

    def select_file(self):
        filename = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta;*.fa;*.fs")])
        if filename:
            # Disable button during processing
            self.select_button.config(state='disabled')
            # Show progress bar
            self.progress_label.config(text="Reading file...")
            self.progress_label.pack(side='left', padx=5)
            self.progress_bar.pack(side='left')
            self.progress_bar.start(10)
            
            # Run analysis in a separate thread to keep UI responsive
            thread = threading.Thread(target=self.analyze_file, args=(filename,))
            thread.daemon = True
            thread.start()
    
    def analyze_file(self, filename):
        try:
            sequence = read_fasta(filename)
            # Update UI in the main thread
            self.master.after(0, self.update_results, sequence)
        except Exception as e:
            self.master.after(0, self.show_error, str(e))
    
    def update_results(self, sequence):
        self.results_display.display_results(sequence)
        self.hide_progress()
    
    def show_error(self, error_msg):
        self.results_display.text_widget.delete(1.0, 'end')
        self.results_display.text_widget.insert('end', f"Error: {error_msg}")
        self.hide_progress()
    
    def hide_progress(self):
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.progress_label.pack_forget()
        self.select_button.config(state='normal')

if __name__ == "__main__":
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()