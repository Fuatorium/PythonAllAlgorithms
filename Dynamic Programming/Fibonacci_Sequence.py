def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} is {fibonacci(n)}")
