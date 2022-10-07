


def knapsack(val, cost, weights):
    n = len(val)
    dp = [[0 for _ in range(weights + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(weights + 1):
            if cost[i - 1] <= w:
                choosethisknap = val[i - 1] + dp[i-1][w - cost[i - 1]]
                notchoosethisknap = dp[i - 1][w]
                dp[i][w] = max(choosethisknap, notchoosethisknap)
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[-1][-1]

def test_knapsack():
    val = [1,3,1]
    cost = [2,4,2]
    weights = 5
    print(knapsack(val, cost, weights))
    assert knapsack(val, cost, weights) == 3

