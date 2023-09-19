#  集合sets
# Note:
#     1. 集合元素必须是可哈希的
#     2. set类型不可哈希
#     3. frozenset可以哈希
#     4. 中缀运算符, a|b(并集), a&b(交集), a-b(差集), a^b(对称差集)
# 构造: set(), 获取{....}形式, 如{1}; 如果写作{}, 代表dict类型
# 字典是python的基石
from unicodedata import name


def first_sets():
    l = ['a', 'b', 'a', 'c', 'd', 'b', 'e']
    s1 = set(l)
    print(s1)
    print(list(s1))
    # 如果想去除重复项, 同时保留每一项出现位置的顺序, 可以使用普通的dict
    d = dict.fromkeys(l).keys()
    print(d)


def infix_operation():
    # 两个操作对象必须都是集合
    s1 = {'a', 'b', 'a', 'c', 'd', 'b', 'e'}
    s2 = {'a', 'f'}
    print(len(s1 | s2))
    print(len(s1 & s2))
    print(len(s1 - s2))
    print(len(s1 ^ s2))


def set_derivation():
    s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
    print(s)


if __name__ == '__main__':
    # first_sets()
    # infix_operation()
    set_derivation()
