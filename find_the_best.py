import io
from telnetlib import SE
#from turtle import color
#from turtle import color
from src.utils.segmentation import Segmentation
from src.utils.metrics import Metrics
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import os

#matplotlib.use("TkAgg")


images_stand_golden = os.listdir("Padrao_Ouro")
diretorio_imagens = os.path.join("Imagens","raw")
metrics = Metrics()

imagens = []
iou = []
iou_02 = []
iou_03 = []

for file in images_stand_golden:
    dados = {}
    path_for_file = os.path.join(diretorio_imagens,file)
    path_for_file_gold = os.path.join("Padrao_Ouro",file)

    dados["imagem"] = path_for_file
    dados["imagem_ouro"] = cv.imread(path_for_file_gold,0)
    imagens.append(dados)

for dados in imagens:
    segmentacao = Segmentation(dados["imagem"])
    
    imagem_segmentada = segmentacao.__ChanVeseSegmentation__()
    imagem_segmentada_02 = segmentacao.tecSeg02()
    imagem_segmentada_03 = segmentacao.tecSeg03()
    
    mascara = dados["imagem_ouro"]

    iou_seg = metrics.__IoU__(imagem_segmentada,mascara)
    iou_seg_02 = metrics.__IoU__(imagem_segmentada_02,mascara)
    iou_seg_03 = metrics.__IoU__(imagem_segmentada_03,mascara)

    iou.append(iou_seg)
    iou_02.append(iou_seg_02)
    iou_03.append(iou_seg_03)

resultado  = [round(np.mean(iou),2)*100,round(np.mean(iou_02),2)*100,round(np.mean(iou_03),2)*100]

print("imagem segmentada:",resultado[0], "minimo:",min(iou),"maximo:",max(iou),"desvio padrao:",np.std(iou))
print("imagem segmentada tec 02:",resultado[1], "minimo:",min(iou_02),"maximo:",max(iou_02),"desvio padrao:",np.std(iou_02))
print("imagem segmentada tec 03:",resultado[2], "minimo:",min(iou_03),"maximo:",max(iou_03),"desvio padrao:",np.std(iou_03))



"""plt.bar(["tec 01","tec 02","tec 03"],resultado,color=["blue","green","red"]) 
plt.title("IoU")
plt.ylim(0,100)
plt.ylabel("porcentagem")

plt.text(0,76,str(int(resultado[0]))+"%")
plt.text(1,86,str(int(resultado[1]))+"%")
plt.text(2,90,str(int(resultado[2]))+"%")

plt.show()"""