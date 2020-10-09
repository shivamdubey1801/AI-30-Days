import cv2
import imutils
img=cv2.imread("sample.jpg")
gaussianBlur=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussianImg.jpg",gaussianBlur)
