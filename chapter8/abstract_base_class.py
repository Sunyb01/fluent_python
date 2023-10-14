# 抽象基类
from collections.abc import Mapping, Sequence, Iterable as ITE, Hashable
from collections import Counter
from decimal import Decimal
from random import shuffle
from typing import Iterable
# 显示使用TypeAlias
from typing import TypeAlias, TypeVar

FromTo: TypeAlias = tuple[str, str]

# 发送时要保守, 接收时要大方;
"""
    由于类型注解为abc.Mapping, 因此调用方可以提供dict、defaultdict、ChainMap的实例, UserDict子类的实例, 或者Mapping的任何子类型
    但是注解为dict的, 必须是dict或其子类型; 如defaultDict或OrderedDict; 注意使用collections.UserDict的子类型无法通过类型检查;
    UserDict和dict是同级关系, 都是abc.MutableMapping的子类;
    一般来说在参数的类型提示中最好使用abc.Mapping或abc.MutableMapping
"""


def name2hex(name: str, color_map: Mapping[str, int]) -> str:
    pass


def name2hex2(name: str, color_map: dict[str, int]) -> str:
    pass


# Iterable 可迭代对象
def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text


def use_iterable():
    l33t = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'), ]
    text = 'mad skilled noob powned leet'
    print(zip_replace(text, l33t))


# 参数化泛型和TypeVar
T = TypeVar('T')


def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError('size must be >= 1')
    result = list(population)
    shuffle(result)
    return result[:size]


# 1. 受限的TypeVar
# 第一个参数为类型参数的名称, 类似于Java中的T,E等泛型词. 后面为其支持的范围;
# 写法与Golang中的相似, Go中的泛型为VarName[T type1 | type2 | type3, E type4]
NumberT = TypeVar('NumberT', float, int, Decimal)


def mode(data: ITE[NumberT]) -> NumberT:
    pass


# 有界的TypeVar
# 第一个参数为类型参数的名称, 类似于Java中的T,E等泛型词
# 第二个参数为其上边界, 此处为Hashable或其子类;
# 类似于Java中的<T extend Type_Class>
HashableT = TypeVar('HashableT', bound=Hashable)


def mode2(data: ITE[HashableT]) -> HashableT:
    pass


# 预定义的类型变量AnyStr
# type模块提供了一个预定义的类型变量, AnyStr;
# 接收btyes或str, 返回值也是这两个中的一个;


if __name__ == '__main__':
    use_iterable()
