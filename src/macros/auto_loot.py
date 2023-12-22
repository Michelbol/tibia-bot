from pynput.keyboard import Key, Controller
import pyautogui

PADDING = {
    'x': -130,
    'y': -80
}
CENTER_SQM_DISTANCE = 80

class AutoLoot:

    def __init__(self, player) -> None:
        self.player = player
    
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

    def getCoordsCenterAutoLoot():
        (x,y) = pyautogui.size()
        (characterX, characterY) = (x/2, y/2)
        return (characterX+PADDING['x'], characterY+PADDING['y'])
    
    def getCoordsTopCenter():
        (middleX, middleY) = AutoLoot.getCoordsCenterAutoLoot()
        return (middleX, middleY-CENTER_SQM_DISTANCE)
    
    def getCoordTopRight():
        (middleX, middleY) = AutoLoot.getCoordsCenterAutoLoot()
        return (middleX+CENTER_SQM_DISTANCE, middleY-CENTER_SQM_DISTANCE)
    
    def getCoordCenterRight():
        (middleX, middleY) = AutoLoot.getCoordsCenterAutoLoot()
        return (middleX+CENTER_SQM_DISTANCE, middleY)
    
    def getCoordDownRight():
        (middleX, middleY) = AutoLoot.getCoordsCenterAutoLoot()
        return (middleX+CENTER_SQM_DISTANCE, middleY+CENTER_SQM_DISTANCE)
    
    def getCoordDownCenter():
        (middleX, middleY) = AutoLoot.getCoordsCenterAutoLoot()
        return (middleX, middleY+CENTER_SQM_DISTANCE)
    
    def getCoordDownLeft():
        (middleX, middleY) = AutoLoot.getCoordsCenterAutoLoot()
        return (middleX-CENTER_SQM_DISTANCE, middleY+CENTER_SQM_DISTANCE)
    
    def getCoordCenterLeft():
        (middleX, middleY) = AutoLoot.getCoordsCenterAutoLoot()
        return (middleX-CENTER_SQM_DISTANCE, middleY)
    
    def getCoordTopLeft():
        (middleX, middleY) = AutoLoot.getCoordsCenterAutoLoot()
        return (middleX-CENTER_SQM_DISTANCE, middleY-CENTER_SQM_DISTANCE)
