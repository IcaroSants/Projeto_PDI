from skimage.segmentation import  chan_vese
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

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

    
   


    




    
    
