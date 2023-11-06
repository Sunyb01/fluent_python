# 处理具有动态结构的数据, TypedDict根本不能取代运行时数据验证.
# 真想做数据验证, 可以使用pydantic.

import json
from typing import TypedDict, TYPE_CHECKING

from typing_extensions import reveal_type

AUTHOR_ELEMENT = '<AUTHOR>{}</AUTHOR>'


class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int


def to_xml(book: BookDict) -> str:
    elements: list[str] = []
    for key, value in book.items():
        if isinstance(value, list):
            elements.extend(AUTHOR_ELEMENT.format(n) for n in value)

        else:
            tag = key.upper()
            elements.append(f'<{tag}>{value}</{tag}>')

    xml = '\n\t'.join(elements)
    return f'<BOOK>\n\t{xml}</BOOK>'


def from_json(data: str) -> BookDict:
    whatever: BookDict = json.loads(data)
    return whatever


def demo() -> None:
    NOT_BOOK_JSON = """
        {"title": "Andromeda Strain",
        "flavor": "pistachio",
        "authors": true
        }
    """
    not_book = from_json(NOT_BOOK_JSON)
    if TYPE_CHECKING:
        reveal_type(not_book)
        reveal_type(not_book['authors'])

    print(not_book)
    print("flavor = ", not_book['flavor'])
    xml = to_xml(not_book)
    print(xml)


if __name__ == '__main__':
    demo()
