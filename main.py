import imp
from src.utils.segmentation import Segmentation
import matplotlib.pyplot as plt
import os

seg = Segmentation(os.path.join("Padrao_Ouro","folha 32.png"))

plt.imshow(seg.__ChanVeseSegmentation__(),cmap='gray')
plt.show()


