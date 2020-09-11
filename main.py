import pynput

from voice.voice_shortcuts import Voice

keyboard = pynput.keyboard

def main():
    
    while(True):
        set_pressed = key_listen()
        if '/' in set_pressed:
            v = Voice(keyboard)
            v.open_shortcut()

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