import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
key = None
glove = False
bluetime = 0

while(key != 27):
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converting RGB values to HSV values
    height = 720
    width = 1280

    cx = int(height / 2)
    cy = int(width / 2)

    pixel_center = hsv_frame[cx, cy]
    hue_value = pixel_center[0]

    #Defining the colors
    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"
    
    #Checking if the camera is pointed at a glove
    if color == "BLUE":
        glove = True
        bluetime += 1
        if bluetime > 100:
            giveItem()
            bluetime = 0
    else:
        glove = False
        bluetime = 0
        
    def giveItem():
        #This will work as a function for sending information to the Raspberry PI.
        cv2.putText(frame, "Item Given!",(1170,100),0, 1,(255, 0, 0), 2)


    #Drawing "UI"
    pixel_center_bgr = frame[cx, cy]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(frame, color, (10,50), 0, 1, (b, g, r), 2)
    cv2.putText(frame, str(glove),(1170,50),0, 1,(255, 0, 0), 2)
    cv2.putText(frame, str(bluetime),(1170,200),0, 1,(255, 0, 0), 2)
    cv2.circle(frame, (cy, cx), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

#Closing the window(s)
cap.release()
cv2.destroyAllWindows()