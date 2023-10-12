# 函数中的类型提示
from typing import Optional


def show_count(count, word):
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'


def show_count2(count: int, singular: str, plural: str = '') -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}s'


def show_count3(count: int, singular: str, plural: Optional[str] = '') -> str:
    """
        当参数使用None作为默认值时, 可以使用Optional[param_type] = default_value, 必须显式的提供默认值
    :param count:
    :param singular:
    :param plural:
    :return:
    """
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}s'


class Bird:
    pass


class Duck(Bird):
    def quack(self):
        print('Quick!')


def alter(birdie):
    birdie.quack()


def alter_duck(birdie: Duck):
    birdie.quack()


def alter_bird(birdie: Bird):
    # 这里会提示: 类 'Bird' 的未解析的特性引用 'quack';
    # 但是也只是提醒, 如果出现错误将会在运行时报错, 编译器不会
    birdie.quack()


def daffy_duck_class():
    daffy = Duck()
    alter(daffy)
    alter_duck(daffy)
    alter_bird(daffy)


def woody_duck_class():
    woody = Bird()
    alter(woody)
    # 这里会失败
    alter_duck(woody)
    alter_bird(woody)

if __name__ == '__main__':
    # print(show_count(1, 'bird'))
    # print(show_count2(1, 'bird'))
    # daffy_duck_class()
    woody_duck_class()