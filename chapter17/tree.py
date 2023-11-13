#
def tree(cls):
    # 这里是相当于返回了一个元组, Go中与其一致; Rust需要手动返回元组; Java不支持
    # 依赖于解构
    yield cls.__name__, 0
    for sub_cls in cls.__subclasses__():
        yield sub_cls.__name__, 1


def display(cls):
    for cls_name, level in tree(cls):
        indent = ' ' * 4 * level
        print(f'{indent}{cls_name}')


if __name__ == '__main__':
    display(BaseException)
