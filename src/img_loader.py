import cv2

def loadImage(path):
    return cv2.imread(path)

def saveImage(path, img):
    cv2.imwrite(path, img)