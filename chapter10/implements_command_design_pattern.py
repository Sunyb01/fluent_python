# 命令模式
# 命令模式的目的是解耦调用操作的对象(调用者)和提供实现的对象(接收者).
# 比如异步里面的回调

class MacroCommand:
    """
        一个执行一组命令的命令
    """
    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()