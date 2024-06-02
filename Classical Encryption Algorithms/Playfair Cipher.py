def generate_playfair_matrix(key):
    matrix = []
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # Remove duplicates and replace J with I
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    used_chars = set(key)
    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def playfair_cipher(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = next((r, c) for r, row in enumerate(matrix) for c, char in enumerate(row) if char == a)
        row_b, col_b = next((r, c) for r, row in enumerate(matrix) for c, char in enumerate(row) if char == b)
        if row_a == row_b:
            result += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            result += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            result += matrix[row_a][col_b] + matrix[row_b][col_a]
    return result

text = "HELLO WORLD"
key = "KEYWORD"
print(playfair_cipher(text, key))  
