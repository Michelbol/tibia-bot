import pytesseract
import cv2
from pytesseract import Output

minConf = 40
limiar = 25


img = cv2.imread('text-recognize/Imagens/imagem-processada.png')
print(img)

# cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cvt = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
valor, lim_simples4 = cv2.threshold(cvt,  0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(cvt, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)
cv2.imshow('Limiarizado4', lim_simples4)
cv2.imshow('Preto e Branco', cvt)
cv2.waitKey(0)


config_tesseract = '--tessdata-dir tessdata'
lang = 'eng'

texto = pytesseract.image_to_string(lim_simples4, lang, config_tesseract)

# print(texto)

resultado = pytesseract.image_to_data(lim_simples4, lang, config_tesseract, 0, output_type=Output.DICT)
print(resultado)

img_copy = th2.copy()

def caixa_texto(resultado, img, cor = (0, 100, 255)):
    x = resultado['left'][i]
    y = resultado['top'][i]
    w = resultado['width'][i]
    h = resultado['height'][i]
    
    cv2.rectangle(img, (x, y), (x+w, y+h), cor, 2)

    return x, y, img

for i in range(len(resultado['text'])):
    confianca = int(resultado['conf'][i])
    if(confianca > minConf):
        x, y, img = caixa_texto(resultado, img_copy)
        text = resultado['text'][i]
        cv2.putText(img_copy, text, (x,y -10), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0,100,255))

cv2.imshow('Teste', img_copy)
cv2.waitKey(0)

# from PIL import Image
# import matplotlib.pyplot as plt

# img = Image.open('text-recognize/Imagens/Aula2-livro.png')
# print(pytesseract.image_to_osd(img))