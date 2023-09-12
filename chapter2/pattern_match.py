# 模式匹配, 支持析构; 和switch/case很像
# 语法为
# match target_obj:
# case obj1:
#   表达式
# case _:
# 标识默认
# 注意事项:
# 1. 匹配对象是序列
# 2. 匹配对象和模式的项数要一致
# 3. 对应的项要相互匹配, 包括嵌套的项
# 4. str、bytes、bytearray不作为序列处理
# 5. as可作为关键字绑定
def unpacking_with_match_case():
    metro_areas = [('Tdd', 'JP', 36.933, (35.689722, 139.691667)),
                   ('Ddd', 'IN', 21.935, (36.689722, -10.691667)),
                   ]
    # 也可以使用'*_'匹配任意数量的项,而且不绑定变量;
    # 但是如果换成'*args', 则是将匹配的零项或多项作为列表绑定到到args上
    for record in metro_areas:
        match record:
            # [name, _, _, (lat, lon)]是匹配模式, if lon <= 0是卫语句(可选); 若同时出现则必须同时满足
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:1} | {lat:9.4f} | {lon:9.4f}')
            case [name, _, _, (lat, lon) as rc]:
                print(f'{name:1} | {lat:9.4f} | {lon:9.4f}, {rc}')
            case _:
                print('this is default')


def x(s1, *args, **keyword):
    print(f'{s1} \n {args} \n {keyword}')


def y(s1, s2, *args, city):
    print(f'{s1} \n {s2} \n {args}')


if __name__ == '__main__':
    unpacking_with_match_case()
    x('zs', 'china', 18, x=3)
    y('zs', 'china', 18, 12, city='ss')
