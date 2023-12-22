from pynput.keyboard import Key, Controller
import pyautogui


class AutoLoot:

    def __init__(self, player) -> None:
        self.player = player
    
    def loot(self):
        if(self.player.justKillAMonster):
          self.lootArroundPlayer()

    def lootArroundPlayer(self):
        (x,y) = pyautogui.size()
        middleX = x/2
        middleY = y/2

        # Click Center
        pyautogui.moveTo(middleX,middleY)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        # Click Top Center
        pyautogui.moveRel(0,50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        # Click Top Right
        pyautogui.moveRel(50,0)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Center Right
        pyautogui.moveRel(0,-50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Right
        pyautogui.moveRel(0,-50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Center
        pyautogui.moveRel(-50,0)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Left
        pyautogui.moveRel(-50,0)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Center Left
        pyautogui.moveRel(0,-50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Top Left
        pyautogui.moveRel(0,-50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()


    def executeHotkeyLoot(self):
        keyboard = Controller()
        keyboard.press(Key.shift)
        pyautogui.rightClick()
        keyboard.release(Key.shift)