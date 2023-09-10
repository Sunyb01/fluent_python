# 向量2

import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 与此方法对照的是__str__()方法, 在python中__repr__()方法优先级高于__str__()
    def __repr__(self):
        # 3. f'{variable}' 这是python3的写法; 其中!r表示以标准的形式显示属性
        # 1. '{}{}'.format(var1, var2)
        # 2. 'hello, {obj} ,i am {name}'.format(obj = obj,name = name)
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v = Vector(3, 4)
    print(v)
