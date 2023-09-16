# dict
from collections import OrderedDict, abc
# 1. 字典api
# 1. setdefault(key, default_value); 返回key对应的value, 如果不存在, 将value设置为default_value, 并返回key对应的value -> default_value

# 1. 字典推导式
def dict_generate():
    dial_codes = [(880, 'Bangladesh'), (55, 'Brazil'), (86, 'China'), ]
    # 转换为country为key, code为value的dict; 通过遍历dial_codes
    country_dial = {country: code
                    for code, country in dial_codes}
    print(country_dial)
    cd = {code: country.upper()
          for country, code in sorted(country_dial.items())
          if code < 90}
    print(cd)


def mapping_unpacking(**keywords):
    return keywords

def merge_for_new_feature():
    d1 = {'a': 1, 'b': 3}
    d2 = {'a': 2, 'b': 4, 'c': 6}
    return d1 | d2

def merge_for_new_feature_modify():
    d1 = {'a': 1, 'b': 3}
    d2 = {'a': 2, 'b': 4, 'c': 6}
    d1 |= d2
    print('d1 = ', d1)

def match_case_dict(record: dict) -> list:
    # 与序列不同, 计算只有部分匹配, 映射模式也算成功匹配
    # 而且没有必要使用**extra来接收多出的键值对;
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f'Invalid \'book\' record: {record!r}')
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid \'book\' record: {record!r}')

def type_match():
    my_dict = {}
    print(isinstance(my_dict, abc.Mapping))
    print(isinstance(my_dict, abc.MutableMapping))

def test_method_update():
    d1 = {'a': 1, 'b': 3}
    d2 = {'d': 2, 'e': 4, 'c': 6}
    # 使用d2更新d1
    d1.update(d2)
    print(d1)


if __name__ == '__main__':
    # dict_generate()
    # print(mapping_unpacking(**{'x': 1}, y=2, **{'z': 3}))
    # print(merge_for_new_feature())
    # merge_for_new_feature_modify()
    # print(match_case_dict(dict(api=1, author='Douglas Hofstadter', type='book', title='Godel, Escher, Bach')))
    # print(match_case_dict(OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())))
    # 第三个case, 会报错
    # print(match_case_dict({'type':'book', 'package':100}))
    # type_match()
    test_method_update()