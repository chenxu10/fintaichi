import taichi as ti
ti.init(arch=ti.cpu)

a = ti.Vector([1.0,2.0])
print(a)
b = ti.Matrix([[1.0,2.0]])
print(b[0])

heat_field = ti.field(dtype=ti.f32, shape=(256,256))