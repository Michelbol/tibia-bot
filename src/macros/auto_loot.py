from pynput.keyboard import Key, Controller
import pyautogui
from environment import Environment

CENTER_SQM_DISTANCE = 40

class AutoLoot:

    def __init__(self, player) -> None:
        self.player = player
        self.PADDING = Environment.resolveAutoLootPadding()
        self.keyboard = Controller()
    
    def loot(self):
        if(self.player.justKillAMonster):
            self.lootArroundPlayer()

    def lootArroundPlayer(self):
        self.lootCenter()

        # Click Top Center
        self.lootTopCenter()

        # Click Top Right
        self.lootTopRight()

        #Click Center Right
        self.lootCenterRight()

        #Click Down Right
        self.lootDownRight()

        #Click Down Center
        self.lootDownCenter()

        #Click Down Left
        self.lootDownLeft()

        #Click Center Left
        self.lootCenterLeft()

        #Click Top Left
        self.lootTopLeft()

    def lootCenter(self):
        self.executeHotkeyLoot(*self.getCoordsCenterAutoLoot())
        self.executeHotkeyLoot(*self.getCoordsCenterAutoLoot())
    
    def lootTopCenter(self):
        self.executeHotkeyLoot(*self.getCoordsTopCenter())
        self.executeHotkeyLoot(*self.getCoordsTopCenter())
    
    def lootTopRight(self):
        self.executeHotkeyLoot(*self.getCoordTopRight())
        self.executeHotkeyLoot(*self.getCoordTopRight())
    
    def lootCenterRight(self):
        self.executeHotkeyLoot(*self.getCoordCenterRight())
        self.executeHotkeyLoot(*self.getCoordCenterRight())

    def lootDownRight(self):
        self.executeHotkeyLoot(*self.getCoordDownRight())
        self.executeHotkeyLoot(*self.getCoordDownRight())
    
    def lootDownCenter(self):
        self.executeHotkeyLoot(*self.getCoordDownCenter())
        self.executeHotkeyLoot(*self.getCoordDownCenter())
    
    def lootDownLeft(self):
        self.executeHotkeyLoot(*self.getCoordDownLeft())
        self.executeHotkeyLoot(*self.getCoordDownLeft())

    def lootCenterLeft(self):
        self.executeHotkeyLoot(*self.getCoordCenterLeft())
        self.executeHotkeyLoot(*self.getCoordCenterLeft())

    def lootTopLeft(self):
        self.executeHotkeyLoot(*self.getCoordTopLeft())
        self.executeHotkeyLoot(*self.getCoordTopLeft())

    def executeHotkeyLoot(self, x, y):
        self.keyboard.press(Key.shift)
        pyautogui.rightClick(x, y)
        self.keyboard.release(Key.shift)

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
    
