# 使用鸭子类型编程
from collections import namedtuple, abc

Card = namedtuple('Card', ['rank', 'suit'])


class French2Deck(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    # 继承 MutableSequence 类必须实现 __delitem__ 方法, 这是 MutableSequence 的一个抽象方法.
    def __delitem__(self, position):
        del self._cards[position]

    # 这是 MutableSequence 的第三个抽象方法.
    def insert(self, position, value):
        self._cards.insert(position, value)
