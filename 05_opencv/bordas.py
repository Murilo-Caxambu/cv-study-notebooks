import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

placa = cv.imread("photos/placa.jpg")

def resize(frame, scale = 0.5):
    altura = int(frame.shape[0] * scale)
    largura = int(frame.shape[1]* scale)
    dimensions = (largura, altura)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img = resize(placa)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_gray, (9, 9), 0)
_, img_thresh = cv.threshold(img_blur, 130, 255, cv.THRESH_BINARY)
contornos, _ = cv.findContours(img_thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contornos = sorted(contornos, key=cv.contourArea, reverse=True)[:5]

img_debug = img.copy()

for cnt in contornos:
    area = cv.contourArea(cnt)
    perimetro = cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, 0.03 * perimetro, True)
    pontos = len(approx)

    if area > 30000 and pontos == 4:
        x, y, w, h = cv.boundingRect(approx)
        
        cv.rectangle(img_debug, (x, y), (x + w, y + h), (0, 255, 0), 2)

        placa_recortada = img[y:y+h, x:x+w]
        
        cv.imshow("Recorte Simples", placa_recortada)
        cv.imwrite("placa_recortada_simples.jpg", placa_recortada)
        
        print(f"Placa recortada salva! Dimensões: {w}x{h}")
        break
cv.imshow("Debug Final", img_debug)
cv.waitKey(0)