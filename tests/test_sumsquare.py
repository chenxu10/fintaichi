import taichi as ti
from fintaichi.inv_square import inv_square_acc

@ti.kernel
def test_inv_square() -> float:
    input = 2
    result = inv_square_acc(input)
    assert result == 0.25
    return result

