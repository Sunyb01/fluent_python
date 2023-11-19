# 除了if语句之外的else
# else蕴含着 "排他性" 这层意思, 例如"要么运行这个循环, 要么做那件事". 可是, 在循环中, else的语义恰好相反;
# 变成了 "运行这个循环, 然后做那件事". 因此, 使用then关键字或许更好.
# then 在 try 语句的上下文中也说得通: "尝试运行这个, 然后做那件事".

# else 子句规则
# for: 仅当for循环运行完毕时(即for循环没有被break语句中止)才运行else块
# while: 仅当while循环条件为 假值 而退出时(即while循环没有被break语句中止)才运行else块
# try: 仅当try块没有抛出异常时才运行else块. 官方文档还指出: "else子句抛出的不由前面的except子句处理".

# 两种风格:
# 1. EAFP(Easier to ask for forgiveness than permission)
#    取得原谅比获取许可容易. 这是一种常用的Python编程风格, 先假定存在有效的键或属性, 如果假设不成立, 那么捕获异常.
#    这种风格简单明快, 特点是代码中有很多try和except语句. 与其他语言一样, 这种风格的对立面是LBYI风格.
#
# 2. LBYI(Look before you leap)
#    三思而后行. 这种编程风格在调用函数或查找属性或键之前显示测试前提条件.
#    与EAFP风格相比, 这种风格的特点是代码中有很多if语句.
#    在多线程环境中, LBYI风格可能会在"检查" 与 "行事"的空隙引入条件竞争, 例如: 对if key in mapping: return mapping[key]这段代码来说,
#    如果在测试之后 - 但在查找之前 - 另一个线程从映射中删除了键, 那么这段代码就会失败,
#    这个问题可以使用锁或者EAFP风格解决.

def for_loop_use_else():
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        if item == 4:
            print("will be break")
            # break

        print("item = ", item)
    else:
        # 不提前break这里才可以执行
        print("this is else block")


def while_loop_use_else():
    count = 0
    while count < 3:
        print("count = ", count)
        count += 1
    else:
        print("this is else")


def try_except_use_else():
    try:
        if 1 == 1:
            print("will be raise")
            # raise TypeError("出错了啊")
    except TypeError as te:
        print("error = ", te)
    else:
        # try块不抛出异常, 这里才可以执行
        print("this is else")


if __name__ == '__main__':
    # for_loop_use_else()
    while_loop_use_else()
    # try_except_use_else()
