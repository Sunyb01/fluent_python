# 带类型的具名元组
from typing import NamedTuple


class Coordinate(NamedTuple):
    """
        每个实例都要注解类型;
        与collections.namedtuple相比,唯一的区别是多了类属性__annotations__, 运行时会自动忽略掉.
        还有一点是函数可以自定义, 且后续维护也更加方便(个人感觉)
    """
    lat: float
    lon: float
    # 自定名: 类型 = 默认值
    reference: str = 'WGS84'  # 不仅指定了类型, 还指定了默认值


def ignore_type_check_on_runtime():
    """
        IDE有对应的提示, 但是运行时并没有任何报错;
        由此可见运行时不检查类型
    """
    v = Coordinate('No', None, 3)
    print(v)


class DemoPlainClass:
    """
        特殊属性__annotations__由解释器创建, 记录源码中出现的类型提示;
        如果自定没有绑定值, 那么只会作为注解存在, 而不是类属性;
        Note: 这个感觉很怪, 和java、golang都不一样
    """
    a: int
    b: float = 1.1
    c = 'spam'


def class_fields():
    print(DemoPlainClass.__annotations__)
    # 下面这一行会报错, 因为没有绑定值, 所以a只作为注解存在, 而不是类属性;
    # print(DemoPlainClass.a)
    print(DemoPlainClass.b)
    print(DemoPlainClass.c)
    x = DemoPlainClass()
    # 下面这一行也会报错, 同之前一样
    # print(x.a)

class DemoNTClass(NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'

def class_nt_fields():
    print(DemoNTClass.__annotations__)
    # 下面这一行会报错, 因为没有绑定值, 所以a只作为注解存在, 而不是类属性;
    print(DemoNTClass.a)
    print(DemoNTClass.b)
    print(DemoNTClass.c)
    print(DemoNTClass.__doc__)
    # 构造时, 必须要为没有默认值的参数提供; 否则访问时会TypeError报错
    x = DemoNTClass(8)
    print(x.a)
    print(x.b)
    print(x.c)
    # 高级元祖也是元祖, 所以可以进行重新赋值; 否则会报AttributeError错误
    # x.a = 9

if __name__ == '__main__':
    # ignore_type_check_on_runtime()
    # class_fields()
    class_nt_fields()