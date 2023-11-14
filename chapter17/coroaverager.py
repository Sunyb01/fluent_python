# 定义一个计算累计平均值的协程

from collections.abc import Generator


def averager() -> Generator[float, float, None]:
    """ 每次激活之后, 协程在yield处暂停, 等待发送值. coro_ave.send(10)那一行发送一个值, 激活协程,
        yield表达式把得到的值(10)赋给term变量. 循环余下的部分更新total、count和average这三个变量.
        while循环的下一次迭代产出average变量的值, 协程在yield关键字处再一次暂停.
    """
    total = 0.0
    count = 0
    average = 0.0
    while True:
        # 激活后, 在此处将average返回给调用方; 然后等待发送过来的的数据赋值给变量term
        # 然后继续执行代码到此处, 并将值返回给发送方;
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coro_ave = averager()
    # 调用next()或.send(None)向前执行到第一个yield的过程叫做 预激协程;
    print(next(coro_ave))
    # 每次激活后, 协程在yield处暂停, 等待发送值
    print(coro_ave.send(10))
    print(coro_ave.send(30))
    print(coro_ave.send(5))
