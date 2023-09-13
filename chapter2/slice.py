# 切片
# golang中也有切片, 但是对于切片的操作来说, python还是跟方便的
# python为[startIndex, endIndex, step], golang为[startIndex, endIndex]
# 都是[startIndex,endIndex)
# numpy 中也可以对二维数组快捷操作[m:n, j:k]
def split_slice_with_index(tar, mark=0):
    if tar:
        left = tar[:mark]
        right = tar[mark:]
        print(f'left is {left} \n right is {right}')


def slice_split(tar, sl=slice(1, )):
    print(tar[sl])


def test_step(tar, step=1):
    s1 = tar[::step]
    print(s1)


def test_assign_slice():
    # 赋值目标是切片, 右边必须是一个可迭代对象
    l = list(range(10))
    print(l)
    # 下标2, 3, 4, 依次赋值;
    # 如果右边的数量大于左边的下标差, 就会添加进列表
    l[2:5] = [20, 30, ]
    print(l)
    # 删除下标5, 6的值
    del l[5:7]
    print(l)
    # 下标3开始, 步长为2赋值
    l[3::2] = [11, 22]
    print(l)
    # 右边不是一个可迭代对象, 所以这里会报错
    # l[2:5] = 100
    l[2:5] = [100]
    print(l)


def fast_append():
    # '+' 和 '*'始终都是创建一个新对象
    # 注意: 如果序列中包含可变项, 会出现意料之外的事
    # l = [[]] * 3初始化一个列表, 但是嵌套的3个引用指向同一个列表
    l = [1, 2, 3]
    l2 = 5 * l
    print(f'l is {l} \n l2 is {l2}')
    print(5 * 'abc')
    l3 = [5, 6, 7]
    print(l + l3)


def test_nested_list():
    board = [['_'] * 3 for i in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)
    print('wrong ==========')
    b2 = [['_'] * 3] * 3
    b2[1][2] = 'X'
    print(b2)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7]
    # split_slice_with_index(l, 4)
    # test_step(l, -2)
    # slice_split(l, slice(1,len(l)))
    # test_assign_slice()
    # fast_append()
    test_nested_list()
