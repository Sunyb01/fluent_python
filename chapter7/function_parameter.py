# 位置参数到仅限关键字参数
# 如果想指定仅限关键字参数, 就要把他们放在前面有*的参数后面, 如果不想支持数量不定的位置参数, 但是想支持仅限过关键字参数, 则可以在签名中放一个*
# 仅限关键字参数怒不一定要有默认值, 通过f(a, *, b)这样前置要求传入参数

def tag(name, *content, class_=None, **attrs):
    """
        生成一个活多个HTML标签
    """
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr} ="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'


def tag_method_test():
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', class_='sidebar'))
    print(tag(content='testing', name="img"))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class': 'framed'}
    print(tag(**my_tag))


def parameter_location_only(name, /, first, second):
    print(f'name = {name}, first = {first}, second = {second}')


# PEP 484约定, 在仅限位置参数的名称参数加两个下划线, 可与参数中加'/'的表示法相同
def parameter_location_only2(__name, first, second):
    print(f'name = {__name}, first = {first}, second = {second}')


if __name__ == '__main__':
    # tag_method_test()
    # parameter_location_only('hello', 'fi', 'se')
    parameter_location_only2('hello', 'fi', 'se')
