# 函数
# 高阶函数有: map, fileter, reduce, apply
# all(iterable) iterable 表示没有假值的元素时返回True, 如all([])返回True
# any(iterable) iterable 表示有真值的元素时返回True, 如any([])返回False
# 9钟可调用对象:
#   1. 用户定义的函数. 如def语句或lambda表达式创建
#   2. 内置函数. 如使用C语言(CPython)实现的函数,例如len或time.strftime
#   3. 内置方法. 使用C语言实现的方法, 如dict.get
#   4. 方法. 在类主体中定义的函数; (注意与Java不同的是, 方法和函数所表达的含义并不相同. Python中的表达更加具象)
#   5. 类. Python中没有new关键字, 所以调用类就当于调用函数
#   6. 类的实例
#   7. 生成器函数, 主体中有yield(很重要的关键字)关键字的函数或方法;
#   8. 原生协程函数. 使用async def定义的函数或方法. 如async factorial(n)
#   9. 异步生成器函数. 使用async def定义, 而且主体中有yield关键字的函数或方法;
# 注意生成器、原生协程和异步生成器函数的返回值不是应用程序数据, 而是需要进一步处理的对象, 要么产出应用程序数据, 要么执行某种操作;
# 可以通过callable()函数测试是否可以调用

from functools import reduce
from operator import add


def factorial(n):
    """
        returns n!
    """
    return 1 if n < 2 else n * factorial(n - 1)


def func_attr():
    print(factorial(42))
    print(factorial.__doc__)
    print(type(factorial))


def func_as_key_in_map():
    fact = factorial
    print(fact)
    print(fact(5))
    m1 = map(fact, range(11))
    print(m1)
    print(list(map(factorial, range(11))))


def func_as_key_in_sorted():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(fruits)
    fruits = sorted(fruits, key=len)
    print(fruits)


def reverse(word):
    return word[::-1]


def func_as_key_in_sorted2():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(fruits)
    fruits = sorted(fruits, key=reverse)
    print(fruits)


# map fileter reduce 替代品
def higher_order_function_replacement():
    # map
    print(list(map(factorial, range(6))))
    print([factorial(n) for n in range(6)])
    # filter
    print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
    print([factorial(n) for n in range(6) if n % 2])
    # reduce, sum函数更加的简洁且无需引入其他依赖
    print(reduce(add, range(100)))
    print(sum(range(100)))


def use_callable_test_function_can_access():
    print([callable(obj) for obj in (abs, str, 'Ni!')])


if __name__ == '__main__':
    # func_attr()
    # func_as_key_in_map()
    # func_as_key_in_sorted()
    # func_as_key_in_sorted2()
    # higher_order_function_replacement()
    use_callable_test_function_can_access()
