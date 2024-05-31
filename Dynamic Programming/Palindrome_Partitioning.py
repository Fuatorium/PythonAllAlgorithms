import sys

def min_palindrome_partitions(str):
    n = len(str)
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i+L-1
            if str[i] == str[j] and L == 2:
                dp[i][j] = 0
            elif str[i] == str[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = sys.maxsize
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1)
    return dp[0][n-1]

if __name__ == "__main__":
    str = "ababbbabbababa"
    print(f"Min cuts needed for Palindrome Partitioning is {min_palindrome_partitions(str)}")
