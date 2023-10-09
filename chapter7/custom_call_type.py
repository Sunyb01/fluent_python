# 用户自定义的可调用类型
import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick form empty BingoCage')

    def __call__(self):
        return self.pick()

def random_items():
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo.pick())
    print(callable(bingo))

if __name__ == '__main__':
    random_items()