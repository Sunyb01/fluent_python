# 泛化映射
import sys
import re
import unicodedata
from collections.abc import Iterator

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1


def tokenize(text: str) -> Iterator[str]:
    """
        返回全大写的单词构成的可迭代对象
    """
    for match in RE_WORD.finditer(text):
        yield match.group().upper()


def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)

    return index


if __name__ == '__main__':
    index_dict = name_index(32, 65)
    print(index_dict['SIGN'])