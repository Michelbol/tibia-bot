from cropper import cropImage
import cv2
import pytesseract
from img_loader import *
import re

CROP_CONFIG = {
    'x': 1015,
    'y': 170,
    'h': 60,
    'w': 180,
    'config_tesseract': '--tessdata-dir tessdata --psm 13',
}

CROP_MONSTERS = {
    'y': 3,
    'h': 22
}

class BattleAnalyser: 
    def getFirstMonsterInBattle(self, lastPrint):
        config_tesseract = CROP_CONFIG['config_tesseract']
        lang = 'eng'
        monster = cropImage(
            lastPrint, 
            CROP_CONFIG['x'], 
            CROP_CONFIG['y']+CROP_CONFIG['h']+CROP_MONSTERS['y'], 
            CROP_MONSTERS['h'],
            CROP_CONFIG['w']
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
    
    def firstMonsterIsTarget(self, lastPrint):
        monster = cropImage(
            lastPrint, 
            CROP_CONFIG['x'], 
            CROP_CONFIG['y']+CROP_CONFIG['h']+CROP_MONSTERS['y'], 
            CROP_MONSTERS['h'],
            CROP_CONFIG['w']
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