# 序列的特殊方法
import itertools
import operator
from array import array
import reprlib
import math
from collections import namedtuple
import functools
from itertools import zip_longest


# 如果实现了__getattr__ , 那么请一定也要重新定义 __setattr__方法, 以防止对象行为的不一致.
class Vector3d:
    typecode = 'd'
    __match__args__ = ('x', 'y', 'z', 't')

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
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        # if len(self) != len(other):
        #     return False
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        # return True

    def __hash__(self):
        # 这里也可以使用map()函数, 其在Python2和Python3中的表现并不相同.
        # Python3中是惰性的, 会创建一个生成器, 按需产出结果.
        hashes = (hash(x) for x in self._components)
        # 使用3个参数的方法, 可以避免出现异常: TypeError: reduce() of empty sequence with no initial value
        # 对于+、| 、^来说, 第三个参数应该为0
        # 对于* 和& 来说应该为1
        return functools.reduce(operator.xor(), hashes, 0)

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

    def __getattr__(self, name):
        """
            属性检查失败后, 解释器会调用 __getattr__ 方法.
            简单来说, 对于my_obj.x表达式, Python会检查my_obj实例有没有名为x的属性.
            如果没有, 就到类(my_obj.__class__)中查找;
            如果还没有就沿着集成图继续向上查找;
            如果依旧找不到, 则调用my_obj所属的类中定义的 __getattr__ 方法, 传入self和属性名称的字符串形式(例如'x').
        :param name: -
        :return: -
        """
        cls = type(self)
        try:
            pos = cls.__match__args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    def __setattr__(self, key, value):
        """
            在未定义此方法之前. 存在一个问题.
            如v = Vector3d(range(5))
            如果是进行了v.x = 10, 然后print(v.x)会输出10;
            但是当print(v)时, 会发现打印的结果与预期的不一致.
            这是因为v.x会在v中新增一个和_components同级别的属性'x', 因此使用v.x获取x的属性的值时不会再调用__getattr__方法, 解释器会直接返回v.x绑定的值.
            注意: 请不要随意使用__slots__进行防止新属性的设置. __slots__ 只应该用于节省内存, 而且仅当内存严重不足时才应该这么做.
        :param key: -
        :param value: -
        :return: -
        """
        cls = type(self)
        if len(key) == 1:
            if key in cls.__match__args__:
                # 这些提示词是原作者参考了complex函数后明确的.
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls.__name__, attr_name=key)
                raise AttributeError(msg)
            # 因为Python支持多继承, 因此super()这个方法经常用于把子类方法的某些任务委托给超类中适当的方法.
            super().__setattr__(key, value)

    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

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


def zip_func_test():
    print(zip(range(3), 'ABC'))
    print(list(zip(range(3), 'ABC')))
    print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3, ])))
    print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3, ], fillvalue=-1)))


if __name__ == '__main__':
    # can_get_len_and_index()
    # can_use_slice()
    zip_func_test()
