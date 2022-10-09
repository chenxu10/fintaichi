import numpy as np

def knapsack(val, cost, weights):
    n = len(val)
    dp = [[0 for _ in range(weights + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(weights + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0 
            elif cost[i - 1] <= w:
                choosethisknap = val[i - 1] + dp[i-1][w - cost[i - 1]]
                notchoosethisknap = dp[i - 1][w]
                dp[i][w] = max(choosethisknap, notchoosethisknap)
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][weights]

def test_knapsack():
    N = 3
    val = np.random.randint(0, 100, N, dtype=np.int32)
    print(val)
    cost = np.random.randint(0, 100, N, dtype=np.int32)
    print(cost)
    weights = 49
    print(knapsack(val, cost, weights))
    # assert knapsack(val, cost, weights) == 3

if __name__ == '__main__':
    test_knapsack()