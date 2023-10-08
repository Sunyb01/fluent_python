# 匿名函数
# lambda关键字是使用Python表达式创建匿名函数
# Note:
#     1. 不能有while、try等语句
#     2. '='号赋值也是一种语句, 也不能出现
#     3. 只能是最纯粹的表达式
# 如果一个lambda表达式可读性低, 那么应该将其重构为def定义的函数


def refactor_sorted_fruits():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(fruits)
    fruits = sorted(fruits, key=lambda word: word[::-1])
    print(fruits)


if __name__ == '__main__':
    refactor_sorted_fruits()
