# 定义 左上为 (0,0)

X = 20
Y = 10

# class character:
#     def __init__(self):
#         self.location = [0,0]

location = [0, 0]
velocity = [0, 0]


# 每帧更新数据
def update():
    move(velocity[0], velocity[1])


def set_v(x: int, y: int):
    velocity[0] = x
    velocity[1] = y


def move(x: int, y: int):
    location[0] += x
    location[1] += y

    if location[0] < 0:
        location[0] = 0
    elif location[0] >= X:
        location[0] = X-1

    if location[1] < 0:
        location[1] = 0
    elif location[1] >= Y:
        location[1] = Y-1
    # # DEBUG
    # print(location)


def get_location():
    return (location[0], location[1])
