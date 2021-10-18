# 游戏 main

# from time import sleep
from click import getchar
# import keyboard
# from keyboard import is_pressed
# 自定义库
from handler import handler
from displayer import display

# 常量表
QUIT = 'q'

# 全局变量


def main():
    init()

    # TODO: 因为是阻塞式输入所以多一个display
    display()

    # 游戏主循环
    c = ['']  # 用以传引用
    game_should_close = False
    while not game_should_close:
        # 阻塞输入
        game_should_close = check_input(c)

        handler(c[0])
        display()
    final()


def init():
    # 游戏初始化
    print('Game Loading...')
    # sleep(1)


def check_input(c: list) -> bool:
    c[0] = getchar()
    if c[0] == QUIT:
        return True


def final():
    # 游戏结束运行后
    print('Game Over')


main()
