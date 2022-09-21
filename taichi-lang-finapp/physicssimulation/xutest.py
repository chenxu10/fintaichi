import taichi as ti
ti.init(arch=ti.metal)

n = 512
pixels = ti

# open a blanket huabu
pixels = ti.Vector.field(3, dtype=ti.f32, shape=(n,n))
gui = ti.GUI("xushenzuoye", (n,n))

# 灰色的斜杠
# random, 出现一个白噪声
# Use t to make it move
# Use block size to make the square appears

@ti.func
def frac(x):
    return x - ti.floor(x)

@ti.kernel
def paint(t:ti.f32):
    for i_, j_ in pixels:
        #c = (i + j) % 100/100
        c = 0.0
        levels = 7
        for k in range(levels):
            block_size = 2 * 2 ** k
            i = i_ + t 
            j = j_ + t
            p = i % block_size / block_size
            q = j % block_size / block_size
            i = i // block_size
            j = j // block_size
            #brightness = 1 - max(abs(p-0.5),abs(q-0.5))
            brightness = (0.7 - ti.Vector([p - 0.5, q - 0.5]).norm()) * 2
            weight = 0.5 ** (levels - k - 1) * brightness
            c += frac(ti.sin(float(i * 8 + j * 42 + t * 1e-4)) * 128) * (1/levels) * weight
        # color
        # c *= 0.7
        pixels[i_, j_] = ti.Vector([c,c * 1.2,c * 0.9])

# open a black window
t = 0
while True:
    t += 0.05
    paint(t)
    gui.set_image(pixels)
    gui.show()