# deque, 应该是链表的一种实现方式
# append和popleft是原子操作

from collections import deque

def first_deque():
    dq = deque(range(10), maxlen=10)
    print(dq)
    # 轮转, n > 0 从右端取几项到左侧
    dq.rotate(3)
    print(dq)
    # 轮转, n < 0 从左端取几项放入右端
    dq.rotate(-4)
    print(dq)
    # 左侧添加, 容量已满, 会从右侧抛弃
    dq.appendleft(-1)
    print(dq)
    # 右侧添加, 容量已满会从左侧抛弃
    dq.extend([11, 22, 33, ])
    print(dq)
    # 左侧批量添加
    dq.extendleft([10, 20, 30, 40, ])
    print(dq)

if __name__ == '__main__':
    first_deque()
