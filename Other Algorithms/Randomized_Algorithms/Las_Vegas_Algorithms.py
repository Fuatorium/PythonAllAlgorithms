import random

def las_vegas_quickselect(arr, k):
    while True:
        pivot = random.choice(arr)
        lows = [el for el in arr if el < pivot]
        highs = [el for el in arr if el > pivot]
        pivots = [el for el in arr if el == pivot]
        if k < len(lows):
            arr = lows
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            arr = highs
            k -= len(lows) + len(pivots)

if __name__ == "__main__":
    arr = [3, 6, 2, 1, 7, 4, 5]
    k = 3
    print(f"{k}th smallest element is {las_vegas_quickselect(arr, k)}")
