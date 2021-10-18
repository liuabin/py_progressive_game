# 按键处理器
from keyboard import KeyboardEvent

from data import set_v

DIRECTIONS = {
    'w': 0,
    's': 1,
    'a': 2,
    'd': 3,
}

move_vector = [0, 0, 0, 0]
def handler(c: KeyboardEvent):
    global move_vector
    
    if c.event_type == 'down':
        move_vector[DIRECTIONS[c.name]] = 1
    else:
        move_vector[DIRECTIONS[c.name]] = 0
    set_v(move_vector[3]-move_vector[2],
         move_vector[1]-move_vector[0])


def _handler(c: str):
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
