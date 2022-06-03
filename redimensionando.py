import cv2 as cv
import os

count = 0
for file in os.listdir("Imagens"):
    count += 1
    path_for_file = os.path.join("Imagens",file)
    imagem = cv.imread(path_for_file)
    imagem_red = cv.resize(imagem,(224,224))
    path_for_img_red = os.path.join("Imagens","folha "+str(count)+".png")
    cv.imwrite(path_for_img_red,imagem_red)


