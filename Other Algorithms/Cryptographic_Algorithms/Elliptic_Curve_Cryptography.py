def inverse_mod(k, p):
    if k == 0:
        raise ZeroDivisionError("division by zero")
    if k < 0:
        return p - inverse_mod(-k, p)
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s % p

def ecc_add(a, b, P, Q, p):
    if P == Q:
        m = (3 * P[0] ** 2 + a) * inverse_mod(2 * P[1], p) % p
    else:
        m = (Q[1] - P[1]) * inverse_mod(Q[0] - P[0], p) % p
    x_r = (m ** 2 - P[0] - Q[0]) % p
    y_r = (m * (P[0] - x_r) - P[1]) % p
    return x_r, y_r

def ecc_mult(k, P, a, p):
    R = P
    for i in bin(k)[3:]:
        R = ecc_add(a, b, R, R, p)
        if i == '1':
            R = ecc_add(a, b, R, P, p)
    return R

if __name__ == "__main__":
    p = 17
    a = 2
    b = 2
    P = (5, 1)
    k = 2
    Q = ecc_mult(k, P, a, p)
    print(f"{k} * {P} = {Q}")
