from tkinter import Frame, Text, Scrollbar, END
from collections import defaultdict

class ResultsDisplay(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create a text widget with scrollbar
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side="right", fill="y")
        
        self.text_widget = Text(self, height=15, width=50, yscrollcommand=self.scrollbar.set)
        self.text_widget.pack(side="left", fill="both", expand=True)
        
        self.scrollbar.config(command=self.text_widget.yview)
    
    def display_results(self, sequence):
        # Clear previous results
        self.text_widget.delete(1.0, END)
        
        if not sequence:
            self.text_widget.insert(END, "No sequence found in file.")
            return
        
        alphabet = set(sequence)
        counts = defaultdict(int)
        
        for char in sequence:
            counts[char] += 1
        
        self.text_widget.insert(END, "Symbol percentages in sequence:\n\n")
        
        for symbol in sorted(alphabet):
            percentage = counts[symbol] / len(sequence) * 100
            self.text_widget.insert(END, f"{symbol}: {counts[symbol]} ({percentage:.2f}%)\n")
        
        self.text_widget.insert(END, f"\nTotal length: {len(sequence)}")