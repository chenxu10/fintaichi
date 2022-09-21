import taichi as ti
ti.init()
n = 512
gui = ti.GUI("xudemo", (n,n))
pixels = ti.Vector.field(n=3, dtype=ti.f32, shape=(n,n))

@ti.kernel
def paint():
    for i, j in pixels:
        # c = (i + j) % 100 / 100
        c = ti.random()
        pixels[i, j] = ti.Vector([c,c,c])

t = 0
while True:
    t += 0.01
    paint()
    gui.set_image(pixels)
    gui.show()