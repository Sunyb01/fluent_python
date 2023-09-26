# 变量引用
# 变量不是盒子, 变量是便利贴;
# 如 x = dict(), 先执行'='号右侧, 进行实例的创建, 然后将变量x绑定到创建的实例上; 或者可以说将创建的实例赋值给变量x
# 注意: list(tar), set(tar)等, 都属于浅拷贝; 如果序列中有引用对象, 可能会存在未知的错误
# 通过copy模块的copy()方法可以获取浅拷贝, 通过deepcopy可以获取深拷贝(不用担心循环引用的问题)

def same_equal_alias():
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    print(lewis is charles)
    print(id(charles), id(lewis))
    lewis['balance'] = 950
    print(charles)
    ales = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    # 底层会通过__eq__()方法进行对比, 比较的是值; java中需要显示的通过equals()方法进行判, 这个与java还是相反的
    print(ales == charles)
    # 比较的是id(instance), 也就是标识(内存地址)
    print(ales is not charles)

def compare_is_and_eq_mark():
    """
        ==运算符比较的是两个对象的值, is比较对象的标识;
        is运算符比==速度快, 因为is不能重载;
    """
    ales = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    charles = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    # 是否为None可以通过is,
    print(ales is None)
    print(charles is None)
    # 碰到if语句时,可以这样写
    if ales:
        print("Not None")
    else:
        print("Is None")
    # 这是一个语法糖, 等同于ales.__eq__(charles)
    print(ales == charles)
    # 比较一个变量和一个单例时应该使用is
    print(ales is charles)


def tuple_relative_immutability():
    t1 = (1, 2, [30, 40, ])
    t2 = (1, 2, [30, 40, ])
    print(t1 == t2)
    print(id(t1[-1]))
    t1[-1].append(99)
    print(id(t1[-1]))
    print(t1)
    print(t1 == t2)

def default_shallow_copy():
    l1 = [1, 2, [30, 40, ]]
    l2 = list(l1)
    print(l1 == l2)
    print(l1 is l2)
    l2[-1].append(50)
    # 所属语言都会有这种情况
    print(l1)


def default_shallow_copy2():
    l1 = [3, [66, 55, 44, ], (7, 8, 9)]
    l2 = list(l1)
    print('l1:', l1)
    print('l2:', l1)
    print("--------1--------")
    l1.append(100)
    print('l1:', l1)
    print('l2:', l2)
    print("--------2--------")
    l1[1].remove(55)
    print('l1:', l1)
    print('l2:', l2)
    print("--------3--------")
    l2[1] += [33, 22, ]
    l2[2] += (10, 11)
    print('l1:', l1)
    print('l2:', l2)

class HauntedBus:
    """
        一个手幽灵乘客折磨的校车
    """
    def __init__(self, passengers=[]):
        """
            这里的passengers相当于java中的类属性了;
            默认值在定制函数时求解(通常是在加载模块时), 因此默认值变成了函数对象的属性;
            一般将None作为可变值的参数默认值;
        """
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

def haunted_bus():
    bus1 = HauntedBus(['Alice', 'Bill', ])
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print('bus1.passengers: ', bus1.passengers)
    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print('bus2.passengers: ', bus2.passengers)
    bus3 = HauntedBus()
    print('bus3.passengers: ', bus3.passengers)
    bus3.pick('Dave')
    print('bus2.passengers: ', bus2.passengers)
    print(bus2.passengers is bus3.passengers)
    # 变成了函数的默认属性
    print(HauntedBus.__init__.__defaults__)


if __name__ == '__main__':
    # same_equal_alias()
    # compare_is_and_eq_mark()
    # tuple_relative_immutability()
    # default_shallow_copy()
    # default_shallow_copy2()
    haunted_bus()