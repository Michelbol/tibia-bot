import cv2
from environment import Environment
import os

class ImgLoader:

    alreadyAnalisedPrints = []

    def loadImage(path):
        return cv2.imread(path)

    def saveImage(path, img):
        if(Environment.isProduction() != True):
            cv2.imwrite(path, img)

    def loadLastPrintSave(self):
        path = Environment.resolveScreenshotsPath()
        files = os.listdir(path)
        if(len(files) == 0):
            return [], [], []
        nameOflastPrintSave = sorted(files)[-1]
        lastPrintSave = ImgLoader.loadImage(path+nameOflastPrintSave)

        if (self.alreadyAnalisedPrints.count(path+nameOflastPrintSave) > 0):
            return [], [], []
        
        print('Analisando o print: '+nameOflastPrintSave)
        self.alreadyAnalisedPrints.append(str(path+nameOflastPrintSave))
        ImgLoader.saveImage('temp_crop/original-print.png', lastPrintSave)
        lastPrintSaveGray = cv2.cvtColor(lastPrintSave, cv2.COLOR_BGR2GRAY) 
        valor, lim_simples4 = cv2.threshold(lastPrintSaveGray,0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
        lastPrintSaveGrayLimAndInvert = 255 - lim_simples4
        return lastPrintSave, lastPrintSaveGray, lastPrintSaveGrayLimAndInvert