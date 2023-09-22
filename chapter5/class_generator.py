# 类构建器
# 1. collections.namedtuple  最简单的构建方式
# 2. typing.NamedTuple  需要为字段添加类型提示
# 3. @dataclasses.dataclass  一个类装饰器, 可定制的内容更多
# 区别:
# 1. 可变实例:
#           1. collections.namedtuple和typing.NamedTuple是tuple的子类, 因此实例是不可变的;
#           2. @dataclass默认构建可变的类, 可以通过指定frozenTrue达到不可变
# 2. class语句句法:
#           只有typing.NamedTuple和dataclass支持常规的class语句句法
# 3. 构造字典:
#           两种具名字典提供了构造dict对象的实例方法(._asdict), dataclass通过(dataclasses.asdict)
# 4. 获取字段名和默认值:
#           都支持, 形式有所不同
# 5. 获取字段类型:
#           typing.NamedTuple和@dataclass支持; 推荐使用inspect.get_annotations(MyClass);
#           或typing.get_type_hints(MyClass)获取类型信息
# 6.运行时定义新类:
#           都使用默认的函数调用语句, 但是@dataclass使用make_dataclass函数



import typing
from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass


class Coordinate:
    """
        保存经纬度
    """

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


def first_data_class():
    moscow = Coordinate(55.76, 37.62)
    print(moscow)
    location = Coordinate(55.76, 37.62)
    print(location == moscow)
    print((location.lat, location.lon) == (moscow.lat, moscow.lon))


def use_namedtuple_build_data_class():
    """
        namedtuple构建的类,其实例占用的内存量与元组相同
    """
    Coordinate2 = namedtuple('Coordinate2', 'lat lon')
    print(issubclass(Coordinate2, tuple))
    moscow = Coordinate2(55.76, 37.62)
    print(moscow)
    print(moscow == Coordinate2(55.76, 37.62))


def use_typing_namedtuple_build_data_class():
    Coordinate3 = NamedTuple('Coordinate3', [('lat', float), ('lon', float), ])
    print(issubclass(Coordinate3, tuple))
    moscow = Coordinate3(55.76, 37.62)
    print(moscow)
    print(moscow == Coordinate3(55.76, 37.62))
    print(typing.get_type_hints(Coordinate3))


class Coordinate4(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        # 还可以这么写....
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


def extend_typing_namedtuple():
    moscow = Coordinate4(55.76, 37.62)
    print(moscow)
    print(issubclass(Coordinate4, typing.NamedTuple))
    print(issubclass(Coordinate4, tuple))


@dataclass(frozen=True)
class Coordinate5:
    """
        不建议直接读取__annotation__属性, 推荐使用inspect.get_annotations(MyClass) ;
        或typing.get_type_hints(MyClass)获取类型信息;
        这两个函数提供了额外的服务, 可以解析类型提示中的向前引用
    """
    lat: float
    lon: float

    def __str__(self):
        # 还可以这么写....
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


if __name__ == '__main__':
    # first_data_class()
    # use_namedtuple_build_data_class()
    # use_typing_namedtuple_build_data_class()
    extend_typing_namedtuple()
