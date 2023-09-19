# 字符问题
# Note:
#      1. 可以使用熟悉的字符串方法处理二进制序列, 如:endswith、replace、strip、translate、upper等
#      2. 如果正则表达式编译自二进制序列而不是字符串, 那么re模块中的正则表达式函数也能处理二进制序列

import array
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


if __name__ == '__main__':
    # code()
    # bytes_and_bytearray()
    # parse_hex()
    array_2_bytes()