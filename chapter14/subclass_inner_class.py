# 子类化内置类型
import collections


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

def non_expect_result():
    dd = DoppelDict(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    # 这里没有出现预期的[3, 3]
    dd.update(three=3)
    print(dd)


class AnswerDict(dict):

    def __getitem__(self, item):
        return 42



def override_parent_method():
    ad = AnswerDict(a='foo')
    print(ad['a'])
    print(ad.get('a'))
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)


class DoppelDict2(collections.UserDict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

def use_user_dict_subclass():
    dd = DoppelDict2(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)


class AnswerDict2(collections.UserDict):

    def __getitem__(self, item):
        return 42

def override_parent_method2():
    ad = AnswerDict2(a='foo')
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)

# 多继承出现的 菱形继承问题(Java不支持多继承, 但是多实现时也可能出现)
# 唤醒过程取决于子类声明罗列的父类的顺序, 即按照生命的顺序依次唤醒; 如果声明的父类也有父类, 那么按照继承关系向上查找, 然后结束, 进行下一个父类, 依次类推
# 其中利用协作方法可以实现协作多重继承. super().override_method(), 依次传递, 依次唤醒;
class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'

class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()

class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')

class Leaf(A, B):
    def ping(self):
        """ 调用路线为 A -> B -> Root"""
        print(f'{self}.ping() in Leaf')
        # 协作方法
        super().ping()

def use_leaf_test_diamond_inheritance():
    leaf1 = Leaf()
    print("----- ping ---- \n")
    leaf1.ping()
    print("----- pong ---- \n")
    # B 的pong()方法中,没有调用父类的, 所以在B就结束了
    # 整个方法的链路为 A -> B
    leaf1.pong()
    print("----- __mro__ ---- \n")
    print(Leaf.__mro__)


class U:
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()

class LeafU(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafU')
        # 目前是(U, A),
        # 当前方法的super().ping() 唤醒了 U; 然后U执行ping(), 内部执行了super().ping()唤醒了A; 然后A执行ping(), 内部执行了super().ping()唤醒了Root
        # 如果为(A, U) 则不会唤醒U.ping(), 因为A唤醒了其父类Root, 但是Root的ping()方法没有在进行协作调用;
        super().ping()

class LeafU2(A, U):
    def ping(self):
        print(f'{self}.ping() in LeafU')
        # 目前是(U, A),
        # 当前方法的super().ping() 唤醒了 U; 然后U执行ping(), 内部执行了super().ping()唤醒了A; 然后A执行ping(), 内部执行了super().ping()唤醒了Root
        # 如果为(A, U) 则不会唤醒U.ping(), 因为A唤醒了其父类Root, 但是Root的ping()方法没有在进行协作调用;
        super().ping()

def use_cooperation_extend():
    print('----- u1---- \n')
    u1 = LeafU()
    u1.ping()
    print(LeafU.__mro__)
    print('\n')
    print('----- u2---- \n')
    u2 = LeafU2()
    u2.ping()
    print(LeafU2.__mro__)


if __name__ == '__main__':
    # non_expect_result()
    # override_parent_method()
    # use_user_dict_subclass()
    # override_parent_method2()
    # use_leaf_test_diamond_inheritance()
    use_cooperation_extend()