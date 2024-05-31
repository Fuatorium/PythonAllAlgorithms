def interpolation_search(arr, n, x):
    lo = 0
    hi = (n - 1)
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1

if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    n = len(arr)
    x = 18
    result = interpolation_search(arr, n, x)
    if result != -1:
        print("Element found at index", result)
    else:
        print("Element not found in array")
