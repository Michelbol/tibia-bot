from pynput.keyboard import Key, Controller
import time

class Player:

    def execute(self, actions): 
        for action in actions:
            if(action != None and action['hotkeyToPress'] != None):
                print('Irá pressionar a tecla: '+str(action['hotkeyToPress']))
                keyboard = Controller()
                keyboard.press(action['hotkeyToPress'])
                time.sleep(0.1)
                keyboard.release(action['hotkeyToPress'])
