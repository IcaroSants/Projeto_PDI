import cv2 as cv
import numpy as np
import os

diretorio_atual = os.getcwd()
diretorio = os.path.join(diretorio_atual,"Padrao_Ouro")
diretorio_final =  os.path.join(diretorio_atual,"teste")

if os.path.isdir(diretorio_final)==False:
    os.makedirs(diretorio_final)

arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    caminho_para_arquivo = os.path.join(diretorio,arquivo)
    imagem = cv.imread(caminho_para_arquivo,0)
    _,imagem_binarizada = cv.threshold(imagem,200,255,cv.THRESH_BINARY)
    caminho_para_imagem_bina = os.path.join(diretorio_final,arquivo)
    cv.imwrite(caminho_para_imagem_bina,imagem_binarizada)