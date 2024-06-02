def generate_four_square_matrices(key1, key2):
    def create_matrix(key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = ""
        for char in key.upper():
            if char not in matrix and char in alphabet:
                matrix += char
        for char in alphabet:
            if char not in matrix:
                matrix += char
        return matrix

    matrix1 = create_matrix(key1)
    matrix2 = create_matrix(key2)
    alphabet_matrix = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    return alphabet_matrix, matrix1, matrix2, alphabet_matrix

def four_square_cipher(text, key1, key2):
    matrix_a, matrix_b, matrix_c, matrix_d = generate_four_square_matrices(key1, key2)
    text = text.replace("J", "I").upper()
    if len(text) % 2 != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = divmod(matrix_a.index(a), 5)
        row_b, col_b = divmod(matrix_d.index(b), 5)
        result += matrix_b[row_a * 5 + col_b] + matrix_c[row_b * 5 + col_a]

    return result

text = "HELLO"
key1 = "KEYWORD1"
key2 = "KEYWORD2"
print(four_square_cipher(text, key1, key2))  
