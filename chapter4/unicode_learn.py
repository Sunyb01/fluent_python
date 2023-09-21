# coding: utf-8
# 字符问题
# Note:
#      1. 可以使用熟悉的字符串方法处理二进制序列, 如:endswith、replace、strip、translate、upper等
#      2. 如果正则表达式编译自二进制序列而不是字符串, 那么re模块中的正则表达式函数也能处理二进制序列
# 推荐使用unicodedata下的normalize处理数据, 类型为NFC
# 库pyuca可以处理一些语言的排序问题, 更加稳定的是PyICU库(但是有一个扩展必须安装, 在某些系统中可能比单纯使用pyuca难安装)
# f'{}'字符串格式化
# r'\d+'正则匹配
import array
import os
import locale
import sys
import unicodedata
from unicodedata import normalize, name


def code():
    # 把码点转换为字节序列称为编码; 把字节序列转为码点称为解码
    # 将字节序列变为人类可读的字符串是解码, 将字符串变成用于存储或传输的字节序列是编码
    s = 'cafe'
    print(len(s))
    # 编码
    b = s.encode('utf-8')
    print(b)
    # 解码
    s2 = b.decode('utf-8')
    print(s2)


def bytes_and_bytearray():
    cafe = bytes('cafe', encoding='utf_8')
    print(cafe)
    # cafe[0] 和 cafe[:1]的结果不同的原因; 习惯了python的str后, 对于str类型来说, 默认了s[0] == s[:1]
    print(cafe[0])
    print(cafe[:1])
    cafe_arr = bytearray(cafe)
    print(cafe_arr)
    print(cafe_arr[:1])


def parse_hex():
    print(bytes.fromhex('31 4B CE A9'))


def array_2_bytes():
    numbers = array.array('h', [-2, -1, 0, 1, 2, ])
    octets = bytes(numbers)
    print(octets)


def for_loop_codec():
    for codec in ['latin_1', 'utf_8', 'utf_16', ]:
        print(codec, 'El Nino'.encode(codec), sep='\t')


def process_str():
    with open('cafe.txt', 'w', encoding='utf_8') as fp:
        # 空格占用一个字节
        fp.write("hello world!")

    size = os.stat('cafe.txt').st_size
    print(size)
    with open('cafe.txt', 'r') as fp:
        print(fp.encoding)
        print(fp)
        for line in fp.readlines():
            print(line)
    with open('cafe.txt', 'rb') as fp:
        print(fp)
        for line in fp.readlines():
            print(line)


def print_default_env():
    expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
    my_file = open('dummy', 'w')
    for expression in expressions.split():
        value = eval(expression)
        print(f'{expression:>30} -> {value!r}')


def normalize_test():
    ohm = '\u2126'
    print(name(ohm))
    ohm_c = normalize('NFC', ohm)
    print(name(ohm_c))
    print(ohm == ohm_c)
    print(normalize('NFC', ohm) == normalize('NFC', ohm_c))


START, END = ord(' '), sys.maxunicode + 1


def find_unicode_from(*query_words, start=START, end=END):
    query = {w.upper() for w in query_words}
    for code in range(START, END):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name and query.issubset(name.split()):
            print(f'U+{code:04X}\t{char}\t{name}')


def main(words):
    if words:
        find_unicode_from(*words)
    else:
        print("Please provide")


if __name__ == '__main__':
    # code()
    # bytes_and_bytearray()
    # parse_hex()
    # array_2_bytes()
    # for_loop_codec()
    # process_str()
    # print_default_env()
    # normalize_test()
    main(sys.argv[1:])
