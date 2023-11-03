# 混入类
import collections


def _upper(key):
    try:
        return key.upper()
    except AttributeError:
        return key


class UpperCaseMixin:

    def __setitem__(self, key, value):
        super().__setitem__(_upper(key), value)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))


class UpperDict(UpperCaseMixin, collections.UserDict):
    pass


class UpperCounter(UpperCaseMixin, collections.Counter):
    """ 一个特殊的计数器, 字符串键是大写形式"""


def use_mixin_subclass():
    d = UpperDict([('a', 'letter A'), (2, 'digit two')])
    print(list(d.keys()))
    # 调用了__setitem__
    d['b'] = 'letter B'
    print('b' in d)
    # 调用了__getitem__
    print(d['a'])
    print(d.get('B'))
    print(list(d.keys()))


if __name__ == '__main__':
    use_mixin_subclass()
