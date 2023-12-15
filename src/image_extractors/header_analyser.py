import cv2
from cropper import cropImage
from img_loader import *
import pytesseract
from pytesseract import Output
import re
from environment import Environment

class HeaderAnalyser:
    def __init__(self, character) -> None:
        self.character = character
        self.lifeCurrentCrop = Environment.resolveHeaderAnalyser()['life']
        self.manaCurrentCrop = Environment.resolveHeaderAnalyser()['mana']
        

    def extractLife(self, lastPrint):
        config_tesseract = self.lifeCurrentCrop['config_tesseract']
        lang = 'eng'
        header = cropImage(lastPrint, self.lifeCurrentCrop['x'], self.lifeCurrentCrop['y'], self.lifeCurrentCrop['h'], self.lifeCurrentCrop['w'])
        headerGray = cv2.cvtColor(header, cv2.COLOR_BGR2GRAY)
        saveImage('temp_crop/life-gray.png', headerGray)

        texto = pytesseract.image_to_string(headerGray, lang, config_tesseract)
        if(texto.count('/') == 1):
            characterLife = texto.split('/');
            trim = re.compile(r'[^\d.,]+')
            characterLife[0] = trim.sub('', characterLife[0])
            characterLife[1] = trim.sub('', characterLife[1])
        else:
            trim = re.compile(r'[^\d.,]+')
            result = trim.sub('', texto)
            characterLife = result.split('7')
        return characterLife

    def extractMana(self, lastPrint):
        config_tesseract = self.manaCurrentCrop['config_tesseract']
        lang = 'eng'

        header = cropImage(lastPrint, self.manaCurrentCrop['x'], self.manaCurrentCrop['y'], self.manaCurrentCrop['h'], self.manaCurrentCrop['w'])
        headerGray = cv2.cvtColor(header, cv2.COLOR_BGR2GRAY)
        saveImage('temp_crop/mana-gray.png', headerGray)
        texto = pytesseract.image_to_string(headerGray, lang, config_tesseract)
        trim = re.compile(r'[^\d.,]+')
        result = trim.sub('', texto)
        characterMana = result.split('7')
        return characterMana

    def headerAnalyser(self, lastPrint): 
        characterLife = self.extractLife(lastPrint)
        characterMana = self.extractMana(lastPrint)
        
        if(len(characterLife) != 2 ):
            print('was not possible to extract life')
            return

        if(len(characterMana) != 2 ):
            print('was not possible to extract mana')
            return

        self.character.currentLife = int(characterLife[0])
        self.character.maxLife = int(characterLife[1])

        self.character.currentMana = int(characterMana[0])
        self.character.maxMana = int(characterMana[1])
    

def limiarizacao(headerGray, lang, config_tesseract): 

        valor, lim_simples4 = cv2.threshold(headerGray,  0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        saveImage('temp_crop/life-lim.png', lim_simples4)
        texto2 = pytesseract.image_to_data(lim_simples4, lang, config_tesseract, 0, output_type=Output.DICT)
        
        th2 = cv2.adaptiveThreshold(headerGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)
        saveImage('temp_crop/life-th2.png', th2)
        texto3 = pytesseract.image_to_string(th2, lang, config_tesseract)