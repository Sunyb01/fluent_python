# 类型定义和install函数

from typing import TypeVar, Generic


class Beverage:
    """任何饮料"""


class Juice(Beverage):
    """任何果汁"""


class OrangeJuice(Juice):
    """使用巴西橙子制作的美味果汁"""


T = TypeVar("T")


# 不变的类型
# Java中的泛型是这种的超集
# Rust中的泛型效果与此一致
class BeverageDispenser(Generic[T]):
    """一个参数化饮料类型的自动售货机"""

    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """安装一个果汁自动售货机"""


T_co = TypeVar('T_co', covariant=True)


# 协变的类型, 这个与Java中的<T extends ParentObject>类似,
# Rust中Box<dyn CustomStructTrait>
class BeverageDispenser2(Generic[T_co]):
    """一个参数化饮料类型的自动售货机"""

    def __init__(self, beverage: T_co) -> None:
        self.beverage = beverage

    def dispense(self) -> T_co:
        return self.beverage
