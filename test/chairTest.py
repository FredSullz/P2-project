from pymycobot.mycobot import MyCobot
import time as t
i = 0

mc = MyCobot('COM9',115200)
mc.send_angles([0,0,0,0,0,0],20)
t.sleep(5)

while i < 10:
    mc.send_angles([170,0,0,0,0,0],0)
    t.sleep(2)
    mc.send_angles([0,0,0,0,0,0],0)
    t.sleep(2)
    mc.send_angles([0,90,0,0,0,0],0)
    t.sleep(2)
    mc.send_angles([0,0,0,0,0,0],0)
    i += 1
    t.sleep(5)
