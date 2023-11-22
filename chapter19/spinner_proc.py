# spin 和 slow函数

import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize


# Python3.8开始, 标准库提供了multiprocessing.shared_memory包, 但是不支持用户定义类的实例.
# 除了原始字节, 这个包还允许进程共享一个ShareableList. 这是一个可变序列类型, 存放固定数量的项,
# 项的类型可以是int、float、bool和None, 以及单项不超过10MB的str和bytes.

def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def slow() -> int:
    # 阻塞所在的线程, 但是释放GIL, 其他Python线程可以继续运行.
    time.sleep(3)
    return 42


def supervisor() -> int:
    done = Event()
    # 跨进程传递的数据只有Even状态, 在multiprocessing模块底层的C代码中, Event状态通过操作系统底层信号量实现.
    spinner = Process(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
