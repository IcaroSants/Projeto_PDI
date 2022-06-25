

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imgs/folha 56.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
fig = plt.gcf()
fig.set_size_inches(18,6)
plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.show()

val, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
print(val)
fig = plt.gcf()
fig.set_size_inches(18,6)
plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.show()

dilatacao = cv2.dilate(thresh, np.ones((3,3), np.uint8), iterations = 2)
seg = cv2.erode(dilatacao, np.ones((3,3), np.uint8), iterations = 2)
print(val)
fig = plt.gcf()
fig.set_size_inches(18,6)
plt.imshow(seg, cmap='gray')
plt.axis('off')
plt.show()