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
img_blur = cv.GaussianBlur(img, (15,15),3)
img_canny = cv.Canny(img_blur, 50, 150)

kernel = np.ones((2,2), np.uint8)
img_dilatada = cv.dilate(img_canny, kernel, iterations=1)

contornos, _ = cv.findContours(img_dilatada, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contornos = sorted(contornos, key=cv.contourArea, reverse=True)[:5]

img_debug = img.copy()

for cnt in contornos:
    area = cv.contourArea(cnt)
    perimetro = cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, 0.02 * perimetro, True)

    pontos = len(approx)

    if area > 2000:
        cv.drawContours(img_debug, [approx], -1, (0,0,255), 2)
        x, y = approx[0][0]
        cv.putText(img_debug, f"pontos: {pontos}", (x, y -10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(f"Area: {area} | Pontos detectados: {pontos}")

cv.imshow("Debug de Geometria", img_debug)
cv.waitKey(0)