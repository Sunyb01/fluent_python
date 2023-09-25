# @dataclass
# 其中含有多个属性: init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False
# init生成__init__, repr生成__repr__, eq生成__eq__, order生成__lt__、__le__、__gt__、__ge__
# unsafe_hash生成__hash__, frozen是否不可变
# Note:
#      1. 当使用list、dict、set等类型时, 若考虑默认值请使用 field_name: field_type = dataclasses.field(default_factory=target_func),
#         default_factory可以是函数、类或其他可调用对象
#      2. python3.9开始支持泛型如 list[str]
#      3. 带类型的类属性, field_name:typing.ClassVar[set[str]] = set()


from dataclasses import dataclass


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    # 类属性
    c = 'spam'


def print_dataclass_annotations():
    print(DemoDataClass.__annotations__)
    print(DemoDataClass.__doc__)
    # 也是和namedtuple一样的结果, 没有对应的属性
    # print(DemoDataClass.a)


if __name__ == '__main__':
    print_dataclass_annotations()
