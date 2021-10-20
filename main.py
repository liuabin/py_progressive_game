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
    game_should_close = [False]

    init(game_should_close)

    # 游戏主循环
    # start_time = time()
    # c = ['']  # 用以传引用
    while not game_should_close[0]:
        f_time = time()

        if is_pressed('q'):
            game_should_close[0] = True
        # 必须加上数据的更新
        update()
        display()

        # !锁帧 30 fps
        while time() <= f_time + 0.033:
            pass
        # 检测帧数
        # temp_time = time() - start_time
        # if temp_time >= 1.0:
        #     print('每秒帧率\n消耗时间',temp_time)
        #     break
    final()


def init(game_should_close: list):
    # 游戏初始化
    print('Game Loading...')
    # 注册输入 handler
    keyboard.hook(handler(game_should_close))


# def check_input(c: list) -> bool:
#     c[0] = getchar()
#     if c[0] == QUIT:
#         return True


def final():
    # 游戏结束运行后
    print('Game Over')


def close():
    global game_should_close

    game_should_close = True


main()
