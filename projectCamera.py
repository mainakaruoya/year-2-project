from tkinter import *
from datetime import datetime as dt
"""import serial
from gpiozero import LED
from picamera import PiCamera
from time import sleep"""

"""camera = PiCamera()
camera.rotation = 180
i = 0
j = 0
#LED Light objects created
blue = LED(17)
white = LED(27)

serialTrigger = serial.Serial('/dev/ttyACMO', 9600)
serialTrigger.baudrate = 9600"""
#Don't forget to change the directory path
#as well as some of the sections with triple quotes!

#this section defines the name (title) and size of our GUI
window = Tk()
window.title("Motion Activated Security Camera")
window.geometry('350x300')

#the functions called by the buttons directly are specified here
def triggerFunction():
    print("All systems go!")
    readSerialInput()

def logFileButton():
    buttonPressed = True
    if (buttonPressed == True):
        viewLogFile()

def videoCapture():
    print("Video here!")
    """global j
    j += 1
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/image_%s.jpg' % i)
    camera.stop_recording()
    camera.stop_preview()
    print("Video Capture Successful.")
    updateLogFile()
    #lightBlinks()"""

#here we create our buttons, and set them out on our grid
btn = Button(window, text = "Activate Picture Mode", padx = 5, pady = 5,
             command = triggerFunction)
btn.grid(column = 0, row = 0)
btnTwo = Button(window, text = "Activate Video Mode", padx = 5, pady = 5,
                command = videoCapture)
btnTwo.grid(column =0, row = 4)
btnThree = Button(window, text = "Read Security Log", padx = 5, pady = 5,
                  command = logFileButton)
btnThree.grid(column = 0, row = 8)
btnFour = Button(window, fg = "red", text = "Quit!",
                 command = quit, padx = 5, pady = 5)
btnFour.grid(column = 0, row = 12)

#the functions come here
def cameraCapture():
    print("Camera here!")
    camera.start_preview()
    sleep(2)
    global i
    i += 1
    camera.capture('/home/pi/Desktop/image_%s.jpg' % i)
    camera.stop_preview()
    #LED blinks to indicate capture successful
    print("Camera capture successful.")
    #lightBlinks()

def viewLogFile():
    logfile = open("securitylog.txt", mode = 'r', encoding = 'utf-8')
    for line in logfile:
        print(line, end = '')
    print("Will view log file here.")

def updateLogFile():
    with open("securitylog.txt",'a',encoding = 'utf-8') as logfile:
        logfile.write("Motion detected at " + dt.now().strftime("%m-%d-%Y, %H:%M"))
    #print("Updating log file..")

def readSerialInput():
    print("Reading serial input..")
    """readSerialTrigger = serialTrigger.readline()
    if (readSerialTrigger == "Motion detected!"):
        cameraCapture()
        updateLogFile()"""

"""def lightBlinks():
    blue.blink()
    for i in range(3):
        white.on()
        sleep(0.3)
        white.off()
        sleep(0.3)"""

#this is the command that enables the user to view the GUI.
#all functions come in here.
window.mainloop()
