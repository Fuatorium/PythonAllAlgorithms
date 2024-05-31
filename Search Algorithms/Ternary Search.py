def ternary_search(l, r, key, arr):
    if (r >= l):
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if (arr[mid1] == key):
            return mid1
        if (arr[mid2] == key):
            return mid2
        if (key < arr[mid1]):
            return ternary_search(l, mid1 - 1, key, arr)
        elif (key > arr[mid2]):
            return ternary_search(mid2 + 1, r, key, arr)
        else:
            return ternary_search(mid1 + 1, mid2 - 1, key, arr)
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = 0
    r = 9
    key = 5
    result = ternary_search(l, r, key, arr)
    if result != -1:
        print("Element found at index", result)
    else:
        print("Element not found in array")
