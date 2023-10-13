# 注解中可用的类型
from typing import Any, Union, NamedTuple
from geolib import geohash as gh
from collections import Sequence


# 1. Any类型
def double_method(x):
    return x * 2


def double_for_any(x: Any) -> Any:
    return x * 2


# Mypy等类型检查工具拒绝以下函数
def double_for_object(x: object) -> object:
    return x * 2


# 2. 简单的类型与类
# 向int、float、str和bytes这样的简单的类型可以直接在类型提示中使用;
# int与float相容, float与complex相容; 他们都是boject的直接子类, 但各自直接却没有关系;

# 3. Optional与Union类型
# 文件 type_hints_for_function.py 中的方法show_count3()中 plural: Optional[str] = None, 也可以写成 plural: Union[str, None]
# Optional[str]结构其实是Union[str, None]的简写形式
# 自3.10版本开始可以使用新的写法:
# (旧) plural: Optional[str] = None
# (新) plural: str | None = None
# 嵌套的Union与扁平化的Union是等效的; 如Union[A, B, C, Union[D, E]] 等效于 Union[A, B, C, D, E]
# Union内的类型不应相容
# 但是尽量避免使用Union做为返回值
def return_union(token: str) -> Union[str, float]:
    try:
        return float(str)
    except ValueError:
        return token


# 4. 泛化容器
# 如 stuff: list 与 stuff: list[Any] 是一致的
# 版本3.9或以上可以直接使用, 3.7与3.8中需要从__future__中导入相关内容;
# 这个还是比较乱的
def tokenize(text: str) -> list[str]:
    return text.upper().split()


# 5. 元组类型
# 元组类型注解有3种:
#   1. 用作记录的元组
#   2. 带有具名字段, 用作记录的元组
#   3. 用作不可变序列的元组

# 1. 用作记录的元组
def record_with_tuple():
    shanghai = 31.2304, 121.4737
    print(geohash(shanghai))


def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, 9)


# 2. 带有具名字段, 用作记录的元组
class Coordinate(NamedTuple):
    lat: float
    lon: float


def geohash2(lat_lon: Coordinate) -> str:
    return gh.encode(*lat_lon, 9)


# typing.NamedTuple是tuple子类的制造工厂, 因此Coordinate与tuple[float, float]相容; 反之则不成立;
def display(lat_lon: tuple[float, float]) -> str:
    lat, lon = lat_lon
    ns = 'N' if lat >= 0 else 'S'
    ew = 'E' if lon >= 0 else 'W'
    return f'{abs(lat):0.1f} {ns}, {abs(lon):0.1f} {ew}'


# 3. 用作不可变序列的元组
# tuple[int, ...] 标识元组内元素的数量>= 1, 但是类型只能为int
# stuff: tuple[Any, ...] 与 stuff: tuple 的意思相同, 都是表示长度不定, 但是可以包含任意类型的元组
def columnize(sequence: Sequence[str], num_columns: int = 0) -> list[tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence) ** 0.5)
    num_rows, reminder = divmod(len(sequence), num_columns)
    num_rows += bool(reminder)
    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]
