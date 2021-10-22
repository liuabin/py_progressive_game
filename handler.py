# 按键处理器
from keyboard import KeyboardEvent

from data import set_v

DIRECTIONS = {
    'w': 0,
    's': 1,
    'a': 2,
    'd': 3,
}


def handler(close: list):
    def _handler(c: KeyboardEvent):
        if c.name in DIRECTIONS:
            _move_handler(c)
        else:
            # 交叉引用
            # 怎么把关闭信息回传给主循环
            # from main import close
            # close()
            # 使用闭包
            close[0] = True
    return _handler


_move_vector = [0, 0, 0, 0]


def _move_handler(c: KeyboardEvent):
    global _move_vector

    if c.event_type == 'down':
        _move_vector[DIRECTIONS[c.name]] = 1
    else:
        _move_vector[DIRECTIONS[c.name]] = 0
    set_v(_move_vector[3]-_move_vector[2],
          _move_vector[1]-_move_vector[0])
