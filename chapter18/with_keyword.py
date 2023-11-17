# with关键字
# 通过上下文管理器来管理with语句, 就像迭代器是为了管理for语句一样.
# with语句的目的是简化一些常用的try/finally结构, 这种结构可以保证一段代码运行完毕后执行某项操作,
# 即使那段代码由于 return语句、异常或sys.exit()调用而终止, 也执行指定的操作.
# finally子句中的代码通常用于释放重要的资源(如: 文件), 或者还原临时改变的状态
# 与Java中的try-with-resource类似, 但是还是有些不同

from mirror import LookingGlass


def read_py_file():
    """
        上下文管理器接口包含 __enter__ 和 __exit__ 两个方法.
        with语句开始运行时, Python在上下文管理器对象上调用__enter__方法.
        with块运行结束时, 或者由于什么原因终止后, Python在上下文管理器对象上调用__exit__方法.
    """
    # 求解with后面的表达式的得到的结果是上下文管理器对象,
    # 不过, 绑定到目标变量(在 as 子句中)上的值是在上下文管理器对象上调用__enter__方法返回的结果;
    # 也就是说 变量te 是上下文管理器对象调用__enter__方法返回的结果
    with open('../chapter17/tree.py') as te:
        for line in te.readlines():
            print(line)
    # 当代码执行到以下后, 控制流会退出with块, 都在上下文管理器对象上调用__exit__方法, 而不是在__enter__方法返回的对象上调用


def example_for_looking_glass():
    """
        打印的结果为:
            pordwonS dna yttiK ,ecilA
            YKCOWREBBAJ
            JABBERWOCKY
        所以执行顺序为:
            __enter__    => 将标准输出重置, 设置what变量
            print(Alice) => 执行修改后的标准输出
            print(what)  => 执行修改后的标准输出
            __exit__     => 重置标准输出, 恢复正常
    """
    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print(what)


def use_looking_glass_out_with():
    manager = LookingGlass()
    print(manager)
    monster = manager.__enter__()
    print(monster == 'JABBERWOCKY')
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)


if __name__ == '__main__':
    # read_py_file()
    # example_for_looking_glass()
    use_looking_glass_out_with()