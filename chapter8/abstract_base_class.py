# 抽象基类
from collections.abc import Mapping
from typing import Iterable

# 发送时要保守, 接收时要大方;
"""
    由于类型注解为abc.Mapping, 因此调用方可以提供dict、defaultdict、ChainMap的实例, UserDict子类的实例, 或者Mapping的任何子类型
    但是注解为dict的, 必须是dict或其子类型; 如defaultDict或OrderedDict; 注意使用collections.UserDict的子类型无法通过类型检查;
    UserDict和dict是同级关系, 都是abc.MutableMapping的子类;
    一般来说在参数的类型提示中最好使用abc.Mapping或abc.MutableMapping
"""
def name2hex(name: str, color_map: Mapping[str, int]) -> str:
    pass


def name2hex2(name: str, color_map: dict[str, int]) -> str:
    pass

# Iterable 可迭代对象
def zip_replace(text: str, changes: Iterable[tuple[str, str]]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text

def use_iterable():
    l33t = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'), ]
    text = 'mad skilled noob powned leet'
    print(zip_replace(text, l33t))

if __name__ == '__main__':
    use_iterable()