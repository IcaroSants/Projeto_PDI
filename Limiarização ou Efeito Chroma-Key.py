import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imgs/folha 56.jpeg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img)
fig = plt.gcf()
fig.set_size_inches(18,6)
plt.axis('off')

minimo = (20, 60, 20)
maximo = (80, 255, 255)
minimo = np.array(minimo, dtype = "uint8")
maximo = np.array(maximo, dtype = "uint8")
mascara = cv2.inRange(img_hsv, minimo, maximo)
plt.imshow(mascara, cmap='gray')
fig = plt.gcf()
fig.set_size_inches(18,6)
plt.axis('off')

mascara = 255 - mascara
plt.imshow(mascara, cmap='gray')
fig = plt.gcf()
fig.set_size_inches(18,6)
plt.axis('off')