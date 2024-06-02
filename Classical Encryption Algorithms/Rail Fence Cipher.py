def rail_fence_cipher(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0

    for char in text:
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1

    result = []
    for i in range(key):
        result.extend([rail[i][j] for j in range(len(text)) if rail[i][j] != '\n'])
    return "".join(result)

text = "Hello, World!"
key = 3
print(rail_fence_cipher(text, key))  
