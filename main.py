"""
small project for experimenting with speech recognition by opening shortcuts
using pynput by moses-palmer and speechrecognition by Uberi
"""

import pynput
import speech_recognition as sr

from voice.voice_shortcuts import Voice

def main():
    """
    function for calling Voice.open_shortcut if / is pressed
    """
    while True:
        set_pressed = key_listen()
        if '/' in set_pressed:
            voice = Voice(pynput.keyboard, sr)
            voice.open_shortcut()

def key_listen():
    """
    function for detecting key presses and returning them in a set
    """

    pressed = set()

    def on_release(key):
        pressed.add(str(key)[1])
        listener.stop()

    with pynput.keyboard.Listener(on_release=on_release) as listener:
        listener.join()

    return pressed

if __name__ == "__main__":
    print('Voice shortcuts ready press / to listen')
    main()
