from img_loader import *
from environment import Environment
from image_extractors.battle_analyser import BattleAnalyser
from macros.auto_loot import AutoLoot
from models.player import Player

class PreviewConfig:

    def preview(self):
        rightHealthBar = Environment.resolveRightHealthBar()
        headerLevelBar = Environment.resolveHeaderLevelBar()
        skillsWindow = Environment.resolveSkillsWindow()
        battleConfigs = Environment.resolveBattleConfigs()
        battleMonsterConfigs = Environment.resolveBattleMonsterConfigs()

        imgLoader = ImgLoader()
        lastPrintSave, lastPrintSaveGray, lastPrintSaveGrayLimAndInvert = imgLoader.loadLastPrintSave()
        if(lastPrintSaveGray is list):
            return

        self.printRectange(lastPrintSave, rightHealthBar['life'])
        self.printRectange(lastPrintSave, rightHealthBar['mana'])
        self.printRectange(lastPrintSave, headerLevelBar['level'])
        self.printSkillsWindow(lastPrintSave, skillsWindow['default'], skillsWindow['position']['food'])
        self.printRectange(lastPrintSave, battleConfigs)
        self.printRectange(lastPrintSave, BattleAnalyser.generateFirstMonsterCoords(battleConfigs, battleMonsterConfigs))
        self.printRectange(lastPrintSave, BattleAnalyser.generateFirstMonsterTarget(battleConfigs, battleMonsterConfigs))
        self.printAutoLootPoint(lastPrintSave)
        
        
        cv2.imshow('Configuration Image', lastPrintSave)
        cv2.waitKey(0)
    

    def printRectange(self, image, coords):
        cv2.rectangle(
            image, 
            (coords['x'], coords['y']), 
            (coords['x']+coords['w'], coords['y']+coords['h']), 
            (0, 100, 255),
            2
        )

    def printAutoLootPoint(self, img):
        player = Player()
        autoLoot = AutoLoot(player)
        (x,y) = autoLoot.getCoordsCenterAutoLoot()
        position = {
            'x': int(x),
            'y': int(y),
            'w': 2,
            'h': 2
        }
        self.printRectange(img, position)
        (x,y) = autoLoot.getCoordsTopCenter()
        position['x'] = int(x)
        position['y'] = int(y)
        self.printRectange(img, position)

        (x,y) = autoLoot.getCoordTopRight()
        position['x'] = int(x)
        position['y'] = int(y)
        self.printRectange(img, position)

        (x,y) = autoLoot.getCoordCenterRight()
        position['x'] = int(x)
        position['y'] = int(y)
        self.printRectange(img, position)

        (x,y) = autoLoot.getCoordDownRight()
        position['x'] = int(x)
        position['y'] = int(y)
        self.printRectange(img, position)

        (x,y) = autoLoot.getCoordDownCenter()
        position['x'] = int(x)
        position['y'] = int(y)
        self.printRectange(img, position)

        (x,y) = autoLoot.getCoordDownLeft()
        position['x'] = int(x)
        position['y'] = int(y)
        self.printRectange(img, position)

        (x,y) = autoLoot.getCoordCenterLeft()
        position['x'] = int(x)
        position['y'] = int(y)
        self.printRectange(img, position)

        (x,y) = autoLoot.getCoordTopLeft()
        position['x'] = int(x)
        position['y'] = int(y)
        self.printRectange(img, position)


    def printSkillsWindow(self, image, default, y):
        skillPosition = {
            'x': default['x'],
            'y': y,
            'w': default['w'],
            'h': default['h']
        }
        self.printRectange(image, skillPosition)