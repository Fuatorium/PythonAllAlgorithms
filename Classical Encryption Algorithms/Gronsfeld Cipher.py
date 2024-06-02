def gronsfeld_cipher(text, key):
    def shift_char(c, k):
        shift_base = 65 if c.isupper() else 97
        return chr((ord(c) - shift_base + int(k)) % 26 + shift_base)

    key_length = len(key)
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            result += shift_char(char, key[i % key_length])
        else:
            result += char

    return result

text = "HELLO"
key = "314"
print(gronsfeld_cipher(text, key))  
