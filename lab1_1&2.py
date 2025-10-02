from collections import defaultdict

print(" ex 1")
text = 'abbabbbbabbabb'

alphabet = set()
for i in text:
    alphabet.add(i)

print(alphabet)

print(" ex 2")

seq = 'ACGGGCATATGCGC'
alphabet1 = set()
chars = {}

for i in seq:
    alphabet1.add(i)
    if i not in chars:
        chars[i] = 1
    else:
        chars[i] += 1

for i in alphabet1:
    print(f"{i}: {chars[i] / len(seq) * 100:.2f}%")

print(" ex 3")
def read_fasta(filename):
    seq = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith('>'):
                seq += line.strip()
    return seq

filename = 'your_fasta_file.fs'  # Replace with your fasta file path
sequence = read_fasta(filename)

alphabet = set(sequence)
counts = defaultdict(int)

for char in sequence:
    counts[char] += 1

print("Symbol percentages in sequence:")
for symbol in alphabet:
    print(f"{symbol}: {counts[symbol] / len(sequence) * 100:.2f}%")