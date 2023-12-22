from pynput.keyboard import Key, Controller
import pyautogui


class AutoLoot:

    def __init__(self, player) -> None:
        self.player = player
    
    def loot(self):
        if(self.player.justKillAMonster):
          self.lootArroundPlayer()

    def lootArroundPlayer(self):

        # Click Center
        pyautogui.moveTo(*self.getCoordsCenterAutoLoot())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        # Click Top Center
        pyautogui.moveTo(*self.getCoordsTopCenter())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        # Click Top Right
        pyautogui.moveTo(*self.getCoordTopRight())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Center Right
        pyautogui.moveTo(0,-50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Right
        pyautogui.moveTo(0,-50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Center
        pyautogui.moveTo(-50,0)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Left
        pyautogui.moveTo(-50,0)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Center Left
        pyautogui.moveTo(0,-50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Top Left
        pyautogui.moveTo(0,-50)
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()


    def executeHotkeyLoot(self):
        keyboard = Controller()
        keyboard.press(Key.shift)
        pyautogui.rightClick()
        keyboard.release(Key.shift)

    def getCoordsCenterAutoLoot(self):
        (x,y) = pyautogui.size()
        return (y/2, x/2)
    
    def getCoordsTopCenter(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX, middleY+50)
    
    def getCoordTopRight(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX+50, middleY+50)
    