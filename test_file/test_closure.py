def main():
    l = [1]
    handler(l)('liuabin')
    print(l)


def handler(ref: list):
    def _handler(res: str):
        ref[0] += 1
        print(res)
    return _handler


main()
