# 1. 装饰器
# 装饰器的3个基本性质:
#   1. 是一个函数或其他可调用对象
#   2. 可以把被装饰的函数替换成别的函数
#   3. 在加载模块时立即执行

# 1. 装饰器测试
def deco(func):
    def inner():
        func()
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


# 2. 何时执行装饰器
# 函数装饰器在导入模块时立即执行, 而被装饰函数只在显示调用时运行;
registry = []


# 1. 类似于这样原封不动的返回被装饰的函数,在很多Python框架中会使用这种方法, 将函数添加到某种中央注册处; 可以看一下flask
# 2. 常规的做法是返回在装饰器内部定义的函数, 取代被装饰的函数(和Java中的Aop思想上很相似); 与Go在使用上也相似;
def register(func):
    print(f'running register{func}')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('runnign main()')
    print('registry -> ', registry)
    f1()
    f2()
    f3()


# 3. 变量作用域规则
b = 9


def f4(a):
    # 如果不想让下方的b出现错误, 可以通过下面的代码告知Python解释器, 变量b不是局部变量而是全局变量
    # global b
    print(a)
    print(b)
    # 如果没有下面这一行, 方法可以正常执行; 但是一旦解开后方法就会报错
    # 错误类型为UnboundLocalError: local variable 'b' referenced before assignment
    # 造成这种问题的原因是: Python编译主体函数时, 判断b是局部变量, 因为在函数门内给他赋值了;而且生成的字节码证实了这种判断.
    # 所以Python会从局部作用域中获取b. 但是尝试获取局部变量b时, 发现还没有绑定值
    # b = 3


if __name__ == '__main__':
    # target()
    # main()
    f4(3)
