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


# 当应用程序真正需要这些特殊方法时才应实现它们.
# 当前这个类知识一个特例, 不是每个用户定义的类都需要这样做.
class Vector2d:
    typecode = 'd'

    # 如果一个类的__init__方法可能有全都赋值给实例属性的必需的参数和可选参数, __match__args__应当列出必需的参数, 而不必列出可选的参数. 类似于Java中只提供了一个有参的构造函数.
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    # 通过上面的__前缀使其不可读, 然后通过@property与函数定义只读属性
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # 支持hash
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

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
#   4. 格式化方法format(value, 'format_spec')
# 如时间格式化 format(now, '%H:%M:%S') / '{:%I:%M %p}'.format(now)
# 如果一个类没有定义__format__方法, 那么该方法就会从object继承, 并返回str(my_object)

# 11.8 支持位置模式匹配
def keyword_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(0, 0):
            print(f'{v!r} is null')
        case Vector2d(0):
            print(f'{v!r} is vertical')
        case Vector2d(_, 0):
            print(f'{v!r} is horizontal')
        case Vector2d(x, y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')


# 11.10 私有属性和"受保护"的属性
# Python不能像Java那样使用private修饰符创建私有属性, 但是它有一个简单的机制, 能避免子类意外覆盖私有属性 -> 名称改写
# 如Dog中定义了一个属性, __mood, 那么Python会把属性名存入实例属性__dict__中, 而且会在前面加一个下划线和类名.
# 因此对于Dog类来说, __mood属性会变成_Dog__mood
# 名称改写是一种安全措施, 不能保证万无一失; 目的是避免意外访问, 不能防止故意做错事.
# 注意:
#   1. Python不会对使用单下划线的属性名做特殊处理. 单下划线这种写法是一种Python程序员的通用约定, 他们不会在类的外部访问这种属性.(也有人称之为私有属性而不是受保护的属性)
#   2. 在模块中, 如果顶层名称使用一个前导下划线, 那么会对导入有影响. 如form mymod import * , 将不会导入前缀为一个下划线的名称. 除非显示的使用 -> form mymod import _xxxx
def print_private_var(v: Vector2d):
    print(v.__dict__)
    # 只要知道改写私有属性名称的机制, 任何人都能直接读取私有属性(对于调试和序列化很有用).
    print(v._Vector2d__x)


if __name__ == '__main__':
    # keyword_pattern_demo(Vector2d(x=0, y=0))
    print_private_var(Vector2d(x=0, y=0))
