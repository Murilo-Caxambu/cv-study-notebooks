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
cv.imshow("placa", img)
cv.waitKey(0)