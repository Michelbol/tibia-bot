from cropper import cropImage
from img_loader import *
import pytesseract
import re
import time

class NumberExtractor:
    def extract(lastPrint, CROP_CONFIG, img_name):
        print("===================Extract Number Start===================")
        config_tesseract = CROP_CONFIG['config_tesseract']
        lang = 'eng'
        header = cropImage(lastPrint, CROP_CONFIG['x'], CROP_CONFIG['y'], CROP_CONFIG['h'], CROP_CONFIG['w'])
        ImgLoader.saveImage('temp_crop/'+img_name, header)
        
        imgToString = time.time()
        texto = pytesseract.image_to_string(header, lang, config_tesseract)
        print("imgToString: %s seconds" % (time.time() - imgToString))

        onlyNumbers = re.compile(r'[^\d]+')
        result = onlyNumbers.sub('', texto)
        if (result == ''):
            result = 0
        return int(result)