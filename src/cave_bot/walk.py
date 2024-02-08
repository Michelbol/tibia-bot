from pynput.keyboard import Key, Controller
import time

class Walk:

    HOTKEY_LEFT = Key.left
    HOTKEY_RIGHT = Key.right
    HOTKEY_UP = Key.up
    HOTKEY_DOWN = Key.down

    def walk(key):
        keyboard = Controller()
        time.sleep(3)
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(1)

    def left():
        Walk.walk(Walk.HOTKEY_LEFT)

    def right():
        Walk.walk(Walk.HOTKEY_RIGHT)

    def up():
        Walk.walk(Walk.HOTKEY_UP)

    def down():
        Walk.walk(Walk.HOTKEY_DOWN)