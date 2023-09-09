# 数据模型

import collections
from random import choice

# 一摞纸牌

# 使用namedtuple 创建一个只有属性没有自定义方法的类对象
Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # 类似于Java构造函数与Golang的init()方法
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    # 组合模式实现遍历
    def __len__(self):
        # len()是内置方法, 如果自定义类实例的话, 需要实现 __len__() 方法
        return len(self._cards)

    # 组合模式实现遍历
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(choice(deck))
    print(deck)
    # 从下标12处开始截取(包含12), 一直到最后, 步长为13
    print(deck[12::13])
    # 循环的背后调用为iter(deck), 然后调用deck的__iter__()方法(前提是有这个方法)或__getitem__()方法
    # 感觉像是模板模式与策略模式
    for card in deck:
        print(card)

    # 反向迭代
    for card in reversed(deck):
        print(card)

    # 如果一个容器没有实现 __contains__方法, in运算符会做顺序扫描
    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)

    for card in sorted(deck, key=spades_high):
        print(card)
