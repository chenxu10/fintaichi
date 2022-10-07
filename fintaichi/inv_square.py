import taichi as ti
ti.init(arch=ti.cpu)

@ti.func
def inv_square_acc(x):
    return 1.0 / (x * x)

@ti.kernel
def partial_sum(x:int):
    print(x)

if __name__ == '__main__':
    partial_sum(1)
