import time as t
import cv2
from pymycobot.mycobot import MyCobot
import speech_recognition as sr


"""

SPEECH RECOGNITION SETUP

"""
#used for speech recognition
r = sr.Recognizer()
keyword1 = "base"
keyword2 = "t. v."
keyword3 = "face"
keyword4 = "fink"
keyword5 = "keyboard"
keyword6 = "no"
keyword7 = "okay"
keyword8 = "so"
keyword9 = "table"
keyword10 = "tee shirt"

keywordArray = [keyword1, keyword2, keyword3, keyword4, keyword5, keyword6, keyword7, keyword8, keyword9, keyword10]
"""

COLOR DETECTION SETUP

"""

#used to capture from camera and create window to view cameras view
cap = cv2.VideoCapture(index = 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#threshold array for color detection
threshArray = [180, 240]
key = None
glove = False
bluetime = 0
atDropoff = False

"""

ROBOT SETUP

"""
#is the raspberri pi being used or is computer connected to robot True/False
computerInUse = True
#what is the color of the robot "black"/"white"
robotColor = "black"
speed = 33

#connecting to the robot is done differently depending on what robot is being used and how it is being used
if computerInUse:
    if robotColor == "white":
        mc = MyCobot('COM9',115200)
    else:
        mc = MyCobot('COM11',115200)
else:
    mc = MyCobot('/dev/ttyAMA0',115200)
"""

CORRECTION SETUP

"""
correction = True
correctionVal = 6
correctionVal2 = correctionVal/2


"""

POINT SETUP

"""
#Defining points using joint angles (Calculated with MatLab code):

point0 = [0, 0, 0, 0, 0, 0]
point1Approach = [104.64 , (-27.9), (-71.56), 9.45 , 90, 104.64]#(6, 290, 40)
point1 = [104.64, (-32.34), (-82), 24.34 , 90, 104.64]#(6, 290, 5
point2Approach = [107.85,(-5.82),(-101),16.81 ,90,107.85]#(6, 240, 40)
point2 = [107.85, (-12.47),(-111.6),34.06 ,90,107.85]#(6, 240, 5)
point3Approach = [84.13, (-25.27),(-75.53),10.8 ,90,84.13]#(106, 260, 40)
point3 = [84.14,(-30),(-85.84),25.84 ,90,84.14]#(106, 260, 5)
point4Approach = [81.54, (-6.63), (-100.08), 16.71 , 90, 81.54]#(106, 210, 40)
point4 = [81.54, (-13.21), (-110.63), 33.84 , 90, 81.54]#(106, 210, 5)
point5Approach = [60.22, (-24.93), (-76.04), 10.97 , 90, 60.22]#(196, 190, 40)
point5 = [60.22, (-29.7), (-86.34), 26.04 , 90, 60.22] #(196, 190, 5)
point6Approach = [54.09, (-11.41), (-94.42), 15.83 , 90, 54.09] #(196, 140, 40)
point6 = [54.09, (-17.55), (-104.74), 32.3 , 90, 54.09] #(196, 140, 5)
point7Approach = [36.26 , (-22.82), (-79.12), 11.94 , 90, 36.26] #(251, 85, 40)
point7 = [36.26 , (-27.82), (-89.35), 27.17 , 90, 36.26] #(251, 85, 5)
point8Approach = [26.82 , (-17.99), (-85.9), 13.89 , 90, 26.82] #(251, 35, 40)
point8 = [26.82 , (-23.49), (-96.08), 29.57 , 90, 26.82] #(251, 35, 5)
point9Approach = [16.24 , (-17.17), (-87.01), 14.17 , 90, 16.24] #(251, -15, 40)
point9 = [16.24 , (-22.75), (-97.19), 29.94 , 90, 16.24] #(251, -15, 5)
point10Approach = [5.19 , (-21.42), (-82.55), 12.96 , 90, 5.19] #(251, -65, 40)
point10 = [5.19 , (-25.67), (-92.73), 28.4 , 90, 5.19] #(251, -65, 5)
pointDropOff = [(-66.3) + correctionVal2, (-11.84), (-64.92), (-13.24) + correctionVal, 90, (-66.3)] #(0, -255, 100)

pointArray = [point1,point2,point3,point4,point5,point6,point7,point8,point9,point10]
pointApproachArray = [point1Approach,point2Approach,point3Approach,point4Approach,point5Approach,point6Approach,point7Approach,point8Approach,point9Approach,point10Approach]

if correction:
    for i in range(len(pointArray)):
        pointArray[i][0] = pointArray[i][0] + correctionVal2
        pointArray[i][3] = pointArray[i][3] + correctionVal
        pointApproachArray[i][0] = pointApproachArray[i][0] + correctionVal2
        pointApproachArray[i][3] = pointApproachArray[i][3] + correctionVal


"""

ROBOT POSITION SETUP

"""
#Set robot to 0 (base position) and open gripper
mc.set_gripper_value(35, 0)
mc.send_angles(point0, speed)


"""

FUNCTION SETUP

"""
#function used to recognize speech
def voiceReg():
    r = sr.Recognizer()
    with sr.Microphone(3) as source:
        print("Say something!")
        audio = r.listen(source)
        text = r.recognize_sphinx(audio)

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + text)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    return text

def pickup(word):
    global atDropoff
    if word in keywordArray:
        pointIndex = keywordArray.index(word)
        point = pointArray[pointIndex]
        approach = pointApproachArray[pointIndex]
        mc.send_angles(approach,speed)
        t.sleep(5)
        mc.send_angles(point,speed)
        t.sleep(2)
        mc.set_gripper_value(40,0)
        t.sleep(1)
        mc.send_angles(approach,speed)
        t.sleep(2)
        mc.send_angles(pointDropOff,speed)
        t.sleep(7)
        atDropoff = True
    else:
        mc.send_angles(point0,speed)
        print("Keyword not in keywordArray")

#function that sends end effector to desired point
def goToPoint(point, speed):
    mc.send_angles(point,speed)

#function used to calibrate HSV values used for color detection
def calibrateColor():
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
        calibrateColor()


"""

MAIN LOOP

"""
calibrateColor()

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
            if atDropoff is False:
                bluetime = 0
                mc.send_angles([30, 0, 0, 0, 0, 0], 30)
                mc.set_gripper_value(65, 0)
                word = voiceReg()
                pickup(word)

            else:
                bluetime = 0
                atDropoff = False
                mc.set_gripper_value(65, 0)
                t.sleep(1)
                mc.send_angles(point0, speed)
                mc.set_gripper_value(35, 0)


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
