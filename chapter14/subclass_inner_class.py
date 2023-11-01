# 子类化内置类型

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

if __name__ == '__main__':
    non_expect_result()
