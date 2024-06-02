def keyword_cipher(text, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_alphabet = "".join(sorted(set(keyword.upper()), key=keyword.index))
    remaining_letters = ''.join([char for char in alphabet if char not in key_alphabet])
    substitution_alphabet = key_alphabet + remaining_letters

    result = ""
    for char in text.upper():
        if char.isalpha():
            result += substitution_alphabet[alphabet.index(char)]
        else:
            result += char
    return result

text = "Hello, World!"
keyword = "KEYWORD"
print(keyword_cipher(text, keyword))  
