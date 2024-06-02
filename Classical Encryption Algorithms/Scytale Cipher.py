def scytale_cipher(text, key):
    num_rows = len(text) // key + (0 if len(text) % key == 0 else 1)
    matrix = [['' for _ in range(key)] for _ in range(num_rows)]

    for i, char in enumerate(text):
        row, col = i // key, i % key
        matrix[row][col] = char

    result = ''.join([''.join(row) for row in matrix])
    return result

text = "Hello, World!"
key = 5
print(scytale_cipher(text, key))  