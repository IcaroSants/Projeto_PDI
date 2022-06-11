import imp
from typing_extensions import Self
from src.utils.segmentation import SegmentationAllImages
import matplotlib.pyplot as plt
import os

diretorio = os.path.join("Imagens","raw")

seg = SegmentationAllImages(diretorio)
all_images = seg.__segmentationAllImages__()
print(all_images)

"""plt.imshow()
plt.show()"""


