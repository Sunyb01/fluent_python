# Callable
from collections.abc import Callable


# Callable[[], float] 说明没有参数传递, 且返回值为float类型
# Callable[[float], None] 说明有float类型的参数传递, 但是没有返回值
# Python中float是包容int的, 但是int到float会有精度丢失的问题
# 协变:
#   在Callable[[], float]出现的地方, Callable[[], int]始终可以替换; 因为float可以包容int, 相当于Java中的子类关系; 称之为协变
# 逆变:
#   Callable[[int], None]出现的地方不能替换为Callable[[float], None]; 涉及到降级的过程; 虽然int是float的子类,
# 但是在参数化Callable类型中, 关系是相反的, 级Callable[[float], None]是Callable[[int], None]的子类型.
# 因此我们说, 那个Callable声明的参数类型经历了逆变;
# 不变:
#   大多数参数泛型是不变的, 如果声明scores: list[float]就只能将list[float]类型赋值给scores, 而不是其他类型如: list[int]
def update(probe: Callable[[], float], display: Callable[[float], None]) -> None:
    pass


def probe_ok():
    return 42


def display_wrong(temperature: int) -> None:
    print(hex(temperature))

# NoReturn
# 这是一个特殊类型, 仅用于注解觉返回的函数的返回值类型(有的拗口), 这类函数通常会抛出异常.
# 比如Java中自定义的异常类静态方法;
# Python中,可以参考sys.exit()方法;
