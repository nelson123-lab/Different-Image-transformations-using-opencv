import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C://Users//NELSON JOSEPH//Desktop//blaze-athletics.png")
kernel = np.ones((5,5),np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(9,9),0)
imgCanny = cv2.Canny(imgGrey,50,50)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray image", imgGrey)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation", imgDialation)
cv2.imshow("Eroded", imgEroded)
path ='C:/Users/NELSON JOSEPH/Desktop/'
plt.imsave(path + 'Blaze Logo.png',imgCanny, cmap='gray', format='png')
cv2.waitKey(0)
