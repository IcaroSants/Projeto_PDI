import cv2
import numpy as np
from src.utils.util_in import load_image

def process_image(path_image):

    img_ori = load_image(path_image=path_image, flag_scale=1) #BGR
    
    img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)

    # img_b = img_ori[:,:,0]
    img_g = img_ori[:,:,1]
    # img_r = img_ori[:,:,2]

    return img_ori, img_gray, img_g

def seg_image(img_g):

    ret3,th3 = cv2.threshold(img_g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    img_otsu = np.array(th3.max()-th3, dtype=np.uint8)

    contours, hierarchy = cv2.findContours(img_otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    all_areas=[]

    for cnt in contours:
        area= cv2.contourArea(cnt)
        all_areas.append(area)
    
    ind_max_area = all_areas.index(max(all_areas))

    img_zeros = np.zeros_like(img_g)

    img_contours = cv2.drawContours(img_zeros, [contours[ind_max_area]], 0, 255, -1)

    return img_otsu, img_contours

def get_width_length(img_bin):
    ind = np.where(img_bin!=0)
    print(ind)

    # M = cv2.moments(c)
	# cX = int(np.nonzero(img_bin)/)
	# cY = int(M["m01"] / M["m00"])
    # for angle in range(0, 5, 180):
    #     x=0
    return None

