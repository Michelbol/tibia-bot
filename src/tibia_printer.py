from pynput.keyboard import Key, Controller
import time

HOTKEY_TO_PRINT = Key.scroll_lock

class TibiaPrinter:
    
    def print(self):
        keyboard = Controller()
        keyboard.press(HOTKEY_TO_PRINT)
        keyboard.release(HOTKEY_TO_PRINT)
        time.sleep(1)