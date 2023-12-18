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

actionExample = {
    'hotkeyToPress': 'F1'
}

alreadyAnalisedPrints = []

def loadLastPrintSave():
    path = Environment.resolveScreenshotsPath()
    files = os.listdir(path)
    if(len(files) == 0):
        return [], []
    lastPrintSave = sorted(files)[-1]
    img = loadImage(path+lastPrintSave)

    if (alreadyAnalisedPrints.count(path+lastPrintSave) > 0):
        return [], []
    
    print('Analisando o print: '+lastPrintSave)
    alreadyAnalisedPrints.append(str(path+lastPrintSave))
    saveImage('temp_crop/original-print.png', img)
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    return grayImage, img

def analyseLastPrintSave(lastPrintSaveGray, lastPrintSave):
    actions = []
    character = Character()

    headerLevelBar = HeaderLevelBar()
    character.level = headerLevelBar.extractLevel(lastPrintSaveGray)

    character.vocation = 'knight'
    character.maxLife = character.calcLifeByLevel()
    character.maxMana = character.calcManaByLevel()

    skillWindow = SkillsWindow(lastPrintSaveGray)
    character.food = skillWindow.extractFood()

    healthBar = RightHealthBar(lastPrintSaveGray)
    character.currentLife = healthBar.extractLife()
    character.currentMana = healthBar.extractMana()

    healer = Healer()
    actions.append(healer.isNeedToHealLife(character))
    actions.append(healer.isNeedToHealMana(character))

    autoEat = AutoEat()
    actions.append(autoEat.isNeedToEat(character))

    autoAttack = AutoAttack(lastPrintSave)
    actions.append(autoAttack.isNeedToAtack())

    return actions

def clearTempCrop():
    path = "temp_crop/"
    dir = os.listdir(path) 
    for file in dir:
        if(file == '.gitkeep'):
            continue
        os.remove(path+file)

def main():
    player = Player()
    while(1):
        tibiaPrinter = TibiaPrinter()
        tibiaPrinter.print()

        [lastPrintSaveGray, lastPrintSave] = loadLastPrintSave()
        if(type(lastPrintSave) is list):
            time.sleep(1)
            continue

        actions = analyseLastPrintSave(lastPrintSaveGray, lastPrintSave)
        player.execute(actions)

        clearTempCrop()
        time.sleep(2)

main()