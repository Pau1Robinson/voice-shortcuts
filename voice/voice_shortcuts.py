import speech_recognition as sr

class Voice():
    """

    """
    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.controller = self.keyboard.Controller()
        self.shortcuts_dict = {
            'task manager':((self.keyboard.Key.ctrl_l, self.keyboard.Key.shift_l), self.keyboard.Key.esc)
        }

    def listen(self):
        print("listening ....")
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            audio = r.listen(source)
        response = r.recognize_google(audio)
        print(response)
        return(response)
    
    def open_shortcut(self):
        response = self.listen()
        print(f'detected {response}')
        if response in self.shortcuts_dict:
            print(f'opening {response}')
            #TODO make number of modifers varable
            with self.controller.pressed(self.shortcuts_dict[response][0][0], self.shortcuts_dict[response][0][1]):
                self.controller.press(self.shortcuts_dict[response][1])
        else:
            print('shortcut not found')
