from genericpath import isdir
from skimage.segmentation import  chan_vese
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import mahotas
from scipy.spatial import distance

class Segmentation():
    def __init__(self,path):
        self.path = path

    def cordenadas_horizontais(self, img):
        cord = []
        for y in range(img.shape[0]):
            if 1 in img[y, :]:
                x = np.where(img[y, :]!=0)[0][0] #[y,x]
                cord.append([y, x])
                break
        
        for y in range(img.shape[0]-1, 0, -1):
            if 1 in img[y, :]:
                x = np.where(img[y, :]!=0)[0][0] #[y,x]
                cord.append([y, x])
                break

        return cord

    def cordenadas_verticais(self, img):
        cord = []
        for x in range(img.shape[1]):
            if 1 in img[:, x]:
                y = np.where(img[:, x]!=0)[0][0] #[y,x]
                cord.append([y, x])
                break
        
        for x in range(img.shape[1]-1, 0, -1):
            if 1 in img[:, x]:
                y = np.where(img[:, x]!=0)[0][0] #[y,x]
                cord.append([y, x])
                break

        return cord

    def measurements(self, image_segmentated):
        cord_hoz = self.cordenadas_horizontais(image_segmentated)
        cord_vrt = self.cordenadas_verticais(image_segmentated)

        start_pt_hoz = (cord_hoz[0][1], cord_hoz[0][0])
        end_pt_hoz =   (cord_hoz[1][1], cord_hoz[1][0])
        start_pt_vrt = (cord_vrt[0][1], cord_vrt[0][0])
        end_pt_vrt =   (cord_vrt[1][1], cord_vrt[1][0])
        color = (255)
        thickness = 2    
        line_hor = cv.line(np.zeros_like(image_segmentated), start_pt_hoz, end_pt_hoz, color, thickness)
        line_vrt = cv.line(np.zeros_like(image_segmentated), start_pt_vrt, end_pt_vrt, color, thickness)
        
        image_draw_line = np.array(image_segmentated) 
        image_draw_line[image_draw_line!=0] = 255 
        image_draw_line[line_hor!=0] = 127
        image_draw_line[line_vrt!=0] = 127

        distancia_1 = np.round(distance.euclidean(cord_hoz[0], cord_hoz[1]), 2)
        distancia_2 = np.round(distance.euclidean(cord_vrt[0], cord_vrt[1]), 2)

        if distancia_1 >= distancia_2:
            comprimento = distancia_1
            largura = distancia_2
        else:
            comprimento = distancia_2
            largura = distancia_1

        return [comprimento, largura], image_draw_line 

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
        T = mahotas.thresholding.otsu(suave)
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
            # image_segmentaded = super().tecSeg02()
            # image_segmentaded = super().tecSeg03()
            super().__del__()

            info = {}
            info["arquivo"]=path_image
            info["imagem_segmentada"]=image_segmentaded

            all_images_segmented.append(info)
        
        return all_images_segmented   
            

   

        
    




    
    
