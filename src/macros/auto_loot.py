from pynput.keyboard import Key, Controller
import pyautogui
from environment import Environment

CENTER_SQM_DISTANCE = 40

class AutoLoot:

    def __init__(self, player) -> None:
        self.player = player
        self.PADDING = Environment.resolveAutoLootPadding()
    
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
        pyautogui.moveTo(*self.getCoordCenterRight())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Right
        pyautogui.moveTo(*self.getCoordDownRight())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Center
        pyautogui.moveTo(*self.getCoordDownCenter())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Down Left
        pyautogui.moveTo(*self.getCoordDownLeft())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Center Left
        pyautogui.moveTo(*self.getCoordCenterLeft())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()

        #Click Top Left
        pyautogui.moveTo(*self.getCoordTopLeft())
        self.executeHotkeyLoot()
        self.executeHotkeyLoot()


    def executeHotkeyLoot(self):
        keyboard = Controller()
        keyboard.press(Key.shift)
        pyautogui.rightClick()
        keyboard.release(Key.shift)

    def getCoordsCenterAutoLoot(self):
        (x,y) = pyautogui.size()
        (characterX, characterY) = (x/2, y/2)
        return (characterX+self.PADDING['x'], characterY+self.PADDING['y'])
    
    def getCoordsTopCenter(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX, middleY-CENTER_SQM_DISTANCE)
    
    def getCoordTopRight(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX+CENTER_SQM_DISTANCE, middleY-CENTER_SQM_DISTANCE)
    
    def getCoordCenterRight(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX+CENTER_SQM_DISTANCE, middleY)
    
    def getCoordDownRight(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX+CENTER_SQM_DISTANCE, middleY+CENTER_SQM_DISTANCE)
    
    def getCoordDownCenter(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX, middleY+CENTER_SQM_DISTANCE)
    
    def getCoordDownLeft(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX-CENTER_SQM_DISTANCE, middleY+CENTER_SQM_DISTANCE)
    
    def getCoordCenterLeft(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX-CENTER_SQM_DISTANCE, middleY)
    
    def getCoordTopLeft(self):
        (middleX, middleY) = self.getCoordsCenterAutoLoot()
        return (middleX-CENTER_SQM_DISTANCE, middleY-CENTER_SQM_DISTANCE)
