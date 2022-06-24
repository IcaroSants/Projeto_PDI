# import imp
# from typing_extensions import Self
from src.utils.segmentation import SegmentationAllImages
import matplotlib.pyplot as plt
import os


diretorio = os.path.join("Imagens","raw")

seg = SegmentationAllImages(diretorio)
seg.__generateCSV__("Metadados das imagens segmentadas")
seg.__saveImagesSegmented__("Imagens_Segmentadas")



