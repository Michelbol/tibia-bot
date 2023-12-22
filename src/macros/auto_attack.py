from image_extractors.battle_analyser import BattleAnalyser
from pynput.keyboard import Key

class AutoAttack:

    LIST_OF_MONSTERS = [
        'ROTWORM',
        'SWAMPTROLL',
        'SWAMPLING'
    ]

    HOTKEY_TO_ATTACK = Key.space

    def isNeedToAtack(self, firstMonsterInBattle, isBattleAttacking):
        if(AutoAttack.LIST_OF_MONSTERS.count(firstMonsterInBattle.upper()) > 0 and isBattleAttacking == False):
            return self.attack()

    def attack(self): 
        return {
                'hotkeyToPress': AutoAttack.HOTKEY_TO_ATTACK
            }