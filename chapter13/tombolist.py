# 虚拟子类

from random import randrange
from abstract_base_class import Tombola

# 类的继承关系是在一个名为 __mro__ 的特殊类属性中指定的; 它会按照顺序列出类及其超类, 而Python会按照这个顺序搜索方法.
# 在Python3.3之前不能这样定义虚拟子类的关系
# @Tombola.register  # 把TomboListList注册为Tombola的虚拟子类
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(self)


if __name__ == '__main__':
    print(issubclass(TomboList, Tombola))
    print(TomboList.__mro__)
    # 在Python3.3之前必须使用下面这种方式建立虚拟子类的关系
    Tombola.register(TomboList)
    print(issubclass(TomboList, Tombola))
