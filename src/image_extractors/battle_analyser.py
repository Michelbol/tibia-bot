from cropper import cropImage
import cv2
import pytesseract
from img_loader import *
import re

CROP_CONFIG_DB1 = {
    'x': 1015,
    'y': 170,
    'h': 60,
    'w': 180,
    'config_tesseract': '--tessdata-dir tessdata --psm 13',
}

CROP_MONSTERS_DB1 = {
    'y': 3,
    'h': 22
}
CROP_CONFIG_NOTEBOOK = {
    'x': 1190,
    'y': 547,
    'h': 60,
    'w': 180,
    'config_tesseract': '--tessdata-dir tessdata --psm 13',
}

CROP_MONSTERS_NOTEBOOK = {
    'y': 3,
    'h': 22
}

CURRENT_CROP_CONFIG = CROP_CONFIG_NOTEBOOK
CURRENT_CROP_MONSTERS = CROP_MONSTERS_NOTEBOOK

class BattleAnalyser: 
    def getFirstMonsterInBattle(self, lastPrint):
        config_tesseract = CURRENT_CROP_CONFIG['config_tesseract']
        lang = 'eng'
        battleHeader = cropImage(
            lastPrint, 
            CURRENT_CROP_CONFIG['x'], 
            CURRENT_CROP_CONFIG['y'],
            CURRENT_CROP_CONFIG['h'],
            CURRENT_CROP_CONFIG['w']
        )
        monster = cropImage(
            lastPrint, 
            CURRENT_CROP_CONFIG['x']+20, 
            CURRENT_CROP_CONFIG['y']+CURRENT_CROP_CONFIG['h']+CURRENT_CROP_MONSTERS['y'], 
            CURRENT_CROP_MONSTERS['h'],
            CURRENT_CROP_CONFIG['w']
        )

        headerGray = cv2.cvtColor(monster, cv2.COLOR_BGR2GRAY)
        valor, lim_simples4 = cv2.threshold(headerGray,0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
        invert = 255 - lim_simples4
        saveImage('temp_crop/'+'battle-analyser.png', monster)
        #saveImage('temp_crop/'+'battle-analyser-header.png', battleHeader)
        
        # dataInvert = pytesseract.image_to_data(invert, lang, '--tessdata-dir tessdata --psm 6', 0, Output.DICT)
        texto = pytesseract.image_to_string(invert, lang, config_tesseract)
        
        onlyLetters = re.compile('[^A-Za-z]+')
        result = onlyLetters.sub('', texto)
        return result
    
    def firstMonsterIsTarget(self, lastPrint):
        monster = cropImage(
            lastPrint, 
            CURRENT_CROP_CONFIG['x'], 
            CURRENT_CROP_CONFIG['y']+CURRENT_CROP_CONFIG['h']+CURRENT_CROP_MONSTERS['y'], 
            CURRENT_CROP_MONSTERS['h'],
            CURRENT_CROP_CONFIG['w']
        )
        hsv_img = cv2.cvtColor(monster, cv2.COLOR_BGR2HSV)
        lower_range = (0, 50, 50) # lower range of red color in HSV
        upper_range = (10, 255, 255) # upper range of red color in HSV
        mask = cv2.inRange(hsv_img, lower_range, upper_range)
        color_image = cv2.bitwise_and(monster, monster, mask=mask)
        headerGray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        points = cv2.findNonZero(headerGray)
        rect = cv2.boundingRect(points)
        return rect == (3,1,20,20)