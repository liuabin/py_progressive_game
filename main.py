# 游戏 main

from click import getchar
# from keyboard import is_pressed, read_key

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
    frame_count = 0
    while True:
        # 阻塞输入
        c = getchar()
        if c == QUIT:
            break

        # if is_pressed('q'):
        #     break

        # c = read_key()
        # print(c)

        handler(c)
        display()
        print(frame_count)
        frame_count += 1
    final()


def final():
    # 游戏结束运行后
    pass


main()
