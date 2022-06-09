from itertools import count
import cv2 as cv
import os

diretorio = os.path.join("Imagens","raw")
diretorio_final = os.path.join("Imagens","preprocessado")

if os.path.isdir(diretorio_final) == False:
    os.makedirs(diretorio_final)

arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    caminho_para_arquivo = os.path.join(diretorio,arquivo)
    imagem = cv.imread(caminho_para_arquivo)
    if imagem.shape == (224,224,3):
        print("ja foi redimensionada")
    else:
       imagem_redimensionada = cv.resize(imagem,(224,224),interpolation=cv.INTER_LINEAR)
       caminho_para_imagem_redi = os.path.join(diretorio_final,arquivo)
       cv.imwrite(caminho_para_imagem_redi,imagem_redimensionada)


