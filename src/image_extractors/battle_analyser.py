from cropper import cropImage
import cv2
import pytesseract
from img_loader import *
import re

class BattleAnalyser: 

    def __init__(self, lastPrint) -> None:
        self.lastPrint = lastPrint
        self.CURRENT_CROP_CONFIG = Environment.resolveBattleConfigs()
        self.CURRENT_CROP_MONSTERS = Environment.resolveBattleMonsterConfigs()

    def getFirstMonsterInBattle(self):
        config_tesseract = self.CURRENT_CROP_CONFIG['config_tesseract']
        lang = 'eng'
        coords = BattleAnalyser.generateFirstMonsterCoords(self.CURRENT_CROP_CONFIG,self.CURRENT_CROP_MONSTERS)
        monster = cropImage(self.lastPrint, coords['x'],coords['y'],coords['h'],coords['w'],)

        headerGray = cv2.cvtColor(monster, cv2.COLOR_BGR2GRAY)
        valor, lim_simples4 = cv2.threshold(headerGray,0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
        invert = 255 - lim_simples4
        ImgLoader.saveImage('temp_crop/'+'battle-analyser.png', monster)
        
        # dataInvert = pytesseract.image_to_data(invert, lang, '--tessdata-dir tessdata --psm 6', 0, Output.DICT)
        texto = pytesseract.image_to_string(invert, lang, config_tesseract)
        
        onlyLetters = re.compile('[^A-Za-z]+')
        result = onlyLetters.sub('', texto)
        return result
    
    def firstMonsterIsTarget(self):
        coords = BattleAnalyser.generateFirstMonsterTarget(self.CURRENT_CROP_CONFIG, self.CURRENT_CROP_MONSTERS)
        monster = cropImage(
            self.lastPrint, 
            coords['x'],
            coords['y'],
            coords['h'],
            coords['w'],
        )
        self.saveBatteHeader()
        ImgLoader.saveImage('temp_crop/'+'battle-analyser-first-monster.png', monster)
        hsv_img = cv2.cvtColor(monster, cv2.COLOR_BGR2HSV)
        lower_range = (0, 200, 200) # lower range of red color in HSV
        upper_range = (10, 255, 255) # upper range of red color in HSV
        mask = cv2.inRange(hsv_img, lower_range, upper_range)
        color_image = cv2.bitwise_and(monster, monster, mask=mask)
        headerGray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        points = cv2.findNonZero(headerGray)
        ImgLoader.saveImage('temp_crop/battle-analyser-target.png', color_image)
        rect = cv2.boundingRect(points) 
        return rect == (3,1,20,20) or rect == (4,1,20,20)
    

    def saveBatteHeader(self):
        battleHeader = cropImage(
            self.lastPrint, 
            self.CURRENT_CROP_CONFIG['x'], 
            self.CURRENT_CROP_CONFIG['y'],
            self.CURRENT_CROP_CONFIG['h'],
            self.CURRENT_CROP_CONFIG['w']
        )
        ImgLoader.saveImage('temp_crop/'+'battle-analyser-header.png', battleHeader)

    def generateFirstMonsterCoords(defaultCords, monsterCords):
        return {
            'x': defaultCords['x']+25, 
            'y': defaultCords['y']+defaultCords['h']+monsterCords['y'], 
            'h': monsterCords['h'],
            'w': defaultCords['w']-80
        }
    
    def generateFirstMonsterTarget(defaultCords, monsterCords):
        return {
            'x': defaultCords['x'], 
            'y': defaultCords['y']+defaultCords['h']+monsterCords['y'], 
            'h': monsterCords['h'],
            'w': defaultCords['w']-155
        }