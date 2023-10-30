# 定义抽象基类

import abc


# 整体上和Java中的抽象类相似
class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """ 从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """ 随机删除元素, 在返回被删除的元素.
            如果实例为空, 那么这个方法应该抛出LookupError
        """

    def loaded(self):
        """ 如果至少有一个元素, 就返回True, 否则返回False"""
        return bool(self.inspect())

    def inspect(self):
        """返回由容器中的当前元素构成的有序数组"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)

# 装饰器 @abc.abstractmethod 使用示例
class MyAbc(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def an_abstract_method(self):
        """ 与其他方法描述符一起使用时, abstractmethod应该放在最里层"""
        pass