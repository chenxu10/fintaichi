# How I used Taichi Language to Conquer Blackjack
我第一次体会到动态规划的美妙是在读量化金融之父爱德华索普的自传。他用动态规划征服了21点这个游戏并打败了赌场。在现实生活中，我们经常遇到固定时间和资源约束下的
选择取舍问题，小到去超市购物，大到实时广告交易市场上的投放调度问题。这些场景都是动态规划可以一展拳脚的场景。

最近在学习太极编程语言，发现它对大规模动态规划计算有很好的加速功能。我在这篇博客中做了一个经典动态规划问题0-1背包问题的Python Numpy计算与taichi计算速度的对比。

0-1背包问题是指给定约束的资源，比如最大重量``W=5``，给定货物的价值和重量比如``Val = [1,3,1]``和``Cost=[2,4,2]``，决策者只能选择装或者不装某项货物进背包。那么在这个问题中决策者能获得的最优解就是3。如果我们把货物的价值换成``[1,4,1]``其余条件没变，那么最优解就是5。在此类问题中，我们可以把背包的约束换成是预算或者时间，把货物换成投资标的价格和期望收益或者其他任何感兴趣的变量。

我们可以用``dp[i,j]``表示当我们遍历到第i个货物时还剩j个重量时的最优解。此时需要分情况讨论问题，如果第i个货物的重量已经超过还剩的j个最大允许重量时，那么答案一定是``dp[i - 1, j]``中。反之，如果第i个货物的重量还未超过还剩的j个最大允许重量时，答案必定是``dp[i - 1, j]``或``dp[i - 1, j - cost[i - 1]] + val[i - 1]``的更大值。

Python代码如下

```python
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
```

我们用太极语言加速，代码如下
```python
ti.init(arch=ti.cpu)
@ti.kernel
def knapsack_budget(
    val: ti.types.ndarray(), cost: ti.types.ndarray(), weights:ti.int16) -> ti.i32:
    ti.loop_config(serialize=True) # To forbid automatic parallelism
    for i in range(n + 1):
        for j in range(weights + 1):
            if cost[i - 1] <= j:
                choosethisknap = val[i - 1] + dp[i-1, j - cost[i - 1]]
                notchoosethisknap = dp[i - 1, j]
                dp[i,j] = max(choosethisknap, notchoosethisknap)
            else:
                dp[i,j] = dp[i - 1, j]

    return dp[n, w]
```