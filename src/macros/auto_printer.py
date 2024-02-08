from pynput.keyboard import Key, Controller
import time

class AutoPrinter:
    HOTKEY_TO_PRINT = Key.scroll_lock
    
    def print(self):
        keyboard = Controller()
        keyboard.press(AutoPrinter.HOTKEY_TO_PRINT)
        keyboard.release(AutoPrinter.HOTKEY_TO_PRINT)
        time.sleep(1)