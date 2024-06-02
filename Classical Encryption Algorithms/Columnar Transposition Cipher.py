def columnar_transposition_cipher(text, key):
    num_columns = len(key)
    num_rows = len(text) // num_columns + (0 if len(text) % num_columns == 0 else 1)
    matrix = ['' for _ in range(num_columns)]

    for i, char in enumerate(text):
        column = i % num_columns
        matrix[column] += char

    ordered_columns = sorted([(char, i) for i, char in enumerate(key)], key=lambda x: x[0])
    result = ''.join([matrix[col[1]] for col in ordered_columns])
    return result

text = "Hello, World!"
key = "31452"
print(columnar_transposition_cipher(text, key))  
