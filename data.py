# 定义 左上为 (0,0)

X = 10
Y = 10

# class character:
#     def __init__(self):
#         self.location = [0,0]

location = [0, 0]

def move(x:int, y:int):
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