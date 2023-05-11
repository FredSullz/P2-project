from pymycobot.mycobot import MyCobot
import time as t
mc = MyCobot('COM9', 115200)
mc.send_angles([0, 0, 0, 0, 0, 0], 20)
i = 0

while i < 10 :
    mc.send_angles([0,-110,0,0,0,0],40)
    t.sleep(3)
    print ("Press on the emergency stop button and then release it")
    t.sleep(10)
    mc.power_on()
    print ("Power is on")
    t.sleep(5)
    mc.send_angles([0,0,0,0,0,0],40)
    i += 1
    print((i))
    t.sleep(3)
