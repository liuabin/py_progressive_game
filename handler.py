# 按键处理器
from data import move

# direction = {
#     'w':
# }


def handler(c: str):
    print(c)  # , type(c))

    # 暂时用最简单的if else
    if c == 'w':
        move(0, -1)
    elif c == 's':
        move(0, 1)
    elif c == 'a':
        move(-1, 0)
    elif c == 'd':
        move(1, 0)
