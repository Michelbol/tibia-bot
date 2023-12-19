from pynput.keyboard import Key

class AutoHealer:
    hotkeyToHealLife = Key.f3
    hotkeyToFillMana = Key.f2

    percentToHealLife = 80
    percentToFillMana = 80

    def __init__(self, character) -> None:
        self.character = character

    def isNeedToHealLife(self):
        if(self.character.currentLife == None or self.character.maxLife == None):
            return None
        if(((self.character.currentLife / self.character.maxLife)*100) < AutoHealer.percentToHealLife): 
            return {
                'hotkeyToPress': AutoHealer.hotkeyToHealLife
            }
        return None
    
    def isNeedToHealMana(self):
        if(self.character.currentMana == None or self.character.maxMana == None):
            return None
        if(((self.character.currentMana/self.character.maxMana)*100) < AutoHealer.percentToFillMana):
            return {
                'hotkeyToPress': AutoHealer.hotkeyToFillMana
            }
        return None