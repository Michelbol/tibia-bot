from image_extractors.number_extractor import NumberExtractor
from environment import Environment

class RightHealthBar:

    def __init__(self) -> None:
        self.LIFE_CROP = Environment.resolveRightHealthBar()['life']
        self.MANA_CROP = Environment.resolveRightHealthBar()['mana']

    def extractLife(self, lastPrint):
        return NumberExtractor.extract(lastPrint, self.LIFE_CROP, 'health-bar-life.png')

    def extractMana(self, lastPrint):
        return NumberExtractor.extract(lastPrint, self.MANA_CROP, 'health-bar-mana.png')