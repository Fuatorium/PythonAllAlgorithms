def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 56
    b = 98
    print(f"GCD of {a} and {b} is {gcd(a, b)}")
