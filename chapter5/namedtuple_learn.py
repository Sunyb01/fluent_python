# 典型的具名元组
import json
from collections import namedtuple


def define_namedtuple():
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo[1])
    print(City._fields)


def define_namedtuple2():
    City = namedtuple('City', 'name country population coordinates')
    print(City._fields)
    Coordinate = namedtuple('Coordinate', 'lat lon')
    delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.444, 77.2222))
    # 根据可迭代对象构建实例
    delhi = City._make(delhi_data)
    # 返回根据具名元组实例构建的dict对象
    print(delhi._asdict())
    # 可把数据序列化成JSON格式
    # 3.7之前返回OrderDict, 3.8之后就返回dict了
    print(json.dumps(delhi._asdict()))

def special_default_value():
    """
       还可以通过注入的方式向实例提供函数;
       如 Coordinate.new_func = target_func
    """
    Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
    v = Coordinate(0, 0)
    print(v)
    print(v._field_defaults)


if __name__ == '__main__':
    # define_namedtuple()
    # define_namedtuple2()
    special_default_value()