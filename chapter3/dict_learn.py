# dict
import collections
from collections import OrderedDict, abc, ChainMap, Counter
import re
import sys
import builtins
from types import MappingProxyType


# 1. 字典api
# 1. setdefault(key, default_value); 返回key对应的value, 如果不存在, 将value设置为default_value, 并返回key对应的value -> default_value
# 2. 创建新的dict应该继承UserDict而不是dict


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


def method_update_test():
    d1 = {'a': 1, 'b': 3}
    d2 = {'d': 2, 'e': 4, 'c': 6}
    # 使用d2更新d1
    d1.update(d2)
    print(d1)


def defaultdict_test():
    WORD_RE = re.compile(r'\w+')
    # 将list()函数, 作为default_factory; 如果index[key]的值不存在, 则使用default_factory创建默认值;
    # 如果没有提供作为default_factory, 遇到缺失的键会抛出KeyError
    # defaultdict只会为index[key]提供初始化的默认值, 但是index.get(key)依然会返回None, 而且key in index 也会返回False
    index = collections.defaultdict(default_factory=list)
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index[word].append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])


def chain_map_test():
    d1 = dict(a=1, b=2)
    d2 = dict(a=6, c=3, d=4)
    c1 = ChainMap(d1, d2)
    print(c1['a'])
    print(c1['d'])
    # 只影响第一个映射
    c1['c'] = -1
    print(d1)
    print(d2)


def buildin_test():
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    print(pylookup)


def method_counter_test():
    # 可以查找键的数量
    ct = Counter('abracadabra')
    print(ct)
    ct.update('aaaaazzz')
    print(ct)
    mc = ct.most_common(3)
    print(mc)


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value

def immutable_mapping():
    d1 = {'a': 1, 'b': 3}
    d2 = MappingProxyType(d1)
    print(d2)
    # 不可访问的
    d2['a'] = 2

def dict_values_view():
    d1 = {'a': 1, 'b': 3}
    # values视图是可迭代的
    values = d1.values()
    print(values)
    print(len(values))
    print(list(values))
    # 视图实现了__reversed__方法, 返回一个自定义迭代器
    print(reversed(values))
    # 不支持获取视图中的项
    # print(values[0])
    d1['c'] = 4
    # 视图是动态代理的, 原dict更新后, 视图会同步更新
    # 视图支持&、|、-、^等四种集合运算; 仅当dict中的所有值均可哈希时, dict_items视图才可当做集合使用
    print(values)

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
    # defaultdict_test()
    # chain_map_test()
    # buildin_test()
    # method_counter_test()
    # immutable_mapping()
    dict_values_view()