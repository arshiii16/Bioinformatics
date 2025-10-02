from tkinter import Tk, filedialog, Button, Label
from core.fasta_parser import read_fasta
from collections import defaultdict

class FileSelector:
    def __init__(self, master):
        self.master = master
        self.master.title("FASTA File Selector")
        
        self.label = Label(master, text="Select a FASTA file to analyze:")
        self.label.pack(pady=10)

        self.select_button = Button(master, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.result_label = Label(master, text="")
        self.result_label.pack(pady=10)

    def select_file(self):
        filename = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta;*.fa")])
        if filename:
            self.analyze_fasta(filename)

    def analyze_fasta(self, filename):
        sequence = read_fasta(filename)
        alphabet = set(sequence)
        counts = defaultdict(int)

        for char in sequence:
            counts[char] += 1

        result = "Symbol percentages in sequence:\n"
        for symbol in alphabet:
            percentage = counts[symbol] / len(sequence) * 100
            result += f"{symbol}: {percentage:.2f}%\n"

        self.result_label.config(text=result)