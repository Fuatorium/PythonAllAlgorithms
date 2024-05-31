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
    base = 2
    exp = 5
    mod = 13
    print(f"{base}^{exp} % {mod} = {mod_exp(base, exp, mod)}")
