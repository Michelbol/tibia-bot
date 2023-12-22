from pynput.keyboard import Key, Controller
import time

class Player:

    def __init__(self) -> None:
        self.attacking = False
        self.justKillAMonster = False

    def execute(self, actions): 
        for action in actions:
            if(action != None and action['hotkeyToPress'] != None):
                self.executeAction(action)

    def executeAction(self, action):
        print('Irá pressionar a tecla: '+str(action['hotkeyToPress']))
        keyboard = Controller()
        keyboard.press(action['hotkeyToPress'])
        time.sleep(0.1)
        keyboard.release(action['hotkeyToPress'])       


    def isAttacking(self, isTarget, willTarget):
        if(isTarget or willTarget):
            self.attacking = True
            return True
        self.attacking = False
        return False

    def killMonster(self, willTarget, isBattleAttacking):
        if(self.stopTargetAndWillAttackAgain(willTarget, isBattleAttacking)):
            self.justKillAMonster = True
        
        if(self.stopTargetAndWillNotTargetAgain(willTarget, isBattleAttacking)):
            self.justKillAMonster = True
        self.justKillAMonster = False

    def stopTargetAndWillNotTargetAgain(self, willTarget, isBattleAttacking):
        return willTarget == False and self.attacking == True and isBattleAttacking == False

    def stopTargetAndWillAttackAgain(self, willTarget, isBattleAttacking):
        return willTarget == True and self.attacking == True and isBattleAttacking == False