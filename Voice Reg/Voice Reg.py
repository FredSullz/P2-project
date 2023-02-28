import speech_recognition as sr
import pyttsx3
import time as t

#setting r to be the recognizer function
r = sr.Recognizer()
#here er create a function that allows the program to return what we say.
def SpeakText(command):
    
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
#here we make a while loop, where we do both the speech reconition and the transcribing  
with sr.Microphone() as source2:
    #first thing we do is calibrating the ambient noise
    print("Calibrating... ")
    r.adjust_for_ambient_noise(source2, duration=2)
    print("Calibrated ")
    
    #here after we begin listening to the microphone
    audio2 = r.listen(source2)
    #then we wait for 2 sec
    t.sleep(2)
    
    #here we use googles recongitions aip to transcribe what we say
    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()
    
    #for last we print "did you say" + what we said
    print("Did you say " + MyText)
    #here is where we get the program to say back what we spoke to it
    SpeakText(MyText)