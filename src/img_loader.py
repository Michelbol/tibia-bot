import cv2
from environment import Environment

def loadImage(path):
    return cv2.imread(path)

def saveImage(path, img):
    if(Environment.isProduction() != True):
        cv2.imwrite(path, img)