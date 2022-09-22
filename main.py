import cv2 
import numpy as np 
import imutils

img = cv2.imread("red_indian2.jpg")
img = imutils.resize(img, width=720)

a11 = 1 
a12 = 0
a13 = 400
a21 = 0
a22 = 1
a23 = 50 

M = np.float32([[a11, a12, a13],
                [a21, a22, a23]])

rows,cols,ch = img.shape
dst = cv2.warpAffine(img,M,(cols,rows))  


cv2.imshow("Original",img)
cv2.imshow("Transformed", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()