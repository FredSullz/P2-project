from pymycobot.mycobot import MyCobot
import time as t
speed = "half"
joint = 1
degree = 90
i = 0

mc = MyCobot('COM9',115200)
mc.send_angles([0,0,0,0,0,0],20)
t.sleep(5)
joint1 = ([90,0,0,0,0,0])
joint2 = ([0,90,0,0,0,0])
joint3 = ([0,0,90,0,0,0])
joint4 = ([0,0,0,90,0,0])
joint5 = ([0,0,0,0,90,0])
joint6 = ([0,0,0,0,0,90])
jointList = [joint1, joint2, joint3, joint4, joint5, joint6]


if speed == "half":
    while i < 20:
        mc.send_angles(jointList[joint - 1],50)
        t.sleep(5)
        print(mc.get_angles())
        t.sleep(1)
        mc.send_angles(jointList[joint - 1],50)
        t.sleep(5)
        print(mc.get_angles())
        t.sleep(1)
        i += 1

if speed == "full":
    while i < 20:
        mc.send_angles(jointList[joint - 1], 0)
        t.sleep(5)
        print(mc.get_angles())
        t.sleep(1)
        mc.send_angles(jointList[joint - 1], 0)
        t.sleep(5)
        print(mc.get_angles())
        t.sleep(1)
        i += 1
