from img_loader import *
from models.player import Player
from models.character import Character
from macros.auto_healer import AutoHealer
from macros.auto_printer import AutoPrinter
from macros.auto_eat import AutoEat
from macros.auto_attack import AutoAttack
import time
from image_extractors.right_health_bar import RightHealthBar
from image_extractors.header_level_bar import HeaderLevelBar
from image_extractors.skills_window import SkillsWindow
from image_extractors.battle_analyser import BattleAnalyser
from garbage_collector.delete_files import DeleteFiles
from environment import Environment
from cave_bot.venore.rotworm import Rotworm
import threading

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
    lastPrintSaveGrayLimAndInvert: list = []

    settings = {
        'autoHealing': False,
        'autoEat': False,
        'autoAttack': False
    }
    
    def fillCharacterInformation(self):
        self.character = Character()

        self.character.level = self.headerLevelBar.extractLevel()

        self.character.vocation = 'knight'
        self.character.maxLife = self.character.calcLifeByLevel()
        self.character.maxMana = self.character.calcManaByLevel()
        self.character.food = self.skillsWindow.extractFood()

        self.character.currentLife = self.rightHealthBar.extractLife()
        self.character.currentMana = self.rightHealthBar.extractMana()

    def analyseLastPrintSave(self):
        actions = []

        self.fillCharacterInformation()

        if(self.settings['autoHealing']):
            healer = AutoHealer(self.character)
            actions.append(healer.isNeedToHealLife())
            actions.append(healer.isNeedToHealMana())
        

        if(self.settings['autoEat']):
            autoEat = AutoEat()
            actions.append(autoEat.isNeedToEat(self.character))

        if(self.settings['autoAttack']):
            autoAttack = AutoAttack()
            firstMonsterInBattle = self.battleAnalyser.getFirstMonsterInBattle()
            isAlreadyAttacking = self.battleAnalyser.firstMonsterIsTarget()
            actions.append(autoAttack.isNeedToAtack(firstMonsterInBattle, isAlreadyAttacking))

        return actions
    
    def autoPrinter(self):
        while(1):
            tibiaPrinter = AutoPrinter()
            tibiaPrinter.print()

    def analyseView(self):
        while(1):
            imgLoader = ImgLoader()
            self.lastPrintSave, self.lastPrintSaveGray, self.lastPrintSaveGrayLimAndInvert = imgLoader.loadLastPrintSave()
            if(type(self.lastPrintSave) is list):
                continue

            self.battleAnalyser = BattleAnalyser(self.lastPrintSave)
            self.headerLevelBar = HeaderLevelBar(self.lastPrintSaveGrayLimAndInvert)
            self.rightHealthBar = RightHealthBar(self.lastPrintSaveGrayLimAndInvert)
            self.skillsWindow = SkillsWindow(self.lastPrintSaveGrayLimAndInvert)

            actions = self.analyseLastPrintSave()
            self.player.execute(actions)

            DeleteFiles.deleteFilesInFolder('temp_crop/')
            time.sleep(1)

    def clearScreenshotFolder(self):
        while(1):
            DeleteFiles.deleteFilesInFolderButNotLastOne(Environment.resolveScreenshotsPath())
            time.sleep(60)

    def startCaveBot(self):
        rotworm = Rotworm(self.player)
        rotworm.script()

    def start(self):
        self.player = Player()
        autoPrinterThread = threading.Thread(target=self.autoPrinter)
        autoPrinterThread.start()
        anayseViewThread = threading.Thread(target=self.analyseView)
        anayseViewThread.start()
        garbageCollectorThread = threading.Thread(target=self.clearScreenshotFolder)
        garbageCollectorThread.start()
        