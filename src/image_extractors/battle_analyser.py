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
        monster = cropImage(
            self.lastPrint, 
            self.CURRENT_CROP_CONFIG['x']+20, 
            self.CURRENT_CROP_CONFIG['y']+self.CURRENT_CROP_CONFIG['h']+self.CURRENT_CROP_MONSTERS['y'], 
            self.CURRENT_CROP_MONSTERS['h'],
            self.CURRENT_CROP_CONFIG['w']-80
        )

        headerGray = cv2.cvtColor(monster, cv2.COLOR_BGR2GRAY)
        valor, lim_simples4 = cv2.threshold(headerGray,0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
        invert = 255 - lim_simples4
        saveImage('temp_crop/'+'battle-analyser.png', monster)
        
        # dataInvert = pytesseract.image_to_data(invert, lang, '--tessdata-dir tessdata --psm 6', 0, Output.DICT)
        texto = pytesseract.image_to_string(invert, lang, config_tesseract)
        
        onlyLetters = re.compile('[^A-Za-z]+')
        result = onlyLetters.sub('', texto)
        return result
    
    def firstMonsterIsTarget(self):
        monster = cropImage(
            self.lastPrint, 
            self.CURRENT_CROP_CONFIG['x'], 
            self.CURRENT_CROP_CONFIG['y']+self.CURRENT_CROP_CONFIG['h']+self.CURRENT_CROP_MONSTERS['y'], 
            self.CURRENT_CROP_MONSTERS['h'],
            self.CURRENT_CROP_CONFIG['w']-150
        )
        self.saveBatteHeader()
        saveImage('temp_crop/'+'battle-analyser-first-monster.png', monster)
        hsv_img = cv2.cvtColor(monster, cv2.COLOR_BGR2HSV)
        lower_range = (0, 200, 200) # lower range of red color in HSV
        upper_range = (10, 255, 255) # upper range of red color in HSV
        mask = cv2.inRange(hsv_img, lower_range, upper_range)
        color_image = cv2.bitwise_and(monster, monster, mask=mask)
        headerGray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        points = cv2.findNonZero(headerGray)
        saveImage('temp_crop/battle-analyser-target.png', color_image)
        rect = cv2.boundingRect(points) 
        return rect == (3,1,20,20)
    

    def saveBatteHeader(self):
        battleHeader = cropImage(
            self.lastPrint, 
            self.CURRENT_CROP_CONFIG['x'], 
            self.CURRENT_CROP_CONFIG['y'],
            self.CURRENT_CROP_CONFIG['h'],
            self.CURRENT_CROP_CONFIG['w']
        )
        saveImage('temp_crop/'+'battle-analyser-header.png', battleHeader)