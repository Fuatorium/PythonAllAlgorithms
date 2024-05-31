def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

if __name__ == "__main__":
    text = "hello world"
    pattern = "world"
    result = brute_force_string_match(text, pattern)
    print(f"Pattern found at index {result}")
