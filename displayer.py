# 显示

from os import system

from data import get_location, X, Y

frame_count = 0


def display():
    x, y = get_location()
    # # LOG
    # print(x,y)

    # 清屏
    system('cls')

    # 绘制
    for _ in range(X + 2):
        print('-', end='')
    print()
    for _ in range(y):
        print('|', end='')
        for _ in range(X):
            print(' ', end='')
        print('|')
    print('|', end='')
    # 所在行
    for _ in range(x):
        print(' ', end='')
    print('*', end='')
    for _ in range(X-x-1):
        print(' ', end='')
    print('|\n', end='')
    #
    for _ in range(Y-y-1):
        print('|', end='')
        for _ in range(X):
            print(' ', end='')
        print('|')
    for _ in range(X + 2):
        print('-', end='')
    print()
    print(_one_frame())


def _one_frame() -> int:
    global frame_count

    frame_count += 1
    return frame_count
