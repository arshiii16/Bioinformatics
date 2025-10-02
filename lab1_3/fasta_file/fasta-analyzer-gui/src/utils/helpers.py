def format_percentage(symbol, count, total_length):
    return f"{symbol}: {count / total_length * 100:.2f}%"

def handle_file_error(error):
    print(f"Error: {error}")