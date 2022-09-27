import cv2 
import numpy as np 
import imutils
from extra_funs import get_matrix_as_image
import streamlit as st


a00 = 1 
a01 = 0
a02 = 0
a10 = 0
a11 = 1
a12 = 0

M = np.float32([[a00, a01, a02],
                [a10, a11, a12]])

def update_M(a00, a01, a02, a10, a11, a12, angle, scale, center):
    M = np.float32([[a00, a01, a02],
                    [a10, a11, a12]])
    M_rotated = cv2.getRotationMatrix2D( center, angle, scale )

    #setting the a11 and a22 values for M_rotated to be 0
    # to not count them twice 
    M_rotated[0][0] = 0
    M_rotated[1][1] = 0
    M_rotated[0][2] = 0
    M_rotated[1][2] = 0

    M = M + M_rotated
    #print(M)

    return M

def get_result(img, M):
    # print("This got called",M)
    rows,cols,ch = img.shape    
    dst = cv2.warpAffine(img,M,(cols,rows))  
    return dst

img = cv2.imread("red_indian2.jpg")
img = imutils.resize(img, width=720)
result = img.copy()

height, width = img.shape[:2]
center = (width//2, height//2)

# st.image(result[:,:,::-1])
bg_image = get_matrix_as_image(M)
col1, col2 = st.columns(2) 

a00 = col1.slider("a00", 0.0, 2.0, 1.0, 0.001, key="a00")
a01 = col1.slider("a01", -2.0, 2.0, 0.0, 0.001, key="a01")
a02 = col1.slider("a02", -width, width, 0, 1, key="a02")
a10 = col1.slider("a10", -2.0, 2.0, 0.0, 0.001, key="a10")
a11 = col1.slider("a11", 0.0, 2.0, 1.0, 0.001, key="a11")
a12 = col1.slider("a12", -height, height, 0, 1, key="a12")
angle = col2.slider("Angle", -180, 180, 0, key="angle")
scale = col2.slider("Scale", 0.0, 2.0, 1.0, key="scale")

M = update_M(a00, a01, a02, a10, a11, a12, angle, scale, center)
bg_image = get_matrix_as_image(M)
col2.image(bg_image, width = 600)
result = get_result(img, M)
st.image(result[:,:,::-1])

#doing the same for paddded image
padded_image = cv2.copyMakeBorder(img.copy(),100,100,100,100,cv2.BORDER_CONSTANT,value=(0,0,0))
height_pd, width_pd = img.shape[:2]
center_pd = (width_pd//2, height_pd//2)
M = update_M(a00, a01, a02, a10, a11, a12, angle, scale, center_pd)
padded_result = get_result(padded_image, M)
st.image(padded_result[:,:,::-1])

# col2.image(bg_image, width = 600)
