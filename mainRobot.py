import cv2
import time as t
from pymycobot.mycobot import MyCobot

mc = MyCobot('/dev/ttyAMA0',115200)
mc.send_angles([0,0,0,0,0,0],0)

cap = cv2.VideoCapture(index = 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

threshArray = [180, 240]
key = None
glove = False
bluetime = 0

x = input("Do you want to calibrate? If not, default values are used (y/n)")
threshArray[0] = int(input("What is your lower threshold?"))
threshArray[1] = int(input("What is your upper threshold?"))

#Defining functions

#Main loop
while(key != 27):
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converting RGB values to HSV values
    height = 480
    width = 640

    cx = int(height / 2)
    cy = int(width / 2)

    pixel_center = hsv_frame[cx, cy]
    hue_value = pixel_center[0] * 2

    #Checking if the camera is pointed at a glove
    if hue_value in range(threshArray[0],threshArray[1]):
        glove = True
        bluetime += 1
        if bluetime > 100:
            bluetime = 0
            mc.send_angles([100,0,0,0,0,0],0)
            t.sleep(1)
            mc.send_angles([0,0,0,0,0,0],0)
    else:
        glove = False
        bluetime = 0


    #Drawing "UI"
    pixel_center_bgr = frame[cx, cy]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(frame, str(hue_value), (10,50), 0, 1, (b, g, r), 2)
    cv2.putText(frame, str(glove),(10,300),0, 1,(255, 0, 0), 2)
    cv2.circle(frame, (cy, cx), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

#Closing the window(s)
cap.release()
cv2.destroyAllWindows()
