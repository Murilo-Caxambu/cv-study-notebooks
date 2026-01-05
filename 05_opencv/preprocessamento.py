import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#variavel da placa original que trabalharemos no codigo
placa_original = cv.imread("photos/placa.jpg")
if placa_original is None:
    print("Arquivo nao encontrado.")
    exit()

#funcao pra reescalar a imagem da placa
def reescala(frame, scale =0.5):
    largura = int(frame.shape[1] * scale)
    altura = int(frame.shape[0] * scale)
    dimensions = (largura, altura)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

#placa reescalada
placa_original_reescala = reescala(placa_original)

#imagem em rgb
placa_rgb = cv.cvtColor(placa_original_reescala, cv.COLOR_BGR2RGB)
#palca em escala cinza
placa_cinza = cv.cvtColor(placa_original_reescala, cv.COLOR_BGR2GRAY)

#placa borrada
placa_borrada = cv.GaussianBlur(placa_original_reescala, (15,15), 3)
placa_borrada_rgb = cv.cvtColor(placa_borrada, cv.COLOR_BGR2RGB)


#placa canny
placa_canny = cv.Canny(placa_borrada,50,150)
placa_canny_rgb = cv.cvtColor(placa_canny, cv.COLOR_BGR2RGB)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12,8))
#placa original
ax[0,0].imshow(placa_rgb)
ax[0,0].set_title("Placa original")
ax[0,0].axis("off")

#placa em escala cinza
ax[0,1].imshow(placa_cinza, cmap = "grey")
ax[0,1].set_title("Placa em cinza")
ax[0,1].axis("off")

#placa borrada
ax[1,0].imshow(placa_borrada_rgb)
ax[1,0].set_title("Placa borrada")
ax[1,1].axis("off")

#placa canny
ax[1,1].imshow(placa_canny_rgb, cmap="grey")
ax[1,1].set_title("Placa sem bordas")
ax[1,1].axis("off")

cv.waitKey(0)
plt.show()