# del 和 垃圾回收
# 对象绝不会自行销毁; 然而, 对象不可达时, 可能会被当做垃圾回收;
# Note: __del__方法, 不粗则销毁实例, 而且不应该在代码中调用; 类似与Java中的finalize()方法

import weakref

def first_del():
    a = [1, 2, 3,]
    b = a
    # 删除引用a, 而不删除对象
    del a
    # 给变量b重新赋值后, 原内存地址内的数据将会被回收
    b = [1, 2]


def call_del():
    s1 = {1, 2, 3}
    s2 = s1
    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'span'
    print(ender.alive)

def bye():
    print('.....like tears, in rain')


def immutable_for_tuple():
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print('t1 id = ', id(t1))
    print('t2 id = ', id(t2))
    print(t2 is t1)
    # 注意frozenset不是序列, 所以不会达到如下预期
    # 但是frozenset的copy()方法, 效果和下面的写法一致
    t3 = t1[:]
    print('t1 id = ', id(t1))
    print('t3 id = ', id(t3))
    print(t3 is t1)


def str_var_for_share():
    t1 = (1, 2, 3)
    t2 = (1, 2, 3)
    # 这个和书中的结果不一致, 可能是由于版本不同导致的
    print(t2 is t1)
    # 与Java中的效果一致, Java采用享元模式进行节省内存
    # 这里是一种称为驻留的优化措施, 但是此种行为并不可靠
    s1 = 'ABC'
    s2 = 'ABC'
    print(s2 is s1)

if __name__ == '__main__':
    # first_del()
    # call_del()
    # immutable_for_tuple()
    str_var_for_share()