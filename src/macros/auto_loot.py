from pynput.keyboard import Key, Controller
import pyautogui
from environment import Environment

CENTER_SQM_DISTANCE = 80

class AutoLoot:

    def __init__(self, player) -> None:
        self.player = player
        self.PADDING = Environment.resolveAutoLootPadding()
    
    def loot(self):
        if(self.player.justKillAMonster):
          self.lootArroundPlayer()

    def lootArroundPlayer(self):

        # Click Center
        pyautogui.moveTo(*AutoLoot.getCoordsCenterAutoLoot())
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()

        # Click Top Center
        pyautogui.moveTo(*AutoLoot.getCoordsTopCenter())
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()

        # Click Top Right
        pyautogui.moveTo(*AutoLoot.getCoordTopRight())
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()

        #Click Center Right
        pyautogui.moveTo(*AutoLoot.getCoordCenterRight())
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()

        #Click Down Right
        pyautogui.moveTo(*AutoLoot.getCoordDownRight())
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()

        #Click Down Center
        pyautogui.moveTo(*AutoLoot.getCoordDownCenter())
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()

        #Click Down Left
        pyautogui.moveTo(*AutoLoot.getCoordDownLeft())
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()

        #Click Center Left
        pyautogui.moveTo(*AutoLoot.getCoordCenterLeft())
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()

        #Click Top Left
        pyautogui.moveTo(0,-50)
        AutoLoot.executeHotkeyLoot()
        AutoLoot.executeHotkeyLoot()


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
