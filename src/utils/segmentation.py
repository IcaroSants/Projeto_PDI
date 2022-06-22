from genericpath import isdir
from skimage.segmentation import  chan_vese
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
from skimage.filters import threshold_otsu
from scipy.spatial import distance

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
    
    def preProcessing(self, imageBGR):
        image_channel_green = imageBGR[:,:,1]
        return image_channel_green
    
    def ContoursAreaSegmentation(self, image_channel_green):
        ret3,th3 = cv.threshold(image_channel_green,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        img_otsu = np.array(th3.max()-th3, dtype=np.uint8) # resultado Otsu

        contours, hierarchy = cv.findContours(img_otsu, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

        all_areas=[]
        for cnt in contours:
            area= cv.contourArea(cnt)
            all_areas.append(area)
    
        # indice do contorno de maior area interna 
        ind_max_area = all_areas.index(max(all_areas)) 

        img_zeros = np.zeros_like(image_channel_green)

        # Retorna imagem com o contorno que possui maior area interna  
        image_segmentated = cv.drawContours(img_zeros, [contours[ind_max_area]], 0, 255, -1)
        image_segmentated[image_segmentated!=0] = 1
        
        return image_segmentated
    
    def morphology(self, image_gray):
        #Passo 2: Blur/Suavização da imagem
        #suave = cv2.blur(img, (3, 3))
        suave = cv.GaussianBlur(image_gray, (3, 3), 0)

        # Binarização resultando em pixels brancos e pretos
        T = threshold_otsu(suave)
        bin = suave.copy()
        bin[bin > T] = 255
        bin[bin < 255] = 0
        bin = cv.bitwise_not(bin)

        # Operações morfológicas
        kernel = np.ones((5, 5), np.uint8)
        img_closing = cv.morphologyEx(bin, cv.MORPH_CLOSE, kernel)
        img_opening = cv.morphologyEx(img_closing, cv.MORPH_OPEN, kernel)
        image_segmentated = img_opening
        image_segmentated[image_segmentated!=0] = 1           
        
        return image_segmentated

    def __ChanVeseSegmentation__(self):
        image_gray = self.__getGrayImage__()
        image_segmentated = chan_vese(image_gray)
        return image_segmentated

    def tecSeg02(self):
        imageBGR = self.__getImage__() #BGR
        image_channel_green = self.preProcessing(imageBGR)
        image_segmentated = self.ContoursAreaSegmentation(image_channel_green)
        return image_segmentated
    
    def tecSeg03(self):
        image_gray = self.__getGrayImage__()
        image_segmentated = self.morphology(image_gray)
        return image_segmentated

    

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
            # image_segmentaded = super().tecSeg02()
            # image_segmentaded = super().tecSeg03()
            super().__del__()

            info = {}
            info["arquivo"]=path_image
            info["imagem_segmentada"]=image_segmentaded

            all_images_segmented.append(info)
        
        return all_images_segmented   
            

   

        
    




    
    
