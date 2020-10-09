import cv2
import imutils
img=cv2.imread("sample.jpg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresholdImg=cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImg2.jpg",thresholdImg)
