def rod_cut(price, n):
    dp = [0 for x in range(n+1)]
    for i in range(1, n+1):
        max_val = -1
        for j in range(i):
            max_val = max(max_val, price[j] + dp[i-j-1])
        dp[i] = max_val
    return dp[n]

if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print(f"Maximum obtainable value is {rod_cut(arr, size)}")
