from img_loader import *
from player import Player
from character import Character
from healer import Healer
from tibia_printer import TibiaPrinter
from auto_eat import AutoEat
from auto_attack import AutoAttack
import os
import time
from image_extractors.right_health_bar import RightHealthBar
from image_extractors.header_level_bar import HeaderLevelBar
from image_extractors.skills_window import SkillsWindow
from image_extractors.battle_analyser import BattleAnalyser
from environment import Environment

class Program:

    actionExample: dict = {
        'hotkeyToPress': 'F1'
    }

    alreadyAnalisedPrints: list = []
    battleAnalyser: BattleAnalyser = None
    headerLevelBar: HeaderLevelBar = None
    rightHealthBar: RightHealthBar = None
    skillsWindow: SkillsWindow = None
    player: Player = None
    character: Character = None

    lastPrintSave: list = []
    lastPrintSaveGray: list = []

    def loadLastPrintSave(self):
        path = Environment.resolveScreenshotsPath()
        files = os.listdir(path)
        if(len(files) == 0):
            self.lastPrintSave = []
            self.lastPrintSaveGray = []
            return
        lastPrintSave = sorted(files)[-1]
        self.lastPrintSave = loadImage(path+lastPrintSave)

        if (self.alreadyAnalisedPrints.count(path+lastPrintSave) > 0):
            self.lastPrintSave = []
            self.lastPrintSaveGray = []
            return
        
        print('Analisando o print: '+lastPrintSave)
        self.alreadyAnalisedPrints.append(str(path+lastPrintSave))
        saveImage('temp_crop/original-print.png', self.lastPrintSave)
        self.lastPrintSaveGray = cv2.cvtColor(self.lastPrintSave, cv2.COLOR_BGR2GRAY) 
    
    def fillCharacterInformation(self):
        self.character = Character()

        self.character.level = self.headerLevelBar.extractLevel()

        self.character.vocation = 'knight'
        self.character.maxLife = self.character.calcLifeByLevel()
        self.character.maxMana = self.character.calcManaByLevel()
        self.character.food = self.skillsWindow.extractFood()

        self.character.currentLife = self.rightHealthBar.extractLife()
        self.character.currentMana = self.rightHealthBar.extractMana()

    def analyseLastPrintSave(self, lastPrintSaveGray, lastPrintSave):
        actions = []

        self.fillCharacterInformation()

        healer = Healer(self.character)
        actions.append(healer.isNeedToHealLife())
        actions.append(healer.isNeedToHealMana())

        autoEat = AutoEat()
        actions.append(autoEat.isNeedToEat(self.character))

        autoAttack = AutoAttack(lastPrintSave)
        firstMonsterInBattle = self.battleAnalyser.getFirstMonsterInBattle()
        isAlreadyAttacking = self.battleAnalyser.firstMonsterIsTarget()
        actions.append(autoAttack.isNeedToAtack(firstMonsterInBattle, isAlreadyAttacking))

        return actions

    def clearTempCrop(self):
        path = "temp_crop/"
        dir = os.listdir(path) 
        for file in dir:
            if(file == '.gitkeep'):
                continue
            os.remove(path+file)

    def start(self):
        self.player = Player()
        while(1):
            tibiaPrinter = TibiaPrinter()
            tibiaPrinter.print()

            self.loadLastPrintSave()
            if(type(self.lastPrintSave) is list):
                time.sleep(1)
                continue

            self.battleAnalyser = BattleAnalyser(self.lastPrintSave)
            self.headerLevelBar = HeaderLevelBar(self.lastPrintSaveGray)
            self.rightHealthBar = RightHealthBar(self.lastPrintSaveGray)
            self.skillsWindow = SkillsWindow(self.lastPrintSaveGray)

            actions = self.analyseLastPrintSave(self.lastPrintSaveGray, self.lastPrintSave)
            self.player.execute(actions)

            self.clearTempCrop()
            time.sleep(2)