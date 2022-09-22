import cv2 
import numpy as np 
import imutils
from extra_funs import get_matrix_as_image

a11 = 1 
a12 = 0
a13 = 0
a21 = 0
a22 = 1
a23 = 0


def show_result(img, M):
    rows,cols,ch = img.shape
    dst = cv2.warpAffine(img,M,(cols,rows))  

    background_score_img = get_matrix_as_image(M)

    cv2.imshow("Manipulating the matrix",background_score_img)
    cv2.imshow("Original",img)
    cv2.imshow("Transformed", dst)

def update_a13(val):
    global a11, a12, a13, a21, a22, a23, img
    a13 = val 
    M = np.float32([[a11, a12, a13],
                    [a21, a22, a23]])
    
    show_result(img, M)


    

img = cv2.imread("red_indian2.jpg")
img = imutils.resize(img, width=720)

max_value = max(img.shape[0], img.shape[1])

cv2.namedWindow("Manipulating the matrix")

cv2.createTrackbar("a13", "Manipulating the matrix" , 0, max_value, update_a13)

M = np.float32([[a11, a12, a13],
                [a21, a22, a23]])



update_a13(0)

cv2.waitKey(0)
cv2.destroyAllWindows()