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

    def killMonster(self, monsterMiss):
        wasAttacking = self.attacking == True
        if(wasAttacking and monsterMiss):
            self.justKillAMonster = True
            return True
        self.justKillAMonster = False
        return False
        
    def printStats(self):
        isAttacking = "Sim" if self.attacking else "Não"
        print('isAttacking:'+isAttacking)
        justKillAMonster = "Sim" if self.justKillAMonster else "Não"
        print('JustKillAMonster:'+ justKillAMonster)
        print('\n')