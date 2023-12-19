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

        healer = AutoHealer(self.character)
        actions.append(healer.isNeedToHealLife())
        actions.append(healer.isNeedToHealMana())

        autoEat = AutoEat()
        actions.append(autoEat.isNeedToEat(self.character))

        autoAttack = AutoAttack()
        firstMonsterInBattle = self.battleAnalyser.getFirstMonsterInBattle()
        isAlreadyAttacking = self.battleAnalyser.firstMonsterIsTarget()
        actions.append(autoAttack.isNeedToAtack(firstMonsterInBattle, isAlreadyAttacking))

        return actions

    def start(self):
        self.player = Player()
        imgLoader = ImgLoader()
        while(1):
            DeleteFiles.deleteFilesInFolder(Environment.resolveScreenshotsPath())
            tibiaPrinter = AutoPrinter()
            tibiaPrinter.print()

            self.lastPrintSave, self.lastPrintSaveGray = imgLoader.loadLastPrintSave()
            if(type(self.lastPrintSave) is list):
                continue

            self.battleAnalyser = BattleAnalyser(self.lastPrintSave)
            self.headerLevelBar = HeaderLevelBar(self.lastPrintSaveGray)
            self.rightHealthBar = RightHealthBar(self.lastPrintSaveGray)
            self.skillsWindow = SkillsWindow(self.lastPrintSaveGray)

            actions = self.analyseLastPrintSave()
            self.player.execute(actions)

            DeleteFiles.deleteFilesInFolder('temp_crop/')
            time.sleep(1)