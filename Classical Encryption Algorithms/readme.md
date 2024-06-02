# Classical Encryption Algorithms

This repository contains Python implementations of various classical encryption algorithms. Each algorithm is implemented in a separate Python file and stored in the relevant folder.

## Algorithms

### Caesar Cipher (caesar_cipher.py)
A substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. It is a simple and widely known encryption technique. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

### Atbash Cipher (atbash_cipher.py)
A substitution cipher where the letters of the alphabet are reversed. 'A' becomes 'Z', 'B' becomes 'Y', etc. This cipher is a special case of the affine cipher where both a and b are equal to 25.

### Vigenère Cipher (vigenere_cipher.py)
A polyalphabetic substitution cipher that uses a keyword to determine the shift for each letter. Each letter in the keyword provides a different shift, creating a more complex and harder to break cipher compared to the Caesar cipher.

### Playfair Cipher (playfair_cipher.py)
A digraph substitution cipher that encrypts pairs of letters using a 5x5 matrix. It is designed to encrypt pairs of letters instead of single letters, making frequency analysis attacks more difficult.

### Affine Cipher (affine_cipher.py)
A substitution cipher where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter. The encryption function is of the form E(x) = (ax + b) mod m, where a and b are keys, and m is the size of the alphabet.

### Rail Fence Cipher (rail_fence_cipher.py)
A transposition cipher where the plaintext is written in a zigzag pattern on a number of 'rails' and then read line by line. It is a form of transposition cipher that derives its name from the way it is encoded.

### Columnar Transposition Cipher (columnar_transposition_cipher.py)
A transposition cipher that involves writing the plaintext out in rows and then reading the ciphertext off in columns one by one. The order of the columns is determined by a keyword.

### Baconian Cipher (baconian_cipher.py)
A substitution cipher in which each letter is replaced by a sequence of five characters consisting of 'A' or 'B'. This cipher can encode messages in various ways, including binary form, to hide the message within other text.

### Scytale Cipher (scytale_cipher.py)
An ancient transposition cipher where a strip of parchment is wound around a cylinder and the message is written along the length of the cylinder. When unwound, the message is scrambled, and can only be read when rewrapped around a cylinder of the same diameter.

### Keyword Cipher (keyword_cipher.py)
A monoalphabetic substitution cipher where a keyword determines the substitution of letters. The keyword is written at the beginning of the ciphertext alphabet, followed by the remaining letters in the alphabet in their usual order.

### Beaufort Cipher (beaufort_cipher.py)
A polyalphabetic substitution cipher similar to the Vigenère cipher but with a slightly different method for encryption. It uses the Beaufort square and the encryption process is reciprocal, meaning the same process is used for both encryption and decryption.

### Gronsfeld Cipher (gronsfeld_cipher.py)
A polyalphabetic substitution cipher very similar to the Vigenère cipher but uses digits (0-9) instead of letters in the key. It is a variant of the Vigenère cipher and uses numerical keys to encrypt the text.

### Four-Square Cipher (four_square_cipher.py)
Uses four 5x5 matrices arranged in a square to encrypt digraphs (pairs of letters). It employs the use of two keyed Polybius squares along with two standard Polybius squares to achieve encryption.

### ADFGVX Cipher (adfgvx_cipher.py)
Uses a combination of a Polybius square and a columnar transposition. It was used by the German Army during World War I. The name comes from the six possible letters used in the ciphertext: A, D, F, G, V, and X.

### Bifid Cipher (bifid_cipher.py)
Combines the Polybius square with transposition to achieve diffusion. It is a combination of substitution and transposition, providing a more secure encryption by spreading the information from the plaintext throughout the ciphertext.

### ROT13 Cipher (rot13_cipher.py)
A special case of the Caesar cipher where the shift is 13. It is commonly used in forums and online to obscure text, providing a simple means of obfuscation that can be easily reversed.

### Morse Code (morse_code.py)
A method used in telecommunication to encode text characters as sequences of dots and dashes. It is a widely recognized and used method for transmitting text information through on-off signals, beeps, or flashes.

### Pigpen Cipher (pigpen_cipher.py)
A simple substitution cipher that exchanges letters for symbols based on a grid pattern. It is also known as the masonic cipher and uses a grid to define the substitution alphabet.

## How to Run

To run any of the algorithms, simply navigate to the relevant folder and execute the Python file. For example, to run the Caesar Cipher algorithm:

```sh
python caesar_cipher.py
