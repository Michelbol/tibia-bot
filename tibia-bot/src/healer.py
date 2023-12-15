from pynput.keyboard import Key

class Healer:
    hotkeyToHealLife = Key.f3
    hotkeyToFillMana = Key.f2

    percentToHealLife = 80
    percentToFillMana = 80

    def isNeedToHealLife(self, character):
        if(character.currentLife == None or character.maxLife == None):
            return None
        if(((character.currentLife / character.maxLife)*100) < Healer.percentToHealLife): 
            return {
                'hotkeyToPress': Healer.hotkeyToHealLife
            }
        return None
    
    def isNeedToHealMana(self, character):
        if(character.currentMana == None or character.maxMana == None):
            return None
        if(((character.currentMana/character.maxMana)*100) < Healer.percentToFillMana):
            return {
                'hotkeyToPress': Healer.hotkeyToFillMana
            }
        return None