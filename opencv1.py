import cv2
img=cv2.imread("sample1.jpg")
cv2.imshow("pantechLogo",img)#Opening the image with a name
cv2.imwrite("logo.png",img)#Saving opened image with specified name
cv2.waitKey(0)
cv2.destroyAllWindow()
