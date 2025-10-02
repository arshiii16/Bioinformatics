def read_fasta(filename):
    seq = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith('>'):
                seq += line.strip()
    return seq

def calculate_symbol_percentages(sequence):
    from collections import defaultdict
    counts = defaultdict(int)
    alphabet = set(sequence)

    for char in sequence:
        counts[char] += 1

    percentages = {symbol: counts[symbol] / len(sequence) * 100 for symbol in alphabet}
    return percentages