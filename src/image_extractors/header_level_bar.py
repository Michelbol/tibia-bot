from image_extractors.number_extractor import NumberExtractor
from environment import Environment

class HeaderLevelBar:

    def __init__(self, lastPrint) -> None:
        self.LEVEL_CROP = Environment.resolveHeaderLevelBar()['level']
        self.lastPrint = lastPrint

    def extractLevel(self):
        return NumberExtractor.extract(self.lastPrint, self.LEVEL_CROP, 'level-head-bar.png')