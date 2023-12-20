import cv2
from cropper import cropImage
from img_loader import *
import pytesseract
import re

class NumberExtractor:
    def extract(lastPrint, CROP_CONFIG, img_name):
        config_tesseract = CROP_CONFIG['config_tesseract']
        lang = 'eng'
        header = cropImage(lastPrint, CROP_CONFIG['x'], CROP_CONFIG['y'], CROP_CONFIG['h'], CROP_CONFIG['w'])
        # valor, lim_simples4 = cv2.threshold(header,0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
        # invert = 255 - lim_simples4
        ImgLoader.saveImage('temp_crop/'+img_name, header)
        
        # dataInvert = pytesseract.image_to_data(invert, lang, '--tessdata-dir tessdata --psm 6', 0, Output.DICT)
        texto = pytesseract.image_to_string(header, lang, config_tesseract)

        onlyNumbers = re.compile(r'[^\d]+')
        result = onlyNumbers.sub('', texto)
        if (result == ''):
            result = 0
        return int(result)