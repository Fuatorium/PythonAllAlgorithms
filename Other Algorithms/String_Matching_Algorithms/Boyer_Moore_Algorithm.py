def bad_character_heuristic(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char

def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = bad_character_heuristic(pattern)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return -1

if __name__ == "__main__":
    text = "ABAAABCD"
    pattern = "ABC"
    result = boyer_moore_search(text, pattern)
    print(f"Pattern found at index {result}")
