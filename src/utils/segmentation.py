from genericpath import isdir
from skimage.segmentation import  chan_vese
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

class Segmentation():
    def __init__(self,path):
        self.path = path

    def __getImage__(self):
        image = cv.imread(self.path)
        return image
    
    
    def __getGrayImage__(self):
        image = self.__getImage__()
        image_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        return image_gray

    def __ChanVeseSegmentation__(self):
        image_gray = self.__getGrayImage__()
        image_segmentated = chan_vese(image_gray)
        return image_segmentated

    def __IoU__(self,original):
        mask = original != False
        image = self.__ChanVeseSegmentation__()
        intersection = np.logical_and(mask,image)
        union = np.logical_or(mask,image)
        iou_score = np.sum(intersection)/np.sum(union)
        
        return iou_score

    def __del__(self):
       del(self)


class SegmentationAllImages(Segmentation):
    def __init__(self, dirImagens):
        if os.path.isdir(dirImagens):
            self.dirImagens = dirImagens
            
        else:
            raise  "Diretorio {} nao existe".format(dirImagens)
        
    def __getPathAllImages__(self):
        path_for_all_images = []
        for arquivo in os.listdir(self.dirImagens):
            path_for_image = os.path.join(self.dirImagens,arquivo)
            path_for_all_images.append(path_for_image)
        
        return path_for_all_images

    def __segmentationAllImages__(self):
        all_images = self.__getPathAllImages__()
        all_images_segmented = []
        for path_image in all_images:
            super().__init__(path_image)
            image_segmentaded = super().__ChanVeseSegmentation__()
            super().__del__()

            info = {}
            info["arquivo"]=path_image
            info["imagem_segmentada"]=image_segmentaded

            all_images_segmented.append(info)
        
        return all_images_segmented   
            

   

        
    




    
    
