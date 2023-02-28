import cv2

cap = cv2.VideoCapture(index = 0)
height = 480
width = 640
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

key = None

while(key != 27):
	_, frame = cap.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	cx = int(height/2)
	cy = int(width/2)
	
	pixel_center = hsv_frame[cx, cy]
	hue_value = pixel_center[0] * 2
    
	if(key == 32):
		color = input("Lower threshold?")
		colorarr = [color, hue_value]
		print(colorarr)
	
	#Drawing "UI"
	pixel_center_bgr = frame[cx, cy]
	b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
	cv2.putText(frame, str(hue_value), (10,50), 0, 1, (b, g, r), 2)
	cv2.circle(frame, (cy, cx), 5, (25, 25, 25), 3)
	
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1)

#Closing the window(s)
cap.release()
cv2.destroyAllWindows()
