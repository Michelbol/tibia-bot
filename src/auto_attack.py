from image_extractors.battle_analyser import BattleAnalyser
from pynput.keyboard import Key

class AutoAttack:

    LIST_OF_MONSTERS = [
        'rotworm'
    ]

    HOTKEY_TO_ATTACK = Key.space

    def isNeedToAtack(self, lastPrint):
        battleAnalyser = BattleAnalyser()
        isAlreadyTarget = battleAnalyser.firstMonsterIsTarget(lastPrint)
        monster = battleAnalyser.getFirstMonsterInBattle(lastPrint)
        if(AutoAttack.LIST_OF_MONSTERS.count(monster) > 0 and isAlreadyTarget == False):
            return self.attack()

    def attack(self):
        return {
                'hotkeyToPress': AutoAttack.HOTKEY_TO_ATTACK
            }