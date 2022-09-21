import taichi as ti
import numpy as np
ti.init(arch=ti.cpu)

benchmark = True
N = 15000

f = ti.field(dtype=ti.i32,shape=(N + 1, N + 1))

if benchmark:
    a_array = np.random.randint(0,100,N,dtype=np.int32)
    b_array = np.random.randint(0,100,N,dtype=np.int32)
else:
    a_array = np.array([0,1,2,3,4,5])
    b_array = np.array([1,2,3,4,5,0])

@ti.kernel
def longestCommonSubsequence(s1: ti.types.ndarray(), s2: ti.types.ndarray()) -> ti.i32:
    n = s1.shape[0]
    m = s2.shape[0]

    ti.loop_config(serialize=True)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[n, m] = max(f[i - 1, j - 1] + (s1[i - 1] == s2[j - 1]), 
                        max(f[i - 1, j],f[i, j - 1]))

    return f[n,m]

print(longestCommonSubsequence(a_array, b_array))
