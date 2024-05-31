import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def generate_keypair(p, g):
    n = p * g
    phi = (p - 1) * (g - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = mod_inv(e, phi)
    return ((e, n), (d, n))

def mod_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [mod_exp(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(mod_exp(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == "__main__":
    p = 61
    g = 53
    public, private = generate_keypair(p, g)
    message = "HELLO"
    encrypted_msg = encrypt(public, message)
    print(f"Encrypted message: {encrypted_msg}")
    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")
