# 支持函数的包
from functools import reduce, partial
from operator import mul, itemgetter, methodcaller
from unicodedata import normalize
"""
    引用作者原文: <Python Cookbook> 一书的第七章采用不同方式探讨了相关概念, 是本章的不错的补充;
"""

def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


def factorial2(n):
    return reduce(mul, range(1, n + 1))


def use_itemgetter():
    metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
                  ('Delhi NCR', 'In', 21.935, (28.613889, 77.208889)),
                  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)), ]
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)


def use_itemgetter2():
    metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
                  ('Delhi NCR', 'In', 21.935, (28.613889, 77.208889)),
                  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)), ]
    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))

def use_methodcaller():
    """
        methodcaller方法和Java中的反射很相似
    :return:
    """
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))
    hyphenate = methodcaller('replace', ' ', '-')
    print(hyphenate(s))


def use_partial_with_mul():
    # 使用partial将mul的第一个参数绑定为3
    triple = partial(mul, 3)
    print(triple(7))
    print(list(map(triple, range(1, 10))))

def use_partial_with_unicode_normalize():
    # 更像闭包和反射的结合
    nfc = partial(normalize, 'NFC')
    s1 = 'café'
    s2 = 'cafe\u0301'
    print('s1 = ', s1, 's2 = ', s2, '\n')
    print(s1 == s2)
    print(nfc(s1) == nfc(s2))

if __name__ == '__main__':
    # print(factorial(5))
    # print(factorial2(5))
    # use_itemgetter()
    # use_itemgetter2()
    # use_methodcaller()
    # use_partial_with_mul()
    use_partial_with_unicode_normalize()