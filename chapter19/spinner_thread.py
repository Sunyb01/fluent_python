# spin 和 slow函数

import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:
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
