from pynput.keyboard import Key

class Healer:
    hotkeyToHealLife = Key.f3
    hotkeyToFillMana = Key.f2

    percentToHealLife = 80
    percentToFillMana = 80

    def __init__(self, character) -> None:
        self.character = character

    def isNeedToHealLife(self):
        if(self.character.currentLife == None or self.character.maxLife == None):
            return None
        if(((self.character.currentLife / self.character.maxLife)*100) < Healer.percentToHealLife): 
            return {
                'hotkeyToPress': Healer.hotkeyToHealLife
            }
        return None
    
    def isNeedToHealMana(self):
        if(self.character.currentMana == None or self.character.maxMana == None):
            return None
        if(((self.character.currentMana/self.character.maxMana)*100) < Healer.percentToFillMana):
            return {
                'hotkeyToPress': Healer.hotkeyToFillMana
            }
        return None