"""
Contains class for activating voice shortcuts
"""

class Voice():
    """
    Class for activating keyboard shortcuts using the python speech recognition library
    variables:
    self.keyboard: pynput keyboard class
    self.recongiser: speechrecognition Recognizer
    self.mic: speechrecognition Microphone
    self.controller: pynput keyboard controller
    self.shortcuts_dict: dictionary containing the shortcuts able to be activated stored as
    'string name of shortcut to be spoken':((tuple of modifer keys), key press to activate shortcut)
    """
    def __init__(self, keyboard, sr):
        self.keyboard = keyboard
        self.recogniser = sr.Recognizer()
        self.mic = sr.Microphone()
        self.controller = self.keyboard.Controller()
        self.shortcuts_dict = {
            'task manager':((self.keyboard.Key.ctrl_l, self.keyboard.Key.shift_l), self.keyboard.Key.esc)
        }

    def listen(self):
        """
        Method for listening for microphone input using speechrecognition and returning the resulting string
        """
        print("listening ....")
        with self.mic as source:
            audio = self.recogniser.listen(source)
        response = self.recogniser.recognize_google(audio)
        print(f'detected {response}')
        return response

    def open_shortcut(self):
        """
        Method for opening shortcuts in shortcuts_dict using string from listen() method and pynput
        """
        response = self.listen()
        if response in self.shortcuts_dict:
            print(f'opening {response}')
            with self.controller.pressed(*self.shortcuts_dict[response][0]):
                self.controller.press(self.shortcuts_dict[response][1])
        else:
            print('shortcut not found')
