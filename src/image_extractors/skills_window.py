from image_extractors.number_extractor import NumberExtractor
from environment import Environment

class SkillsWindow:

    CROP_PC_DB1 = {
        'level': 18,
        'experience': 40,
        'xp-rate': 52,
        'life': 83,
        'mana': 100,
        'soul': 116,
        'capacity': 130,
        'speed': 144,
        'food': 158,
        'stamina': 172,
        'magic-level': 225
    }

    def __init__(self, lastPrint) -> None:
        self.DEFAULT_CROP = Environment.resolveSkillsWindow()['default']
        self.CROP = Environment.resolveSkillsWindow()['position']
        self.lastPrint = lastPrint


    def extractFood(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['food']), 'skill-window-food.png')
    
    def extractLevel(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['level']), 'skill-window-level.png')
    
    def extractExperience(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['experience']), 'skill-window-experience.png')
    
    def extractXpRate(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['xp-rate']), 'skill-window-xp-rate.png')
    
    def extractLife(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['life']), 'skill-window-life.png')
    
    def extractMana(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['mana']), 'skill-window-mana.png')
    
    def extractSoul(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['soul']), 'skill-window-soul.png')
    
    def extractCapacity(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['capacity']), 'skill-window-capacity.png')

    def extractSpeed(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['speed']), 'skill-window-speed.png')

    def extractStamina(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['stamina']), 'skill-window-stamina.png')
    
    def extractMagicLevel(self):
        return NumberExtractor.extract(self.lastPrint, self.defaultCrop(self.CROP['magic-level']), 'skill-window-magic-level.png')

    def defaultCrop(self, y):
        self.DEFAULT_CROP['y'] = y
        return self.DEFAULT_CROP