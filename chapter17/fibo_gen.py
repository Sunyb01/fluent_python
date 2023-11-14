# 返回一个产出整数的生成器

from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
