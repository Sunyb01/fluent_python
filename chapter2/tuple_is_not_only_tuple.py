# 元组不仅仅是不可变列表
# 也是没有字段名称的记录(可参见数据库返回记录)

# 用作 没有字段名称的记录


def record1():
    # 这里使用了 '元组拆包 或 可迭代对象拆包'
    city, year, pop, chg, area = ('China', 2003, 32_450, 0.66, 8014)
    print(f'在{year} 的 {city}, {pop}, {chg}, {area}')


def list_tuple():
    traveler_ids = [('USA', '31195855'), ('BRA', 'CEC342567'), ('ESP', 'XDA205856')]
    for password in traveler_ids:
        print('%s/%s', password)


def list_tuple2():
    traveler_ids = [('USA', '31195855'), ('BRA', 'CEC342567'), ('ESP', 'XDA205856')]
    # for循环知道如何获取元组中单独的每一项, 叫做'元组拆包 或 可迭代对象拆包'
    # 这里的'_'称为虚拟变量, 匹配值但不绑定值; golang中也是如此使用
    for country, _ in traveler_ids:
        print(country)


# 用作不可变列表
# 1. 意图清晰
# 2. 性能优越(不可变, 估计是使用了压缩技术)
# 而且元组的不可变, 指的是自身不可变; 如果元组内的引用可变的, 元组的值也会发生变化(引用指向的内存区域内, 数据发生变化)
# 只有值不可变的对象才是可哈希的, 不可哈希的元组不能作为字典的key, 也不能作为集合(set)的元素
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True
