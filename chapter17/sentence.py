# 把句子拆分成单次序列

import re
import reprlib

RE_WORD = re.compile(r'\w+')


# 迭代时Python会自动调用iter()方法, 然后检查对象是否实现了 __iter__()方法,
# 如果没有实现 __iter__()方法, 但是实现了 __getitem__()方法, 那么iter()创建一个迭代器, 并尝试按索引获取项
# 如果尝试失败, 则Python抛出TypeError异常;
# 所以从Python3.10开始, 检查对象x是否可迭代, 最准确的方式是调用iter(x), 如果不可迭代, 则处理TypeError异常即可;
# 如果实现了 __iter__()方法, 那么相当于实现了abc.Iterable;
# 如果调用issubclass(obj, abc.Iterable) 或 isinstance(obj, abc.Iterable) 都会返回True
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


def use_iter():
    s3 = Sentence('Life of Brian')
    it = iter(s3)
    print(it)
    print(next(it))
    print(next(it))
    print(next(it))
    # 没有元素了
    try:
        print(next(it))
    except StopIteration as e:
        print(e.value)

    # 消耗完毕了, 此时it中是空的
    # 和Java中的Stream是类似的, 一旦消耗过后, 不可重复使用, 只能重新生成
    print(list(it))
    # 创建新的迭代器
    print(list(iter(s3)))


# 经典迭代器
class Sentence2:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self):
        return f'fSentence({reprlib.repr(self.text)})'


# 如果是一个迭代器类型, 需要同时实现 __next__() 和 __iter__()方法;
class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    use_iter()
