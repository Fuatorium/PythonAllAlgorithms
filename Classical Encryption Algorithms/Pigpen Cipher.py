def pigpen_cipher(text):
    pigpen_dict = {
        'A': '🅰', 'B': '🅱', 'C': '🅲', 'D': '🅳', 'E': '🅴', 'F': '🅵',
        'G': '🅶', 'H': '🅷', 'I': '🅸', 'J': '🅹', 'K': '🅺', 'L': '🅻',
        'M': '🅼', 'N': '🅽', 'O': '🅾', 'P': '🅿', 'Q': '🆀', 'R': '🆁',
        'S': '🆂', 'T': '🆃', 'U': '🆄', 'V': '🆅', 'W': '🆆', 'X': '🆇',
        'Y': '🆈', 'Z': '🆉'
    }

    result = ''.join(pigpen_dict.get(char.upper(), char) for char in text)
    return result

text = "HELLO"
print(pigpen_cipher(text))  
