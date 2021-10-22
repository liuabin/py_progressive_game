# 这里大概之后会成为一个模块
file_name = '../map.txt'

s = []

with open(file_name, 'r') as f:
    s = f.readline()

print([s])
