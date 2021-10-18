import keyboard

should_close = False

def main():
    keyboard.hook(hook)
    while not should_close:
        pass


def hook(c: keyboard.KeyboardEvent):
    global should_close
    
    print(c.name, c.event_type)
    if c.name == 'q':
        should_close = True

main()
