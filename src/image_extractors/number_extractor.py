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
        ImgLoader.saveImage('temp_crop/'+img_name, header)
        
        texto = pytesseract.image_to_string(header, lang, config_tesseract)

        onlyNumbers = re.compile(r'[^\d]+')
        result = onlyNumbers.sub('', texto)
        if (result == ''):
            result = 0
        return int(result)