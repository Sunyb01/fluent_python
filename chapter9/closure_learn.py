# 闭包
# 闭包就是延伸了作用域的函数, 包括函数主题中引用的非全局变量和局部变量
# 闭包是一个函数, 它保留了定义函数时存在的自由变量的绑定. 如此一来, 调用函数时, 虽然定义作用域不可用了, 但是仍能使用那些绑定
# 注意, 只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量. 这些外部变量位于外层函数的局部作用域内;
# 装饰器函数相当于Decorator的具体子类, 而装饰器返回的内部函数相当于此装饰器的实例. 返回的函数包装了被装饰的函数,相当于设计模式中的组件;
import decimal
import fractions
import functools
import html
import numbers
import time
from collections import abc


# 可调用对象
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def use_callable_class():
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))


# 计算累计平均值的高阶函数
def make_averager():
    series = []

    def averager(new_value):
        # series在averager是自由变量(????, 未在局部作用域中绑定的变量)
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def use_closure():
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print('----------------')
    # 局部变量
    print('avg.__code__.co_varnames --> ', avg.__code__.co_varnames)
    # 自由变量
    print('avg.__code__.co_freevars --> ', avg.__code__.co_freevars)
    print('avg.__closure__ --> ', avg.__closure__)
    print('avg.__closure__[0].cell_contents --> ', avg.__closure__[0].cell_contents)


# nonlocal声明
def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        # 如果将下面的 nonlocal count, total这一行注释掉将会报错;
        # 产生错误的原因如下:
        #   对于数值或不可变类型, 相当于将变量重新赋值了, 这回把count变为当前函数的局部变量而不是自由变量了;
        #   之前的方法没有问题是因为我们利用了"列表是可变对象"这一事实
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


# 变量查找逻辑:
# 1. 如果是global x声明, 则x来自模块全局作用域, 并赋予那个作用域中x的值.
# 2. 如果是nonlocal x声明, 则x来自最近一个定义它的外层函数, 并赋予那个函数中局部变量x的值.
# 3. 如果x是参数, 或者在函数主体中服了只, 那么x就是局部变量.
# 4. 如果引用了x, 但是没有赋值也不是参数, 则遵循一下规则(就近原则):
#   1. 在外层函数主体的局部作用域(非局部作用域)内查找x.
#   2. 如果在外层作用域内未找到, 则从模块全局作用域内读取.
#   3. 如果在模块全局作用域内未找到, 则从__builtins__.dict中读取.

# 实现一个简单的装饰器
# Python中的装饰器与设计模式中的装饰器还是不一致的, 看起来更像aop的思想实现
# 1. 一个会显示函数运行时间的简单装饰器
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


def use_closure_func_clock():
    snooze(.123)


# 进阶版
def clock2(func):
    @functools.wraps(func)
    def clocked2(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f'{k}={v}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result

    return clocked2


@clock2
def factorial(n, key=None):
    return 1 if n < 2 else n * factorial(n - 1, key)


def use_closure_func_clock2():
    factorial(2, "hello")


# 3. 标准库中的装饰器
# 3.1 functools.cache
# @cache装饰器实现了备忘. 这是一项优化, 能把耗时的函数得到的结果保存起来, 避免传入相同的参数时重复计算.
# 注意:
#   1. 当前的特性是从3.9版本新增的, 如果是3.8请替换成@lru_cache, 更早的需要写成@lru_cache()
#   2. 被装饰的函数所接受的参数必须是可哈希的, 因为底层lru_cache使用dict存储
#   3. @cache可能耗尽内存, @cache更适合短期的命令行脚本; 对于长期运行的进程, 推荐使用@lru_cache, 并设置合理的maxsize参数
# 示例: 生成第n个斐波那契数, 递归方式非常耗时
# 当去除@cache时, 发现1重复计算了很多次
# 另外, 叠放装饰器越靠近函数, 执行的优先级越高; 示例中的叠放相当于 cache(clock(func))
@functools.cache
@clock
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


# 4. lru_cache
# 其中默认参数有:
#   1. maxsize = 128 设定最多可以储存多少条目, 缓存满了之后, 丢弃最不常用的条目; 如果设为None代表LRU逻辑被禁用, 效果和@cache一致
#   2. typed = False 决定是否把不同的参数类型得到的结果分开保存.
@functools.lru_cache
@clock
def fibonacci2(n):
    if n < 2:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


# 5. singledispatch(单分派泛化函数)
# Python不支持Java中的重载, 所以常见的做法都是使用if/elfi/else或者match/case实现.
# 但是快速实现就是通过使用singledispatch装饰器将整体方案拆分为多个模块, 甚至可以为第三方包中无法编辑的类型提供专门的函数.
# 使用@singledispatch装饰的普通函数, 变成了泛化函数(Java中支持的重载等)
# 在单分派中使用抽象基类或type.Protocol可以让代码支持抽象基类胡实现协议的类当前和未来的具体子类或虚拟子类.
# 普通装饰器时, Python会把被装饰的函数作为第一个参数传给装饰器函数.
@functools.singledispatch
def htmlize(obj: object):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'


@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = '</li>\n<li>'.join((htmlize(item) for item in seq))
    return f'<ul>\n<li>' + inner + '</li>\n</ul>'


@htmlize.register
def _(n: numbers.Integral) -> str:
    return f'<pre>{n}(0x{n:x})</pre>'


@htmlize.register
def _(n: bool) -> str:
    return f'<pre>{n}</pre>'


@htmlize.register(fractions.Fraction)
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'


@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f'<pre>{x}({frac.numerator}/{frac.denominator})</pre>'


def use_htmlize():
    print(htmlize({1, 2, 3}))
    print(abs)
    print('Heimlich & Co.\n- a game')
    print(htmlize(42))
    print(htmlize(['alph', 66, {3, 2, 1}]))
    print(htmlize(True))
    print(htmlize(fractions.Fraction(2, 3)))
    print(htmlize((2 / 3)))
    print(htmlize((decimal.Decimal('0.02380952'))))


# 6. 参数化装饰器
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


class Clock:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = [repr(arg) for arg in args]
            arg_lst.extend(f'{k}={v}' for k, v in kwargs.items())
            arg_str = ', '.join(arg_lst)
            print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
            return result

        return clocked


if __name__ == '__main__':
    print('\n')
    # use_callable_class()
    # use_closure()
    # use_closure_func_clock()
    # print(snooze.__name__)
    # use_closure_func_clock2()
    # fibonacci(6)
    # fibonacci2(20)
    use_htmlize()
