import cv2
import time

cam=cv2.VideoCapture(0)# zero is primary should change if external connected
time.sleep(1)
while True:
    _,img=cam.read()
    cv2.imshow("cameraFeed",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

