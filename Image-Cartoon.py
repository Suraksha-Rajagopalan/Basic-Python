import cv2
import numpy as np

image=cv2.imread('download.jpg')

g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
g=cv2.medianBlur(g,5)
e=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

color=cv2.bilateralFilter(image,9,250,250)
c=cv2.bitwise_and(color,color,mask=e)

cv2.imshow('Image',image)
cv2.imshow('Edges',e)
cv2.imshow('Cartoon',c)
cv2.waitKey(0)
cv2.destroyAllWindows()
