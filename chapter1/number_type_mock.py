# 数字类型模拟
import numpy
from fontTools.misc.vector import Vector

if __name__ == '__main__':
    v1 = Vector((2, 4))
    v2 = Vector((2, 1))
    print(v1 + v2)
    v = Vector((3, 4))
    print(abs(v))
    print(v * 3)
    print(abs(v * 3))