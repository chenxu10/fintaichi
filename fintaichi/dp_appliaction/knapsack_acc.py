import taichi as ti
import numpy as np

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

if __name__ == "__main__":
    val = np.array([1,3,1], dtype=np.int32)
    cost = np.array([2,4,2], dtype=np.int32)
    Weights = 5
    n = val.shape[0]
    w = Weights
    dp = ti.field(dtype=ti.i32, shape=(n + 1, Weights + 1))
    print(knapsack_budget(val, cost, Weights))
