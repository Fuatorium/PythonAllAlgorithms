def coin_change(coins, m, V):
    dp = [0 for i in range(V+1)]
    dp[0] = 1
    for i in range(0, m):
        for j in range(coins[i], V+1):
            dp[j] += dp[j-coins[i]]
    return dp[V]

if __name__ == "__main__":
    coins = [1, 2, 3]
    m = len(coins)
    V = 4
    print(f"Number of ways to get {V} using coins is {coin_change(coins, m, V)}")
