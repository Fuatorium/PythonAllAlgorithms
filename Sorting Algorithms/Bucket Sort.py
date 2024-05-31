def insertion_sort_for_bucket(arr):
    for i in range(1, len(arr)):
        up = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > up:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = up
    return arr

def bucket_sort(arr):
    bucket = []
    slot_num = 10
    for i in range(slot_num):
        bucket.append([])

    for j in arr:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)

    for i in range(slot_num):
        bucket[i] = insertion_sort_for_bucket(bucket[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

if __name__ == "__main__":
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    bucket_sort(arr)
    print("Sorted array is:", arr)
