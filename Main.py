#first we import the nessecary libraries
from subprocess import call
import time as t
import sys

#here we create a function that allow us to call another script from this script
def Open_color():
    call(["python","ColorRecognition\ColorRecognition.py"])

#we then make a while true loop for checking the input in the console
while True:
    #we create a valuble called input_var that alow us writes an input in the console 
    input_var = input("Please enter something: ")
    
    #here we check if input_var == run and if it is it then waits for 2 secounds then run the script function and then breaks out of the if statement
    #if the input_var is not == run that it just prints "you entered" + what is writen in input_var  
    if input_var == "run":
        t.sleep(2)
        Open_color()
        break
    else:
        print("You Entered " + input_var)
    

