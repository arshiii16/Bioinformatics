from tkinter import Tk, Frame, Button, Label, filedialog, Text, Scrollbar
from collections import defaultdict

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

        self.results_display = Text(self.frame, wrap='word', height=15, width=50)
        self.results_display.pack(pady=5)

        self.scrollbar = Scrollbar(self.frame, command=self.results_display.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.results_display['yscrollcommand'] = self.scrollbar.set

    def select_file(self):
        filename = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta;*.fa")])
        if filename:
            self.analyze_fasta(filename)

    def analyze_fasta(self, filename):
        sequence = self.read_fasta(filename)
        if sequence:
            self.display_results(sequence)

    def read_fasta(self, filename):
        seq = ''
        with open(filename, 'r') as f:
            for line in f:
                if not line.startswith('>'):
                    seq += line.strip()
        return seq

    def display_results(self, sequence):
        alphabet = set(sequence)
        counts = defaultdict(int)

        for char in sequence:
            counts[char] += 1

        results = "Symbol percentages in sequence:\n"
        for symbol in alphabet:
            results += f"{symbol}: {counts[symbol] / len(sequence) * 100:.2f}%\n"

        self.results_display.delete(1.0, 'end')
        self.results_display.insert('end', results)

if __name__ == "__main__":
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()