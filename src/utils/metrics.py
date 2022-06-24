import numpy as np
import pandas as pd
import cv2 as cv
from scipy.spatial import distance

class Metrics():

    def __IoU__(self,image1,image2):
        intersection = np.logical_and(image1,image2)
        union = np.logical_or(image1,image2)
        iou_score = np.sum(intersection)/np.sum(union)
        
        return iou_score

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

    def area(self,img):

        area = len(np.nonzero(img)[0])

        return area

    
    def getAllMetrics(self,img):
        shape, _ = self.measurements(img)
        
        all_metrics = {}
        all_metrics["area"] = self.area(img)
        all_metrics["comprimento"] = shape[0]
        all_metrics["largura"] = shape[1]

        return all_metrics