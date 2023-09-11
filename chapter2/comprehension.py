# 内置序列

# 容器序列: 所包含对象的引用
# list, tuple, collections.deque
# 扁平序列: 在自己内存空间中所存储所含内容的值
# str, bytes, array.array

# 列表推导式(list comprehension), 符号 ':=' 称为海象表达式
# old forloop
def generate_unicodes():
    symbols = '$#%&'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))

    return codes


# list comprehension
def listcomps_unicodes():
    symbols = '$#%&'
    # listcomps 尽量要简短, 最好不要超过2行
    return [ord(symbol) for symbol in symbols]


def get_int_list():
    # 项与项之间使用','分隔, 最好在最后添加一个','; 减少代码差异给阅读带来的干扰
    return [1, 2, 3, 4, ]


# map和filter函数
def mp_fi_generate_unicodes():
    symbols = '$#%&'
    # 感觉比listcomps难理解,
    return list(filter(lambda c: c > 127, map(ord, symbols)))


# listcomps计算笛卡尔积
def get_tshirt():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    return [(color, size) for color in colors
            for size in sizes]


# 生成器表达式
# 将[]换成了()
def first_generate_lambda():
    symbols = '$#%&'
    gen_lam = (ord(symbol) for symbol in symbols)
    # tuple(ord(symbol) for symbol in symbols) 这是等价的;
    # 如果生成器表达式是函数唯一的参数, 则不需要额外在使用()括起来
    return tuple(gen_lam)


def gen_lam_tshirt():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    # 生成器表达式一次产出一个, 可以节省大量内存; yield表达式也是返回一个生成器表达式
    # 内存占用特别低
    for tshirt in (f'{c}{s}' for c in colors for s in sizes):
        print(tshirt)
