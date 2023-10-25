# 序列的特殊方法
import operator
from array import array
import reprlib
import math
from collections import namedtuple


class Vector3d:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    # 为了迭代
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        # reprlib.repr()用于生成大型结构或递归结构的安全表示形式, 它会限制输出字符串的长度, 用'...'表示截断的部分.
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector3d({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        # isinstance()不应该大量使用, 但是在 __getitem__ 中使用它处理切片是合理的.
        if isinstance(key, slice):
            cls = type(self)
            # 通过类构造器, 使用_components 数组的切片构建一个新Vector实例
            return cls(self._components[key])
        # 如果从key中得到的是单个索引
        # operator.index()函数背后调用特殊方法 __index__.
        # operator.index()与int()之间的主要区别是, 前者只有一个用途.
        # 而且如果从key中得不到索引, 会报错TypeError
        index = operator.index(key)
        return self._components[index]

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


def can_get_len_and_index():
    v1 = Vector3d([3, 4, 5, ])
    print(len(v1))
    print(v1[0])
    print(v1[2])


def can_use_slice():
    v1 = Vector3d(range(7))
    print(v1[1:4])


# 12.4 协议和鸭子类型
# Python的序列协议只需要 __len__ 和 __getitem__ 这两个方法.

Card = namedtuple('Card', ['rank', 'suit', ])


# 重写了__len__ 和 __getitem__, 因为行为像序列, 所以它是序列.
# 这种也可以称为 鸭子类型.
# 协议是非正式的, 没有强制力. 因此如果知道类的具体使用场景, 那么通常只需要实现协议的一部分.
# 隐式的实现与Go相似, 与Java这种强类型的语言相反.
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    # can_get_len_and_index()
    can_use_slice()
