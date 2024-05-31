def egg_drop(n, k):
    dp = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = 1
        dp[i][0] = 0
    for j in range(1, k+1):
        dp[1][j] = j
    for i in range(2, n+1):
        for j in range(2, k+1):
            dp[i][j] = float('inf')
            for x in range(1, j+1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                if res < dp[i][j]:
                    dp[i][j] = res
    return dp[n][k]

if __name__ == "__main__":
    n = 2
    k = 36
    print(f"Minimum number of trials in worst case with {n} eggs and {k} floors is {egg_drop(n, k)}")
