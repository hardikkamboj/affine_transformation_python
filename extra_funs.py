import numpy as np
import cv2 
import matplotlib.pyplot as plt 

BACKGROUND_IMG = "matrix.png"

def get_matrix_as_image(M, background_img = BACKGROUND_IMG):
    
    M = np.vstack([M, [0,0,1]])

    background = cv2.imread(background_img)

    height_indices = [100,200,300]
    width_indices = [520, 680, 840]

    temp = background.copy()

    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0,0,0)
    scale = 1.5
    thickness = 3

    for h_i,h in enumerate(height_indices):
        for w_i,w in enumerate(width_indices):
            val = M[h_i][w_i]
            cv2.putText(temp, str(val), (w, h),font, scale, color=color, thickness = thickness)

    return temp
