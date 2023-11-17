# 使用生成器实现上下文管理器

import contextlib
import sys

"""
    1. 使用 @contextmanager 装饰器时, 要把yield语句放在try/finally语句中(或者放在with块中),
       这是不可避免的, 因为我们永远不知道上下文管理器的用户会在with块中做什么;
    2. @contextmanager还有一个鲜为人知的功能: 它装饰的生成器也可用用作装饰器.
       这是因为@contextmanager是由 contextlib.ContextDecorator类实现的.
"""


@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'

    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


@looking_glass()
def verse():
    print('The time has come')


if __name__ == '__main__':
    # with looking_glass() as what:
    #     print('Alice, Kitty and Snowdrop')
    #     print(what)
    #
    # print(what)
    # print('back to normal')
    verse()
