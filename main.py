import cv2 
import numpy as np 
import imutils
from extra_funs import get_matrix_as_image
import streamlit as st

st.title("Visualizing Affine Transformation")

img_file = st.file_uploader("Choose a file")

a00 = 1 
a01 = 0
a02 = 0
a10 = 0
a11 = 1
a12 = 0
angle = 0
scale = 1 

M = np.float32([[a00, a01, a02],
                [a10, a11, a12]])

def update_M(a00, a01, a02, a10, a11, a12, angle, scale, center):
    M = np.float32([[a00, a01, a02],
                    [a10, a11, a12]])
    M_rotated = cv2.getRotationMatrix2D( center, angle, scale )

    # taking the average of the two
    M = (M + M_rotated) / 2.0
    #print(M)

    return M

def get_result(img, M):
    # print("This got called",M)
    rows,cols,ch = img.shape    
    dst = cv2.warpAffine(img,M,(cols,rows))  
    return dst

if img_file is None:
    img = cv2.imread("grid.png")
else:
    img = cv2.imread(img_file.name) 

img = imutils.resize(img, width=720)
result = img.copy()

height, width = img.shape[:2]
center = (width//2, height//2)

# st.image(result[:,:,::-1])
bg_image = get_matrix_as_image(M)
col1, col2, col3, col4 = st.columns(4) 

a00 = col1.slider("a00", 0.0, 2.0, 1.0, 0.001, key="a00")
a01 = col2.slider("a01", -2.0, 2.0, 0.0, 0.001, key="a01")
a02 = col3.slider("a02", -width, width, 0, 1, key="a02")
a10 = col1.slider("a10", -2.0, 2.0, 0.0, 0.001, key="a10")
a11 = col2.slider("a11", 0.0, 2.0, 1.0, 0.001, key="a11")
a12 = col3.slider("a12", -height, height, 0, 1, key="a12")




cola , colb = st.columns((0.8,0.2))

# adding angle and scale slider
angle = colb.slider("Angle", -180, 180, 0, key="angle")
scale = colb.slider("Scale", 0.0, 2.0, 1.0, key="scale")


#add an option for rotation from center 
rotate_from_center = colb.checkbox('Rotate from Center')

center = (width//2, height//2) if rotate_from_center  else (0,0)

M = update_M(a00, a01, a02, a10, a11, a12, angle, scale, center)
bg_image = get_matrix_as_image(M)
col4.image(bg_image, width = 600)
result = get_result(img, M)
cola.image(result[:,:,::-1])



#doing the same for paddded image
padded_image = cv2.copyMakeBorder(img.copy(),100,100,100,100,cv2.BORDER_CONSTANT,value=(0,0,0))
height_pd, width_pd = img.shape[:2]
center_pd = (width_pd//2, height_pd//2)
M = update_M(a00, a01, a02, a10, a11, a12, angle, scale, center_pd)
padded_result = get_result(padded_image, M)
st.image(padded_result[:,:,::-1])

# col2.image(bg_image, width = 600)
