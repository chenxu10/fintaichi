import numpy as np

N = 15000
def longestCommonSubsequence(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + (s1[i - 1] == s2[j - 1]), 
                        max(dp[i - 1][j],dp[i][j - 1]))

    return dp[-1][-1]

a_array = np.random.randint(0,100,N,dtype=np.int32)
b_array = np.random.randint(0,100,N,dtype=np.int32)

print(longestCommonSubsequence(a_array, b_array))