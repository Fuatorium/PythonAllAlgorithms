def polyalphabetic_cipher(text, key):
    result = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        if text[i].isalpha():
            shift_base = 65 if text[i].isupper() else 97
            value = (text_as_int[i] - shift_base + key_as_int[i % key_length] - shift_base) % 26
            result += chr(value + shift_base)
        else:
            result += text[i]
    return result

text = "Hello, World!"
key = "ABC"
print(polyalphabetic_cipher(text, key))  
