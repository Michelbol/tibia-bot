from image_extractors.battle_analyser import BattleAnalyser
from pynput.keyboard import Key

class AutoAttack:

    LIST_OF_MONSTERS = [
        'ROTWORM',
        'SWAMPTROLL',
        'SWAMPLING'
    ]

    HOTKEY_TO_ATTACK = Key.space

    def __init__(self, lastPrint) -> None:
        self.lastPrint = lastPrint

    def isNeedToAtack(self, firstMonsterInBattle, isAlreadyAttacking):
        if(AutoAttack.LIST_OF_MONSTERS.count(firstMonsterInBattle.upper()) > 0 and isAlreadyAttacking == False):
            return self.attack()

    def attack(self): 
        return {
                'hotkeyToPress': AutoAttack.HOTKEY_TO_ATTACK
            }