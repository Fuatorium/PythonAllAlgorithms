def rot13_cipher(text):
    def shift_char(c):
        if c.isalpha():
            shift_base = 65 if c.isupper() else 97
            return chr((ord(c) - shift_base + 13) % 26 + shift_base)
        return c

    result = "".join(shift_char(c) for c in text)
    return result

text = "Hello, World!"
print(rot13_cipher(text))  
