def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr(shift_base + (25 - (ord(char) - shift_base)))
        else:
            result += char
    return result

text = "Hello, World!"
print(atbash_cipher(text))  
