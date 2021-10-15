# 显示

from os import system

from data import get_location, X, Y


def display():
    # # LOG
    x, y = get_location()
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
