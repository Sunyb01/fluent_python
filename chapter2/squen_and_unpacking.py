# 序列和可迭代对象拆包


def unpacking_tuple():
    # 并行赋值
    city, year, pop, chg, area = ('China', 2003, 32_450, 0.66, 8014)
    print(f'在{year} 的 {city}, {pop}, {chg}, {area}')
    # 通配符
    t = (20, 8)
    print(divmod(*t))
    # 类似于函数多返回值, 可参考golang的函数返回
    quotient, remainder = divmod(*t)
    print(quotient, remainder)


def get_other_args():
    # 并行赋值, 且使用*arg接收余下的参数
    # *arg只能应用到一个变量上
    a, b, *rest = range(5)
    print(a, b, rest)


def get_match_arg(a, b, c, d, *rest):
    return a, b, c, d, rest


def nested_unpacking():
    metro_areas = [('Tdd', 'JP', 36.933, (35.689722, 139.691667)),
                   ('Ddd', 'IN', 21.935, (36.689722, -10.691667)),
                   ]
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:1} | {lat:9.4f} | {lon:9.4f}')

# 当返回单条数据时, 可以采用 (record) = query_returning_single_row(); 变量写法是固定的
def return_single_row():
    return ('zs', 18)
def test_single_row():
    (r1) = return_single_row()
    print(r1)
    name, age = r1
    print(f'{name} - {age}')

# 当返回单挑数据且单个字段时, (field,) = query_returning_single_row_with_single_field()
def return_single_row_with_single_field():
    return (18,)

def test_single_row_with_single_field():
    # 这个','千万不要丢了
    (f1,) = return_single_row_with_single_field()
    print(f1)

if __name__ == '__main__':
    # print(get_match_arg(*[1, 2], 3, *range(4, 7)))
    # nested_unpacking()
    test_single_row()
    test_single_row_with_single_field()