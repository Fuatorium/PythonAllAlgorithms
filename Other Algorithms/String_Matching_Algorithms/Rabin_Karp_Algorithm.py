def rabin_karp(text, pattern, q=101):
    d = 256
    n = len(text)
    m = len(pattern)
    p = t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return -1

if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    result = rabin_karp(text, pattern)
    print(f"Pattern found at index {result}")
