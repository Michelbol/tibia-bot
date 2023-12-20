from pynput.keyboard import Key, Controller
import time

class Walk:

    HOTKEY_LEFT = Key.left
    HOTKEY_RIGHT = Key.right
    HOTKEY_UP = Key.up
    HOTKEY_DOWN = Key.down

    def __init__(self) -> None:
        self.keyboard = Controller()

    def walk(self, key):
        time.sleep(3)
        self.keyboard.press(key)
        self.keyboard.release(key)
        time.sleep(1)

    def left(self):
        self.walk(self.HOTKEY_LEFT)

    def right(self):
        self.walk(self.HOTKEY_RIGHT)

    def up(self):
        self.walk(self.HOTKEY_UP)

    def down(self):
        self.walk(self.HOTKEY_DOWN)