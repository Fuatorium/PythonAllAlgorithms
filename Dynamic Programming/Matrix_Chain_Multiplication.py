import sys

def matrix_chain_order(p, n):
    dp = [[0 for i in range(n)] for i in range(n)]
    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i+l-1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if q < dp[i][j]:
                    dp[i][j] = q
    return dp[1][n-1]

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    size = len(arr)
    print(f"Minimum number of multiplications is {matrix_chain_order(arr, size)}")
