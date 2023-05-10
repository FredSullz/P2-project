import time as t
import random
from pymycobot.mycobot import MyCobot

mc = MyCobot('/dev/ttyAMA0',115200)
correction = True
correctionVal = 5
testRunning = False

#Defining points in joint angles (Calculated with MatLab code):
point0 = [0,0,0,0,0,0] #nulpunkt, inkluderes ikke i array
point1 = [108.4892, -77.4298, -91.5336, 78.9626, 89.9997, 108.4885] #(5,265,20)
point2 = [67.2783, -77.8078, -89.1647, 76.9726, 90.0002, 67.2776] #(180,200,20)
point3 = [19.5737, -77.4262, -91.5609, 78.9879, 90.0003, 19.5739] #(265,0,20)
point4 = [-28.7471, -77.8074, -89.1654, 76.9727, 89.9999, -28.7473] #(180,-200,20)12
point5 = [-69.3489, -77.4296, -91.5343, 78.9638, 89.9996, -69.3486] #(5,-265,20)

pointArray = [point1,point2,point3,point4,point5]

if correction:
    for i in range(len(pointArray)):
        pointArray[i][3] = pointArray[i][3] + correctionVal

mc.send_angles(point2,30)
#Running test sequence
if testRunning:
    #Choosing a random squence of 20 points:
    seqArray = []
    for i in range(6):
        pointI = random.randint(0,4)
        pointNum = pointI + 1
        seqArray.append(pointNum)
    print(seqArray)
    #Running main test sequence

    for i in range(len(seqArray)):
        mc.send_angles(pointArray[seqArray[i]-1],50)
        t.sleep(10)
        mc.send_angles(point0,50)
        t.sleep(5)


#old joint values:
"""
point0 = [0,0,0,0,0,0] #nulpunkt, inkluderes ikke i array
point1 = [108.4891, -75.3472, -93.0539, 78.4009, 89.9995, -71.5108] #(5,265,25)
point2 = [67.2785, -75.7424, -90.6838, 76.4270, 89.9996, -112.7216] #(180,200,25)
point3 = [19.5737, -75.3436, -93.0813, 78.4254, 89.9998, -160] #(265,0,25)
point4 = [-28.7471, -75.7420, -90.6845, 76.4262, 89.9996, 151.2532] #(180,-200,25)
"""