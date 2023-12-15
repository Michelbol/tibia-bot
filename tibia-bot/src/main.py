from img_loader import *
from player import Player
from character import Character
from healer import Healer
from tibia_printer import TibiaPrinter
import os
import time
from image_extractors.right_health_bar import RightHealthBar
from image_extractors.header_level_bar import HeaderLevelBar
from image_extractors.skills_window import SkillsWindow
from environment import Environment

actionExample = {
    'hotkeyToPress': 'F1'
}

alreadyAnalisedPrints = []


def loadLastPrintSave():
    path = Environment.resolveScreenshotsPath()
    files = os.listdir(path)
    lastPrintSave = sorted(files)[-1]
    img = loadImage(path+lastPrintSave)

    if (alreadyAnalisedPrints.count(path+lastPrintSave) > 0):
        return []
    
    print('Analisando o print: '+lastPrintSave)
    alreadyAnalisedPrints.append(str(path+lastPrintSave))
    saveImage('temp_crop/original-print.png', img)
    return loadImage('temp_crop/original-print.png')

def analyseLastPrintSave(lastPrintSave):
    actions = []
    character = Character()

    headerLevelBar = HeaderLevelBar()
    character.level = headerLevelBar.extractLevel(lastPrintSave)

    character.vocation = 'knight'
    character.maxLife = character.calcLifeByLevel()
    character.maxMana = character.calcManaByLevel()

    skillWindow = SkillsWindow()
    character.food = skillWindow.extractAllInformationPossible(lastPrintSave)

    healthBar = RightHealthBar()
    character.currentLife = healthBar.extractLife(lastPrintSave)
    character.currentMana = healthBar.extractMana(lastPrintSave)

    healer = Healer()
    actions.append(healer.isNeedToHealLife(character))
    actions.append(healer.isNeedToHealMana(character))

    return actions

def clearTempCrop():
    path = "temp_crop/"
    dir = os.listdir(path)
    for file in dir:
        os.remove(path+file)

def main():
    player = Player()
    while(1):
        tibiaPrinter = TibiaPrinter()
        tibiaPrinter.print()

        lastPrintSave = loadLastPrintSave()

        if(len(lastPrintSave) == 0):
            time.sleep(1)
            continue

        actions = analyseLastPrintSave(lastPrintSave)
        player.execute(actions)

        clearTempCrop()
        time.sleep(1)



main()