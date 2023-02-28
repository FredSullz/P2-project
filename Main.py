from subprocess import call
import time as t
import sys
def Open_color():
    call(["python","ColorRecognition\ColorRecognition.py"])

while True:
    input_var = input("Please enter something: ")
    
    if input_var == "run":
        t.sleep(2)
        Open_color()
        break
    else:
        print("You Entered " + input_var)
    

