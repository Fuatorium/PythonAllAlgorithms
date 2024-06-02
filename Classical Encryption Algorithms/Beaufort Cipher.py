def beaufort_cipher(text, key):
    def char_value(c):
        return ord(c) - 65

    key = key.upper()
    key_length = len(key)
    key_as_int = [char_value(k) for k in key]
    text_as_int = [char_value(c) for c in text.upper() if c.isalpha()]

    result = ""
    for i in range(len(text_as_int)):
        value = (key_as_int[i % key_length] - text_as_int[i]) % 26
        result += chr(value + 65)

    return result

text = "HELLO"
key = "KEY"
print(beaufort_cipher(text, key))  
