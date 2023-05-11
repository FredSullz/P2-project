import cv2
import time as t
from pymycobot.mycobot import MyCobot

mc = MyCobot('COM9',115200)
mc.send_angles([0,0,0,0,0,0],0)

cap = cv2.VideoCapture(index = 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

threshArray = [180, 240]
key = None
glove = False
bluetime = 0

# ---- Defining points ----
point0 = [0,0,0,0,0,0]
point1 = [90,0,0,0,0,0]
point2 = [0,0,0,0,0,0]
point3 = [0,0,0,0,0,0]
point4 = [0,0,0,0,0,0]
point5 = [0,0,0,0,0,0]

# ---- Defining functions ----
def calibrate():
    lowerThreshold = -1 #Initial value chosen so while loop always returns true at least once
    upperThreshold = -1
    inp = str(input("Do you want to calibrate? If not, default values are used (y/n)"))
    if inp == "y":
        while lowerThreshold < 0 or lowerThreshold > 360:
            lowerThreshold = int(input("What is your lower threshold?"))
            threshArray[0] = lowerThreshold
            if lowerThreshold < 0 or lowerThreshold > 360:
                print("Value must be between 0 and 360, try again")
        while upperThreshold < 0 or upperThreshold > 360:
            upperThreshold = int(input("What is your upper threshold?"))
            t.sleep(1)
            threshArray[1] = upperThreshold
            if upperThreshold < 0 or upperThreshold > 360:
                print("Value must be between 0 and 360, try again")
                t.sleep(1)
        t.sleep(1)
        print(f"Calibration done. Your new thresholds are: {threshArray}")

    elif inp == "n":
        print(f"Using default values: {threshArray}")

    else:
        print("invalid input, must be y or n. Try again")
        t.sleep(1)
        calibrate()

def goToPoint(point, speed):
    mc.send_angles(point,speed)

# ---- Main loop ----
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
            goToPoint(point1, 30)
            t.sleep(10)
            goToPoint(point0, 30)
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
