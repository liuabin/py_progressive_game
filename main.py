# 游戏 main

from click import getchar

from handler import handler
from displayer import display

# 常量
QUIT = 'q'


def main():
    print("hello game.")

    # 游戏初始化
    # TODO: 因为是阻塞式输入所以多一个display
    display()

    # 游戏主循环
    c = ''
    while True:
        # 阻塞输入
        c = getchar()
        if c == QUIT:
            break

        handler(c)
        display()
    final()


def final():
    # 游戏结束运行后
    pass


main()
