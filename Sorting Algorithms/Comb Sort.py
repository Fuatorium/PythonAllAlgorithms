def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

if __name__ == "__main__":
    arr = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
    comb_sort(arr)
    print("Sorted array is:", arr)
