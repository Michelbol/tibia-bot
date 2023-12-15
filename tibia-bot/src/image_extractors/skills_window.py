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

    def __init__(self) -> None:
        self.DEFAULT_CROP = Environment.resolveSkillsWindow()['default']
        self.CROP = Environment.resolveSkillsWindow()['position']


    def extractAllInformationPossible(self, lastPrint):
        level = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['level']), 'skill-window-level.png')
        experience = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['experience']), 'skill-window-experience.png')
        xpRate = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['xp-rate']), 'skill-window-xp-rate.png')
        life = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['life']), 'skill-window-life.png')
        mana = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['mana']), 'skill-window-mana.png')
        soul = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['soul']), 'skill-window-soul.png')
        capacity = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['capacity']), 'skill-window-capacity.png')
        speed = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['speed']), 'skill-window-speed.png')
        food = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['food']), 'skill-window-food.png')
        stamina = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['stamina']), 'skill-window-stamina.png')
        magicLevel = NumberExtractor.extract(lastPrint, self.defaultCrop(self.CROP['magic-level']), 'skill-window-magic-level.png')

        return food

    def defaultCrop(self, y):
        self.DEFAULT_CROP['y'] = y
        return self.DEFAULT_CROP