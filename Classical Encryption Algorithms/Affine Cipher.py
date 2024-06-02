def affine_cipher(text, a, b):
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = (a * (ord(char) - shift_base) + b) % 26
            result += chr(encrypted_char + shift_base)
        else:
            result += char
    return result

text = "Hello, World!"
a = 5
b = 8
print(affine_cipher(text, a, b))  
