import cv2
from subprocess import call
import time as t
import os

cap = cv2.VideoCapture(index = 0)
height = 480
width = 640
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

threshArray = ["lower", "upper"]
key = None
glove = False
bluetime = 0

#Defining functions
def open_file_py():
            call(["python", "If_Blue.py"])

def calibrate():
    global key
    global threshArray
    global width
    global height
    i = 0
    while key != 27 or t > 2:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        cx = int(height/2)
        cy = int(width/2)
        
        pixel_center = hsv_frame[cx, cy]
        hue_value = pixel_center[0] * 2
        
        if key == 32:
            threshArray[i] = hue_value
            i += 1
        
        #Drawing "UI"
        pixel_center_bgr = frame[cx, cy]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
        cv2.rectangle(frame, pt1 = (5,20), pt2 = (140,80), color = (0, 0, 0), thickness = -1)
        cv2.putText(frame, str(hue_value), (10,50), 0, 1, (b, g, r), 2)
        cv2.putText(frame, str(threshArray), (10,70), 0, 0.5, (255, 255, 255), 1)
        cv2.circle(frame, (cy, cx), 5, (25, 25, 25), 3)
        
        cv2.imshow("Calibration", frame)
        key = cv2.waitKey(1)
        
        if i > 1:
            print(f"Your new thresholds are: {threshArray}")
            caliDone = input("Are you happy with these threshholds?(y/n)")
            if caliDone == "y":
                print("Calibration is done!")
                cv2.destroyWindow("Calibration")
                t.sleep(2)
                break
            else:
                print("Starting over")
                t.sleep(2)
                calibrate()


    
    
#Run program
caliPrompt = input("Do you want to calibrate? If not, default values are used (y/n)")

if caliPrompt == "y":
    calibrate()
else:
    threshArray[0] = 180
    threshArray[1] = 240
    
while key != 27:
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

    cv2.imshow("Dillermand", frame)
    key = cv2.waitKey(1)

#Closing the window(s)
cap.release()
cv2.destroyAllWindows()
