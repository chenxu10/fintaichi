import taichi as ti
ti.init(arch=ti.cpu)

@ti.func
def inv_square_acc(x):
    return 1.0 / (x * x)

@ti.kernel
def my_kernel(x: ti.types.ndarray(), y: ti.types.ndarray()):
    for i in range(x.shape[0]):
        x[i] += y[i]