from pynput.keyboard import Key

class AutoEat:
    hotkeyToEat = Key.f4
    minutesLeftToBeHungry = 3

    def isNeedToEat(self, character):
        if (character.food < AutoEat.minutesLeftToBeHungry):
            return {
                'hotkeyToPress': AutoEat.hotkeyToEat
            }
        return None