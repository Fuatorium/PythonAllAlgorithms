def generate_adfgvx_square():
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ0123456789"
    return {char: (r, c) for r, row in enumerate(["ADFGVX"] * 6) for c, char in enumerate(row)}

def adfgvx_cipher(text, key):
    square = generate_adfgvx_square()
    polybius_text = ''.join(f"{square[char][0]}{square[char][1]}" for char in text.upper() if char in square)

    num_columns = len(key)
    num_rows = len(polybius_text) // num_columns + (0 if len(polybius_text) % num_columns == 0 else 1)
    matrix = ['' for _ in range(num_columns)]

    for i, char in enumerate(polybius_text):
        column = i % num_columns
        matrix[column] += char

    ordered_columns = sorted([(char, i) for i, char in enumerate(key)], key=lambda x: x[0])
    result = ''.join([matrix[col[1]] for col in ordered_columns])
    return result

text = "HELLO"
key = "KEY"
print(adfgvx_cipher(text, key))  
