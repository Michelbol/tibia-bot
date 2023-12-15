from image_extractors.battle_analyser import BattleAnalyser
from pynput.keyboard import Key

class AutoAttack:

    LIST_OF_MONSTERS = [
        'ROTWORM',
        'SWAMPTROLL'
    ]

    HOTKEY_TO_ATTACK = Key.space

    def __init__(self, lastPrint) -> None:
        self.lastPrint = lastPrint

    def isNeedToAtack(self):
        battleAnalyser = BattleAnalyser()
        isAlreadyTarget = battleAnalyser.firstMonsterIsTarget(self.lastPrint)
        monster = battleAnalyser.getFirstMonsterInBattle(self.lastPrint)
        if(AutoAttack.LIST_OF_MONSTERS.count(monster.upper()) > 0 and isAlreadyTarget == False):
            return self.attack()

    def attack(self):
        return {
                'hotkeyToPress': AutoAttack.HOTKEY_TO_ATTACK
            }