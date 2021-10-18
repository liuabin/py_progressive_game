# 游戏 main

from time import sleep, time
# from click import getchar
import keyboard
from keyboard import is_pressed
# 自定义库
from handler import handler
from data import update
from displayer import display

# 常量表
QUIT = 'q'

# 全局变量


def main():
    init()

    # # TODO: 因为是阻塞式输入所以多一个display
    # display()

    # 游戏主循环
    # 运行时常量
    # c = ['']  # 用以传引用
    game_should_close = False
    start_time = time()
    while not game_should_close:
        # # 阻塞输入
        # game_should_close = check_input(c)

        # 开始以固定帧率刷新
        if is_pressed('q'):
            game_should_close = True
        # 必须加上数据的更新
        update()
        display()

        # sleep(0.2)
        temp_time = time() - start_time
        if temp_time >= 1.0:
            print('每秒帧率\n消耗时间',temp_time)
            break
    final()


def init():
    # 游戏初始化
    print('Game Loading...')
    keyboard.hook(handler)
    # sleep(1)


# def check_input(c: list) -> bool:
#     c[0] = getchar()
#     if c[0] == QUIT:
#         return True


def final():
    # 游戏结束运行后
    print('Game Over')


main()
