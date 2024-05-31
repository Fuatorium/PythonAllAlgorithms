class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = 0

def knapsack_branch_and_bound(W, wt, val, n):
    Q = []
    u = Node(-1, 0, 0)
    v = Node(0, 0, 0)
    Q.append(u)
    max_profit = 0
    while Q:
        u = Q.pop(0)
        if u.level == -1:
            v.level = 0
        if u.level == n - 1:
            continue
        v.level = u.level + 1
        v.weight = u.weight + wt[v.level]
        v.profit = u.profit + val[v.level]
        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit
        v.bound = bound(v, n, W, wt, val)
        if v.bound > max_profit:
            Q.append(v)
        v = Node(v.level, u.profit, u.weight)
        v.bound = bound(v, n, W, wt, val)
        if v.bound > max_profit:
            Q.append(v)
    return max_profit

def bound(u, n, W, wt, val):
    if u.weight >= W:
        return 0
    profit_bound = u.profit
    j = u.level + 1
    totweight = u.weight
    while j < n and totweight + wt[j] <= W:
        totweight += wt[j]
        profit_bound += val[j]
        j += 1
    if j < n:
        profit_bound += (W - totweight) * val[j] / wt[j]
    return profit_bound

if __name__ == "__main__":
    W = 10
    val = [10, 10, 12, 18]
    wt = [2, 4, 6, 9]
    n = len(val)
    max_profit = knapsack_branch_and_bound(W, wt, val, n)
    print(f"Maximum profit is {max_profit}")
