# python风格的对象
# 需要解决的问题:
#   1. 如何以及何时使用@classmethod装饰器和@staticmethod装饰器
#   2. Python中私有属性和受保护属性的用法、约定和局限

# 1. 对象的表现形式
#   1. repr(): Python控制台或调试器显示对象时采用
#   2. str*(): 使用print()打印对象时采用
# 注意: Python2与Python3有所不同, Python3中__repr__、__str__和__format__都必须返回Unicode字符串(str类型), 只有__bytes__返回字节序列(bytes类型)

from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, octets):
        """
            第一个参数是类自身, 一般写为cls
        :param octets: -
        :return: -
        """
        # 从第一个字节中读取类型
        typecode = chr(octets[0])
        # 使用传入的字节序列创建一个memoryview, 然后使用typecode进行转换.
        memv = memoryview(octets[1:]).cast(typecode)
        # 拆包转换后的memoryview, 得到构造器函数所需的一对参数
        # 类似于Java中的Class.newInstance()
        return cls(*memv)

# @classmethod: 定义操作类而不是操作实例的方法.第一个参数是类本身(cls); 不管怎么调用, 第一参个参数始终是类本身
# @staticmethod: 只是改变了方法的调用方式, 第一参数没有什么特殊的. 静态方法就是普通的函数, 只是碰巧位于类的定义体中.

# 11.6 格式化显示
# 字符串格式化有三种方式:
#   1. f'{variable}'/f''{variable:format_describe}=>f'{rate:.2f}' 推荐优先使用
#   2. '{}'.format(variable) / {variable}.format(variable=value)
#   3. "xxxxxx %s xxxxxx" % (value1, value2)  非常不推荐