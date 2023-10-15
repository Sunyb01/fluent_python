# 静态协议
# Protocol类型类似于Go中的接口, 定义协议类型时指定一个活多个方法,
# 在需要使用协议类型的地方,类型检查工具会核查有没有实现指定的方法;
# 与Go一样, 与接口不需要建立任何关系, 如显示的继承与注册;

from typing import Protocol, TypeVar, Any
from collections.abc import Iterable

# 这相当于是Any, 前提是这个Any必须是可排序的
T = TypeVar('T')


def top_n(series: Iterable[T], length: int) -> list[T]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


def non_sort_key():
    objs = [object() for _ in range(4)]
    try:
        top_n(objs, 2)
    except TypeError as te:
        print('Has Error, ErrorMsg is ', te)


# 暂时还是有些问题,
class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        return False


LT = TypeVar('LT', bound=SupportsLessThan)


def top_n_2(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


# 方法会报错, raise TypeError('Protocols cannot be instantiated')
def non_sort_key2():
    objs = [SupportsLessThan() for _ in range(4)]
    try:
        top_n(objs, 2)
    except TypeError as te:
        print('Has Error, ErrorMsg is ', te)


if __name__ == '__main__':
    # numbers = [4, 1, 5, 2, 6, 7, 3, ]
    # print(top_n(numbers, 3))
    # fruits = 'mango pear apple kiwi banana'.split()
    # print(top_n(fruits, 3))
    # fruits2 = [(len(s), s) for s in fruits]
    # print(top_n(fruits2, 3))
    # non_sort_key()
    non_sort_key2()
