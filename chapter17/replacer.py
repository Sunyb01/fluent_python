#  返回一个产生字符串元祖的迭代器

from collections.abc import Iterable
from typing import TypeAlias

FromTo: TypeAlias = tuple[str, str]


def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text
