# 闭包
# 闭包就是延伸了作用域的函数, 包括函数主题中引用的非全局变量和局部变量
# 闭包是一个函数, 它保留了定义函数时存在的自由变量的绑定. 如此一来, 调用函数时, 虽然定义作用域不可用了, 但是仍能使用那些绑定
# 注意, 只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量. 这些外部变量位于外层函数的局部作用域内;
import functools
import time


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

if __name__ == '__main__':
    print('\n')
    # use_callable_class()
    # use_closure()
    # use_closure_func_clock()
    # print(snooze.__name__)
    # use_closure_func_clock2()
    fibonacci(6)