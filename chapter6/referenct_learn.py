# 变量引用
# 变量不是盒子, 变量是便利贴;
# 如 x = dict(), 先执行'='号右侧, 进行实例的创建, 然后将变量x绑定到创建的实例上; 或者可以说将创建的实例赋值给变量x

def same_equal_alias():
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    print(lewis is charles)
    print(id(charles), id(lewis))
    lewis['balance'] = 950
    print(charles)

if __name__ == '__main__':
    same_equal_alias()