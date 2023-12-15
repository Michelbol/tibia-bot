from image_extractors.number_extractor import NumberExtractor
from environment import Environment

class RightHealthBar:

    def __init__(self, lastPrint) -> None:
        self.LIFE_CROP = Environment.resolveRightHealthBar()['life']
        self.MANA_CROP = Environment.resolveRightHealthBar()['mana']
        self.lastPrint = lastPrint

    def extractLife(self):
        return NumberExtractor.extract(self.lastPrint, self.LIFE_CROP, 'health-bar-life.png')

    def extractMana(self):
        return NumberExtractor.extract(self.lastPrint, self.MANA_CROP, 'health-bar-mana.png')