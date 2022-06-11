import numpy as np
import cv2
import mahotas
import matplotlib.pyplot as plt
from scipy.spatial import distance


imgColorida = cv2.imread('test/original/folha 7.png') #Carregamento da imagem
img_PO = cv2.imread('test/padrao-ouro/folha 7.png')
img_PO = cv2.cvtColor(img_PO, cv2.COLOR_BGR2GRAY)

def segmentacao(img):

    # Conversão para tons de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Passo 2: Blur/Suavização da imagem
    #suave = cv2.blur(img, (3, 3))
    suave = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # Binarização resultando em pixels brancos e pretos
    T = mahotas.thresholding.otsu(suave)
    bin = suave.copy()
    bin[bin > T] = 255
    bin[bin < 255] = 0
    bin = cv2.bitwise_not(bin)

    # Operações morfológicas
    kernel = np.ones((5, 5), np.uint8)
    img_closing = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, kernel)
    img_opening = cv2.morphologyEx(img_closing, cv2.MORPH_OPEN, kernel)
    img_seg = img_opening

    return img_seg

def area(img):

    area = len(numpy.nonzero(img)[0])

    return area

def cordenadas_horizontais(img):
        cord = []
        for i in range(len(img[1])):
            py1 = i
            if 255 in img[:, py1]:
                linha_1 = img[:, py1]
                px1 = int(np.where(linha_1 >= 255)[0][0])
                ponto1 = [py1, px1]
                cord.append(ponto1)

                break

        for j in range(len(img[1])):
            ultima_linha = len(img[0])
            py2 = (ultima_linha - j) - 1
            if 255 in img[:, py2]:
                linha_2 = img[:, py2]
                px2 = int(np.where(linha_2 >= 255)[0][0])
                ponto2 = [py2, px2]
                cord.append(ponto2)

                break
        return cord

def cordenadas_verticais(img):
        cord = []
        for i in range(len(img[0])):
            py1 = i
            if 255 in img[py1, :]:
                linha_1 = img[py1, :]
                px1 = int(np.where(linha_1 >= 255)[0][0])
                ponto1 = [py1, px1]
                cord.append(ponto1)

                break

        for j in range(len(img[0])):
            ultima_linha = len(img[0])
            py2 = (ultima_linha - j) - 1
            if 255 in img[py2, :]:
                linha_2 = img[py2, :]
                px2 = int(np.where(linha_2 >= 255)[0][0])
                ponto2 = [py2, px2]
                cord.append(ponto2)

                break
        return cord

def largura_comprimento(img):
    cord_hoz = cordenadas_horizontais(img)
    cord_vrt = cordenadas_verticais(img)

    distancia_1 = np.round(distance.euclidean(cord_hoz[0], cord_hoz[1]), 2)
    distancia_2 = np.round(distance.euclidean(cord_vrt[0], cord_vrt[1]), 2)

    if distancia_1 >= distancia_2:
        comprimento = distancia_1
        largura = distancia_2
    else:
        comprimento = distancia_2
        largura = distancia_1

    return comprimento, largura

