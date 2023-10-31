# 使用抽象基类实现结构类型
# 静态协议类型
import random
from typing import TypeVar, Protocol, Any, runtime_checkable, Iterable, TYPE_CHECKING

from typing_extensions import reveal_type

T = TypeVar('T')


class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...


RT = TypeVar('RT', bound=Repeatable)


def double(x: RT) -> RT:
    return x * 2


@runtime_checkable
class RandomPicker(Protocol):
    def pick(self) -> Any: ...


# 实现
# 实现了 RandomPicker 的pick()方法, 但是不是它的子类; 这就是静态鸭子类型;
class SimplePicker:
    def __init__(self, items: Iterable):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self) -> Any:
        return self._items.pop()


# 如果想让Mypy检查, 一定要加上类型提示 -> None
def use_isinstance_test() -> None:
    popper: RandomPicker = SimplePicker([1])
    assert isinstance(popper, RandomPicker)


def use_item_type_test() -> None:
    items = [1, 2]
    popper = SimplePicker(items)
    item = popper.pick()
    assert item in items
    if TYPE_CHECKING:
        reveal_type(item) # 在Mypy的输出中生成一个说明
        # 输出 note: Revealed type is "Any"
    assert isinstance(item, int)


if __name__ == '__main__':
    use_isinstance_test()
    use_item_type_test()
