# 游戏 main

from click import getchar

# 常量
QUIT = 'q'

def main():
    print("hello game.")
    
    # 游戏主循环
    c = ''
    while c != QUIT:
        c = getchar()
        print(c)

main()