import cv2
from subprocess import call
import time as t
import os

cap = cv2.VideoCapture(index = 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

lolarr = [" ", ".", "..", "..."]

threshArray = [180, 240]
key = None
glove = False
bluetime = 0

#Defining functions
def open_file_py():
            call(["python", "If_Blue.py"])

def calibrate():
    os.system("clear")
    for i in range(10):
        for i in range(4):
            print("Calibrating" + lolarr[i])
            t.sleep(0.5)
            os.system("clear")
    
    
#Run program
caliPrompt = input("Do you want to calibrate? If not, default values are used (y/n)")

if(caliPrompt == "y"):
    calibrate()
    
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
            open_file_py()
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
