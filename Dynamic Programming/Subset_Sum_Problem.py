def is_subset_sum(arr, n, sum):
    dp = [[False for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][sum]

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(arr)
    if is_subset_sum(arr, n, sum) == True:
        print(f"Found a subset with given sum {sum}")
    else:
        print(f"No subset with given sum {sum}")
