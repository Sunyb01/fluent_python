# 定义一个计算累计平均值的协程

from collections.abc import Generator
from typing import NamedTuple, TypeAlias


class Result(NamedTuple):
    count: int
    average: float


class Sentinel:
    def __repr__(self):
        return f'<Sentinel>'


STOP = Sentinel()
SendType: TypeAlias = float | Sentinel


def averager(verbose: bool = False) -> Generator[None, SendType, Result]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield
        if verbose:
            print('received: ', term)
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def use_averager_generator():
    coro_avg = averager()
    print(next(coro_avg))
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(6.5))
    try:
        coro_avg.send(STOP)
    except StopIteration as exc:
        # 从 StopIteration 异常中偷取协程的返回值, 感觉不是标准做法;
        # 然而PEP342就是这样规定的; StopIteration 异常的文档和<Python语言参考手册> 中6.2.9节 "yield 表达式"也是这么做的
        result = exc.value
        print(result)


def compute():
    res = yield from averager(True)
    print('computed: ', res)
    return res


def use_function_compute():
    comp = compute()
    for v in [None, 10, 20, 30, STOP]:
        try:
            # 第一个None用于预激协程
            comp.send(v)
        except StopIteration as exc:
            result = exc.value
            print("result = ", result)


if __name__ == '__main__':
    # use_averager_generator()
    use_function_compute()
