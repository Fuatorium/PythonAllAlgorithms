import numpy as np

def hill_cipher(text, key_matrix):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    text_vector = [ord(char) - 65 for char in text]
    text_vector = np.array(text_vector).reshape(-1, 2)
    key_matrix = np.array(key_matrix)
    result_vector = np.dot(text_vector, key_matrix) % 26
    result = ''.join(chr(int(num) + 65) for num in result_vector.flatten())
    return result

text = "HELLO WORLD"
key_matrix = [[6, 24], [1, 13]]
print(hill_cipher(text, key_matrix))  
