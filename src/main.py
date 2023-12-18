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

class Main:
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

    def loadLastPrintSave():
        path = Environment.resolveScreenshotsPath()
        files = os.listdir(path)
        if(len(files) == 0):
            Main.lastPrintSave = []
            Main.lastPrintSaveGray = []
            return
        lastPrintSave = sorted(files)[-1]
        Main.lastPrintSave = loadImage(path+lastPrintSave)

        if (Main.alreadyAnalisedPrints.count(path+lastPrintSave) > 0):
            Main.lastPrintSave = []
            Main.lastPrintSaveGray = []
            return
        
        print('Analisando o print: '+lastPrintSave)
        Main.alreadyAnalisedPrints.append(str(path+lastPrintSave))
        saveImage('temp_crop/original-print.png', Main.lastPrintSave)
        Main.lastPrintSaveGray = cv2.cvtColor(Main.lastPrintSave, cv2.COLOR_BGR2GRAY) 
    
    def fillCharacterInformation():
        Main.character = Character()

        Main.character.level = Main.headerLevelBar.extractLevel()

        Main.character.vocation = 'knight'
        Main.character.maxLife = Main.character.calcLifeByLevel()
        Main.character.maxMana = Main.character.calcManaByLevel()
        Main.character.food = Main.skillsWindow.extractFood()

        Main.character.currentLife = Main.rightHealthBar.extractLife()
        Main.character.currentMana = Main.rightHealthBar.extractMana()

    def analyseLastPrintSave(lastPrintSaveGray, lastPrintSave):
        actions = []

        Main.fillCharacterInformation()

        healer = Healer(Main.character)
        actions.append(healer.isNeedToHealLife())
        actions.append(healer.isNeedToHealMana())

        autoEat = AutoEat()
        actions.append(autoEat.isNeedToEat(Main.character))

        autoAttack = AutoAttack(lastPrintSave)
        firstMonsterInBattle = Main.battleAnalyser.getFirstMonsterInBattle()
        isAlreadyAttacking = Main.battleAnalyser.firstMonsterIsTarget()
        actions.append(autoAttack.isNeedToAtack(firstMonsterInBattle, isAlreadyAttacking))

        return actions

    def clearTempCrop():
        path = "temp_crop/"
        dir = os.listdir(path) 
        for file in dir:
            if(file == '.gitkeep'):
                continue
            os.remove(path+file)

    def main():
        Main.player = Player()
        while(1):
            tibiaPrinter = TibiaPrinter()
            tibiaPrinter.print()

            Main.loadLastPrintSave()
            if(type(Main.lastPrintSave) is list):
                time.sleep(1)
                continue

            Main.battleAnalyser = BattleAnalyser(Main.lastPrintSave)
            Main.headerLevelBar = HeaderLevelBar(Main.lastPrintSaveGray)
            Main.rightHealthBar = RightHealthBar(Main.lastPrintSaveGray)
            Main.skillsWindow = SkillsWindow(Main.lastPrintSaveGray)

            actions = Main.analyseLastPrintSave(Main.lastPrintSaveGray, Main.lastPrintSave)
            Main.player.execute(actions)

            Main.clearTempCrop()
            time.sleep(2)

Main.main()