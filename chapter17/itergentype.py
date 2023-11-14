# 注解迭代器的两种方式

from collections.abc import Iterator
from keyword import kwlist
from typing import TYPE_CHECKING

from typing_extensions import reveal_type

short_kw = (k for k in kwlist if len(k) < 5)
if TYPE_CHECKING:
    reveal_type(short_kw)

long_kw:Iterator[str] = (k for k in kwlist if len(k) > 0)
if TYPE_CHECKING:
    reveal_type(short_kw)
