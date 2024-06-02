def baconian_cipher(text):
    baconian_alphabet = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB',
        'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB',
        'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB',
        'S': 'BAABA', 'T': 'BAABB', 'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB',
        'Y': 'BBAAA', 'Z': 'BBAAB'
    }

    result = ""
    for char in text.upper():
        if char.isalpha():
            result += baconian_alphabet[char]
        else:
            result += char
    return result

text = "Hello"
print(baconian_cipher(text))  
