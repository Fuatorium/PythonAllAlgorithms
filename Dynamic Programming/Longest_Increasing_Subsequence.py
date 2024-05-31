def lis(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j]+1
    return max(dp)

if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(f"Length of LIS is {lis(arr)}")
