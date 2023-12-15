from image_extractors.number_extractor import NumberExtractor
from environment import Environment

class HeaderLevelBar:

    def __init__(self) -> None:
        self.LEVEL_CROP = Environment.resolveHeaderLevelBar()['level']

    def extractLevel(self, lastPrint):
        return NumberExtractor.extract(lastPrint, self.LEVEL_CROP, 'level-head-bar.png')