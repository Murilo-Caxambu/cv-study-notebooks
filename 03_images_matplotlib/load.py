import matplotlib.pyplot as plt

img = plt.imread('monet.png')
print(f"Tamanho da imagem: {img.shape}")
print(f"Tipo de arquivo da imagem: {img.dtype}")

plt.imshow(img)
plt.axis('off')
plt.show()