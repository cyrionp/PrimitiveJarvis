import speech_recognition as sr
from os import system as cmd
import time
import sys

upperAlphabet="ABCDEFGHIJKLMNOPRSTUVWXYZ"
lowerAlphabet="abcdefghijklmnoprstuvwxyz"

def GetLower(text:str): #To be sure if given text has lowercases
    newText=str()
    for i in text:
        if i in upperAlphabet:
            index=upperAlphabet.index(i)
            newText+=lowerAlphabet[index]
        else: newText+=i
    return newText

def Regen():
    time.sleep(1) #Program waits 1 second to continue
    cmd("") #Clears the console

def Jarvis_Program():
    r=sr.Recognizer()
    with sr.Microphone() as source: #Detect the systems default microphone as our voice source
        cmd("cls")
        print("Say something")
        audio=r.listen(source) #This listens the voice and transforms it to an element

    global flag
    global told
    flag=False

    try:
        told=r.recognize_google(audio) #Google speech recognition will be recognizes what user said
        print("You said: "+told)
        flag=True #If speech is recognizable, flag turn to True for starting the Jarvis
        told=GetLower(told) #All cases will be transform to lower ones
    except sr.UnknownValueError: print("I didn't get it") #If program can't understand, throws this error
    except sr.RequestError as e: print("I can't access Google services right now; {0}".format(e))

def Jarvis():
    while True:
        Jarvis_Program()
        if flag:
            if "jarvis" in told:
                Regen()
                break
    while True:
        Jarvis_Program()
        if flag:
            if told=="run program" or told=="open program" or told=="run" or told=="start":
                cmd("start Chrome")
                Regen()
            elif "firefox" in told:
                cmd("start Firefox")
                Regen()
            elif "calculator" in told:
                cmd("start calc")
                Regen()
            elif "hub" in told:
                cmd("start github")
                Regen()
            elif "darkness" in told or "dark" or "eyes": #This will set the brightness as 50%
                cmd("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,50)")
                Regen()
            elif "shiny" in told or "hundred": #This will set the brightness as 100% BUT DOESN'T WORK
                cmd("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,100)")
                Regen()
            elif "exit" in told: #Doesn't work
                sys.exit()
                #break

Jarvis()
