import random

def diffie_hellman(p, g, private_key_a, private_key_b):
    public_key_a = mod_exp(g, private_key_a, p)
    public_key_b = mod_exp(g, private_key_b, p)
    shared_key_a = mod_exp(public_key_b, private_key_a, p)
    shared_key_b = mod_exp(public_key_a, private_key_b, p)
    return shared_key_a, shared_key_b

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

if __name__ == "__main__":
    p = 23
    g = 5
    private_key_a = random.randint(1, p-1)
    private_key_b = random.randint(1, p-1)
    shared_key_a, shared_key_b = diffie_hellman(p, g, private_key_a, private_key_b)
    print(f"Shared key A: {shared_key_a}")
    print(f"Shared key B: {shared_key_b}")
