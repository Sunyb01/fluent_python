# spin 和 slow函数

import itertools
import asyncio


def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            # await asyncio.sleep(.1)
            asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def slow() -> int:
    # 阻塞所在的线程, 但是释放GIL, 其他Python线程可以继续运行.
    await asyncio.sleep(.1)
    return 42


async def supervisor() -> int:
    # 跨进程传递的数据只有Even状态, 在multiprocessing模块底层的C代码中, Event状态通过操作系统底层信号量实现.
    spinner = asyncio.create_task(spin("thinking!"))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result


def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
