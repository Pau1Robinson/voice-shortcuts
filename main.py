import pynupt

def main():
    
    while(True):
        set_pressed = key_listen()
        if '/' in set_pressed:
            loader = AutoLoad(capture, mouse)
            loader.auto_load()

def key_listen():

    pressed = set()

    def on_release(key):
        pressed.add(str(key)[1])
        listener.stop()

    with pynput.keyboard.Listener(on_release=on_release) as listener:
        listener.join()
    
    return(pressed)

if __name__ == "__main__":
    print('Voice shortcuts ready press / to listen')
    main()