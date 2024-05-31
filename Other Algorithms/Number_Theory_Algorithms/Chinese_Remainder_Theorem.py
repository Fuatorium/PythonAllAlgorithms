def chinese_remainder(n, a):
    sum = 0
    prod = 1
    for ni in n:
        prod *= ni

    for ni, ai in zip(n, a):
        p = prod // ni
        sum += ai * mul_inv(p, ni) * p
    return sum % prod

def mul_inv(a, b):
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

if __name__ == "__main__":
    n = [3, 5, 7]
    a = [2, 3, 2]
    print(f"Solution of the system is {chinese_remainder(n, a)}")
